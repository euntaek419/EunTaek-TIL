<template>
  <div>
    <p>name : {{ this.$store.state.user.id }}</p>
    <p>karma : {{ this.$store.state.user.karma }}</p>
    <p>created : {{ this.$store.state.user.created }}</p>
  </div>
</template>

<script>
export default {
  created() {
    const userName = this.$route.params.id;
    // axios.get(`https://api.hnpwa.com/v0/user/${this.$route.params.id}.json`);
    this.$store.dispatch('FETCH_USER', userName);
  }
}
</script>

<style>

</style>