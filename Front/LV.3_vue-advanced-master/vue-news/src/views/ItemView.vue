<template>
  <div>
    <section>
      <!-- 사용자 상세 정보 -->
      <user-profile :info="fetchedItem">
        <!-- <div slot="username"> {{ fetchedItem.user }} </div> -->
        <router-link slot="username" :to="`/user/${fetchedItem.user}`">
          {{ fetchedItem.user }}
        </router-link>
        <template slot="time"> {{ 'Posted ' + fetchedItem.time_ago }} </template>
      </user-profile>
    </section>
    <section>
      <h2>{{ fetchedItem.title }}</h2>
    </section>
    <section>
      <!-- 질문 댓글 -->
      <div v-html="fetchedItem.content"/>
    </section>
  </div>
</template>

<script>
import UserProfile from '../components/UserProfile.vue';
import { mapGetters } from 'vuex';
import bus from '../utils/bus.js';
export default {
  components: {
    UserProfile,
    },
  computed:{
    ...mapGetters(['fetchedItem']),
  },
  
  created() {
    const itemId = this.$route.params.id;
    console.log(itemId)
    this.$store.dispatch('FETCH_ITEM', itemId);
    bus.$emit('start:spinner');
    this.$store.dispatch('FETCH_NEWS')
      .then(() => {
        console.log('fetched');
        bus.$emit('end:spinner');
      })
      .catch((error) => {
        console.log(error);
      });
  }

}
</script>

<style scoped>
.user-container{
  display: flex;
  align-items: center;
  padding: 0.5rem;
}
.fa-user {
  font-size: 2.5rem;
}

.user-description {
 padding-left: 8px; 
}
.time {
  font-size: 0.7rem;
}
</style>