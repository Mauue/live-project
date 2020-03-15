#  设置新的一批预约

- 请求方式
    - POST
    
- 请求URL

    `\api\bg\order\set`
    
- 请求参数

    |参数名|类型|说明|
    |:---|:---|:---|
    |start_time|datetime|开始时间|
    |end_time|datetime|结束时间|
    |total|int|总数|
    |order_max|tinyint|预约总量|

- 返回示例
    ```
    {
        "code": 0,
        "msg": "设置成功"
        "data": null
    }
    ```

- 返回参数说明
    - 
    