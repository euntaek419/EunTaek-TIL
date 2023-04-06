<template>
  <input type="checkbox" :value="value" @click="toggleCheckBox">
</template>

<script>
export default {
  // @input 이벤트
  // :value 값
  props: ['checked'], //false
  methods: {
    toggleCheckBox() {
      this.$emit('input', !this.value);
    }
  }
}
</script>