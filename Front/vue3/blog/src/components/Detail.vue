<template>

  <div>
    <h4> {{ $route.params.id }}번 상세페이지</h4>
    <h5>{{ blog_writing[$route.params.id].title }}</h5>
    <h5>{{ blog_writing[$route.params.id].content }}</h5>
    
    </div>
</template>

<script>
export default {
  props : {
    blog_writing : Array,
  }
}
</script>

<style>

</style>