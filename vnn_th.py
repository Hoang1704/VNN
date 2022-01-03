
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
# drop table 
query ="DROP TABLE VNN_th;"
 
cursorObject.execute(query)
dataBase.commit()
# creating database
cursorObject.execute("""CREATE TABLE VNN_th (
    id INT NOT NULL,
    country VARCHAR(1000) NOT NULL,
    question_id INT NOT NULL,
    question VARCHAR(1000) NOT NULL,
    answer VARCHAR(10000) NOT NULL,

    PRIMARY KEY (id)
)""")
def write_data(id, country, question_id, question, answer):
    # preparing a cursor object
    cursorObject = dataBase.cursor()
  
    sql = "INSERT INTO VNN_th (id, country, question_id, question, answer)\
    VALUES (%s, %s, %s, %s, %s)"
    val = (id, country, question_id, question, answer)

    cursorObject.execute(sql, val)
    dataBase.commit()

#th

with open('th/newbie_task_qa.yml', 'r') as file:
    prime_service = yaml.safe_load(file)
for i in range (0,11):
    answer = ''
    for j in range(0,len(prime_service["qa"]["question"][i]["choices"])):
        id = prime_service["qa"]["question"][i]["id"]
        question = prime_service["qa"]["question"][i]["question"]
        country = 'th'
        question_id = prime_service["qa"]["question"][i]["id"] 
        a = prime_service["qa"]["question"][i]["choices"][j]
        answer = answer + a + '\n'
    write_data(id, country, question_id, question, answer)

