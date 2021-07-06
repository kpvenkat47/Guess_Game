import colorama
from colorama import Fore
from colorama import Style
import random
colorama.init()
count=5 #5 chances
v=random.randint(0,11) # generate int 0-10  automatically
print(Fore.LIGHTMAGENTA_EX+ Style.BRIGHT + "I have one number try to guess me within range(0-10) you have 5 chance,lets start!" + Style.RESET_ALL)
#5 chances user have
while count>0:
    c=count
    n =int(input("Enter: "))
    #check the conditions user input "Equal" or "Less" or "Greater"
    if (n>0)and(n<11):
        if(n==v):
            print(Fore.CYAN + Style.DIM + f"congratz your guess correct at {5-count+1} chance" + Style.RESET_ALL)
            freq=500
            dur=500
            break
        elif(n>v):
            print(f"value is high,you only have {c-1} chance")
        elif(n<v):
            print(f"value is low,you only have {c-1} chance")
        count-=1
    #User input give an out of range value    
    else:
        print("not valid value please enter 0 to 10")
        continue
#lost the 5 chances game over        
else:
    print(Fore.LIGHTRED_EX + Style.DIM + f"Game Over,Well Try buddy answer is {v} \U0001F606" + Style.RESET_ALL)
