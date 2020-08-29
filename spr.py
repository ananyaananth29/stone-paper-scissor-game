import random
print('''RULES:\n1. Enter 1 for STONE, enter 2 for PAPER, enter 3 for SCISSOR\n2. First you enter the the number and then the computer plays along \n(Don't worry the compy wont cheat)''')
n=int(input('How many number of rounds you want to play :'))
cs=us=0
flag=0
if not n>0:
    print('Playing smort ah....\nYou do one thing ......\njust consider yourself as the winner ...OK')
    flag=1
for i in range(n):
    u=int(input())
    if u not in range(1,4):
        print('READ THE INSTRUCTIONS CAREFULLY MACCHA :\\')
        flag=1
        break
    dict={1:'STONE',2:'PAPER',3:'SCISSOR'}
    print('You: {}'.format(dict[u]))
    c=random.randint(1,3)
    print('Computer: {}'.format(dict[c]))
    if (u==1 and c==2) or (u==2 and c==3) or (u==3 and c==1):
        cs+=1
    elif u==c:
        cs+=1
        us+=1
    else:
        us+=1
    print(us,cs)
    print('--------------------------------------------------------------')
if flag==0:
    print('SCORES:\nYou: {}\nComp: {}'.format(us,cs))
    print('Ahm ahm......THE WINNER ANNOUNCEMENT:')
    if us>cs:
        print('You won  \($__$)/.....Proud of you maccha!')
    elif cs>us:
        print('Chey its not you :(....Try trying again maccha')
    else:
        print('''Its a coat and 'TIE maccha' XD''')
