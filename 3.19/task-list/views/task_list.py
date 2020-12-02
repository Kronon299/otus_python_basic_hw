from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest

from models import Task, db

task_list_app = Blueprint("task_list_app", __name__)


@task_list_app.route("/")
def task_list():
    tasks = Task.query.filter_by(deleted=False).all()
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
