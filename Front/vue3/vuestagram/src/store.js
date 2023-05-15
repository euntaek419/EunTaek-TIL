import { createStore } from 'vuex'
import axios from 'axios'

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
        },
        setMore(state, data){
            state.more = data
        }
    },
    actions : {
        getData(context) {
            axios.get(`https://codingapple1.github.io/vue/more${this.count}.json`)
            .then((a) =>{
              context.commit('setMore', a.data)
            })
        }
    }
})


export default store;