import Vue from 'vue'
import Vuex from 'vuex'
import todoApp from './modules/todoApps'

Vue.use(Vuex);

export const store = new Vuex.Store({
    modules: {
        todoApp
    }
});