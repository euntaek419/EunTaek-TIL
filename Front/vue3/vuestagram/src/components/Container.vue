<template>
  <div>
    컨테이너 입니다.
    <Post :instar="instar"/>
    <Post/>
    <Post/>
  </div>
</template>

<script>
import Post from './Post.vue'

export default {
  props: {
    instar:Object,
  },
  components: {
    Post,
  }
}
</script>

<style>

</style>