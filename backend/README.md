## 运行方式
运行环境
- Python3.7或3.7以上版本 (测试环境为Python3.7)

运行方式
1. 安装依赖库
    ```
    pip install -r requirements.txt
    ```
2. 配置
    1. 设置环境变量
        windows:    
        ```
        set FLASK_APP=main
        ```
        linux:
        ```
        export FLASK_APP=main
        ```
    2. 初始化数据库
    
        在config_local.py中配置数据库信息
        
        然后执行
        ```
        flask init-db
        ```
    3. 注册管理员账号
        ```
        flask register -u 用户名 -p 密码
        ```
   
3. 运行
    ```
    flask run -p 端口号 --host 地址
    ```


