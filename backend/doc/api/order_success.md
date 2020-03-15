# 获取预约中签信息

- 请求方式
    - GET
    
- 请求URL

    `\api\bg\order\预约场次id`
    

- 返回示例
    ```
    {
        "code": 0,
        "data": [
            {
                "id": 2,
                "id_number": "1",
                "name": "1",
                "order_num": 3,
                "phone": "2"
            },
            {
                "id": 3,
                "id_number": "1",
                "name": "1",
                "order_num": 3,
                "phone": "3"
            }
        ],
        "msg": ""
    }
    ```

- 返回参数说明
    - 
    
- 错误码

    |错误码|含义|
    |---|---|
    |0|成功|
    |100|预约场次不存在|
    |200|该场次未开始抽签|
    