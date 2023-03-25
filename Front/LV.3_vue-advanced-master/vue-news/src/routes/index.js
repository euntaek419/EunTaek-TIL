import Vue from 'vue';
import VueRouter from 'vue-router';
import  NewsView from '../views/NewsView.vue';
import  AskView from '../views/AskView.vue';
import  JobsView from '../views/JobsView.vue';
import  ItemView from '../views/ItemView.vue';
import  UserView from '../views/UserView.vue';

Vue.use(VueRouter);

export const router = new VueRouter({
  mode : 'history', //URL에서 # 값 제거
  routes: [
    {
        path: '/',
        redirect: '/news',

    },
    {
        // path : url 주소 
        //component : url 주소로 갔을 때 표시될 컴포넌트 
        path: '/news',
        component: NewsView,
    },
    {
        path: '/ask',
        component: AskView,
    },
    {
        path: '/jobs',
        component: JobsView,
    },
    {
        path: '/item/:id',
        component: ItemView,
    },
    {
        path: '/user/:id',
        component: UserView,
    },
  ]
});