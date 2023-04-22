<template>

  <div class="menu">
    <a v-for="menu in menus" :key="menu"> {{ menu }} </a>
  </div>

  <!-- <div v-for="(product,i) in products" :key="i">
    <h4>{{ products[i] }}</h4>
  </div> -->

  <div>
    <h4> {{ products[0] }} </h4>
    <p>50 만원</p>
    <button v-on:click="increase0"> 허위 매물 신고</button> <span>신고수 : {{ report_num[0] }} </span>
  </div>

  <div>
    <h4> {{ products[1] }} </h4>
    <p>60 만원</p>
    <button v-on:click="increase1"> 허위 매물 신고</button> <span>신고수 : {{ report_num[1] }} </span>
  </div>

  <div>
    <h4> {{ products[2] }} </h4>
    <p>70 만원</p>
    <button v-on:click="increase2"> 허위 매물 신고</button> <span>신고수 : {{ report_num[2] }} </span>
  </div>

</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      report_num : [0,0,0],
      menus : ['Home', 'Shop', 'About'],
      products : ['역삼동원룸', '천호동원룸', '마포구원룸'],
    }

  },
  methods : {
    increase0() {
      this.report_num[0] += 1;
    },
    increase1() {
      this.report_num[1] += 1;
    },
    increase2() {
      this.report_num[2] += 1;
    }
  }
}
</script>

<style>

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
