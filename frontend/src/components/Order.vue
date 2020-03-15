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
			if(!this.callBackData){
				this.$alert('请检查输入', "false");
				return
			}
			var obj = {
				name:this.callBackData[0],
				identity:this.callBackData[1],
				phone:this.callBackData[2],
				number:this.callBackData[3],
			}
			$ajax.post(require('../js/url.js') + `/api/order`,obj)
			.then(doc=>{
				doc.data.code==0 && this.$alert(doc.data.msg, "true");
				doc.data.code==1 && this.$alert(doc.data.msg, "false");
			}).catch(err=>{
				this.$alert("未知错误", "false");
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
