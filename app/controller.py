from app.modele import database_connect

def add_user(user, password):
    database, connect = database_connect()
    try:
        adduser = "INSERT INTO user (username, password) VALUES (%s, %s)"
        user_data = (user, password)
        database.execute(adduser, user_data)
        connect.commit()
        connect.close()
    except:
        print("error in function 'add_user'")


def add_task(title):
    database, connect = database_connect()
    try:
        addtask = "INSERT INTO task (title) VALUES (%s)"
        database.execute(addtask, title)
        connect.commit()
        connect.close()
    except:
        print("error in function 'add_task'")


def del_user(id):
    database, connect = database_connect()
    try:
        deluser = "DELETE FROM user WHERE user_id = (%s)"
        database.execute(deluser, id)
        connect.commit()
        connect.close()
    except:
        print("error in function 'del_user'")


def del_task(id):
    database, connect = database_connect()
    try:
        deltask = "DELETE FROM task WHERE task_id = (%s)"
        database.execute(deltask, id)
        connect.commit()
        connect.close()
    except:
        print("error in function 'del_task'")


def add_atribution(user_id, task_id):
    database, connect = database_connect()
    try:
        atribution = "INSERT INTO user_has_task (fk_user_id, fk_task_id) VALUES (%s, %s)"
        atribution_data = (user_id, task_id)
        database.execute(atribution, atribution_data)
        connect.commit()
        connect.close()
    except:
        print("error in function add_atribution")


def del_atribution(id):
    database, connect = database_connect()
    try:
        delatrib = "DELETE FROM user_has_task WHERE atribution_id = (%s)"
        database.execute(delatrib, id)
        connect.commit()
        connect.close()
    except:
        print("error in function 'del_task'")


def get_user():
    database, connect = database_connect()
    try:
        request_user = ("SELECT user_id, username FROM user")
        database.execute(request_user)
        user_info = database.fetchall()
        connect.close()
        return user_info
    except:
        print("error in function 'get_user'")

def get_username_from_id(id):
    database, connect = database_connect()
    id = int(id)
    try:
        request_user = ("SELECT user_id, username FROM user")
        database.execute(request_user)
        user_info = database.fetchall()
        for user in user_info:
            if user[0] == id:
                connect.close()
                return user[1]
        connect.close()
        return "no user"
    except:
        print("error in function 'get_username_from_id'")

def get_taskname_from_id(id):
    database, connect = database_connect()
    id = int(id)
    try:
        request_user = ("SELECT * FROM task")
        database.execute(request_user)
        task_info = database.fetchall()
        for task in task_info:
            if task[0] == id:
                connect.close()
                return task[1]
        connect.close()
        return "no task"
    except:
        print("error in function 'get_taskname_from_id'")

def get_task():
    database, connect = database_connect()
    try:
        request_task = ("SELECT * FROM task")
        database.execute(request_task)
        task_info = database.fetchall()
        connect.close()
        return task_info
    except:
        print("error in function 'get_task'")
def get_task_from_user(user_id):
    database, connect = database_connect()
    user_id = int(user_id)
    try:
        list_atrib_user = ()
        user_task_list = ()
        request_task = ("SELECT * FROM task")
        database.execute(request_task)
        task_list = database.fetchall()
        request_atribution = ("SELECT * FROM user_has_task")
        database.execute(request_atribution)
        atribution_list = database.fetchall()
        for atrib_user in atribution_list :
            if (atrib_user[0] == user_id):
                list_atrib_user = list_atrib_user + (atrib_user, )
        for task in task_list :
            for atrib in list_atrib_user :
                if task[0] == atrib[1] :
                    user_task_list = user_task_list + (task, )
        connect.close()
        return user_task_list
    except:
        print("error in function 'get_task_from_user'")

def get_user_from_task(task_id):
    database, connect = database_connect()
    task_id = int(task_id)
    try:
        list_atrib_task = ()
        task_user_list = ()
        request_user = ("SELECT * FROM user")
        database.execute(request_user)
        user_list = database.fetchall()
        request_atribution = ("SELECT * FROM user_has_task")
        database.execute(request_atribution)
        atribution_list = database.fetchall()
        for atrib_task in atribution_list :
            if (atrib_task[1] == task_id):
                list_atrib_task = list_atrib_task + (atrib_task, )
        for user in user_list :
            for atrib in list_atrib_task :
                if user[0] == atrib[0] :
                    task_user_list = task_user_list + (user, )
        connect.close()
        return task_user_list
    except:
        print("error in function 'get_user_from_task'")


def get_user_no_in_task(task_id):
    database, connect = database_connect()
    task_id = int(task_id)
    try:
        list_atrib_task = ()
        task_user_list = ()
        request_user = ("SELECT * FROM user")
        database.execute(request_user)
        user_list = database.fetchall()
        request_atribution = ("SELECT * FROM user_has_task")
        database.execute(request_atribution)
        atribution_list = database.fetchall()
        for atrib_task in atribution_list:
            if (atrib_task[1] == task_id):
                list_atrib_task = list_atrib_task + (atrib_task,)
        for user in user_list:
            is_user = False
            for atrib in list_atrib_task:
                if user[0] == atrib[0]:
                    is_user = True
            if not is_user:
                task_user_list = task_user_list + (user,)
        connect.close()
        return task_user_list
    except:
        print("error in function 'get_user_no_in_task'")


def unassign_user_from_task(task_id, user_id):
    task_id = int(task_id)
    user_id = int(user_id)
    database, connect = database_connect()
    try:
        request_user_has_task = "SELECT * FROM user_has_task"
        database.execute(request_user_has_task)
        atrib_list = database.fetchall()
        for atrib in atrib_list:
            if atrib[0] == user_id and atrib[1] == task_id:
                del_atribution(atrib[2])
        connect.commit()
        connect.close()
    except:
        print("error in function 'unassign_user_from_task")


def change_status(task_id):
    task_id = int(task_id)
    database, connect = database_connect()
    try:
        request_status = "SELECT status FROM task WHERE task_id = "+str(task_id)
        database.execute(request_status)
        status = database.fetchall()
        status = status[0][0]
        print(status)
        if status == "not started":
            new_id = 2
        elif status == "in progress":
            new_id = 3
        else:
            new_id = 1
        request_update = "UPDATE task SET status = '" + str(new_id) + "' WHERE task_id = " + str(task_id)
        database.execute(request_update)
        connect.commit()
        connect.close()
    except:
        print("error in function 'change_status'")
