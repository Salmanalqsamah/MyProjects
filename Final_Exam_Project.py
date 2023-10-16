print('wellcome\n\t this is training for the Final Exam\n\tplease enter the Level \n1-->Level1\n2-->Level2')

level=input("1 or 2?: ")
while(True):
    if(level=='exit'): break
    if(level=="1"):
        count=0
        print("Ex1:")
        print('x=4\ny=6\nz=3\nb=x+y\nz=x\nprint(z,end="-")\nprint(x,end="")\nx=z+b')
        print('\n\n1--> 4-4\n\n2-->4-10\n\n3-->10-4\n\n')
        while(True):
            ex1=input('what is the correct aunser:')
            if(ex1=='1'):
                print('correct')
                count+=1
                break
            elif(ex1=='2' or ex1=='3'):
                print('fault')
                break
            else:
                print('chose one of the options below:-  ')
                print('1--> 4-4\n\n2-->4-10\n\n3-->10-4\n\n')
        print('\n\n')
        print("Ex2:")
        print('i=0\nwhile(i<5):\n    print(i,end=" ")\n    i+=1')
        print('\n\n1--> 0 1 2 3 4\n\n2-->1 2 3 4\n\n3-->0 1 2 3 4 5\n\n')
        while(True):
            ex1=input('what is the correct aunser:')
            if(ex1=='1'):
                print('correct')
                count+=1
                break
            elif(ex1=='2' or ex1=='3'):
                print('fault')
                break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> 0 1 2 3 4\n\n2-->1 2 3 4\n\n3-->0 1 2 3 4 5\n\n')
        print('\n\n')
        print("Ex3:")
        print('i=0\nwhile(i<=5):\n     i+=1\n     print(i,end=" ")')
        print('\n\n1--> 0 1 2 3 4 5 6\n\n2-->1 2 3 4 5 6\n\n3-->1 2 3 4 5\n\n')
        while(True):
            ex1=input('what is the correct aunser:')
            if(ex1=='2'):
                print('correct')
                count+=1
                break
            elif(ex1=='1' or ex1=='3'):
                print('fault')
                break
            else:
                print('chose one of the options below:-  ')
                print('\n\n1--> 0 1 2 3 4 5 6\n\n2-->1 2 3 4 5 6\n\n3-->1 2 3 4 5\n\n')
        print('\n\n')
        print("Ex4:")
        print('i=1\nSum=0\nwhile(i<=5):\n     Sum+=i\n     print(Sum,end=" ") \n     i+=1')
        print('\n\n1--> 1 3 5 6 10 15\n\n2-->1 3\n\n3-->1 3 6 10 15\n\n')
        while(True):
            ex1=input('what is the correct aunser:')
            if(ex1=='3'):
                print('correct')
                count+=1
                break
            elif(ex1=='1' or ex1=='2'):
                print('fault')
                break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> 1 3 5 6 10 15\n\n2-->1 3\n\n3-->1 3 6 10 15\n\n')
        print('\n\n')
        print("Ex5:")
        print('for i in range (5):\n     print(i,end=" ")')
        print('\n\n1--> 1 2 3 4 5\n\n2-->0 1 2 3 4 5\n\n3-->0 1 2 3 4\n\n')
        while(True):
            ex1=input('what is the correct aunser:')
            if(ex1=='3'):
                print('correct')
                count+=1
                break
            elif(ex1=='1' or ex1=='2'):
                print('fault')
                break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> 1 2 3 4 5\n\n2-->0 1 2 3 4 5\n\n3-->0 1 2 3 4\n\n')
        print('\n\n')
        print("Ex6:")
        print('for i in range (0,5):\n     print(i,end=" ")')
        print('\n\n1--> 1 2 3 4 5\n\n2-->0 1 2 3 4 5\n\n3-->0 1 2 3 4\n\n')
        while(True):
            ex1=input('what is the correct aunser:')
            if(ex1=='3'):
                print('correct')
                count+=1
                break
            elif(ex1=='1' or ex1=='2'):
                print('fault')
                break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> 1 2 3 4 5\n\n2-->0 1 2 3 4 5\n\n3-->0 1 2 3 4\n\n')
        print('\n\n')
        print("Ex7:")
        print('for i in range (0,5,2):\n     print(i,end=" ")')
        print('\n\n1--> 0 2 4\n\n2-->1 3 5\n\n3-->0 1 3\n\n')
        while(True):
            ex1=input('what is the correct aunser:')
            if(ex1=='1'):
                print('correct')
                count+=1
                break
            elif(ex1=='2' or ex1=='3'):
                print('fault')
                break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> 0 2 4\n\n2-->1 3 5\n\n3-->0 1 3\n\n')
        print('\n\n')
        print("Ex7:")
        print('x=[2,6,0,3,4,5,1]\nx.sort()\nx.reverse()\nprint(x)')
        print('\n\n1--> [1,5,4,3,0,6,2]\n\n2-->[0,1,2,3,4,5,6]\n\n3-->[6,5,4,3,2,1,0]\n\n')
        while(True):
            ex1=input('what is the correct aunser:')
            if(ex1=='3'):
                print('correct')
                count+=1
                break
            elif(ex1=='1' or ex1=='2'):
                print('fault')
                break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> [1,5,4,3,0,6,2]\n\n2-->[0,1,2,3,4,5,6]\n\n3-->[6,5,4,3,2,1,0]\n\n')
        print('\n\n')
        print("Ex9:")
        print('x=[10,20,30,40,50,60,70]\nx.sort()\nx.insert(0,0)\nx.remove(70)\ny=tuple(x)\nprint(y)\nprint(type(x))')
        print('\n\n1--> [0,10,20,30,40,50,60]\n\t<class tuple>\n\n2-->(0,10,20,30,40,50,60)\n\t<class list>\n\n3-->(0,10,20,30,40,50,60)\n\t<class tuple>\n\n')
        while(True):
            ex1=input('what is the correct aunser:')
            if(ex1=='2'):
                print('correct')
                count+=1
                break
            elif(ex1=='1' or ex1=='3'):
                print('fault')
                break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> [0,10,20,30,40,50,60]\n\t<class tuple>\n\n2-->(0,10,20,30,40,50,60)\n\t<class list>\n\n3-->(0,10,20,30,40,50,60)\n\t<class tuple>\n\n')
        print('\n\n')
        print("Ex10:")
        print('x=2\nwhile(True):\n     if(x==3):\n           break\n     if(x%2==0):\n          x+=1\n     else:\n          print("odd number",end=">")\n          x+=1\nprint("3")')
        print('\n\n1--> odd number >3\n\n2-->3\n\n3-->3 odd number>\n\n')
        while(True):
            ex1=input('what is the correct aunser:')
            if(ex1=='2'):
                print('correct')
                count+=1
                break
            elif(ex1=='1' or ex1=='3'):
                print('fault')
                break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> odd number \n\t 3\n\n2-->3\n\n3-->3\n\t odd number\n\n')
        print('\n\n')
        print("you grade is : (",count,") out of 10\n")
        print('to continue pease 2 or exit:',end="")
        r=input("")
        level=r
        
    elif(level=='2'):
        count2=0
        print('\n\n')
        print("Ex1:")
        print('for i in range (7):\n     print(i,end=" ")\n     i+=2')
        print('\n\n1--> 0 2 4 6\n\n2-->0 2 4 6 8\n\n3-->0 1 2 3 4 5 6\n\n')

        while(True):
            ex2=input("what is the correct aunser:")
            if(ex2=='3'):
                print('correct')
                count2+=1
                break
            elif(ex2=='1' or ex2=='2'):
                print('fault')
                break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> 0 2 4 6\n\n2-->0 2 4 6 8\n\n3-->0 1 2 3 4 5 6\n\n')
        print('\n\n')
        print("Ex2:")
        print('x=[10,30,60]\nfor i in range (len(x)):\n     print(i,end=" ")')
        print('\n\n1--> 10 30 60\n\n2-->0 1 2\n\n3-->1 2 3\n\n')

        while(True):
            ex2=input("what is the correct aunser:")
            if(ex2=='2'):
                print('correct')
                count2+=1
                break
            elif(ex2=='1' or ex2=='3'):
                print('fault')
                break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> 10 30 60\n\n2-->0 1 2\n\n3-->1 2 3\n\n')

            print('\n\n')
        print("Ex3:")
        print('x=[10,30,60]\nfor i in range (2):\n     print(x[i],end=" ")')
        print('\n\n1--> Error\n\n2-->0 1\n\n3-->10 30\n\n4-->10 30 60\n\n')

        while(True):
            ex2=input("what is the correct aunser:")
            if(ex2=='3'):
                print('correct')
                count2+=1
                break
            elif(ex2=='1' or ex2=='2'):
                print('fault')
                break
            elif(ex2=='4'):
                 print('fault')
                 break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> Error\n\n2-->0 1\n\n3-->10 30\n\n4-->10 30 60')
        print("Ex4:")
        print("x={'letter'"':[A,B,C],'"'num'"':[1,2,3]}\nfor i in x.values():\n    print(i,end=" ")')
        print('\n\n1--> Error\n\n2-->letter-num\n\n3-->letter [A,B,C] num [10,30,60]\n\n4-->[A,B,C] [10,30,60]\n\n')

        while(True):
            ex2=input("what is the correct aunser:")
            if(ex2=='4'):
                print('correct')
                count2+=1
                break
            elif(ex2=='1' or ex2=='2'):
                print('fault')
                break
            elif(ex2=='3'):
                 print('fault')
                 break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> Error\n\n2-->letter-num\n\n3-->letter [A,B,C] num [10,30,60]\n\n4-->[A,B,C] [10,30,60]\n\n')
        print("Ex5:")
        print('l=5+5\nx=[10,20,30,40,10,50,10]\nprint(x.count(l))')
        print('\n\n1--> Error\n\n2-->7\n\n3-->3\n\n4-->Nothing will print\n\n')

        while(True):
            ex2=input("what is the correct aunser:")
            if(ex2=='3'):
                print('correct')
                count2+=1
                break
            elif(ex2=='1' or ex2=='2'):
                print('fault')
                break
            elif(ex2=='4'):
                 print('fault')
                 break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> Error\n\n2-->7\n\n3-->3\n\n4-->Nothing will print\n\n')
        print("Ex6:")
        print('x=['"num"':19,20,25,40,18,22,17]\nfor i in x.values():\n     print(i,end=" ")')
        print('\n\n1--> Error\n\n2-->[19, 20, 25, 40, 18, 22, 17] \n\n3-->num [19,20,25,40,18,22,17]\n\n4-->num\n\n')

        while(True):
            ex2=input("what is the correct aunser:")
            if(ex2=='1'):
                print('correct')
                count2+=1
                break
            elif(ex2=='3' or ex2=='2'):
                print('fault')
                break
            elif(ex2=='4'):
                 print('fault')
                 break
            else:
                print('chose one of the options below:-   ')
                print('\n\n1--> Error\n\n2-->[19, 20, 25, 40, 18, 22, 17] \n\n3-->num [19,20,25,40,18,22,17]\n\n4-->num\n\n')
        print('\n\n')
        print("you grade is : (",count2,") out of 6")
        print('to continue press level num or exit: ',end="")
        e=input("")
        level=e
    else:
        print("1 or 2????????!: ",end=" ")
        w=input("")
        level=w
