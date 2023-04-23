<template>

<div class="black-bg" v-if="modalstats == true">
  <div class="white-bg">
    <h4>상세페이지임</h4>
    <p>상세페이지 내용임</p>
    <button @click="modalstats = false">close</button>
  </div>
</div>

  <div class="menu">
    <a v-for="menu in menus" :key="menu"> {{ menu }} </a>
  </div>

  <!-- <div v-for="(product,i) in products" :key="i">
    <h4>{{ products[i] }}</h4>
  </div> -->

  <div>
    <img src="./assets/room0.jpg" class="room-img">
    <h4 @click="modalstats = true"> {{ products[0] }} </h4>
    <p>50 만원</p>
    <button v-on:click="report_num[0]++"> 허위 매물 신고</button> <span>신고수 : {{ report_num[0] }} </span>
  </div>

  <div>
    <img src="./assets/room1.jpg" class="room-img">
    <h4> {{ products[1] }} </h4>
    <p>60 만원</p>
    <button v-on:click="report_num[1]++"> 허위 매물 신고</button> <span>신고수 : {{ report_num[1] }} </span>
  </div>

  <div>
    <img src="./assets/room2.jpg" class="room-img">
    <h4> {{ products[2] }} </h4>
    <p>70 만원</p>
    <button v-on:click="report_num[2]++"> 허위 매물 신고</button> <span>신고수 : {{ report_num[2] }} </span>
  </div>

</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      modalstats: false,
      report_num : [0,0,0],
      menus : ['Home', 'Shop', 'About'],
      products : ['역삼동원룸', '천호동원룸', '마포구원룸'],
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
