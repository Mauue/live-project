<template>
   <div id="app">
      <div id="button" @click="router=0">
         <img src="./assets/arrow.svg" />
         <div>返回</div>
      </div>
		<header>口罩预约系统</header>
      <div v-if="router==0">
         <div id="wrapper">
            <section @click="router=1">
               <img src="./assets/clock.png" />
               <p>摇号预约</p>
            </section>
            <section @click="router=2">
               <img src="./assets/search.png" />
               <p>中签查询</p>
            </section>
            <section @click="router=3">
               <img src="./assets/admin.png" />
               <p>管理员登录</p>
            </section>
            <section @click="router=4">
               <img src="./assets/service.png" />
               <p>联系客服</p>
            </section>
         </div>
      </div>
      <order v-if="router==1"></order>
      <search v-if="router==2"></search>
      <admin v-if="router==3"></admin>
      <service v-if="router==4"></service>
   </div>
</template>

<script>
import order from "./components/Order.vue";
import admin from "./components/Admin.vue";
import service from "./components/Service.vue";
import search from "./components/Search.vue";
export default {
   name: "App",
   components: { order,admin,service,search },
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
   margin:150px auto auto auto;
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
	max-width: 700px;
	margin:0 auto;
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
