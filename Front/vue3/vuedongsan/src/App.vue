<template>

  <Modal
  @closeModal="modalOpen = false;" 
  :onerooms="onerooms" :click_num="click_num" :modalOpen="modalOpen"/>

  <div class="menu">
    <a v-for="menu in menus" :key="menu"> {{ menu }} </a>
  </div>

  <Discount/>

  <Card @openModal="modalOpen = true; click_num = $event" :oneroom="onerooms[i]" v-for="(for_oneroom,i) in onerooms" :key="for_oneroom"/>

  <!-- <div>
    <button v-on:click="report_num[2]++"> 허위 매물 신고</button> <span>신고수 : {{ report_num[2] }} </span>
  </div> -->

</template>

<script>
import roomdata from './assets/oneroom.js';
import Discount from './Discount.vue';
import Modal from './Modal.vue';
import Card from './Card.vue';

export default {
  name: 'App',
  data() {
    return {
      object : { name : 'kim', age : 20},
      click_num: 0,
      onerooms : roomdata,
      modalOpen: false,
      report_num : [0,0,0],
      menus : ['Home', 'Shop', 'About'],
      products : ['역삼동원룸', '천호동원룸', '마포구원룸'],
    }

  },
  components: {
    Discount,
    Modal,
    Card,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Arial, Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

body {
  margin:0;
}

div {
  box-sizing: border-box;
}

.discount {
  background:#eee;
  padding:10px;
  margin:10px;
  border-radius: 5px;
}

.black-bg {
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.5);
  position: fixed; padding: 20px;
}

.white-bg {
  width: 100%; background: white;
  border-radius: 8px;
  padding: 20px;
}

.room-img {
  width: 100%;
  margin-top:40px;
}

.menu {
  background: darkslateblue;
  padding: 15px;
  border-radius: 5px;
}

.menu a{
  color : white;
  padding: 10px;
}

</style>
