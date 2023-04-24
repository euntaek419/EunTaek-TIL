<template>
    <div v-for="(products_room, i) in products_rooms" :key="i">
    <img :src="products_rooms[i].image" class="room-img">
    <!-- <h4 @click="modalstats = true; click_num = i"> {{ products_rooms[i].title }} </h4> -->
    <p> {{ products_rooms[i].price }}원 </p>
  </div>
</template>

<script>
export default {
    name: 'Card',
    props: {
        products_rooms:String,
    },

}
</script>

<style>

</style>