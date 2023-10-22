6# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 08:16:11 2022

@author: Sahin
"""

import text_to_polynomial as func
import emyMath as math
from time import sleep
import general_interpreter_2 as gen     
import plotter

def options_printer():
    optionsFile = open("interface_options.txt","r")
    current_options = {}
    for i in optionsFile:
        print(i)
        if "=" in i:
            current_options[i.split("=")[0].strip()] = i.split("=")[1].strip()
    optionsFile.close()
    return(current_options)

def options_writer(current_options):
    optionsFile = open("interface_options.txt","w")
    for i in current_options:
        optionsFile.write(f"{i} = {current_options[i]}\n")
    optionsFile.close()
  
def options_init():
    optionsFile = open("interface_options.txt","r")
    current_options = {}
    for i in optionsFile:
        if "=" in i:
            current_options[i.split("=")[0].strip()] = i.split("=")[1].strip()
    optionsFile.close()
    starter = float(current_options["Starter"])
    bound = float(current_options["Bound"])
    detail = int(current_options["Detail"])
    legend = current_options["Legend"]     
    offpos = gen.replacewith(current_options["Offset Position"][1:-1],"'","").split(",")
    for i in range(len(offpos)):
        offpos[i] = float(offpos[i])
    directory = current_options["Directory"]
    save_size = float(current_options["Save Size"])
    vertical_asymptotes = current_options["Vertical Asymptotes"]
    return(starter,bound,detail,legend,offpos,directory,save_size,vertical_asymptotes)

def options():
    current_options = options_printer()
    option_selection = "0"    
    while option_selection != "q":
        option_selection = input("Which setting would you like to modify?\n(Please select only one)('q' to quit)\n('info' for information about the options): ")
        if option_selection.lower() in ["ss","save_size","directory","dir","starter","bound","detail","legend","offsetposition","offset position","offpos","p","va","vertical asymptotes"]:
            if option_selection.lower() in ["ss","save_size","directory","dir","starter","bound","detail","legend","offsetposition","offset position","offpos","va","vertical asymptotes"]:
                option_input = input("Please input the new value: ")
            
            if option_selection.lower().strip() == "starter":
                current_options["Starter"] = float(option_input)
            elif option_selection.lower().strip() == "bound":
                current_options["Bound"] = float(option_input)
            elif option_selection.lower().strip() == "detail":
                current_options["Detail"] = int(option_input)
            elif option_selection.lower().strip() == "legend":
                current_options["Legend"] = option_input
            elif option_selection.lower().strip() == "offset position" or option_selection.lower().strip() == "offsetposition" or option_selection.lower().strip() == "offpos":
                option_input = gen.replacewith(option_input , "(", "")
                option_input = gen.replacewith(option_input , ")", "")
                temp = option_input.split(",")
                if len(temp) == 2:
                    current_options["Offset Position"] = (float(temp[0]),float(temp[1]))
            elif option_selection.lower().strip() == "dir" or option_selection.lower().strip() == "directory":
                temp = r""
                temp += option_input    
                current_options["Directory"] = temp
            elif option_selection.lower().strip() == "ss" or option_selection.lower().strip() == "save size":
                current_options["Save Size"] = float(option_input)
            elif option_selection.lower().strip() == "vertical asymptotes" or option_selection.lower().strip() == "va" :
                current_options["Vertical Asymptotes"] = option_input
                options_printer()
                    
                    
        elif option_selection.lower() == "info":
            print()
            print("starter : it is the minimum root for the polynomial that can be found.\nA really small starter guarantees that you will find all the roots.\nHowever, it will increase processing time. Best to change accordingly.\n")
            print("bound : how big an area the plots will display. It displays [-bound,bound]\nPlease enter a integer value.\n")
            print("detail : how detailed the plots will be.\nBest to increase for complicated graphs as it also increases processing time.\nPlease enter a integer value.\n")
            print("Offset Position : the point at the center of the graph")
            print("Legend : whether the legend will be displayed in the 5th selection")
            print("Directory : directory where the graphs are saved")
            print("Save Size: the size(inches) of the graph being saved")
            print("Vertical Asymptotes: whether vertical asmyptotes will be displayed or not")
        elif option_selection != "-1":    
            print("Invalid Selection")
    options_writer(current_options)

def funcLister():
    print("\ntrigonometric functions, inverse trigonometric functions\nhyperbolic functions",end = " ")
    print("inverse hyperbolic functions\nln ,exp, !(x), !!(x), sqrt, cbrt, ceil, floor, round, absolute",end=", ")
    print("sign\n")
    print("Functions below are supported but not recommended for use")
    print("===============================================")
    print("complexLn, isqrt, isqrtString, fraction, fractionString, radians, degrees",end = ", ")
    print("w(lambert gamma)")

def complexfuncLister():
    print("trigonometric,hyperbolic,ln,exp,sqrt,cbrt")
    print("all polynomials")

def get_super(int1):
    result = ""
    supertext = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    normaltext = "0123456789"
    for i in str(int1):
        if i in normaltext:
            result += supertext[normaltext.find(i)]
        else:
            result += i
    return(result)

def funcinput():
    funct = "example Syntax"
                     
    print("")       
    print("Options (You may select more than one)")
    print("=========================================================")
    print("\t 1-Roots")
    print("\t 2-Roots(Alternative)")
    print("\t 3-Degree")#
    print("\t 4-Roots For f(x) = ?")
    print("\t 5-Inverse of f(x)")
    print("\t 6-Factor")
    print("\t 7-Polynomial Divison")#
    print("\t 8-f'(x)")#
    print("\t 9-fⁿ(x)")#
    print("\t 0-Roots of f'(x)")
    print("\t A-Critical Points and Their Evaluation")
    print("\t B-F(x)")#
    print("\t C-Integral of f(x) of any degree")#s
    print("\t D-Polynomial Multiplication (Select by itself)")#
    print("\t E-Polynomial Addition (Select by itself)")#
    print("\t F-Plot")
    print("=========================================================")
    print("")
              
    options = input("Type the numbers of your selections :")
    if options == "":
        options = "1368F"    
        
    while funct.lower() == "example syntax"  and not "d" in options.lower() and not "e" in options.lower():
        funct = input("Enter a Function(Enter 'Example Syntax' for example): ")
        if funct.lower() == "example syntax":
            print("5x^3 - x^2 + x^4 - 1/4x  - 4 + 5/2 (spaces do not matter)")
        if funct == "":
            #funct = "x^5 - 8x^4 + 9x^3 - 14x^2 + 9x - 3"
            #funct = "x^3 - 2x^2 + x"
            #funct = "x^5 - 5x^3 + 4x"
            funct = "x^4 - 5x^2 + 4"
        
    n4 , n5 , n7, n9= None, None, None, None
    if "4" in options:
        n4 = float(input("The value you want to solve for : "))
    if "5" in options:
        n5 = float(input("The value you want to input for inverse of f(x) : "))
    if "7" in options:
        n7 = str(input("Enter another function to divide with : "))
    if "9" in options:
        n9 = str(input("Which derivation would you like to calculate? :"))
          
    return(funct , options , n4 , n5 , n7 , n9)

#what we do in do shadows

def printer(options): 
    if "2" in options: #Emythea's Method
        print(f"Roots of function '{func.function}' are {math.sortList1(func.solve4s(0,starter))}")
    if "1" in options: #Newton's Method
        print(f"Roots of function '{func.function}' are {math.sortList1(func.solve1s(0,starter))}")
    if "3" in options: #Degree
        print(f"Degree of function '{func.function}' is {func.degreeAlt(func.function)}")
    if "4" in options: #Newton's Method for a spesific x
        print(f"Roots of function '{func.function}' are {math.sortList1(func.solve1s(funcinputs[2],starter))}")
    if "5" in options: #Inverse of f
        print(f"Inverse of f({funcinputs[3]}) is {math.sortList1(func.inverse(funcinputs[3],starter))}")
    if "6" in options:
        print(f"f(x) = {func.factor(starter)}")
    if "7" in options: #polynomial division 
        remainder = func.polynomialDivision(func.function, funcinputs[4])[0]
        divident = func.polynomialDivision(func.function, funcinputs[4])[1]
        print(f"The remainder polynomial is : {func.list2str(remainder)}")
        print(f"The divident  polynomial is : {func.list2str(divident)}")                                   
    if "8" in options:
        print("f'(x) = " + func.list2str(func.derive(func.converter(func.minusHandle(func.splitter(func.function))),1)))
    if "9" in options:
        print("f(" + str(get_super(int(funcinputs[5])) + ")(x) = " + str(func.list2str(func.derive(func.converter(func.minusHandle(func.splitter(func.function))),int(funcinputs[5]))))))
    if "0" in options:
        print(f"Roots of f'(x) are {math.sortList1(func.solve1sd(0,starter))}")
    if "a" in options.lower():
        cpoints = (func.criticalPoints(starter))
        for i in cpoints:
            print(i)
    if "b" in options.lower():
        print("F(x) = " + func.list2str((func.integrateWithC(func.converter(func.minusHandle(func.splitter(func.function))),1))))
    if "c" in options.lower():
        degree = int(input("Which integration would you like to calculate? :"))
        print(str(degree) + "th integral of f(x) = " + func.list2str((func.integrateWithC(func.converter(func.minusHandle(func.splitter(func.function))),degree))))
    if "d" in options.lower():
        inputtedFunc = ""
        functions = []
        while inputtedFunc.lower() != "quit":
            inputtedFunc = input("Enter a function('Quit' to quit)")
            functions.append(inputtedFunc)
        functions.pop()
        print(func.polynomialMultiplication(tuple(functions)))
    if "e" in options.lower():
        inputtedFunc = ""
        functions = []
        while inputtedFunc.lower() != "quit":
            inputtedFunc = input("Enter a function('Quit' to quit)")
            functions.append(inputtedFunc)
        functions.pop()
        print(func.polynomialAddition(tuple(functions)))
    if "f" in options.lower():
        plotter.plotter([func.function],bound,detail,legend,offpos,False,"DeletePls",2)
        
def secondselection(ans):
    userinput = "list"
    while userinput.lower() == "list" or userinput.lower() == "example syntax":
        userinput = input("Enter a Function\n(Enter 'List' for list of functions supported)\n(Enter 'Example Syntax' for an example): ")
        if userinput.lower() == "list":
            funcLister()
        if userinput.lower() == "example syntax":
            print("4tan^2( ln^1/2(3x) + 1/3exp(x)) + sin^3(sqrt(x))* tan^-1(x)")
            
    if userinput == "":
        userinput = "4tan^2( ln(3x) + exp(x)) + sin^3(sqrt(x))"  
        userinput= "4tan^2( ln^1/2(3x) + 1/3exp(x)) + sin^3(sqrt(x))"
        userinput = "3tan^2(x) * 1/4tan^-2(x)"
        
    if "x" in userinput:
        x = input("Please write the value x you want to find f(x) :")
       
    else:
        x = "0"
        
    if x.strip().lower() == "ans":
        x = str(ans)
        
    if x == "":
        x = "1/2"
    
    
    x = gen.calculator(x,0)
    print(userinput,"at",x)
    result = gen.calculator(userinput, x)
    print(result)
    #print(result,"or",math.fractionString(result))
    return(result) 
    
def third_selection(userinput,past_functions,bound,detail,legend,offpos,save_size,vertical_asymptotes):
    if userinput == "":
        past_functions = []
    else:
        past_functions.append(userinput)
    plotter.plotter(past_functions, bound, detail,legend,offpos,False,"DeletePls",save_size,vertical_asymptotes)
    return(past_functions)
    
def fourth_selection(userinput,bound,detail,offpos,save_size):
    while userinput == "list":    
        complexfuncLister()
        userinput = input("Enter a Function('list' for complex supporting functions): ")
        
    plotter.complex_plotter(userinput, bound, detail,offpos,False,"DeletePls",save_size)
    
def derivative_calculate(ans):
    userinput = input("Enter a function:")
    x = input("Please write the value x you want to find f(x) :")
    if x.strip().lower() == "ans":
        x = str(ans)
    x = gen.calculator(x,0)
    
    x = float(x)
    result = gen.calculator(gen.derivative(userinput),x)
        
    print(result)
    return(result)  
    
def multivariable():
    userinput = input("Enter a function('Example Sytnax' or 'List' for help):")
    print()
    if userinput.lower() == "example syntax":
        print("lcm2(3,4,5) would return 60")
    elif userinput.lower() == "list":
        return("lcm2, gcd2, log(base,input), complexLog(base,input), cord(r,theta), permutation, combination")
    else:
        return userinput + " = " + str(gen.multi_input_funcitons(userinput))
        
def integralplotting(bound,detail,offpos):
    userinput_f = input("Enter the function you want to integrate: ")
    userinput_l = input("Enter the lower bound of integration: ")
    userinput_u = input("Enter the upper bound of integration: ")
    
    plotter.integral_plotter(function = userinput_f, lower = userinput_l , upper = userinput_u, bound = bound, detail = detail, legend = False, offpos = offpos, save_bool = False, name = "pls_delete.png", save_size = 16)
    return ((userinput_f,userinput_l,userinput_u))
    
def print_options(time):
    print("")
    print("q-Quit ")
    sleep(time)
    print("0-Options")
    sleep(time)
    print("1-Polynomial Calculations")
    sleep(time)
    print("2-Any function at x")
    sleep(time)
    print("3-Any function's derivative at x")
    sleep(time)
    print("4-Derivative of a function")
    sleep(time)
    print("5-Plot functions")
    sleep(time)
    print("6-Plot a function along with its derivative")
    sleep(time)
    print("7-Complex plotting(Wolfram Style)")
    sleep(time)
    print("8-Definite Integral Plotting and Calculation(using riemann sum)")
    sleep(time)
    print("9-Save the last graph")
    sleep(time)
    print("10-Multivariable input functions (was lazy to test)")
    
#main instance from here on out    
    
starter,bound,detail,legend ,offpos,directory,save_size,vertical_asymptotes = options_init()
lastinput = ([],5)
first_selection = "0"
ans = "0"
past_functions = []
while first_selection.lower() != "q":     
    
    print_options(0)
    
    if first_selection == "":
        first_selection = "31"
    
    first_selection = input("Options (Please select only one):")
    while True:
        if first_selection in ["q","0","","1","2","3","4","5","6","7","8","9","10","30","31","32"]:
            break
        print("Invalid Selection")
        first_selection = input("Options (Please select only one):")
        
    if first_selection == "1": #polynomial calculations
        funcinputs = funcinput()
        func.function = funcinputs[0]
        printer(funcinputs[1])
        input("Press enter to continue:")
        
    elif first_selection == "4": # derivative of a function
        userinput = input("Enter the function you want to take the derivative of: ")
        userinput = gen.replacewith(userinput," ","")
        print(gen.replacewith(gen.derivative(userinput),"identity",""))
        input("Press enter to continue:")        

    elif first_selection == "6": # plot a function along with its derivative
        userinput = input("Enter a function:")
        userinput = gen.replacewith(userinput," ","")
        lastinput = (userinput,6)
        plotter.der_plotter(userinput,bound,detail,offpos,False,"DeletePls",save_size,vertical_asymptotes)
    
    elif first_selection == "2": # any function at x
        ans = str(secondselection(ans))
        input("Press enter to continue:")

    elif first_selection == "3": # any functions derivative value
        ans = derivative_calculate(ans)
        input("Press enter to continue:")
    
    elif first_selection == "5": #plot functions
        userinput = input("Enter a Function : ")
        past_functions = third_selection(userinput,past_functions,bound,detail,legend,offpos,save_size,vertical_asymptotes)
        lastinput = (past_functions,5)
        
    elif first_selection == "0": #options
        options()
        starter,bound,detail,legend,offpos,directory,save_size,vertical_asymptotes = options_init()
        
    elif first_selection == "7": #complex plotting
        userinput = input("Enter a Function('list' for complex supporting functions): ")
        fourth_selection(userinput,bound,detail,offpos,save_size)
        lastinput = (userinput,7)
    #𝑥𝑥𝑥𝑥𝑥𝑥
    elif first_selection == "9": #save graph with name
        print(directory)
        filename = input("What would you like to name the file?(leave blank for function) ")
        if filename == "":
            if type(lastinput[0]) != list:
                filename = str(lastinput[0])
                if lastinput[1] == 8:
                    lower,upper = lastinput[2:]
                    filename += " integration from " + str(lower) + " to " + str(upper)
            elif type(lastinput[0]) == list:
                for i in lastinput[0]:
                    filename += i
                    filename += " & "
                filename = filename[:-3]
            
            filename = gen.replacewith(filename , "exp" , "bruhtingen")
            filename = gen.replacewith(filename , "x" , "𝑥")
            filename = gen.replacewith(filename , "bruhtingen" , "exp")
            filename = gen.replacewith(filename , "*", "x")
            filename = gen.replacewith(filename , "/" , "÷")
        else:
            while "/" in filename or ":" in filename or "?" in filename or "*" in filename or "<" in filename or ">" in filename or "|" in filename: #\/:?*"<>|
                print("Invalid File name a filename cannot contain /:?*<>\\|")
                filename = input("What would you like to name the file? ")
        if len(lastinput) == 2:
            lastinput = (lastinput[0],lastinput[1],0,0)
        plotter.saver(name = filename,function = lastinput[0],mode = lastinput[1],bound = bound,detail = detail,legend = legend,offpos = offpos,directory = directory,save_size = save_size,lower = lastinput[2],upper = lastinput[3],vertical_asymptotes=vertical_asymptotes)
    
    elif first_selection == "8": #integral plotting
        temp = integralplotting(bound,detail,offpos)
        lastinput = (temp[0],8,temp[1],temp[2])
    
    elif first_selection == "10": #multi variable functions
        print(multivariable())
        input("Press enter to continue:")
    
    elif first_selection == "30": #developer tool div parts
        userinput = input("function? ")
        print(gen.div_parts(userinput,0))
    
    elif first_selection == "31": #zoooort(easter egg)
        temp = "z"
        for i in range(int(math.map(1,10,math.random(1,32)))):
            temp += "o"
        temp += "rt"
        print(temp)
        
    elif first_selection == "32": #notes for developer
        print("""
 - ile başlayan sıkıtnılar var div parts -yi yanlış anlıyo - olan yeri -1 yapsın çok kolay aslında ama vaktim kalmadı(seems to work dont fix asdşakmsd)\n
complex plotting de sıkıntı var sebep = ?(fixed identity function changeden kaynaklı i = 1j değiştirmeyi unutmuşum)\n
integral plot cant save(fixed enayi gibi modu yanlış girmişim zoooort neyse fixed)\n
multi variable hiçbişeyde çalışmıyo adam akıllı el at(fixed kolaydı)\n
gen.derivative gg olmuş çalışmayan example var general interpreter 2 de git bak çöz pls(mostly fixed)\n
gen.derivaive 3csc^2(x) ikinci türev ne öyle amk(pending)\n
ayrıca sanırım iscontinous kısmında hata var 6 - 3csc^2(x) girdisinde ortaları yok(pending)\n
             """)
        input("Press enter to continue:")
        