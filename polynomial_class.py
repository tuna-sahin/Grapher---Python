# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:46:19 2022

@author: Sahin
"""
from text_to_polynomial import *

class polynomial:
    def __init__(self,polynomial):
        self.polynomial = polynomial
        
    def integrate(self,degree = 1):
        return(polynomial(list2str((integrateWithC(converter(minusHandle(splitter(self.polynomial))),degree)))))

    def derive(self,degree = 1):
        return(polynomial(list2str((derive(converter(minusHandle(splitter(self.polynomial))),degree)))))
    
    def degree(self):
        return(degreeAlt(self.polynomial))
    
    def get_list(self):
        return(dict2list(list2dict(converter(minusHandle(splitter(self.polynomial))))))
        
    def __mul__(self,other):
        return(polynomial(polynomialMultiplication((self.polynomial , other.polynomial,))))

    def __add__(self,other):
        return(polynomial(polynomialAddition((self.polynomial , other.polynomial))))
    
    def __hash__(self):
        temp = hash(self.polynomial)
        #print(temp)
        return temp
    
    def __floordiv__(self,other):
        return polynomial(list2str(polynomialDivision(self.polynomial,other.polynomial)[1]))
    
    def __mod__(self, other):
        return polynomial(list2str(polynomialDivision(self.polynomial,other.polynomial)[0]))
    
    def __str__(self):
        return(self.polynomial)
        
    def __eq__(self,other):
        flag = True
        l1 = self.get_list()
        l2 = other.get_list()
        for i in l1:
            if i in l2:
                l2.remove(i)
        if len(l2) != 0:
            flag = False
        return(flag)
    
    def __sub__(self,other):
        temp = polynomial("-1")
        return(self + (other*temp))
        
    def __repr__(self):
        return(str(preparer2(self.polynomial)))

    def __call__(self,x):
        c_list = preparer2(self.polynomial)
        return(calculator(x, c_list))
    
    def roots(self):
        function = self.polynomial
        return(solve1s(0, -10))

a = polynomial("3x^5 + 4x^2 + 9x + 2")
print(a.derive())
