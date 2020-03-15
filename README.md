# live-project


## 后端部署方法
[链接](backend/README.md)

## 前端部署方法

[链接](frontend/README.md)

## 合并部署方法

配置Nginx

    ```
        server {
            listen 80;
            root <frontend生成的目录路径>;
            index index.html
            server_name  localhost;
            
            location /api/ {
                    rewrite ^(/api/.*) /$1 break; 
                    proxy_pass http://localhost:<服务端的端口号>;
            }  
        }
    ```
