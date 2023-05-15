import { createStore } from 'vuex'

const store = createStore({
    state () {
        return {
            name : 'kim',
            age : 20,
            likes : 30,
            likestate : false,
        }
    },
    mutations : {
        namechange(state, payload) {
            state.name += payload
        },
        ageup(state) {
            state.age++
        },
        likesup(state) {
            if(state.likestate == false){
              state.likes++
              state.likestate = true
            }
            else {
                state.likes--
                state.likestate = false
            }
        }
    },
})


export default store;