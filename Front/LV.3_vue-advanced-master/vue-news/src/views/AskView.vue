<template>

<div>
  <p v-for="item in fetchedAsk">
     <router-link v-bind:to="`item/${item.id}`"> {{item.title}} </router-link>
     <small> {{item.time_ago}} </small>
     <!-- <router-link v-bind:to="`/user/${item.user}`"> {{item.user}} </router-link> -->
  </p>
  </div>


</template>

<script>
import { mapGetters } from 'vuex';

export default {
  computed: {
    ...mapGetters([
      'fetchedAsk'
    ]),
  },
  created() {
    this.$store.dispatch('FETCH_ASK');
  }
}
</script>

<style>

</style>