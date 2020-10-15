from flask import Blueprint, render_template

task_list_app = Blueprint("product_app", __name__)


@task_list_app.route("/")
def task_list():
    return render_template("task_list/index.html")
