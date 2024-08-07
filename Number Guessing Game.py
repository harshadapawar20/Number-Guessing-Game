import random

rd = random.randint(1,9)
guess = 0
c = 0

while guess!=rd and guess!=rd:
    guess = input("Enter the guess between 1 to 9: ")
    
    if guess=='exit':
        break
    
    guess = int(guess)
    c=c+1

    if guess>rd:
        print("Too high!")

    elif guess<rd:
        print("Too low!")

    else:
        print("Right!")
        print("You took only",c,"tries")
        break
              
    


