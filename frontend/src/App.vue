<template>
   <div id="app">
      <order>
         
      </order>
   </div>
</template>

<script>
import order from "./components/Order.vue";
export default {
   name: "App",
   components: { order }
};
</script>

<style>
body {
}
#app {
}
button{
	margin:0 auto;
	display: block;
	background-color:rgb(140, 195, 250);
	border:none;
	padding:6px 24px;
	color:white;
	font-size: 16px;
	border-radius: 6px;
	transition: 0.2s all;
}
button:hover{
	background-color:rgb(120, 179, 238);
}
</style>
