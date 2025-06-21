import random
"""
1 for snake
-1 for water
0 for gun
"""
computer= random.choice([1,-1,0])
user= input("Enter your choice: ")
dict= {"s":1, "w":-1, "g": 0}
reverse_dict= {1: "Snake",-1:"Water",0:"Gun"}

you= dict[user]

print(f'you choose {reverse_dict[you]} \n computer choose{reverse_dict[computer]}')

if (computer== you):
    print ("It's a Draw!")
else:
    if (computer==1 and you==-1):
        print("you loose!")
    elif(computer==1 and you==0):
        print("you win!")
    elif(computer==0 and you==1):
        print("you loose!")
    elif(computer==0 and you==-1):
        print("you win!")
    elif(computer==-1 and you==1):
        print("you win!")
    elif(computer==-1 and you==0):
        print("you loose!")
    else:
        print("something went wrong")
