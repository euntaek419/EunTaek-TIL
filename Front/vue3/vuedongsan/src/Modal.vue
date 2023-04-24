<template>
  <div class="black-bg" v-if="modalstats == true">
  <div class="white-bg">
    <img :src="products_rooms[click_num].image">
    <h4>{{ products_rooms[click_num].title}}</h4>
    <p>{{ products_rooms[click_num].content}}</p>
    <p>{{ products_rooms[click_num].price}}원</p>

    <!-- <button @click="modalstats = false">close</button> -->
  </div>
</div>
</template>

<script>

export default {
    name: 'Modal',
    props : {
      products_rooms : Array,
      click_num : Number,
      modalstats : Boolean,
    },
    data() {
        return {
        
        }
    }
}
</script>

<style>

</style>