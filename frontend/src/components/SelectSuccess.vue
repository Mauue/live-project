<template>
   <div id="app">
        <img src="../assets/common/happy.png" />
            <em>恭喜您，此次中签成功！</em>      
   <div id="confirm">
       <h2>用户购买凭证</h2>
       <p>真实姓名：<br />
       <p>身份证号码：<br />
       <p>手机号码：<br />
       <p>预约口罩数量：<br />
       </p>
       </div>
   </div>
        </template>

        <style>
#app {
	max-width: 700px;
	margin:0 auto;
}
img{
    margin-top:100px;
    width:60px;
    height:60px;
    margin-left:140px;
}
h2{
     margin-left:160px;
}
em{
    padding-top:10px;
    text-decoration: none;
    font-size: 30px;
    font-style: normal;
}
#confirm{
    height:250px;
    width: 500px;
    margin:0 auto;
    margin-top:50px;
    background-color: rgb(140, 195, 250);
   border: none;
   padding:30px;
    opacity: 0.5;
}
</style>
        