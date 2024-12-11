dash="----------------------------------------------"
#exersice 1
def ex1():
    #all file
    with open("3я_лаба\\example.txt",'r') as file:
        content=file.read()
        print(content)
    #line by line
    with open("3я_лаба\\example.txt",'r') as file:
        lines=file.readlines()
        print(lines)

#exersice 2
def ex2_1():
    text1 =input("Введите текст: ")
    with open('3я_лаба\\user_input.txt','w') as file:
        file.write(text1)
def ex2_2():
    text2 = input('Введите текст для добавления: ')
    with open('3я_лаба\\user_input.txt','a') as file:
        file.write('\n' + text2)

#exersice 3
def ex3():
    try:
        #all file
        with open("3я_лаба\\example1.txt",'r') as file:
            content=file.read()
        print(content)
        #line by line
        with open("3я_лаба\\example1.txt",'r') as file:
            line=file.readlines()
            print(line)
    except FileNotFoundError:
        print("файл не найден")

ex1()
print(dash)
ex2_1()
ex2_2()
f=open('3я_лаба\\user_input.txt')
print(f.read())
print(dash)
ex3()