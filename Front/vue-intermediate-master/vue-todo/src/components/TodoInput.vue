<template>
  <div class="inputBox shadow">
    <!-- <button v-on:click="addTodo">add</button> -->
    <input type="text" v-model="newTodoItem" v-on:keyup.enter="addTodo">
    <span class="addContainer" v-on:click="addTodo">
      <i class="fa-solid fa-plus addBtn"></i>
    </span>

    <Modal v-if="showModal" @close="showModal = false">
        <!--
      you can use custom content here to overwrite 
      default content
    -->
        <h3 slot="header">
          경고!
          <span @click="showModal = false">
            <i class="closeModalBtn fa-solid fa-x"></i>
          </span>
          
          </h3>

        <h4 slot="body">값을 입력해주세요.</h4>

        <!-- <h6 slot="footer">Copyright 2023 euntaek All rights reserved.</h6> -->
      </Modal>
  </div>
</template>

<script>
import AlertModal from './common/AlertModal.vue'
export default {
  data: function() {
    return {
      newTodoItem: '',
      showModal: false
    }
  },
  methods: {
    addTodo: function() {
      if (this.newTodoItem !== '') {
        this.$emit('addTodoItem',this.newTodoItem);
        this.clearInput();
      } else {
        this.showModal = !this.showModal;
      }
    },
    clearInput: function() {
      this.newTodoItem = '';
    }
  },
  components: {
     Modal: AlertModal
  }
}
</script>

<style scoped>
input:focus {
  outline: none;
}
.inputBox {
  background: white;
  height: 50px;
  line-height: 50px;
  border-radius: 5px;

  display: flex;
  align-items: center;
}
.inputBox input {
  border-style: none;
  font-size: 0.9rem;

  height:100%;
  width: calc(100% - 3rem);
}
.addContainer {
  background: linear-gradient(to right, #6478FB, #8763FB);
  display: block;
  width: 3rem;
  border-radius: 0 5px 5px 0;

  height:100%;
}
.addBtn {
  color:white;
  vertical-align:middle;
}
.closeModalBtn {
  color: #42b983;
}

</style>