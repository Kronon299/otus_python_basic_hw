from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import InputRequired, Regexp, Length


class AddTask(FlaskForm):
    id_field = HiddenField()
    name = StringField('Task name', [InputRequired(),
                                     Regexp(r'^[A-Za-zА-яа-я\s\-\']+$', message="Invalid task name"),
                                     Length(min=3, max=128, message="Invalid task name length")
                                     ])
    # is_done = HiddenField()
    # deleted = HiddenField()
    submit = SubmitField('Add/Update Record')