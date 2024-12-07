from math import sqrt
from datetime import*
import mymodule
import mypackage

#ex 1
def ex1():
    first=int(input('Введите первое число: '))
    second=int(input('Введите второе число: '))
    print(sqrt(first*second))
    print(datetime.now())
#ex 2
def ex2():
    mymodule.plus()

#ex 3
def ex3():
    mypackage.greet()
    mypackage.max_of_two()
    
    
ex1()
ex2()
ex3()