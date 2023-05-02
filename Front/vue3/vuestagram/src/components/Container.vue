<template>
  <div>
    <Post :vuestar="vuestar[i]" v-for="(vuestars,i) in vuestar" :key="i"/>
    <!-- <Post :vuestar="vuestar[0]"></Post>
    <Post :vuestar="vuestar[1]"></Post> -->
  </div>
</template>

<script>
import Post from './Post.vue'

export default {
  props: {
    vuestar: Array,
  },
  components: {
    Post,
  }
}
</script>

<style>

</style>