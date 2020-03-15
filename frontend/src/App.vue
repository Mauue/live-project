<template>
   <div id="app">
		<header>口罩预约系统</header>
      <div v-if="router==0">
         <div id="wrapper">
            <section @click="router=1">
               <img />
               <p>摇号预约</p>
            </section>
            <section>
               <img src />
               <p>中签查询</p>
            </section>
            <section>
               <img src />
               <p>管理员登录</p>
            </section>
            <section>
               <img src />
               <p>联系客服</p>
            </section>
         </div>
      </div>
      <order v-if="router==1"></order>
   </div>
</template>

<script>
import order from "./components/Order.vue";
export default {
   name: "App",
   components: { order },
   data(){
      return{
         router: 0
      }
   }
};
</script>

<style>
#wrapper{
	display: flex;
	justify-content: space-around;
}
header{
	text-align: center;
	background-color: #BCE7EE;
	padding:15px;
	font-weight: bold;
}
body {
	margin:0;
}
#app {
}
button {
   margin: 0 auto;
   display: block;
   background-color: rgb(140, 195, 250);
   border: none;
   padding: 6px 24px;
   color: white;
   font-size: 16px;
   border-radius: 6px;
   transition: 0.2s all;
}
button:hover {
   background-color: rgb(120, 179, 238);
}
#button {
  position: absolute;
  top:5px;
  width: 100px;
  height: 50px;
  clear: both;
  padding-top: 3px;
}
#button img {
  width: 12px;
  height: 18px;
  float: left;
  margin: 10px;
}
#button :hover {
  filter: brightness(1.4);
  color: rgb(43, 58, 133);
  cursor: pointer;
  transition: 0.15s all;
}
/* #banner:hover{
  filter: brightness(1.4);
  color: rgb(43, 58, 133);
  cursor: pointer;
  transition: 0.15s all;
} */
#button div {
  float: left;
  height: 30px;
  padding: 0;
  margin: 7px 24px 3px -5px;
}
#banner {
  width: auto;
  text-align: center;
  padding-top: 11px;
  transform: translateX(0);
}
</style>
