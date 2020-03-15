<template>
   <div id="app">
		<number :config="getConfig" @callBack="callBackOn"></number>
		<button @click="check" style="margin-top:7px">查询</button>
	</div>
</template>

<script>
import $ajax from 'axios'
import number from './number.vue'
export default {
   name: "App",
	components: {number},
	data(){
		return{
			callBackData:null,
		}
	},
	methods:{
		callBackOn(data){
			this.callBackData = data
			console.log(data)
		},
		check(){
			console.log(this.callBackData)
			var url = ''
			// $ajax.post(url, this.callBackData,(data)=>{
				
			// })
		}
	},
	computed:{
		getConfig(){
			return [
				{name:"预约编号",type:"digit",size:[1,8]},
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
