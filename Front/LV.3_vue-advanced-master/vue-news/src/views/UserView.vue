<template>
  <div>
    <user-profile :info="userInfo">
      <div slot="username"> {{ userInfo.id }}</div>
      <spen slot="time"> {{ 'Joined ' + userInfo.created }}, </spen>
      <spen slot="karma"> {{ 'Karma ' + userInfo.karma }} </spen>
    </user-profile>
  </div>
</template>

<script>
import UserProfile from '../components/UserProfile.vue';
import bus from '../utils/bus.js';

export default {
  components: {
    UserProfile,
  },
  computed: {
    userInfo() {
      return this.$store.state.user;
    }
  },
  created() {
    const userName = this.$route.params.id;
    this.$store.dispatch('FETCH_USER', userName);
    bus.$emit('start:spinner');
    this.$store.dispatch('FETCH_NEWS')
      .then(() => {
        console.log('fetched');
        bus.$emit('end:spinner');
      })
      .catch((error) => {
        console.log(error);
      });
  },
}
</script>

<style>

</style>