# 获取所有预约场次信息

- 请求方式
    - GET
    
- 请求URL

    `\api\bg\order`
    

- 返回示例
    ```
    {
        "code": 0,
        "data": [
            {
                "end_time": "2020-05-10 10:00:11",
                "id": 5,
                "order_max": 2,
                "start_time": "2020-04-10 10:00:00",
                "status": 0,
                "total": 100
            },
            {
                "end_time": "2020-05-10 10:00:11",
                "id": 4,
                "order_max": 2,
                "start_time": "2020-04-10 10:00:00",
                "status": 1,
                "total": 100
            },
            {
                "end_time": "2020-05-10 10:00:11",
                "id": 3,
                "order_max": 2,
                "start_time": "2020-04-10 10:00:00",
                "status": 1,
                "total": 100
            },
            {
                "end_time": "2020-03-15 16:14:10",
                "id": 1,
                "order_max": 3,
                "start_time": "2020-03-15 16:14:08",
                "status": 1,
                "total": 10
            }
        ],
        "msg": ""
    }
    ```

- 返回参数说明
    - 
    