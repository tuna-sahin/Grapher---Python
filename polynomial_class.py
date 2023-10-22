# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:46:19 2022

@author: Sahin
"""
import text_to_polynomial as func

class polynomial:
    def __init__(self,polynomial):
        self.polynomial = polynomial
        
    def integrate(self,degree = 1):
        return(polynomial(func.list2str((func.integrateWithC(func.converter(func.minusHandle(func.splitter(self.polynomial))),degree)))))

    def derive(self,degree = 1):
        return(polynomial(func.list2str((func.derive(func.converter(func.minusHandle(func.splitter(self.polynomial))),degree)))))
    
    def degree(self):
        return(func.degreeAlt(self.polynomial))
    
    def __mul__(self,other):
        return(polynomial(func.polynomialMultiplication(self.polynomial , other.polynomial)))

    def __add__(self,other):
        return(polynomial(func.polynomialAddition((self.polynomial , other.polynomial))))
    
    def __floordiv__(self,other):
        return polynomial(func.list2str(func.polynomialDivision(self.polynomial,other.polynomial)[1]))
    
    def __mod__(self, other):
        return polynomial(func.list2str(func.polynomialDivision(self.polynomial,other.polynomial)[0]))
    
    def __str__(self):
        return(self.polynomial)
    
    def __sub__(self,other):
        temp = polynomial("-1")
        return(self + (other*temp))
        
    def __repr__(self):
        return(str(func.preparer2(self.polynomial)))

    def __call__(self,x):
        c_list = func.preparer2(self.polynomial)
        return(func.calculator(x, c_list))
    
    def roots(self):
        func.function = self.polynomial
        return(func.solve1s(0, -10))

a = polynomial("3x^5 + 4x^2 + 9x + 2")
print(a.derive())