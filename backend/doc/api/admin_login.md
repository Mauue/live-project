# 管理员登录

- 请求方式
    - POST
    
- 请求URL

    `\api\bg\login`
    
- 请求参数

    |参数名|类型|说明|
    |:---|:---|:---|
    |username|string|用户名|
    |password|string|密码|

- 返回示例
    ```
    {
        "code": 0,
        "msg": "登陆成功"
        "data": null
    }
    ```

- 返回参数说明


- 错误码

|错误码|含义|
|---|---|
|0|登陆成功|
|100|密码错误|