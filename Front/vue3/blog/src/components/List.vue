<template>
  <div>
    <h5>{{ blog_writing[0].title }}</h5>
    <p>{{ blog_writing[0].content }}</p>
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