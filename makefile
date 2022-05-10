test=1

.PHONY: build protos up down

build:
	docker build -t demo_nginx_grpc .

protos:
	mkdir -p ./protos/gen
	python -m grpc_tools.protoc -Iprotos/src --python_out=./protos/gen --grpc_python_out=./protos/gen ./protos/src/*

up: protos
	docker compose  -f docker-compose-$(test).yml up

down:
	docker compose  -f docker-compose-$(test).yml down

