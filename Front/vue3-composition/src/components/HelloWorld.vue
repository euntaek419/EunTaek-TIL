<template>
  <div>
    <p>{{ hello }}</p>
    <p>{{ hello2.인사 }}</p>
    <p>{{ hello2.작별인사 }}</p>

    <button @click="변경">변경하는 버튼</button>
  </div>


  <div style="margin-top:100px">
    {{ test }}
    <button @click="axiosData">테스트 변경</button>
  </div>



</template>

<script setup>
import { ref,reactive } from 'vue'
import axios from 'axios'

let hello = ref("안녕")
let hello2 = reactive({
  인사 : "인사",
  작별인사 : "작별인사",
})

function 변경() {
  hello.value = "이제는 안녕"
  hello2.인사 = "반가운 인사"
  hello2.작별인사 = "떠나는 작별인사"
}

let test = ref("안녕")

const axiosData = async () => {
  test.value = await axios.get('https://jsonplaceholder.typicode.com/todos/1');
  console.log(test)
}
</script>

<style lang="scss" scoped>

</style>