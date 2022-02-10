import time
check = True

cheese = time.sleep
names = 'oliver', 'charles', 'fred', 'karl', 
numbers = [2, 3, 5, 7]
answer = names, numbers

wname = 'sam'
wnumb = 1, 0, 4, 6, 8, 9, 10
wrong = wname, wnumb
loop = 1
userinput = ''
q = 0

question = 'What is your first name? ', 'What is a prime number bellow 10? '

good = 'that is a fantastic name!', 'thats a prime!'
bad = 'that is a terrible name!', 'that is not a prime!'

while loop != 3:
    while check is True:
        if q == 0:
            userinput = input(question[0])
            if(len(userinput)):
                check = False
                if userinput in answer[0]:
                    print(good[0])
                elif userinput in wrong[0]:
                    print(bad[0])
        elif q == 1:
            userinput = int(input(question[1]))
            if userinput in answer[1]:
                print(good[1])
                check = False
            elif userinput in wrong[1]:
                print(bad[1])
                check = False
            else:
                print('I asked {}!'.format(question[q]))
        else:
            q = 0
    loop += 1
    q += 1
    check = True

cheese(0.5)

userinput = input('choose a decimal between 1 and 0: ')
check = True
userinput = float(userinput)

while check is True:
    if userinput <= 1 and userinput >= 0.75:
        print('That\'s on the high end of things')
        check = False
    elif userinput <= 0.75 and userinput >= 0.5:
        print('That\'s on the high end of the middle')
        check = False
    elif userinput <= 0.5 and userinput >= 0.25:
        print('That\'s on the low end of the middle')
        check = False
    elif userinput <= 0.25 and userinput >= 0:
        print('That\'s on the low end of things')
        check = False
    else:
        print('That ain\'t between 1 and 0!')

