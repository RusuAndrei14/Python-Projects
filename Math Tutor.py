#import modules
# ask how many questions user wants
#set score start at zero
#loop through number of questions
# create two random numbers and calc answer
# show user the question
# capture answer and modify user score
# output final score 
from random import randrange as r
from time import time as t
questions = int(input("How many questions do you want?"))
score = 0
start = t()
answer_list = []
for q in range(questions):
    num1 = r(1,11)
    num2 = r(1, 11)
    answer = num1 * num2
    user_answer = int(input(f'{num1} x {num2} = '))
    answer_list.append(f'{num1} x {num2} = {answer}. Your answer was {user_answer}')
    if user_answer == answer:
       score = score+1
    end = t()  
print(f"Thanks for playing! Your score is {score} out of {questions} and you % is {round(score/questions)*100}. You spent {round(end-start,1)} seconds")
for a in answer_list:
    print (a)
