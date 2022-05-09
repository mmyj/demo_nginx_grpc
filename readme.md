https://www.nginx.com/blog/nginx-1-13-10-grpc/

`make protos` 编译 protobuff

`make build` 构建镜像

`make test=1 up/down` 开始运行 1_directly demo，客户端与服务端 p2p 访问

`make test=2 up/down` 开始运行 2_load_balancing demo，客户端与服务端在 nginx 做轮询负载均衡