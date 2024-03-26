<template>
  <div>
    <!-- <p> {{ message }}</p> -->
    <!-- <button @click="changeMessage">change</button> -->

    <HelloWorld></HelloWorld>
    <HelloWorld2 v-if="yes == 0" style="margin-top:100px;"></HelloWorld2>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import HelloWorld2 from './components/HelloWorld2.vue';
import { useMessage } from './hooks/useMessage'

export default {
  data() {
    return {
      yes: 1,
    }
  },
  setup() {
    const { message, changeMessage } = useMessage();

    return { message, changeMessage }
  },
  components: {
    HelloWorld,
    HelloWorld2
  }
}
</script>

<style lang="scss" scoped>

</style>