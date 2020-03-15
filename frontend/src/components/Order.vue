<template>
   <div id="app">
		<info :config="getConfig" @callBack="callBackOn"></info>
		<button @click="submit" style="margin-top:7px">
			<img src="../assets/submit.svg" />
			提交
		</button>
	</div>
</template>

<script>
import $ajax from 'axios'
import info from './info.vue'
export default {
   name: "App",
	components: {info},
	data(){
		return{
			MaskMaxNum:3,
			callBackData:null,
		}
	},
	methods:{
		callBackOn(data){
			this.callBackData = data
			//console.log(data)
		},
		submit(){
			//console.log(this.callBackData)  不清楚就输出看一下
			//console.log(require('../js/url').url + `/api/order`)

			if(!this.callBackData){  //因为只有全部合法才会向父组件通信，所以如果没有数据，就是输入不合法
				this.$alert('请检查输入', "false");
				return
			}
			var obj = {  //向对象里添加即将发送的数据
				name:this.callBackData[0],
				id_num:this.callBackData[1],
				phone:this.callBackData[2],
				order_num:this.callBackData[3],   //this.callBackData是输入框返回的数据，你可以直接把它console.log看一下
			}
			$ajax.post(require('../js/url.js').url + `/api/order`,obj) //post请求，/api/order是api文档里的部分
			.then(doc=>{
				doc.data.code==0 && this.$alert(doc.data.msg, "true");  //是api文档里的部分，成功
				doc.data.code==1 && this.$alert(doc.data.msg, "false");  //是api文档里的部分，失败
			}).catch(err=>{
				this.$alert("未知错误", "false");  //服务器还没搭起来
			})
		}
	},
	computed:{
		getConfig(){
			return [
				{name:"真实姓名",type:"chn",size:[2,4]},
				{name:"身份证号码",type:"digit",size:[18,18]},
				{name:"手机号码",type:"digit",size:[11,11]},
				{name:"预约口罩数量",type:"digit",size:[1,1],limit:[1,this.MaskMaxNum]},
			]
		}
	}
};
</script>

<style>
body{
	
}
#app {

}

</style>
