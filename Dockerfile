FROM python:3.8.12-buster@sha256:c60308189ecec21e11a8ec842393c0ba6015de05e2d7e1aeafaaeb7bd41fe115
COPY . /code
RUN python -m pip install virtualenv
RUN bash -c "source /code/venv/bin/activate"
RUN python -m pip install -r /code/requirements.txt
WORKDIR /code
