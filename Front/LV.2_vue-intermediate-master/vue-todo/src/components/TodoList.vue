<template>
  <div>
    <transition-group name="list" tag="ul">
      <li v-for="(todoItem, index) in this.storedTodoItems" v-bind:key="todoItem.item" class="shadow">
        <span class="checkBtn" v-on:click="toggleComplete({todoItem, index})" v-bind:class="{checkBtnCompleted: todoItem.completed}">
          <i class="fa-solid fa-check"></i>
        </span>

        <span v-bind:class="{textCompleted: todoItem.completed}"> {{ todoItem.item }} </span>
        
        <span class="removeBtn" v-on:click="removeTodo({todoItem, index})">
          <i class="removeBtn fa-solid fa-trash"></i>
        </span>
      </li>
    </transition-group>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'

export default {
  methods:{
    ...mapMutations({
      removeTodo: 'removeOneItem',
      toggleComplete: 'toggleOneItem'
    })
  },
  computed: {
    ...mapGetters(['storedTodoItems'])
  }
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
  margin-top: 0;
  text-align: left;
}
li {
  display: flex;
  min-height: 50px;
  height: 50px;
  line-height: 50px;
  margin: 0.5rem 0;
  padding: 0 0.9rem;
  background: white;
  border-radius: 5px;
}
.removeBtn {
  margin-left: auto;
  color: #de4343;
}
.checkBtn {
  line-height: 45px;
  color: #62acde;
  margin-right: 5px;
  cursor: pointer;
}
.checkBtnCompleted {
  color:#b3adad;
}

.textCompleted {
  text-decoration: line-through;
  color:#b3adad;
}

/* 리스트 아이템 트렌지션 효과 */
.list-enter-active, .list-leave-active {
  transition: all 0.5s;
}
.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateY(-30px);
}

</style>