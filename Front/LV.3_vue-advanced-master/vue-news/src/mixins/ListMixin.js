import bus from '../utils/bus.js';
// mixin
export default {
    //재사용할 컴포넌트 옵션
    mounted() {
      bus.$emit('end:spinner');
    }
    // created() {
    //     bus.$emit('start:spinner');
    //     this.$store.dispatch('FETCH_LIST', this.$route.name)
    //       .then(() => {
    //         console.log('fetched');
    //         bus.$emit('end:spinner');
    //       })
    //       .catch((error) => {
    //         console.log(error);
    //       });
    // }
}