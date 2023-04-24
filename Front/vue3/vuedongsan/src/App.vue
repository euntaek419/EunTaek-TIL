<template>

  <Modal :products_rooms="products_rooms" :click_num="click_num" :modalstats="modalstats"/>

  <div class="menu">
    <a v-for="menu in menus" :key="menu"> {{ menu }} </a>
  </div>

  <Discount/>


  <!-- <div>
    <img :src="products_rooms[0].image" class="room-img">
    <h4> {{ products_rooms[0].title }}</h4>
    <p> {{ products_rooms[0].price }}원</p>
  </div> -->

  <Card :products_rooms="products_rooms"/>

  <div>
    <img src="./assets/room2.jpg" class="room-img">
    <h4> {{ products[2] }} </h4>
    <p>70 만원</p>
    <button v-on:click="report_num[2]++"> 허위 매물 신고</button> <span>신고수 : {{ report_num[2] }} </span>
  </div>

</template>

<script>
import roomdata from './assets/oneroom';
import Discount from './Discount.vue';
import Modal from './Modal.vue';
import Card from './Card.vue';

export default {
  name: 'App',
  data() {
    return {
      modalstats: false,
      click_num: 0,
      report_num : [0,0,0],
      menus : ['Home', 'Shop', 'About'],
      products : ['역삼동원룸', '천호동원룸', '마포구원룸'],
      products_rooms : roomdata,
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
