<template>
   <div id="app">
      <div id="button" @click="router=0">
         <img src="./assets/arrow.svg" />
         <div>返回</div>
      </div>
		<header>口罩预约系统</header>
      <div v-if="router==5">        
         <div id="wrapper">           
            <section @click="router=6">
                <img src="../assets/common/look.png" />
               <p>查看预约</p>
            </section>
            <section @click="router=7">
               <img src="../assets/common/publish.png" />
               <p>发布预约</p>
            </section>
            <section @click="router=8">
               <img src="../assets/common/return.png" />
               <p>返回主界面</p>
            </section>
         </div>       
      </div>
      <scan v-if="router==6"></scan>
   </div>
</template>

<script>
import scan from "./components/Scan.vue";
export default {
   name: "App",
   components: { scan },
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