<template>
  <div v-for="(a,i) in 3" :key="i" >
    <h5 @click="$router.push('/detail/' + i)">{{ blog_writing[i].title }}</h5>
    <p>{{ blog_writing[i].content }}</p>
  </div>

  <div>
    <h5>블로그 글 제목</h5>
    <p>블로그 글 날짜</p>
  </div>

  <div>
    <h5>블로그 글 제목</h5>
    <p>블로그 글 날짜</p>
  </div>
</template>

<script>
export default {
    name: 'list',
    props : {
        blog_writing : Array,
    }
}
</script>

<style>

</style>