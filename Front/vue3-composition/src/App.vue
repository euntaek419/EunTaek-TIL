<template>
  <div>
    <p> {{ message }}</p>
    <button @click="changeMessage">change</button>
  </div>
</template>

<script>
import { useMeesage } from './hooks/useMessage'

export default {
  setup() {
    const { message, changeMessage } = useMeesage();

    return { message, changeMessage }
  }
}
</script>

<style lang="scss" scoped>

</style>