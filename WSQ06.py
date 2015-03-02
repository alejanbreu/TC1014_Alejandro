import random
rndm=random.randint(1,100)
numbr=int(input("Guess the number between 1 and 100"))

while(numbr !=rndm):
    if(numbr>rndm):
        print("Too High")
    else:
        print("Too Low")
    numbr=int(input("Try again!"))

print("You got it")
