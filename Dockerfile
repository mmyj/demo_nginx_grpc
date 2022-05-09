
# 从alpine镜像运行程序
FROM python:3.8.12-buster@sha256:c60308189ecec21e11a8ec842393c0ba6015de05e2d7e1aeafaaeb7bd41fe115
COPY . /code
RUN python -m pip install virtualenv -i http://192.168.50.20:3002/repository/pypi/simple --trusted-host 192.168.50.20
RUN bash -c "source /code/venv/bin/activate"
RUN python -m pip install -r /code/requirements.txt -i http://192.168.50.20:3002/repository/pypi/simple --trusted-host 192.168.50.20
WORKDIR /code
