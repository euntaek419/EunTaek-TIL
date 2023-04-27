<template>

  <transition name="fade">
    <Modal
    @closeModal="modalOpen = false;" 
    :onerooms="onerooms" :click_num="click_num" :modalOpen="modalOpen"/>
  </transition>
  

  <div class="menu">
    <a v-for="menu in menus" :key="menu"> {{ menu }} </a>
  </div>

  <Discount v-if="showDiscount == true" />

  <button @click="priceSort">낮은가격순정렬</button>
  <button @click="priceReverseSort">높은가격순정렬</button>
  <button @click="languageSort">가나다순정렬</button>
  <button @click="sortBack">되돌리기</button>
  
  

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
      showDiscount : true,
      onerooms_original : [...roomdata],
      object : { name : 'kim', age : 20},
      click_num: 0,
      onerooms : roomdata,
      modalOpen: false,
      report_num : [0,0,0],
      menus : ['Home', 'Shop', 'About'],
      products : ['역삼동원룸', '천호동원룸', '마포구원룸'],
    }

  },
  methods: {
    sortBack() {
      this.onerooms = [...this.onerooms_original];
    },
    priceSort() {
      this.onerooms.sort(function(a,b){
        return a.price - b.price
      })
    },
    priceReverseSort() {
      this.onerooms.sort(function(a,b){
        return b.price - a.price
      })
    },
    languageSort() {
      this.onerooms.sort(function(a,b){
        return a.title.localeCompare(b.title);
      })
    }
  },

  mounted() {
    setTimeout(() => {
      this.showDiscount = false;
    }, 2000);
  },

  components: {
    Discount,
    Modal,
    Card,
  }
}
</script>

<style>
.fade-enter-from { /* 시작 스타일 */
  opacity: 0;
}
.fade-enter-active { /* 트랜지션 */
  transition: all 1s;
}
.fade-enter.to { /* 시작 스타일 종료 */
  opacity: 1;
}

.fade-leave-from { /* 시작 스타일 */
  opacity: 1;
  /* transform: translateX(0px); */
}
.fade-leave-active { /* 트랜지션 */
  transition: all 1s;
}
.fade-leave.to { /* 시작 스타일 종료 */
  opacity: 0;
  /* transform: translateX(1000px); */
}





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
