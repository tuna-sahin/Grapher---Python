# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 08:16:11 2022

@author: Sahin
"""
import importlib
import emyMath as math
import text_to_polynomial as poly

def replace(string):
    string = str(string)
    string = replacewith(string,"I","i")        
    string = replacewith(string,"X","x")    
    string = replacewith(string,"!!","doubleFactorial")
    string = replacewith(string,"!","factorial")
    string = replacewith(string," ","")
        
    string = replacewith(string,"^-","#")
    string = poly.minusconvert(string)
    string = replacewith(string,"#","^-")
    
    inparanthesis = 0
    for i in range(len(string)):
        if string[i] == "(":
            inparanthesis += 1
        if string[i] == ")":
            inparanthesis -= 1
        if inparanthesis > 0 and string[i] == "+":
            string = string[:i] + "&" + string[i+1:]
        if inparanthesis > 0 and string[i] == "*":
            string = string[:i] + "$" + string[i+1:]
    return(string)

def splitter(string):
    string = replace(string)

    s_list = string.split("+")
    for i in range(len(s_list)):
        s_list[i] = s_list[i].strip()
    return(s_list)
     
def inparanthesisFunc(string):
    
    elements = []
    result = ""
    inparanthesis = 0
    for i in string:
        if i == ")":
            inparanthesis -= 1
        if inparanthesis:
            result += i
        elif not inparanthesis and not result == "":
            elements.append(result)
        if i == "(":
            inparanthesis += 1
    return(result)

def replacewith(string,c1,c2):
    """
    replaces every c1 with c2 in string
    make sure c2 is not in c1    

    Parameters
    ----------
    string : string inputted

    c1 : char removed
    
    c2 : char entered

    Returns
    -------
    None.

    """
    
    while c1 in string:
        index = string.find(c1)
        string = string[:index] + c2 + string[index + len(c1):]
    return(string)
            

def div_parts(string,x):    

    alphabet = "qwertyuıopğüasdfghjklşiQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇzcvbnmöç"

    l1 = splitter(string)
    """
    for i in range(len(l1)):
        print("here")
        if l1[i][-1][0] == "(" and l1[i][-1][-1] == ")":
            l1[i][-1] = l1[i][-1][1:-1]
    """
    
    for i3 in range(len(l1)):
        if "*" in l1[i3]:
            l1[i3] = l1[i3].split("*")
        
        if type(l1[i3]) == list and len(l1[i3]) > 1:
            tempR = 1
            for i4 in range(len(l1[i3])):
                temp = calculator(l1[i3][i4],x)
                tempR *= temp
            if type(tempR) == complex:
                tempR = str(tempR.real) + "imag(" + str(tempR.imag) + ")"
            else:
                tempR = str(tempR)
            l1[i3] = tempR
        elif type(l1[i3]) == list and len(l1) == 1:
            l1[i3] = l1[i3][0]
            

        
    tempL = []
    for i2 in l1:
        tempL.append([])
        i2 = i2.strip()
    
    for i in range(len(l1)):
        
        temp = inparanthesisFunc(l1[i])
        if temp != "" or "e" in l1[i] or "pi" in l1[i]:
            l1[i] = replacewith(l1[i],"(" + temp + ")", "")
            
            
            tempL[i].append(temp)
            
            coefficient = ""
            for char in l1[i]:
                if char in alphabet:
                    break
                coefficient += char
            if coefficient == "":
                coefficient =  "1"
                l1[i] = "1" + l1[i]
            
            tempL[i].insert(0,coefficient)
            
            index = l1[i].find(coefficient)
            l1[i] = l1[i][:index] + "" + l1[i][index + len(coefficient):]
            
            func = ""
            for i2 in l1[i]:
                if i2 == " " or i2 == "(" or i2 == "^":
                    break
                func += i2

            tempL[i].insert(1,func)    
            l1[i] = replacewith(l1[i],func,"")
            
            tempR = l1[i].strip()
            if len(tempR) == 0:
                tempL[i].insert(2,"1")

            elif "^" in l1[i]:
                l1[i] = replacewith(l1[i],"^","")
                tempL[i].insert(2,l1[i])

            else:
                tempL[i].insert(2,l1[i])
                
            tempL[i][-1] = replacewith(tempL[i][-1],"&","+")
            tempL[i][-1] = replacewith(tempL[i][-1],"$","*")
            tempL[i][-1] = replacewith(tempL[i][-1],"+ -", "-")
        else: 
            tempL[i].append(l1[i])
            l1[i] = ""
            
    while i < len(tempL):
        if tempL[i] == "":
            tempL.pop(i)
        else:
            i += 1
    
    return(tempL)
            
def ispoly(string):
    POLYKEY = "1234567890-+/.^ x"
    for i in string:
        if not i in POLYKEY:
            return(False)
    return(True)

def calculator(string,x):
    l1 = div_parts(string,x)            
    result = 0
    for i in range(len(l1)):
        if "-" == l1[i][0]:
            l1[i][0] = "-1"
            
        if ispoly(l1[i][-1]):
            poly.function = l1[i][-1]
            l1[i][-1] = poly.f(x)
                
            try:
                string2 = l1[i][1] 
                libname2 = importlib.import_module("emyMath")
                tempF = getattr(libname2, string2)

                result += poly.fraction(l1[i][0]) * (tempF(float(l1[i][-1])) ** poly.fraction(l1[i][2]))
            except: 
                try:
                    string2 = l1[i][1]
                    libname2 = importlib.import_module("emyMath")
                    tempF = getattr(libname2, string2)
                    
                    result += poly.fraction(l1[i][0]) * (float(tempF) ** poly.fraction(l1[i][2]))
                except:
                    result += float(l1[i][0])
                
            
        elif l1[i][-1] != "":
            string2 = l1[i][1] 
            libname2 = importlib.import_module("emyMath")
            tempF = getattr(libname2, string2)
            
            result += poly.fraction(l1[i][0]) * (tempF(calculator(l1[i][-1],x)) ** poly.fraction(l1[i][2]))
            
        else:
            pass
    return(result)

derivatives = {"sign":"0",
               "sin":"cos(#)",
               "cos":["sin(#)","sign(-1)"],
               "tan":"sec^2(#)",
               "cot":"-csc^2(#)",
               "sec":["sec(#)","tan(#)"],
               "csc":["cot(#)","sign(-1)","csc(#)"],
               "ln":"i^-1(#)",
               "sqrt":"1/2i^-1/2(#)",
               "cbrt":"1/3i^-1/3(#)",
               "sinh":"cosh(#)",
               "cosh":"sinh(#)",
               "tanh":"sech^2(#)",
               "coth":"-csch^2(#)",
               "sech":["-sech(#)","tanh(#)"],
               "csch":["csch(#)","coth(#)"],
               "arcsin":"i^-1(sqrt(1-i^2(#)))",
               "arccos":"-i^-1(sqrt(1-i^2(#)))",
               "arctan":"i^-1(1 + i^2(#))",
               "arccot":"-i^-1(1 + i^2(#))",
               "arcsec":"i^-1(abs(x)*sqrt(i^2(#)-1))",
               "arccsc":"-i^-1(abs(x)*sqrt(i^2(#)-1))",
               "random":"random(#)",
               "ceil":"0",
               "floor":"0",
               "round":"0",
               "w":["w(#)","i^-1(#)","i^-1(1+w(#))"],
               "exp":"exp(#)",
               }

def derive(Sstring):
    if not "+" in Sstring and not "*" in Sstring and not "x" in Sstring:
        return("0")
    
    l1 = splitter(Sstring)
    for i in range(len(l1)):
        l1[i] = replacewith(l1[i],"&","")
        
    
    if ispoly(l1[0]):
        poly.function = l1[0]
        if l1[0] != "x": 
            return(poly.list2str(poly.derive(poly.converter(poly.minusHandle(poly.splitter(poly.function))),1)))
        else: return("1 ")
    if not "*" in l1[0]:
        l1 = div_parts(l1[0],0)[0]
        if type(derivatives[l1[1]]) == str: 
            if l1[0] == "1" and l1[2] == "1":
                return(replacewith( derivatives[l1[1]] , "#" , l1[3]) + " * " + derive(l1[3]))
        
            else:
                coef = float(l1[0])
                if float(l1[0]) == int(l1[0]):
                    coef = int(l1[0])
                
                coef2 = float(l1[2])
                if float(l1[2]) == int(l1[2]):
                    coef2 = int(l1[2])
                
                coef *= coef2
                  
                if float(l1[2]) == 1:
                    return( str(coef) + replacewith(derivatives[l1[1]],"#",l1[3]) )
                elif float(l1[2]) == 2:
                    return( str(coef) + l1[1] + "(" + l1[3] + ") *" + replacewith( derivatives[l1[1]] , "#" , l1[3]) + "*" + derive(l1[3]))
                elif float(l1[2]) > 2:
                    return( str(coef) + l1[1] + "^" + str( coef2 - 1 ) + "(" + l1[3] + ") *" +  replacewith( derivatives[l1[1]] , "#" , l1[3]) + " * " + derive(l1[3]))
        
        elif type(derivatives[l1[1]]) == list:
            if l1[0] == "1" and l1[2] == "1":
                temp = ""
                for i in derivatives[l1[1]]:
                    temp += replacewith( i, "#" ,l1[3]) + " * "
                temp += derive(l1[3]) 
                return(temp)
            
            else:
                coef = float(l1[0])
                if float(l1[0]) == int(l1[0]):
                    coef = int(l1[0])
                
                coef2 = float(l1[2])
                if float(l1[2]) == int(l1[2]):
                    coef2 = int(l1[2])
                
                coef *= coef2
                temp = ""
                if float(l1[2]) == 1:
                    temp += str(coef)
                elif float(l1[2]) == 2:
                    temp += ( str(coef) + l1[1] + "(" + l1[3] + ") *") 
                
                elif float(l1[2]) > 2:
                    temp += ( str(coef) + l1[1] + "^" + str( coef2 - 1 ) + "(" + l1[3] + ") *")
                    
                    
                for i in derivatives[l1[1]]:        
                    temp += replacewith( i , "#" , l1[3]) + " * "
                temp += derive(l1[3])
                return(temp)
    else:
        l1 = l1[0].split("*") # works flawlessly(mostly) for multiplying 2 functions
        if len(l1) == 2:
            right = l1[0]
            left = l1[1]
            return( "i(i(" + derive(right) + "*" + left + ")+i(" + right + "*" + derive(left) + "))" )
        else:
            temp = "" # can derive multiplication of any number of functions
            for i in range(len(l1)):
                for i2 in range(len(l1)):
                    if i == i2:
                        temp += derive(l1[i2])
                    else:
                        temp += l1[i2]
                    temp += " * "
                temp = temp[:-3]
                temp += " + "
            temp = temp[:-3]
            return(temp)
                    
def derivative(string):
    l1 = splitter(string)
    resultingString = ""
    for i in l1:
        resultingString += derive(i)
        resultingString += " + "
    resultingString = replacewith(resultingString,"* 1 ","")
    resultingString = replacewith(resultingString,"(1*","(")
    resultingString = replacewith(resultingString,"(1 *","(")
    resultingString = replacewith(resultingString,"*1 ","")
    resultingString = replacewith(resultingString,"  "," ")
    return(resultingString[0:-3])

def random(*mode):
    order = open("randord.txt", "r")
    temp = order.read()
    temp = int(temp)
    order.close()
    
    order = open("randord.txt", "w")
    order.write(str(temp+1))
    order.close()
    #f = "1/3abs(sin(x^100)) + 1/3abs(cos(x)) + 1/3sin^2(12+x)"
    f = "1/2sin^2(x^100) + 1/2sin^2(exp(x))"
    temp = 10 + temp/100
    if not mode:
        return(calculator(f,temp))
    else:
        return(int(str(calculator(f,temp))[2]))
    
def multi_input_funcitons(string):
    function = string.split("(")[0]
    inputs = string.split("(")[1][:-1].split(",")
    
    for i in range(len(inputs)):
        inputs[i] = int(inputs[i])    
    
    
    libname2 = importlib.import_module("emyMath")
    tempF = getattr(libname2, function)
    if len(inputs) == 2:
        result = tempF(inputs[0],inputs[1])
    else:
        result = tempF(inputs)
    return(result)

def integration_value(string,lower,upper,detail):
    x = []
    multiplier = 1
    lower,upper = calculator(lower,0),calculator(upper,0)
    if lower > upper:
        lower,upper = upper,lower
        multiplier = -1
        
    for i in range(int(lower*detail),int(upper*detail)):
        x.append(i/detail + 1/(2*detail))  
    dx = 1/detail
    area = 0
    for i in x:
        temp = dx * calculator(string,i)
        area += temp
    return(area * multiplier)  


        

if __name__ == "__main__":

    
    
    """
    print(calculator(derivative(derivative("3csc^2(x)")),1))
    print(calculator("6csc(x) * cot(x) * sign( -1) * cot(x) * sign(-1) * csc(x) + 6cot(x) * sign(-1) * csc(x) * cot(x) * sign( -1) * csc(x) + 6csc(x) * -csc^2(x) * sign( -1) * csc(x)",1))
    print("\n",derivative(derivative("3csc^2(x)")))
    """
