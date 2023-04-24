<template>
  <div class="black-bg" v-if="modalOpen == true">
  <div class="white-bg">
    <img :src="onerooms[click_num].image">
    <h4>{{ onerooms[click_num].title}}</h4>
    <p>{{ onerooms[click_num].content}}</p>
    <p>{{ onerooms[click_num].price}}원</p>
    <button @click="$emit('closeModal')">close</button>
    
  </div>
</div>
</template>

<script>

export default {
    name: 'Modal',
    props : {
      onerooms : Array,
      click_num : Number,
      modalOpen : Boolean,
    },
    data() {
        return {
        
        }
    }
}
</script>

<style>

</style>