<template>
   <div id="app">
		<info :config="getConfig" @callBack="callBackOn">
		</info>
		<button @click="submit" style="margin-top:7px">提交</button>
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
