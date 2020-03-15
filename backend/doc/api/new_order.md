# 提交预约信息

- 请求方式
    - POST
    
- 请求URL

    `/api/order`
    
- 请求参数

    |参数名|类型|说明|
    |:---|:---|:---|
    |name|string|名字|
    |phone|string|电话|
    |id_num|string|身份证号|
    |order_num|string|订单数量|


- 返回示例
   ```
   {
        "code": 0,
        "msg": "登录成功"
        "data": null
    }
   ```


- 返回参数说明

    无
- 错误码

    |错误码|含义|
    |---|---|
    |0|登录成功|
    |111|未填写指定信息|