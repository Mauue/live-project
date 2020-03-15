<template>
   <div class="info">
      <header>个人信息</header>
      <section>
			<div>真实姓名</div>
			<div style="color:#ED9E7E">
				<img src="../assets/common/t.svg">姓名字数过多！
			</div>
			<input type="number" placeholder="请输入真实姓名">
		</section>
      <section>
			<div>身份证号码</div>
			<div style="color:#ED9E7E">
				<img src="../assets/common/t.svg">姓名字数过多！
			</div>
			<input placeholder="请输入身份证号码">
		</section>
      <section>
			<div>身份证号码</div>
			<div style="color:#ED9E7E">
				<img src="../assets/common/t.svg">姓名字数过多！
			</div>
			<input placeholder="请输入身份证号码">
		</section>
      <section>
			<div>身份证号码</div>
			<div style="color:#ED9E7E">
				<img src="../assets/common/t.svg">姓名字数过多！
			</div>
			<input placeholder="请输入身份证号码">
		</section>
   </div>
</template>

<script>
export default {
   name: "info",
   props: {
      title: "",
      item: {}
   }
};
</script>


<style scoped>
.info{
	
}
header{
	
}
header::before{
	display: inline-block;
	height:16px;
	width:4px;
	content: "";
	background-color: #1285F8;
	margin:0px 10px -3px 0 ;
	border-radius: 5px;
}
.info section:nth-of-type(1){
	margin-top: 10px;
	border-top:1px #eee solid;
}
section{
	overflow: hidden;
	border-bottom:1px #eee solid;
	padding:10px;
	color:#444;
}
section div:nth-child(1),section div:nth-child(2){
	float: left;
}
section div:nth-child(2){
	margin-left: 8px;
	font-size: 14px;
}
section div:nth-child(2) img{
	width:18px;
	margin-bottom:-4px;
	margin-right: 4px;
}
section input{
	border:none;
	outline:none;
	font-size:16px;
	float:right;
	text-align: right;
}
section input::-webkit-input-placeholder{
	color:#ccc;
}
</style>
