<template>
   <div id="app">
		<number :config="getConfig" @callBack="callBackOn"></number>
		<button @click="check" style="margin-top:7px">
			<img src="../assets/search_s.png" />
			查询
		</button>
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
			//console.log(data)
		},
		check(){
			//console.log(this.callBackData)

			//console.log(require('../js/url').url + `/api/order`)
			if(!this.callBackData){
				this.$alert('请检查输入', "false");
				return
			}
			var obj = {
				orderid:this.callBackData[0],
			}
			$ajax.get(require('../js/url.js') + `/api/order/`,obj)
			.then(doc=>{
				doc.data.code==0 && this.$alert(doc.data.msg, "true");//成功
				doc.data.code==100 && this.$alert(doc.data.msg, "false");//预约编号不存在
				doc.data.code==200 && this.$alert(doc.data.msg, "false");//抽签未开始
				doc.data.code==300 && this.$alert(doc.data.msg, "false");//未中签
			}).catch(err=>{
				this.$alert("未知错误", "false");
			})
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
