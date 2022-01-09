# importing required libraries
import mysql.connector
import yaml
from googletrans import Translator
translater = Translator()

#vn

with open('vn/newbie_task_qa.yml', 'r') as file, open('ph/newbie_task_qa.yml', 'r') as english:
    prime_service = yaml.safe_load(file)
    prime = yaml.safe_load(english)
for i in range (0,11):
    question = prime_service["qa"]["question"][i]["question"]
    country = 'vn'
    question_id = prime_service["qa"]["question"][i]["id"]
    answer = ''
    answer_in_english = ''
    question_in_english = prime["qa"]["question"][i]["question"]
    for j in range(0,len(prime_service["qa"]["question"][i]["choices"])): 
        answer = prime_service["qa"]["question"][i]["choices"][j]
        answer_in_english = prime["qa"]["question"][i]["choices"][j]
        print(answer_in_english)