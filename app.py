import pymysql.cursors

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():

    # Connect to the database
    connection = pymysql.connect(host='mrbartucz.com',
                                 user='lg6757bu',
                                 password='password',
                                 db='lg6757bu_University',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:

            #search by user input
            name = input("Enter a first name to search: ")
            sql = "SELECT * from Students WHERE firstName LIKE %s"

            # execute the SQL command
            cursor.execute(sql, (name,))

            #data = cursor.fetchall()

            #result = dict(data)
                
            # get the results
            for result in cursor:
                print (result)
                
                
            
    finally:
        connection.close()
    
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
