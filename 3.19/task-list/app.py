from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .views import task_list_app
from . import config

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
)
app.register_blueprint(task_list_app, url_prefix="/task_list")

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/", methods=["GET", "POST"])
def index_view():
    return render_template('index.html')
