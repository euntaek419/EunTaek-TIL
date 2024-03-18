<template>
  <TodoHeader :appTitle="title"></TodoHeader>
  <TodoInput @add="addTodoItem"></TodoInput>
  <TodoList :todoItems="todoItems" @remove="removeTodoItem"></TodoList>
</template>

<script>
import TodoHeader from '@/components/TodoHeader.vue';
import TodoInput from '@/components/TodoInput.vue';
import TodoList from '@/components/TodoList.vue';
import {useTodo} from './hooks/useTodo'
import { onBeforeMount } from 'vue'

export default {
  components: {
    TodoHeader, TodoInput, TodoList
  },
  setup(){

    const { todoItems, addTodoItem, removeTodoItem, fetchTodos } = useTodo()

    //라이프사이클 API
    onBeforeMount(() => {
        todoItems.value = fetchTodos();
    })

    return { todoItems, addTodoItem, removeTodoItem }
  },
  methods: {
    // removeTodoItem(item, index) {
    //   this.todoItems.splice(index, 1);
    //   localStorage.removeItem(item);
    // }
  },
  data() {
    return {
      title: '할일 앱'
    }
  },
}

</script>

<style lang="scss" scoped>

</style>