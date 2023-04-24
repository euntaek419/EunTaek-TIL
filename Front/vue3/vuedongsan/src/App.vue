<template>

<div class="black-bg" v-if="modalstats == true">
  <div class="white-bg">
    <img :src="products_rooms[click_num].image">
    <h4>{{ products_rooms[click_num].title}}</h4>
    <p>{{ products_rooms[click_num].content}}</p>
    <p>{{ products_rooms[click_num].price}}원</p>

    <button @click="modalstats = false">close</button>
  </div>
</div>

  <div class="menu">
    <a v-for="menu in menus" :key="menu"> {{ menu }} </a>
  </div>

  <!-- <div v-for="(product,i) in products" :key="i">
    <h4>{{ products[i] }}</h4>
  </div> -->

  <!-- <div>
    <img :src="products_rooms[0].image" class="room-img">
    <h4> {{ products_rooms[0].title }}</h4>
    <p> {{ products_rooms[0].price }}원</p>
  </div> -->

  <div v-for="(products_room, i) in products_rooms" :key="i">
    <img :src="products_rooms[i].image" class="room-img">
    <h4 @click="modalstats = true; click_num = i"> {{ products_rooms[i].title }} </h4>
    <p> {{ products_rooms[i].price }}원 </p>
  </div>

  <div>
    <img src="./assets/room2.jpg" class="room-img">
    <h4> {{ products[2] }} </h4>
    <p>70 만원</p>
    <button v-on:click="report_num[2]++"> 허위 매물 신고</button> <span>신고수 : {{ report_num[2] }} </span>
  </div>

</template>

<script>
import roomdata from './assets/oneroom';

export default {
  name: 'App',
  data() {
    return {
      click_num: 0,
      modalstats: false,
      report_num : [0,0,0],
      menus : ['Home', 'Shop', 'About'],
      products : ['역삼동원룸', '천호동원룸', '마포구원룸'],
      products_rooms : roomdata,
    }

  },
}
</script>

<style>
body {
  box-sizing: border-box;
}

div {
  box-sizing: border-box;
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
