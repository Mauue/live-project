<!--未完成-->
<template>
   <div id="app">
		<div id="message">
            <img src="../assets/cross.svg" />预约失败！
        </div>
        <p class="word">失败原因可能如下，请检查自身情况：</p>
        <p class="word">1.您的手机号或身份证号已经在本次摇号登记过了</p>
        <p class="word">2.您的手机号或者身份证号在此前三次预约中成功中签</p>
        <p class="word">3.如以上情况皆不符合，请联系工作人员核实</p>
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
    margin-left: 180px;
}

</style>