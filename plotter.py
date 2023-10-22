# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:42:52 2022

@author: Sahin
"""

import matplotlib.pyplot as plt
from general_interpreter_2 import calculator,derivative,replacewith,integration_value
import numpy as np
import shutil
import os
import emyMath as math

def iscontinous(x,y,dy):
    discontinuities = []
    for index in range(len(x)-1):
        j,k = y[index],dy[index]
        if j < y[index + 1] and k < 0:
            discontinuities.append(index)
        elif j > y[index + 1] and k > 0:
            discontinuities.append(index)
    return(discontinuities)
            
def sublists(x,y,indexes):
    if indexes == []:
        return(x,y)
    xs = []
    ys = []
    indexes.insert(0,0)
    
    for i in range(len(indexes)-1):
        xs.append(x[indexes[i]+1:indexes[i+1]+1])
        ys.append(y[indexes[i]+1:indexes[i+1]+1])
    return(xs,ys)
    
    
    
def get_path():
    directory = os.getcwd()
    
    temp = ""
    for char in directory:
        temp += char
        temp += " "
        
    temp = replacewith(temp,"\ ","/ ")
    
    counter = 0
    temp2 = r""
    for char in temp:
        if counter % 2 == 0:
            temp2 += char
        counter += 1
    
    temp2 += "/"
    return(temp2)

def plotter(function,bound,detail,legend,offpos,save_bool,name,save_size,vertical_asymptotes):
    plt.style.use('_mpl-gallery')
    counter = 0
    fig, ax = plt.subplots()
    colors = "bgrcmy"
    plt.plot()
    for i2 in function:
        plt.subplot = (len(function),1,counter)
        counter += 1
        if counter == 6:
            counter = 0
        x = []
        for i in range(-1*detail * int(bound + offpos[0]), math.sign(bound + offpos[0]) * 2 * detail * int(bound + offpos[0] + 1)):           
            x.append(i/detail)
        
        y = []
        for i in x:
            try:
                temp = calculator(i2,i)
                if type(temp) != complex:    
                    y.append(temp)   
                else:
                    y.append(0)
            except:
                y.append(0)
                
        
        if vertical_asymptotes.lower() != "on":
            dy = []
            for i in x:
                try:
                    temp = calculator(derivative(i2),i)
                    if type(temp) != complex:
                        dy.append(temp)
                    else:
                        dy.append(0)
                except:
                    dy.append(0)        
            
            discontinuties = iscontinous(x, y, dy)
            
            xs,ys = sublists(x,y,discontinuties) 
            if type(xs[0]) == list:
                for i in range(len(ys)):
                    plt.plot(xs[i],ys[i],colors[counter])
            else:
                plt.plot(xs,ys,colors[counter])
        
        else:
            plt.plot(x, y,colors[counter])
            
        plt.title(function)
    
        
    ax.set(xlim=(-1*bound+offpos[0], bound+offpos[0]), xticks=np.linspace(-1*bound + offpos[0], bound + offpos[0] ,11),                    
    ylim=(-1*bound+offpos[1],bound+offpos[1]), yticks=np.linspace(-1*bound + offpos[1], bound + offpos[1], 11))
    
    plt.plot([-1*bound+offpos[0],bound+offpos[0]],[0,0],"k--")
    plt.plot([0,0],[-1*bound+offpos[1],bound+offpos[1]],"k--")
    if legend == "On" or legend == "on" or legend == "ON":
        plt.legend(function)
    if save_bool:
        fig = plt.gcf()
        fig.set_size_inches(save_size, save_size, forward=True)
        plt.savefig(name + ".png")
    
    plt.show()


def der_plotter(function,bound,detail,offpos,save_bool,name,save_size,vertical_asymptotes):
    functions = function , derivative(function)
    plt.style.use('_mpl-gallery')
    counter = 0
    fig, ax = plt.subplots()
    colors = "bgrcmy"
    plt.plot()
    for i2 in functions:
        plt.subplot = (1,len(functions),counter)
        counter += 1
        if counter == 6:
            counter = 0
        x = []
        for i in range(-detail * int(bound + offpos[0]) , (math.sign(bound + offpos[0]) * 2 * detail  * int(bound + offpos[0] + 1))):           
            x.append(i/detail)
        
        y = []
        for i in x:
            try:
                temp = calculator(i2,i)
                if type(temp) != complex:    
                    y.append(calculator(i2,i))    
                else:
                    y.append(0)
            except:
                y.append(0)
                
        if vertical_asymptotes.lower() != "on":
            dy = []
            for i in x:
                try:
                    temp = calculator(derivative(i2),i)
                    if type(temp) != complex:
                        dy.append(temp)
                    else:
                        dy.append(0)
                except:
                    dy.append(0)        
            
            discontinuties = iscontinous(x, y, dy)
            
            xs,ys = sublists(x,y,discontinuties) 
            if type(xs[0]) == list:
                for i in range(len(ys)):
                    plt.plot(xs[i],ys[i],colors[counter])
            else:
                plt.plot(xs,ys,colors[counter])
        
        else:
            plt.plot(x, y,colors[counter])
            
        #plt.title(function)
        
    
    ax.set(xlim=(-1*bound+offpos[0], bound+offpos[0]), xticks=np.linspace(-1*bound + offpos[0], bound + offpos[0] ,11),                    
    ylim=(-1*bound+offpos[1],bound+offpos[1]), yticks=np.linspace(-1*bound + offpos[1], bound + offpos[1], 11))
    
    plt.plot([-1*bound+offpos[0],bound+offpos[0]],[0,0],"k--")
    plt.plot([0,0],[-1*bound+offpos[1],bound+offpos[1]],"k--")
    plt.legend(("f(x)","f'(x)"))
    
    
    if save_bool:
        fig = plt.gcf()
        fig.set_size_inches(save_size, save_size, forward=True)
        plt.savefig(name + ".png")
    
    plt.show()
    


    
def complex_plotter(function,bound,detail,offpos,save_bool,name,save_size):
    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()
    plt.plot()
    
    x = []
    for i in range(-1*detail * int(bound + offpos[0]), detail * int(bound + offpos[0]+1)):           
        x.append(i/detail)
    
    
    y_real = []
    for i in x:
        if i == 0:
            y_real.append(y_real[-1])
        else:
            y_real.append(complex(calculator(function,i)).real)
        
    y_imag = []
    for i in x:
        if i == 0:
            y_imag.append(y_imag[-1])
        else:
            y_imag.append(complex(calculator(function,i)).imag)
        
    plt.plot(x,y_real,"c")
    plt.plot(x,y_imag,"y")
        
          
    ax.set(xlim=(-1*bound+offpos[0], bound+offpos[0]), xticks=np.linspace(-1*bound + offpos[0], bound + offpos[0] ,11),                    
    ylim=(-1*bound+offpos[1],bound+offpos[1]), yticks=np.linspace(-1*bound + offpos[1], bound + offpos[1], 11))
    
    plt.title(function)
    plt.plot([-1*bound+offpos[0],bound+offpos[0]],[0,0],"k--")
    plt.plot([0,0],[-1*bound+offpos[1],bound+offpos[1]],"k--")
    plt.legend([f"{function}(real)",f"{function}(imag)"])
    if save_bool:
        fig = plt.gcf()
        fig.set_size_inches(save_size, save_size, forward=True)
        plt.savefig(name + ".png")
    plt.show()
    
    
def saver(name = "DeletePls", function= ["x"],mode = 5,bound = 10,detail = 10,legend ="On",offpos=(10,10),directory = r"C:/Users/Sahin/Documents/python/math main/graphs",save_size = 2,lower = 0,upper = 0,vertical_asymptotes = "off"):
    if mode == 5:
        plotter(function = function,bound =bound,detail = detail,legend = legend,offpos = offpos,save_bool = True,name = name,save_size = save_size,vertical_asymptotes=vertical_asymptotes)
    if mode == 6:
        der_plotter(function = function,bound = bound,detail = detail,offpos = offpos,save_bool = True, name = name,save_size = save_size,vertical_asymptotes=vertical_asymptotes)
    if mode == 7:
        complex_plotter(function = function,bound = bound,detail = detail,offpos = offpos,save_bool = True,name = name,save_size = save_size)
    if mode == 8:
        integral_plotter(function = function , lower = lower , upper = upper , bound = bound , detail = detail , legend = False ,offpos = offpos,save_bool = True,name=name,save_size = save_size)
    print("Graph Saved!")
    
    src_path = get_path() + "/" + name + ".png"
    dst_path = directory
    shutil.move(src_path, dst_path)
    print("File Saved to 'graphs' folder!")
    
def interval_plotter(function,lower,upper,detail):
    bound = (upper - lower) // 2
    offpos = (upper-bound,upper-bound)
    plotter(function,bound,detail,False,offpos,False,"pls_delete.png",16)
    
def integral_plotter(function,lower,upper,bound,detail,legend,offpos,save_bool,name,save_size):
    
    plt.style.use('_mpl-gallery')
    counter = 0
    fig, ax = plt.subplots()
    colors = "bgrcmy"
    plt.plot()
    strlower,strupper = lower,upper
    lower,upper = calculator(lower,0),calculator(upper,0)
    
    plt.subplot = (len(function),1,counter)
    counter += 1
    if counter == 6:
        counter = 0
    x = []
    for i in range(-1*detail * int(bound + offpos[0]),detail * int(bound + offpos[0] + 1)):           
        x.append(i/detail)
    
    y = []
    for i in x:
        try:
            temp = calculator(function,i)
            if type(temp) != complex:    
                y.append(temp)   
            else:
                y.append(0)
        except:
            y.append(0)
            
    dy = []
    for i in x:
        try:
            temp = calculator(derivative(function),i)
            if type(temp) != complex:
                dy.append(temp)
            else:
                dy.append(0)
        except:
            dy.append(0)
            
    plt.plot(x, y,colors[counter])
    for i in range(len(x)):
        if x[i] > min(lower,upper) and x[i] < max(lower,upper):
            alpha = 5/detail
            if alpha > 0.5:
                alpha = 0.5
            plt.plot( (x[i],x[i]) , (0,y[i]) , colors[counter] , alpha = alpha)
    
    value = str(integration_value(function,lower,upper,detail))
    
    if not "e" in value:
        value = value[:7]    
    else:
        value = value.split("e")
        value = value[0][:7] + " * 10^" + value[1]
    
    plt.title(function + " from " + strlower +  " to " + strupper)
        
    ax.set(xlim=(-1*bound+offpos[0], bound+offpos[0]), xticks=np.linspace(-1*bound + offpos[0], bound + offpos[0] ,11),                    
    ylim=(-1*bound+offpos[1],bound+offpos[1]), yticks=np.linspace(-1*bound + offpos[1], bound + offpos[1], 11))
    
    plt.plot([-1*bound+offpos[0],bound+offpos[0]],[0,0],"k--")
    plt.plot([0,0],[-1*bound+offpos[1],bound+offpos[1]],"k--")
    plt.legend(("Value:" + str(value),))
    if save_bool:
        fig = plt.gcf()
        fig.set_size_inches(save_size, save_size, forward=True)
        plt.savefig(name + ".png")
    
    plt.show()


    
    
    
if __name__ == "__main__":
    #integral_plotter("x",5,3,10,100,False,(0,0),False,"pls_delete.png",16)
    #plotter(["tan(x)"],10,10,"off",(0,0),False,"pls_detete.png",16,"off")
    plotter(["3sec^2(x)*ln(x^2)"],50,legend = "off",detail = 20,offpos = (0,0),save_bool = False,name = "pls_detete.png",save_size=16,vertical_asymptotes = "off")
    """
    func = "csc(x)"
    x = list(np.linspace(-10,12,1000))
    
    y= []
    for i in x:
        y.append(calculator(func,i))
        
    dy = []
    for i in x:
        dy.append(calculator(derive(func),i))
        
    indexes = iscontinous(x, y, dy)
    xs,ys = sublists(x,y,indexes)
    plt.clf()
    fig,ax = plt.subplots()
    for i in range(len(ys)):
        plt.plot(xs[i],ys[i],"g")
    ax.set(xlim = (-10,10),ylim = (-10,10))
    """  