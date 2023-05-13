<template>
  <div :class="filter + ' filter-item'" :style="`background-image:url(${image})`">
    <slot></slot>
    <button @click="fire">버튼</button>
    <!-- <slot name="a"> <spen> 데이터 a</spen></slot> -->
    <!-- <slot :msg="msg"></slot> -->
  </div>

</template>

<script>
export default {
    name: 'filterbox',
    methods : {
      fire() {
        this.emitter.emit('작명', '데이터')
      }
    },
    data() {
        'hello'
    },
    props: {
        image : String,
        filter : String,
    }
}
</script>

<style>

.filter-item {
  width: 100px;
  height: 100px;
  margin: 10px 10px 10px auto;
  padding: 8px;
  display: inline-block;
  color : white;
  text-shadow: -1px 0 #000, 0 1px #000, 1px 0 #000, 0 -1px #000;
  background-size: cover;
  background-position : center;
}

</style>