from flask import render_template, request, redirect, url_for
from app import app
from app.controller import *


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def list_task():
    return render_template("page/list_task.html",
                           title="epytodo task liste",
                           list=get_task(),
                           title_body="Liste of tasks")


@app.route('/users', methods=['GET'])
def list_user():
    return render_template("page/list_user.html",
                           title="epytodo users liste",
                           list=get_user(),
                           title_body="Liste of users")

@app.route('/user/<int:user_id>', methods=['POST','GET'])
def list_task_from_user(user_id):
    if request.method == 'POST':
        del_user(user_id)
        return redirect(url_for("list_user"))
    else:
        return render_template("page/list_task.html",
                                title="task of"+get_username_from_id(user_id),
                                list=get_task_from_user(user_id),
                                title_body="task of '"+get_username_from_id(user_id)+"'",
                                delete_title="the user "+get_username_from_id(user_id),
                                delete=True)

@app.route('/task/<int:task_id>', methods=['POST', 'GET'])
def list_user_from_task(task_id):
    if request.method == 'POST':
        del_task(task_id)
        return redirect(url_for("list_task"))
    else:
        return render_template("page/list_user.html",
                               title="user of",
                                list=get_user_from_task(task_id),
                                title_body="User assign to '"+get_taskname_from_id(task_id)+"'",
                                delete_title="the task "+get_taskname_from_id(task_id),
                                in_task=True,
                                task_id = task_id)

@app.route('/user/add_user', methods=['POST', 'GET'])
def add_user_view():
    if request.method == 'POST':
        add_user(request.form["username"], request.form["pass"])
        return redirect(url_for("list_user"))
    else:
        return render_template("page/add_user.html",
                               title="registered user",
                               title_body="add user to the database")


@app.route('/task/add_task', methods=['POST', 'GET'])
def add_task_view():
    if request.method == 'POST':
        add_task(request.form["title"])
        return redirect(url_for("list_task"))
    else:
        return render_template("page/add_task.html",
                               title="add task",
                               title_body="add task to the database")


@app.route('/task/<int:task_id>/add_user', methods=['POST', 'GET'])
def add_user_to_task_view(task_id):
    if request.method == 'POST':
        add_atribution(request.form["button_add_asign"], task_id)
        return redirect("/task/"+str(task_id))
    return render_template("page/user_to_task.html",
                           list=get_user_no_in_task(task_id),
                           title="asign user to task",
                           title_body="add user to the task "+get_taskname_from_id(task_id),
                           taskname=get_taskname_from_id(task_id))


@app.route('/<int:task_id>/unassign/<int:user_id>', methods=['GET'])
def unassign_user_from_task_view(task_id, user_id):
    unassign_user_from_task(task_id, user_id)
    return redirect('/task/'+str(task_id))

@app.route('/task/<int:task_id>/status', methods=['GET'])
def change_status_view(task_id):
    change_status(task_id)
    return redirect(url_for("list_task"))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page/yapadepano.html'), 404
