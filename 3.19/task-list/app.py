from flask import Flask, render_template

from views import task_list_app

app = Flask(__name__)
app.register_blueprint(task_list_app, url_prefix="/task_list")


@app.route("/", methods=["GET", "POST"])
def index_view():
    return render_template('index.html')
