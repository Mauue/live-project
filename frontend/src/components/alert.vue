<template>

   <div id="z" @click="clickIn">
      <transition name="fade">
         <div id="black" v-show="visible && (type.match('true')||type.match('false')||type.match('tips'))"></div>
      </transition>
      <transition name="slide-fade">
         <div class="alert" key="al" v-show="visible && (type.match('true')||type.match('false')||type.match('tips'))">
            <div style="margin:1.2rem 0.5rem 1.2rem 0">
               <img v-if="type.match('true')" src="../assets/common/true.svg" />
               <img v-if="type.match('false')" src="../assets/common/false.svg" />
               <img v-if="type.match('tips')" src="../assets/common/tips.svg" />
            </div>
            <div style="margin:2.1rem 0.5rem 0 0">
               <span :class="{greentext:type.match('true'),
               redtext:type.match('false'),bluetext:type.match('tips')}">{{ msg }}</span>
            </div>
         </div>
      </transition>
      <transition name="tiny">
         <div id="tiny" v-show="visible && type.match('tiny')" :style="{left:mouse.x-130 + 'px',top:mouse.y+10 + 'px'}">
         <span v-if="type.match('tiny-clipboard')">
            <span style="white-space:pre">{{msg.split('：')[0]}}：
</span>
            <span id="tiny-msg">{{msg.split('：')[1]}}</span>
         </span>
         <span v-else>
            <span v-for="i in msg.split('')">{{i}}</span>
         </span>   
         </div>
      </transition>
   </div>

</template>

<script>
   export default {
      name: "alert",
      methods:{
         clickIn(e){
             this.visible = false;
             e.stopPropagation();
         }
       },
      data() {
         return {
            type: "",
            msg: "",
            visible: true,
            mouse:null,
         };
      },
      mounted() {
         //Vue.$alertNum ++;
         this.visible = true;
         if(this.type=='tiny-clipboard'){
            this.$nextTick(()=>{
               var obj = document.getElementById('tiny-msg')
               var selection = window.getSelection();
               selection.removeAllRanges();
               var range = new Range();
               range.selectNodeContents(obj);
               selection.addRange(range);
            })

         }
         window.setTimeout(() => {
            //Vue.$alertNum --;
            this.visible = false;
         }, 1400);
      }
   };
</script>

<style scoped>
   #z {
      left: 0;
      top: 0;
      position: absolute;
      z-index: 502;
      height: 100%;
		font-size: 5px;
   }

    #black {
      left: 0;
      bottom: 0;
      position: fixed;
      z-index: 501;
      width: 100%;
      height: 100rem;
      background-image: linear-gradient(bottom,
         rgba(0, 0, 0, 0.00) 0%,rgba(0, 0, 0, 0.2) 50%,rgba(0, 0, 0, 0.5) 90%);
   } 
   #tiny-msg{
      white-space: pre;
   }
   .alert {
      z-index: 503;
      position: fixed;
      top: 1rem;
      left: 50%;
      transform: translateX(-50%);
      width: auto;
      height: auto;
      padding: 0rem 1rem;
      background-color: #ffffff;
      border-radius: 0.5rem;
      border: 1px solid rgb(218, 237, 251);
      box-shadow: 0px 1px 5px 1px rgba(44, 44, 44, 0.194);
      display: flex;
   }

   .alert img {
      width: 6rem;
   }

   .alert {
      text-align: left;
      font-weight: bold;
      color: rgb(92, 92, 92);
      user-select: none;
   }

   .alert span {
      font-size: 18px;
      vertical-align: 2rem;
      line-height: 0;
      white-space: pre;
   }

   .greentext {
      color: rgb(66, 181, 60);
   }

   .redtext {
      color: rgb(181, 60, 60);
   }

   .bluetext {
      color: rgb(60, 147, 181);
   }

   .slide-fade-enter-active {
      transition: all 0.2s cubic-bezier(0.02, 0.575, 0.1, 0.955);
   }

   .slide-fade-leave-active {
      transition: all 0.6s cubic-bezier(0.02, 0.575, 0.1, 0.955);
   }

   .slide-fade-enter,
   .slide-fade-leave-to {
      transform: translateX(-50%)translateY(-135%);
      opacity: 0.5;
   }
   .tiny-enter-active,.tiny-leave-active {
      transition: all 0.15s cubic-bezier(0.02, 0.575, 0.1, 0.955);
   }
   .tiny-enter,.tiny-leave-to {
      transform: translate(0,15%);
      opacity: 0;
   }
   #tiny{
      position: absolute;
      line-height: 20px;
      padding: 6px 10px;
      background-color: rgba(0,0,0,.68);
      color: #fff;
      border-radius: 4px;
      font-size: 14px;
      transition: all .2s;
      /* transform: translate(-45%,0); */
   }
   @media screen and (max-width: 768px) {
      .alert img {
         display: block;
         margin: 0 auto;
         padding-bottom: 2rem;
      }

      .alert span {
         text-align: center;
         line-height: 0rem;
         vertical-align: 1.4rem;
      }
   }

   .fade-enter-active {
      transition: all 0.2s
   }

   .fade-leave-active {
      transition: all 0.2s
   }

   .fade-enter,
   .fade-leave-to {
      opacity: 0;
   }
</style>