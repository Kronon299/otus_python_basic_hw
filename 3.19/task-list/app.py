from flask import Flask, render_template
from flask_migrate import Migrate

from views import task_list_app
import config
from models import db

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
    SECRET_KEY="powerful_secret_key",
    WTF_CSRF_SECRET_KEY="a_csrf_secret_key"
)
app.register_blueprint(task_list_app, url_prefix="/task_list")

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/", methods=["GET", "POST"])
def index_view():
    return render_template('index.html')
