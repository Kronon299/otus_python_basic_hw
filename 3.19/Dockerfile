FROM python:3.8.6-buster

WORKDIR /app

# install and configure poetry for requirements version control
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY task-list/pyproject.toml task-list/poetry.lock ./

RUN poetry install --no-interaction --no-ansi

# Expose project services
EXPOSE 5000

COPY task-list .

CMD ["python", "main.py"]