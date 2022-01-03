
# importing required libraries
import mysql.connector
import yaml
from googletrans import Translator
translater = Translator()
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
    id INT NOT NULL,
    country VARCHAR(1000) NOT NULL,
    question_id INT NOT NULL,
    question VARCHAR(1000) NOT NULL,
    answer VARCHAR(10000) NOT NULL,
    question_in_english VARCHAR(1000) NOT NULL,
    answer_in_english VARCHAR(1000) NOT NULL,

    PRIMARY KEY (id)
)""")
def write_data(id, country, question_id, question, answer, question_in_english, answer_in_english):
    # preparing a cursor object
    cursorObject = dataBase.cursor()
  
    sql = "INSERT INTO VNN_vn (id, country, question_id, question, answer, question_in_english, answer_in_english)\
    VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (id, country, question_id, question, answer, question_in_english, answer_in_english)

    cursorObject.execute(sql, val)
    dataBase.commit()

#vn

with open('vn/newbie_task_qa.yml', 'r') as file:
    prime_service = yaml.safe_load(file)
for i in range (0,11):
    answer = ''
    answer_in_english=''
    for j in range(0,len(prime_service["qa"]["question"][i]["choices"])):
        id = prime_service["qa"]["question"][i]["id"]
        question = prime_service["qa"]["question"][i]["question"]
        country = 'vn'
        question_id = prime_service["qa"]["question"][i]["id"]
        question_in_english= translater.translate (question, dest="en")
        a = prime_service["qa"]["question"][i]["choices"][j]
        answer = answer + a + '\n'
        answer_in_english= translater.translate (answer_in_english, dest="en")
    write_data(id, country, question_id, question, answer, question_in_english, answer_in_english)

