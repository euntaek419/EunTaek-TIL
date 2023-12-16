<template>
  <div>
    <input v-model="message">
    <button @click="saveMessage">save</button>

    <p>{{message}}, {{updateMessage}}</p>
  </div>
</template>

<script>
import {mapGetters} from 'vuex';

export default {
  data() {
    return {
      message : '',
    }
  },
  computed: {
    ...mapGetters(['getMessage','getupdateMessage']),
    message() {
      return this.message
    }
  },
  methods: {
    saveMessage () {
      this.$store.dispatch('setMessage', this.message)
    }
  }

}
</script>

<style>

</style>