# Python-Projects
Trying to get better at Python and also sharing my progress
print('Guessing game')
i = 3
number = 33
while i!=0:
      guess = int(input("What is your guess?"))
      if guess == number:
         print("You won!")
         break
      if guess > number:
           print("Too high")
      else:
           print("Too low")
      i=i-1        
if(i == 0):
    print("You lost!")          
         
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box
#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)

