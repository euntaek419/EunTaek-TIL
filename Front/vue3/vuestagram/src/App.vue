<template>
  <div class="header">
    <ul class="header-button-left">
      <li v-if="step == 1 || step == 2" @click="step--">Cancel</li>
    </ul>
    <ul class="header-button-right">
      <li v-if="step == 1" @click="step++">Next</li>
      <li v-if="step == 2" @click="publish">발행</li>
    </ul>
    <img src="./assets/logo.png" class="logo" />
  </div>

<!-- 
<p>{{ $store.state.more }}</p>
<button @click="$store.dispatch('getData')">더보기 버튼</button>
-->

<!--
  <h4> Hi {{ $store.state.name }} </h4>
  <h4> age {{ $store.state.age }} </h4>
  <button @click="$store.commit('namechange') ">이름변경</button>
  <button @click="$store.commit('ageup', 10)">age+1</button>
-->

  <Container @write="writepost = $event" :choicefilter='choicefilter' :image='image' :vuestar='vuestar' :step='step' />
  <button @click="more">더보기</button>


  <!-- <p> {{ now() }} {{counter}}</p> -->
  <!-- <button @click="counter++">버튼</button> -->

    <div class="footer">
      <ul class="footer-button-plus">
        <input @change="upload" accept="image/*" type="file" id="file" class="inputfile" />
        <label for="file" class="input-plus">+</label>
      </ul>
  </div>

<!--
  <div v-if="step == 0">내용0</div>
  <div v-if="step == 1">내용1</div>
  <div v-if="step == 2">내용2</div>
  <button @click="step = 0">버튼0</button>
  <button @click="step = 1">버튼1</button>
  <button @click="step = 2">버튼2</button>
-->



</template>

<script>
import Container from './components/Container.vue';
import Postdata from './assets/postdata';
import axios from 'axios'
// import {mapMutations, mapState} from 'vuex'

// axios.post('URL', {name : 'kim'}).then().catch((err))

export default {
  name: 'App',
  data(){
    return {
      step : 0,
      vuestar : Postdata,
      count : 0,
      image : '',
      writepost: '',
      choicefilter : '',
      counter: 0,
    }
  },
  mounted() {
    this.emitter.on('boxclick', (firedata)=>{
      this.choicefilter = firedata
      console.log(this.choicefilter)
    });
  },
  components: {
    Container,
  },
  computed: {
    name(){
      return this.$store.state.name
    },
    // ...mapState('name','age','likes'), //store에 있는 state를 한번에 가져올 수 있음.
    // ...mapState( { 내이름 : 'name',}) //작명하여 새로 사용 가능
  },
  methods : {
    // ...mapMutations(['setMore','likes']),

    publish() {
      var myvuestar = {
        name: 'Choi eun taek',
        userImage:'https://placeimg.com/100/100/arch',
        postImage: this.image,
        likes: 26,
        data: 'May 10',
        liked: false,
        content: this.writepost,
        filter: this.choicefilter,
      };
      this.vuestar.unshift(myvuestar);
      this.step = 0;
    },
    more() {
      axios.get(`https://codingapple1.github.io/vue/more${this.count}.json`)
      .then( result =>{
        this.vuestar.push(result.data);
        this.count = this.count + 1;
      })
    },
    upload(e){
      let file = e.target.files;
      let url = URL.createObjectURL(file[0]);
      this.image = url;
      this.step++;
    }
  }
}
</script>

<style>
/* @import 'style.css'; */

body {
  margin: 0;
}
ul {
  padding: 5px;
  list-style-type: none;
}
.logo {
  width: 22px;
  margin: auto;
  display: block;
  position: absolute;
  left: 0;
  right: 0;
  top: 13px;
}
.header {
  width: 100%;
  height: 40px;
  background-color: white;
  padding-bottom: 8px;
  position: sticky;
  top: 0;
}
.header-button-left {
  color: skyblue;
  float: left;
  width: 50px;
  padding-left: 20px;
  cursor: pointer;
  margin-top: 10px;
}
.header-button-right {
  color: skyblue;
  float: right;
  width: 50px;
  cursor: pointer;
  margin-top: 10px;
}
.footer {
  width: 100%;
  position: sticky;
  bottom: 0;
  padding-bottom: 10px;
  background-color: white;
}
.footer-button-plus {
  width: 80px;
  margin: auto;
  text-align: center;
  cursor: pointer;
  font-size: 24px;
  padding-top: 12px;
}
.sample-box {
  width: 100%;
  height: 600px;
  background-color: bisque;
}
.inputfile {
  display: none;
}
.input-plus {
  cursor: pointer;
}
#app {
  box-sizing: border-box;
  font-family: "consolas";
  margin-top: 60px;
  width: 100%;
  max-width: 460px;
  margin: auto;
  position: relative;
  border-right: 1px solid #eee;
  border-left: 1px solid #eee;
}
</style>
