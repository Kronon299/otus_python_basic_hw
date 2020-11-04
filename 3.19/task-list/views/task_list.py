from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest

task_list_app = Blueprint("task_list_app", __name__)


TASKS = {
    1: 'Помыть посуду',
    2: 'Вынести мусор',
    3: 'Сходить в магазин'
}


@task_list_app.route("/")
def task_list():
    return render_template("task_list/index.html", tasks=TASKS)


@task_list_app.route("/<int:task_id>/", methods=['GET', 'DELETE'])
def task_detail(task_id: int):
    try:
        task_name = TASKS[task_id]
    except KeyError:
        raise BadRequest(f'Invalid task id #{task_id}!')

    if request.method == 'DELETE':
        TASKS.pop(task_id)
        return jsonify(ok=True)

    return render_template(
        "task_list/detail.html",
        task_id=task_id,
        task_name=task_name,
    )
