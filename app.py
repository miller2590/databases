from user import User
from database import Database

Database.initialise(database='DataBase Name', host='Host Name', user='User Name', password='Password')

user = User('JohnDoe@gmail.com', 'John', 'Doe', None)

user.save_to_db()

user_from_db = user.load_from_db_by_email('JohnDoe@gmail.com')

print(user_from_db)
