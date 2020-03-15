<template>
   <div class="number">
      <div id="header">请输入预约编号</div>
      <section v-for="(item,i) in config" :key="item.name">
         <div>{{item.name}}</div>
         <div style="color:#ED9E7E" v-if="!inputValid[i]">
            <img src="../assets/common/t.svg" />
            {{"请检查您的输入"}}
         </div>
         <div style="color:#BFECD3" v-else>
            <img src="../assets/common/f.svg" />
            {{"OK"}}
         </div>
         <input :placeholder="'请输入'+item.name" @input="checkInput(item,i)" 
			 v-model="inputText[i]" :key="item.name" :maxlength="item.size[1]">
      </section>
   </div>
</template>

<script>
export default {
   name: "number",
   props: {
		config:{
			type:Array
		}
	},
	data(){
		return{
			inputText:[],
			inputValid:[0,0,0,0,0,0],
			
		}
	},
	computed:{
		
	},
	methods:{
		checkInput(item, index){
			var type = item.type
			var min = item.size[0]
			var max = item.size[1]
			var text = this.inputText[index]
			var t = false
			if(type=='digit'){
				t = /^[0-9]+$/g.test(text) && text.length>=min && text.length<=max
				this.inputValid[index] = Boolean(t)
				if(item.limit && text<item.limit[0] && text) this.inputText[index]=item.limit[0]
				if(item.limit && text>item.limit[1] && text) this.inputText[index]=item.limit[1]
			}
			if(type=='chn'){
				t = /^[^\x00-\xff]+$/g.test(text) && text.length>=min && text.length<=max
				this.inputValid[index] = Boolean(t)
			}
			var flag = true
			for(let i=0;i<this.config.length;i++){
				let v = this.inputValid[i]
				if(!v) flag = false
			}
			if(flag) this.$emit('callBack',this.inputText)
			else  this.$emit('callBack',{})
		}
	}
};
</script>


<style scoped>
.number {
   margin: 0 auto;
   width:600px;
	padding:10px 10px;
}
#header {
}
#header::before {
   display: inline-block;
   height: 16px;
   width: 4px;
   content: "";
   background-color: #1285f8;
   margin: 0px 10px -3px 0;
   border-radius: 5px;
}
.number section:nth-of-type(1) {
   margin-top: 10px;
   border-top: 1px #eee solid;
}
section {
   overflow: hidden;
   border-bottom: 1px #eee solid;
   padding: 10px;
   color: #444;
}
section div:nth-child(1),
section div:nth-child(2) {
   float: left;
}
section div:nth-child(2) {
   margin-left: 8px;
   font-size: 14px;
}
section div:nth-child(2) img {
   width: 18px;
   margin-bottom: -4px;
   margin-right: 4px;
}
section input {
   border: none;
   outline: none;
   font-size: 16px;
   float: right;
   text-align: right;
}
section input::-webkit-input-placeholder {
   color: #ccc;
}
</style>
