import { createStore } from 'vuex';

export default createStore({
  state() {
    return {
        message: '',
        hi: 'hi'
    }
  },
  mutations: {
    setMessage (state, message) {
        state.message = message
    },
    updateMessage(state, message) {
      state.hi = message
    },
  },
  actions : {
    setMessage({commit}, message) {
      commit('setMessage',message)
    },
    updateMessage({commit}, message){
      commit('updateMessage', message)
    }
  },
  getters: {
    getMessage: (state) => state.message,
    getupdateMesaage: (state) => state.updateMessage
  }
})