import random
num=random.randint(1,3)
guesses=0
print('Hello! In this mimi game you need guess a nummer.\nYou have 3 guesses.\nGood luck!\nEnter random number from 1 to 10')
while guesses < 3:
    guess=int(input())
    guesses +=1
    if guess == num:
        print('Exactly!')
    if guess > num:
        print('Oh no! Its too high!')
    if guess < num:
        print('So low!')
    if guesses ==3:
        print('Hey! How did you lose? It was '+str(num)+"!")
        break
    if guess ==num:
        print('That was easy for you!')
        break