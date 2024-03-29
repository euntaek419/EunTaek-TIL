import ListView from './ListView.vue';
import bus from '../utils/bus.js';

export default function createdListView(name) {
    return {
        // 재사용할 인스턴스(컴포넌트) 옵션 & 로직
        name,
        created() {
            bus.$emit('start:spinner');
            this.$store.dispatch('FETCH_LIST', this.$route.name)
              .then(() => {
                console.log('fetched');
                bus.$emit('end:spinner');
                })
              .catch((error) => {
                console.log(error);
                });
            },
        render(createElement) {
            return createElement(ListView);
        },
    }
}