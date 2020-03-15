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
			console.log(this.callBackData)
			var url = ''
			// $ajax.post(url, this.callBackData,(data)=>{
				
			// })
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
