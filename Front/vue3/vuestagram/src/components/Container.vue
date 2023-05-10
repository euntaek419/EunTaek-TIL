<template>
  <div>
    <div v-if="step == 0">
      <Post :vuestar="vuestar[i]" v-for="(vuestars,i) in vuestar" :key="i"/>
    </div>
    <!--
    <Post :vuestar="vuestar[0]"></Post>
    <Post :vuestar="vuestar[1]"></Post>
    -->

    <!-- 필터선택페이지 -->
    <div v-if="step == 1">
      <div class="upload-image" :style="`background-image:url(${image})`"></div>
      <div class="filters">
        <div class="filter-1"></div>
        <div class="filter-1"></div>
        <div class="filter-1"></div>
        <div class="filter-1"></div>
        <div class="filter-1"></div>
      </div>
    </div>

    </div>

    <div v-if="step == 2">
      <!-- 글작성페이지 -->
      <div class="upload-image" :style="`background-image:url(${image})`"></div>
      <div class="write">
        <textarea @input="$emit('write', $event.target.value)" class="write-box">write!</textarea>
      </div>
  </div>
</template>

<script>
import Post from './Post.vue'

export default {
  data() {
    return {
      
    }
  },
  props: {
    vuestar: Array,
    step: Number,
    image : String,
  },
  components: {
    Post,
  }
}
</script>

<style>

</style>