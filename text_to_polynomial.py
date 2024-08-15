# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 08:16:11 2022

@author: Sahin
"""


import emyMath as math
import importlib
#string polynomial interpreter
#explicit polynomials only

function = "x^5 - 8x^3" 

def fraction(string):
    numbers = "1234567890"
    if "e" in string or "pi" in string:
        
        i = 0
        nums = ""
        while i < (len(string)):
            if string[i] in numbers:
                nums += string[i]
                try:
                    string = string[:i] + string[i+1:]
                except:
                    string = string[:i]
            i += 1
        if not "+" in nums or not "-" in nums or not "/" in nums: 
            string = string.strip()
            libname = importlib.import_module("emyMath")
            return(float(getattr(libname, string))*float(nums))
        else:
            pass
    
        
    if "." in string:
        return(float(string))
    
    if "/" in string:
        index = string.find("/")
        nom = string[:index]
        denom = string[index + 1:]
        return(int(nom)/int(denom))
    else:
        return(int(string))
def dmSolve(string):
    if "--" in string:
        index = string.find("--")
        string = string[:index] + "+" + string[index+1:]
    return(string)
def minusconvert(string):
    result = ""
    for i in string:
        if i == "-":
            result += "+ -"
        else:
            result += i
    return result
def splitter(string):
    print(string)
    while True:
        print(string)
    if "+" in string or "-" in string:
        string = minusconvert(string)
        s_list = string.split("+")
        for i in range(len(s_list)):
            s_list[i] = s_list[i].strip()
        return(s_list)
    else:
        return(string)
def minusHandle(s_list):
    temp = ""
    remove = []
    for i in range(len(s_list)):    
        if s_list[i] == "":
            remove.append(s_list[i])
            
        elif s_list[i][0] == "-":
            temp = s_list[i][1:]
            temp = temp.strip()
            temp = "-" + temp
            s_list[i] = temp
            temp = ""
    for i in remove:
        s_list.remove(i)
    return s_list
def converter(v_list):
    functionl = []
    for i in v_list:
        temp = i
        if "-" in temp:
            temp = ""
            for i2 in range(len(i)):
                if i[i2] == "-" and i[i2+1] == "x":
                    temp += "-1"
                else:
                    temp += i[i2]
                mIndex = (v_list.index(i))
            v_list[mIndex] = temp

   
                
        if "x" in temp and "^" in temp and not "-" in temp:
            degree = 1
            xindex = temp.find("x")
            
            if xindex == 0:
                coefficient = 1
            else:
                coefficient = fraction(temp[:xindex])
            
            if i[xindex + 1] == "^":
                degree = fraction(temp[xindex+2:])
            term = [coefficient,degree]
        
        elif "x" in temp and "^" in temp and "-" in temp:
            xindex = temp.find("x")
            
            if xindex == 1:
                coefficient = -1
            else:
                coefficient = fraction(temp[:xindex])
                
            if temp[xindex + 1] == "^":
                eindex = temp.find("^")
                degree = fraction(temp[eindex+1:])
            term = [coefficient , degree]

        elif "x" in temp and not "^" in temp:
            xindex = temp.find("x")
            
            if xindex == 0:
                coefficient = 1
            else:
                coefficient = fraction(temp[:xindex])
            
            degree = 1
            term = [coefficient,degree]
            
        elif not "x" in temp and not "^" in temp:
            term = [fraction(temp),0]
            
        
        
        functionl.append(term)
    return(functionl)
def calculator(numInput ,c_list):
    x = numInput
    result = 0
    for i in c_list:
        if type(i) == list:
            result += i[0] * (x ** i[1])
        elif type(i) == float or type(i) == int:
            result += i
        else:
            return(None),
    return(result)
def derivebase(c_list):

    derivative = []
    for i in c_list:
        if type(i) == list:
            coefficient = i[0] * i[1]
            if i[1] != 0:
                degree = i[1] - 1
            else:
                degree = 0
                
            term = [coefficient , degree]
        elif type(i) == int or type(i) == float:
            term = 0
        derivative.append(term)
    return(derivative)
def integratebase(c_list):
    integral = []
    for i in c_list:
        if type(i) == list:
            if i[0] == "c":
                degree = i[1] + 1
                coefficient = ("c")
                term = [coefficient , degree]
            else:
                coefficient = i[0] / (i[1]+1)
                degree = i[1] + 1
                term = [coefficient , degree]
    
        if type(i) == int or type(i) == float:
            term = [i,1]
            
        integral.append(term)
    return(integral)
def integrate(c_list,degree):
    for i in range(degree):
        c_list = integratebase(c_list)
    return(c_list)
def integrateWithC(c_list,degree):
    for i in range(degree):
        c_list = integratebase(c_list)  
        c_list.append(["c",0])
    return(c_list)
def derive(c_list,degree):
    for i in range(degree):
        c_list = derivebase(c_list)
    return(c_list)
def interpretFunction(integer,string):
    return (calculator(integer , converter(minusHandle(splitter(string)))))
def interpretDerivative(integer,string,degree):
    return (calculator(integer , derive(converter(minusHandle(splitter(string))),degree)))
def interpretIntegral(integer,string,degree):
    return (calculator(integer , integrate(converter(minusHandle(splitter(string))),degree)))
def f(x):
    return(interpretFunction(x,function))
def df(x,n):
    return(interpretDerivative(x, function, n))
def F(x,n):
    return (interpretIntegral(x, function, n))
def degree_f():
    temp = 0
    c_list = converter(splitter(function))
    for i in c_list:
        if type(i) == list:
            if temp < i[1]:
                temp = i[1]
    return(temp)
def SumCoefficients():
    return(f(1))
def constantOfF():
    return(f(0))
def solve4x(n,starter):

    temp = starter
    temp2 = None
    modifier = 0.1
    lastIncrease = None
    while temp != temp2:
        temp2 = temp
        if f(temp) - n > 0:
            temp -= modifier * math.sign(df(temp,1))
            if lastIncrease:
                modifier /= 2
            lastIncrease = False
            
        elif f(temp) - n < 0:   
            temp += modifier * math.sign(df(temp,1))
            if not lastIncrease:
                modifier /= 2
            lastIncrease = True
                
        else:
            return(temp)      
    return(temp)
def solve1x(x,temp):
    temp2 = temp + 1
    while temp != temp2:
        temp2 = temp
        if df(temp,1) == 0:
            temp += 1e-3
        temp -= (f(temp)-x)/df(temp,1)
    return(temp)
def solve1s(x,starter):
    debugList = []
    roots = []
    rootFound = 0
    for i in range(1000):
        rootFound = math.smallRound(solve1x(x,starter))
        debugList.append(rootFound)
        if not rootFound in roots:
            roots.append(rootFound)
        else:
            starter += 0.11
    return(roots)
def solve4s(x,starter):
    debugList = []
    roots = []
    rootFound = 0
    for i in range(abs(starter)*20):
        rootFound = math.smallRound(solve4x(x,starter))
        debugList.append(rootFound)
        if not rootFound in roots:
            roots.append(rootFound)
        else:
            starter += 0.1
    return(roots)  
def inverse(x,starter):
    return(solve1s(x,starter))      
def degree(dict_b1):
    temp = 0
    for i in dict_b1:
        if i > temp:
            temp = i
    return(temp)
def polynomialDivision(l1,l2):
    b1,dict_b1,dict_b2,b3 = [],{},{},[]
    l1 = converter(minusHandle(splitter(l1)))
    l2 = converter(minusHandle(splitter(l2)))
    for i in l1:
        dict_b1[i[1]] = i[0]
    for i2 in l2:
        dict_b2[i2[1]] = i2[0]
    
    
    counter = degree(dict_b1)
    for i in range(counter+1):
        if not i in dict_b1:
            dict_b1[i] = 0
    

    firstTime0 = False
    permD = degree(dict_b2)
    permC = dict_b2[permD]
    while degree(dict_b1) >= permD:

        tempD = degree(dict_b1)
        tempC = dict_b1[tempD]
        dd = degree(dict_b1) - permD #difference in degrees
        dc = tempC / permC
        b3.append([dc,dd])
        
        for i3 in dict_b2:
            dict_b1[i3+dd] -= dc * dict_b2[i3]
        dict_b1.pop(tempD)
        
        if firstTime0:
            break
        if degree(dict_b1) == 0:
            firstTime0 = True
        


    remove = []
    for i4 in dict_b1:
        if dict_b1[i4] == 0:
            remove.append(i4)
            
    for i5 in remove:
        dict_b1.pop(i5)
    
    
    for i6 in dict_b1:
        b1.append([dict_b1[i6],i6])

    return((b1,b3))    
def list2str(list_b):
    c_counter = 0
    if len(list_b) == 0:
        return("0")
    if len(list_b) > 0:
        result = ""
        for i in list_b: 
            if i[0] == "c":
                result += "+ "
                   
                if i[1] == 0:
                    result += "c(" + str(c_counter) + ")" 
                elif i[1] == 1:
                    result += "c(" + str(c_counter) + ")x" 
                else:
                    result += str(1/math.factorial(i[1])) + "c(" + str(c_counter) + ")x^" + str(i[1])
                c_counter += 1   
            else:    
                if i[0] <= 0:
                    sign = "-" 
                    i[0] = abs(i[0])
                elif i[0] >  0:
                    sign = "+"
                
                if i[0] % 1 == 0:
                    i[0] = int(i[0])
    
    
                if i[0] == 0:
                    result += ""
                elif i[0] != 0 and i[0] != 1 and i[1] !=0 and i[1] != 1: 
                    result += sign + " " + str(i[0]) + "x^" + str(i[1]) + " "
                elif i[0] != 0 and i[1] !=0 and i[1] != 1: 
                    result += sign + " x^" + str(i[1]) + " "
                elif i[0] == 1 and i[1] == 1:
                    result += sign + " x "
                elif i[0] != 0 and i[1] == 1:
                    result += sign + " " + str(i[0]) + "x "
                elif i[0] != 0 and i[1] == 0:
                    result += sign + " " + str(i[0]) + " "             
            
        if len(result) == 0:
            return("0")
        if result[0:2] == "+ ":
            result = result[2:]
        return(result)
def factor(starter):
    result = ""
    tempF = list2str(converter(minusHandle(splitter(function))))
    roots = math.sortList1(solve1s(0,starter))
    counter=[]

    for i in range(len(roots)):
        counter.append(0)            
        
    for i2 in range(len(roots)):
        if i2 % 1 == 0:    
            if roots[i2] > 0:
                quotient = str("x-" + str(int(roots[i2])))    
            elif roots[i2] < 0 :
                quotient = str("x+" + str(int(abs(roots[i2]))))
            elif roots[i2] == 0:
                quotient = "x"
                
            while list2str(polynomialDivision(tempF, quotient)[0]) == "0":
                tempF = list2str(polynomialDivision(tempF, quotient)[1])
                counter[i2] += 1
                
            result += "(" + quotient + ")^" + str(counter[i2]) + " . "
        
    if tempF != "1":
        result += "(" + tempF.strip() + ")"
    
    if result[-3:] == " . ":
        result = result[0:-3]
    return(result)
def degreeAlt(string):
    l1 = (converter(minusHandle(splitter(string))))
    temp = 0
    for i in l1:
        if temp < i[1]:
            temp = i[1]
    return(temp)
def strs2dictlist(l1):
    l2 =  []
    for i in l1:
        l2.append(converter(minusHandle(splitter(i))))

    dictList = []
    for i3 in l2:
        tempDict = {}
        for i4 in i3:
            tempDict[i4[1]] = i4[0]
        dictList.append(tempDict)
    return(dictList)
def polynomialAddition(strlist):
    
    dictList = strs2dictlist(strlist)
    temp = 0
    for i in dictList:
        for i2 in i:
            if temp < i2:
                temp = i2
    result = {}
    for i3 in range(temp+1):
        result[i3] = 0
    for i4 in dictList:
        for i5 in i4:
            result[i5] += i4[i5]
    
    listr = []
    for i6 in result:
        listr.append([result[i6],i6])
        
    stringr = list2str(listr)
    return(stringr)
def solve1xd(x,temp):
    temp2 = temp + 1
    while temp != temp2:
        temp2 = temp
        if df(temp,2) == 0:
            temp += 1e-3
        temp -= (df(temp,1)-x)/df(temp , 2)
    return(temp)
def solve1sd(x,starter):
    debugList = []
    roots = []
    rootFound = 0
    for i in range(1000):
        rootFound = math.smallRound(solve1xd(x,starter))
        debugList.append(rootFound)
        if not rootFound in roots:
            roots.append(rootFound)
        else:
            starter += 0.11
    return(roots)
def criticalPoints(starter):
    xs = solve1sd(0,starter)
    result = {0:[],1:[],2:[]}
    for i in xs:
        if f(i) > 0:
            result[0].append(i)
        elif f(i) < 0:
            result[1].append(i)
        elif f(i) == 0:
            result[2].append(i)
    
    resultS = ["At points:","At points:","At points:"]
    suffixS = ["f(x) has a local maximum","f(x) has a local minumum","f'(x) = 0 but is inconclusive"]
    for i in range(len(result)):        
        for i2 in result[i]:
            if i2 != []:
                
                resultS[i] += str(i2) + " "
        resultS[i] += suffixS[i]
        
    for i in range(len(result)):
        if result[i] == []:
            resultS.pop(i)        
    return(resultS)
def list2dict(l1):
    resultingDict = {}
    for i in l1:
        resultingDict[i[1]] = i[0]
    return(resultingDict)
def multiply2(d1,d2):
    resultingDict = {}
    for i in d1:
        for i2 in d2:
            if i + i2 in resultingDict:
                resultingDict[i + i2] += d1[i] * d2[i2]
            else:    
                resultingDict[i + i2] = d1[i] * d2[i2]
    return(resultingDict)
preparer = lambda string: list2dict(converter(minusHandle(splitter(string))))
preparer2 = lambda string: converter(minusHandle(splitter(string)))
def polynomialMultiplication(functions):
    result =  preparer(functions[0])
    functions = functions[1:]
    for i in functions:
        result = multiply2(result,preparer(i))
    return(list2str(dict2list(result)))
def dict2list(d1):
    result = []
    for i in d1:
        temp = [d1[i],i]
        result.append(temp)
    return(result)



if __name__ == "__main__":
    pass
