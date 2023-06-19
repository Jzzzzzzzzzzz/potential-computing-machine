#Урок 9,10 на Python  не был


import sqlite3

'''try:
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
except sqlite3.DatabaseError:
    print("Ошибка открытия")
finally:
    connection.close()
'''
class User:
    def __init__(self,name=None,surname=None,gender=None):
        self.name = name
        self.surname = surname
        self.gender = gender

def create_teable_users(cursor):
    command = """
       CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,name TEXT, surname TEXT,gender TEXT);
       """

    cursor.execute(command)

def add_user(cursor,user):
    command = """
    INSERT INTO users (name,surname,gender) VALUES (?,?,?)
    """
    cursor.execute(command, (user.name, user.surname, user.gender))

def get_users_list(cursor):
    command = """
    
    SELECT * FROM users;
    
    """
    result = cursor.execute(command)
    users = result.fetchall()

    return users

def get_user(cursor,user_id):
    command = """
    SELECT * FROM USERS WHERE id =  ?;
    """
    result=cursor.execute(command,(user_id,))
    user = result.fetchall()
    return user

def update_user_name(cursor,new_name,user_id):
    command = """
    UPDATE users SET name = ? WHERE ID = ?;
    """
    cursor.execute(command,(new_name,user_id))

def delete_users(cursor):
    command = """
    DELETE FROM USERS;
    """
    cursor.execute(command)

def gender(cursor,gender:str):
    command = """
    SELECT * FROM users WHERE gender = ?
    """
    result_of_gender=cursor.execute(command,(gender,))

    return result_of_gender.fetchall()




def delete_users_with_id(cursor,id):

    command = """
    DELETE FROM users WHERE id = ?
    """
    cursor.execute(command,(id,))


if __name__ =="__main__":
    with sqlite3.connect('date.db') as cursor:


        create_teable_users(cursor)
        delete_users(cursor)
        user_1 = User('Максим','Иванов','М')
        add_user(cursor,user_1)
        add_user(cursor,User('Владимир','Петров','М'))
        add_user(cursor, User('Катя', 'Кузнецова', 'Ж'))
        print(gender(cursor,("М")))
        n=0
        for i in gender(cursor,("М")):
            n+=1
        print(f"В списке(или же таблице) {n} человек мужского пола ")
        print(gender(cursor,("Ж")))
        n=0
        for i in gender(cursor, ("Ж")):
            n += 1
            print(gender(cursor,("М")))
        print(f"В списке(или же таблице) {n} человек женского пола ")
       # delete_users_id(cursor, 1)
        print(get_users_list(cursor))
        #update_user_name(cursor,"Dima",2)
        #print(get_user(cursor,1))


#До встречи!Удачи!!