<template>
   <div id="app">
		<info :config="getConfig" @callBack="callBackOn"></info>
		<button @click="router=5" style="margin-top:7px">登录</button>
	</div>
</template>

<script>
import $ajax from 'axios'
import info from './adminInfo.vue'
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
			console.log(data)
		},
		submit(){
			//console.log(this.callBackData)  //不清楚就输出看一下
			
			//console.log(require('../js/url').url + `/api/order`)
			if(!this.callBackData){
				this.$alert('请检查输入', "false");
				return
			}
			var obj = {
				name:this.callBackData[0],
				password:this.callBackData[1],
			}
			$ajax.post(require('../js/url.js') + `/api/bg/login`,obj)
			.then(doc=>{
				doc.data.code==0 && this.$alert(doc.data.msg, "true");
				doc.data.code==100 && this.$alert(doc.data.msg, "false");//未填写用户名或密码
				doc.data.code==200 && this.$alert(doc.data.msg, "false");//账号不存在或密码错误
			}).catch(err=>{
				this.$alert("未知错误", "false");
			})
		}
	},
	computed:{
		getConfig(){
			return [
				{name:"用户名",type:"chn",size:[2,8]},
				{name:"密码",type:"digit",size:[6,18]},
			]
        }
    }
};
</script>
