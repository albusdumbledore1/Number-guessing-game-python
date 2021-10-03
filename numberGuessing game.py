import random
name = input ("enter your name : ")
print("hello ",name)
print("welcome to the game")
rand = random.randint(1,20)
age = int( input("enter your age "))
if (age>18):
    print("you too old to play this game nevertheless enjoy and guess a number between 1 and 10")
elif age > 12:
    print("you are perfect go ahead and guess a number between 1 and 10")
else : print ("you are still a kid nevertheless enjoy and guess a number between 1 and 10")

chances = 5
while chances > 0:
    print("no of chances left:",chances)
    guess = int(input("enter your guess : "))
    if (guess == rand):
        print("Wonderfull you won !!!")
        break
    elif(guess >rand):
        print("guess a smaller number")
    elif(guess <rand):
        print("guess a bigger number")
        
    chances = chances - 1