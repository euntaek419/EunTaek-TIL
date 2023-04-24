<template>
  <div class="black-bg" v-if="modalOpen == true">
  <div class="white-bg">
    <img :src="onerooms[click_num].image">
    <h4>{{ onerooms[click_num].title}}</h4>
    <p>{{ onerooms[click_num].content}}</p>
    <input v-model.number="month"> <!-- <input type="range" min="1" max="12"> -->
    <p> {{ month }} 개월 선택함 : {{ onerooms[click_num].price * month}}원</p>
    <button @click="$emit('closeModal')">close</button>

  </div>
</div>
</template>

<script>

export default {
    name: 'Modal',
    data() {
        return {
          month : 3,
        }
    },
    beforeUpdate() {
        if(this.month == 2) {
          alert('2개월은 너무 적소. 4개월쯤 합시다.')
          this.month = "3"
      }
    },
    watch : {
      month(a) {
        if(a >= 13){
          alert('13이상 입력하지 마시오.');
          this.month = "3"
        }
        else if( isNaN(a) == true ) {
          // else if(/^[0-9]*$|^$/.test(a) == false ) {
          alert('숫자만 입력 가능합니다.')
          this.month = "3"
        }
        else if( a === " ") {
          alert('숫자만 입력 가능합니다.')
          this.month = "3"
        }
      },
  },
    
    
    props : {
      onerooms : Array,
      click_num : Number,
      modalOpen : Boolean,
    },
  
}
</script>

<style>

</style>