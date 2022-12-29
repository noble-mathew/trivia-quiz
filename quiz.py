"""
Playground:
Write code for fun
"""

## Library Imports 

import requests
import random
import base64
import json
import pp

# Category Code Setup

category_codes = {
    "any category": "",
    "general knowledge": "9",
    "books": "10",
    "film": "11",
    "music": "12",
    "musicals and theaters": "13",
    "television": "14",
    "video games": "15",
    "board games": "16",
    "science and nature": "17",
    "computers": "18",
    "mathematics": "19",
    "mythology": "20",
    "sports": "21",
    "geography": "22",
    "history": "23",
    "politics": "24",
    "art": "25",
    "celebrities": "26",
    "animals": "27",
    "vehicles": "28",
    "comics": "29",
    "gadgets": "30",
    "japanese anime and manga": "31",
    "cartoon and animations": "32"
    }

## Variables for Question Loops

valid_question_count = False
valid_category = False
valid_difficulty = False
valid_question_type = False

## Choosing Number of Questions

while not valid_question_count:
    
    question_count = input("How many questions would you like to have? ")
    
    if int(question_count) < 1:
        print("\nYou must enter a number greater than 0.")
        print()
    else:
        break

## Choosing Category

print("\nHere's a list of all the categories: ")
for key in category_codes.keys():
    print("\t" + "- " + key)
    
print()

while not valid_category:
    
    category = (input("Which category would you like to select? ")).lower()
    
    if category not in category_codes.keys():
        print("\nThat is not a valid category.")
    else:
        break

## Choosing Difficulty

print()

while not valid_difficulty:
    
    difficulty = (input("What difficulty would you like the questions to be: Easy, Medium, Hard, or Any Difficulty? ")).lower()
    
    if difficulty != "easy" and difficulty != "medium" and difficulty != "hard" and difficulty != "any difficulty":
        print("\nThat is not a valid difficulty option.")
    else:
        break

## Choosing Question Type

print()

while not valid_question_type:
    
    question_type = (input("What type of questions would you like to be asked: Multiple Choice, True or False, or Any Type? ")).lower()
    question_param = ""

    if question_type == "multiple choice":
        question_param = "multiple"
        break
    elif question_type == "true or false":
        question_param == "boolean"
        break
    elif question_type == "any type":
        question_param == ""
        break
    else:
        print("\nThat is not a valid question type.")

## Accessing the API

base = "https://opentdb.com/api.php"
parameters = {"amount": question_count, "category": category_codes[category], "difficulty": difficulty, "type": question_param, "encode": "base64"}

response = requests.get(base + "/", params=parameters)
collection = response.json()
questions = collection["results"]

## Status Code Error

if response.status_code != 200:
    print("Error code: " + str(response.status_code))
    
## Keep Track of Questions Answered Correctly

correct = 0

## Trivia Loop

print("\n-- TRIVIA TIME -- ")
print("** When answering, please respond with the number correlating to the answer choice you believe to be correct. **")
input("Please press ENTER to begin the quiz.")

for index, key in enumerate(questions):

    if index == int(question_count) + 1:
        break
        
    ## Display the Question
    
    question =  base64.b64decode(key["question"])
    print("\nQUESTION " + str(index+1))
    print(question)
    
    ## Decode the Right and Wrong Answers

    answers = []
    answers.append(base64.b64decode(key["correct_answer"]))
    for incorrect in key["incorrect_answers"]:
        answers.append(base64.b64decode(incorrect))
    answers.sort()

    ## Display Answer Choices

    for number, answer in enumerate(answers):
        print("\t" + str(number+1) + ": " + answer)

    ## User's Guess

    response = input()

    ## Question Result

    if answers[int(response)-1] == base64.b64decode(key["correct_answer"]):
        print("\nThat's right!")
        correct += 1
    else:
        print("\nThe correct answer was " + base64.b64decode(key["correct_answer"]) + ".")

    input("Press ENTER to continue.")
    
## Final Score

print("\nYou scored a " + str(int((correct / int(question_count)) * 10))+ "0%")
    
