<template>
  <div>
    <img :src="oneroom.image" class="room-img">
    <h4 @click="modalPlz">  {{ oneroom.title }}</h4>
    <p> {{ oneroom.price }}원 </p>
  </div>
</template>

<script>
export default {
    name: 'Card',
    props: {
        oneroom:Object,
    },
    methods: {
        modalPlz(){
            this.$emit('openModal', this.oneroom.id);
        }
    }

}
</script>

<style>

</style>