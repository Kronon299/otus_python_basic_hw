from flask import Blueprint, render_template, request, jsonify, flash
from werkzeug.exceptions import BadRequest

from forms import AddTask
from models import Task, db

task_list_app = Blueprint("task_list_app", __name__)


@task_list_app.route("/")
def task_list():
    tasks = Task.query.order_by(Task.id).all()
    return render_template("task_list/index.html", tasks=tasks)


@task_list_app.route("/<int:task_id>/", methods=['GET', 'DELETE'])
def task_detail(task_id: int):
    task = Task.query.filter_by(id=task_id).one_or_none()
    if task is None:
        raise BadRequest(f'Invalid task id #{task_id}!')

    if request.method == 'DELETE':
        task.deleted = True
        db.session.commit()
        return jsonify(ok=True)

    return render_template("task_list/detail.html", task=task)


@task_list_app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    task_form = AddTask()
    if task_form.validate_on_submit():
        name = request.form['name']
        # the data to be inserted into Task model
        task = Task(name)
        # Flask-SQLAlchemy magic adds record to database
        db.session.add(task)
        db.session.commit()
        # create a message to send to the template
        message = f"The data for task {name} has been submitted."
        return render_template('task_list/add_record.html', message=message)
    else:
        for field, errors in task_form.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(task_form, field).label.text,
                    error
                ), 'error')
        return render_template('task_list/add_record.html', task_form=task_form)
