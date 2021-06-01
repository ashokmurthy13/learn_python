import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database",
)

cursor = con.cursor()
word = input("Enter the word: ")
query = cursor.execute("SELECT * FROM Dictionary where Expression = '%s' " % word)
result = cursor.fetchall()

# result may be empty (False)
if result:
    for item in result:
        print(item[1])
else:
    print("Word Not Found!")