import dbhelper as db
import mariadb

print('would you like to sign up for a new accout or sign into an existing')
print('1: sign_in')
print('2: sign_up')
 
users_choice = input('enter your selection:')

 
def sign_up():
    cursor = db.connect_db()
    results = db.execute_statment('CALL user_sign_up(?,?)', [username, password])
    db.close_connect(cursor)
    username = input('username:')
    password = input('password:')
    print(results)



def sign_in():
    cursor = db.connect_db()
    results = db.execute_statment(cursor, 'CALL user_sign_in(?,?)')
    db.close_connect(cursor)
    print(results)



if(users_choice == 1):
    sign_in()
elif(users_choice == 2):
    sign_up()


# print('1: create new fighter')
# print('2: Pick existing fighter')