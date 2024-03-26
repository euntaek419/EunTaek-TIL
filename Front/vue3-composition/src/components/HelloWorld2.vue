<template>
    <div>
        {{ test }}
    </div>

</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

let test = ref("HelloWorld2")

onMounted(() => {
    axiosData();
})

const axiosData = async () => {
    test.value = await axios.get('https://jsonplaceholder.typicode.com/todos/1');
    console.log(test)
}

</script>