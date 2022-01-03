
# importing required libraries
import mysql.connector
import yaml

dataBase = mysql.connector.connect(
host ="localhost",
port = "3307",
user ="admin",
password ="password",
tls_versions= ["TLSv1.2", "TLSv1.3"],
database ="user"
)

# preparing a cursor object
cursorObject = dataBase.cursor()
# drop table VNN
query ="DROP TABLE VNN_vn;"
 
cursorObject.execute(query)
dataBase.commit()
# creating database
cursorObject.execute("""CREATE TABLE VNN_vn (
    id INT NOT NULL AUTO_INCREMENT,
    country VARCHAR(1000) NOT NULL,
    question_id INT NOT NULL,
    question VARCHAR(1000) NOT NULL,
    answer VARCHAR(10000) NOT NULL,

    PRIMARY KEY (id)
)""")
def write_data(country, question_id, question, answer):
    # preparing a cursor object
    cursorObject = dataBase.cursor()
  
    sql = "INSERT INTO VNN_vn (country, question_id, question, answer)\
    VALUES (%s, %s, %s, %s)"
    val = (country, question_id, question, answer)

    cursorObject.execute(sql, val)
    dataBase.commit()

#vn

with open('vn/newbie_task_qa.yml', 'r') as file:
    prime_service = yaml.safe_load(file)
for i in range (0,11):
    question = prime_service["qa"]["question"][i]["question"]
    country = 'vn'
    question_id = prime_service["qa"]["question"][i]["id"]
    answer = ''
    for j in range(0,len(prime_service["qa"]["question"][i]["choices"])): 
        answer = prime_service["qa"]["question"][i]["choices"][j]
        write_data(country, question_id, question, answer)
#th

with open('th/newbie_task_qa.yml', 'r') as file:
    prime_service = yaml.safe_load(file)
for i in range (0,11):
    question = prime_service["qa"]["question"][i]["question"]
    country = 'th'
    question_id = prime_service["qa"]["question"][i]["id"]
    answer = ''
    for j in range(0,len(prime_service["qa"]["question"][i]["choices"])): 
        answer = prime_service["qa"]["question"][i]["choices"][j]
        write_data(country, question_id, question, answer)

#ph

with open('ph/newbie_task_qa.yml', 'r') as file:
    prime_service = yaml.safe_load(file)
for i in range (0,11):
    question = prime_service["qa"]["question"][i]["question"]
    country = 'ph'
    question_id = prime_service["qa"]["question"][i]["id"]
    answer = ''
    for j in range(0,len(prime_service["qa"]["question"][i]["choices"])): 
        answer = prime_service["qa"]["question"][i]["choices"][j]
        write_data(country, question_id, question, answer)

#id

with open('id/newbie_task_qa.yml', 'r') as file:
    prime_service = yaml.safe_load(file)
for i in range (0,11):
    question = prime_service["qa"]["question"][i]["question"]
    country = 'id'
    question_id = prime_service["qa"]["question"][i]["id"]
    answer = ''
    for j in range(0,len(prime_service["qa"]["question"][i]["choices"])): 
        answer = prime_service["qa"]["question"][i]["choices"][j]
        write_data(country, question_id, question, answer)
