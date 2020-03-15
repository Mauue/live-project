<!--未完成-->
<template>
   <div id="app">
		<div id="message">
            <img src="../assets/yes.svg" />预约成功！
        </div>
        <p class="word">您的预约编号为：</p>
        <p class="word">本次摇号结束后，可凭此编号进行查询</p>
		<button @click="back" style="margin-top:7px">返回界面</button>
	</div>
</template>


<style>
body{
	
}
#message {
    font-size: 30px;
    margin-left: 250px;
}
.word{
    margin-left: 250px;
}

</style>