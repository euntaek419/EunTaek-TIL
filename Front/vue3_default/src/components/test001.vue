<template>
  <div>
    <div class="section" v-for="(section, index) in sections" :key="index">
      <!-- 각 섹션의 내용 -->
    </div>
  </div>
</template>

<script>
import { gsap } from "gsap";
import { ScrollToPlugin } from "gsap/ScrollToPlugin";
import { ScrollSmoother } from "gsap/ScrollSmoother";

gsap.registerPlugin(ScrollToPlugin, ScrollSmoother);

export default {
  data() {
    return {
      sections: ['Section 1', 'Section 2', 'Section 3', 'Section 4'], // 섹션의 데이터 배열
    };
  },
  mounted() {
    // ScrollSmoother 초기화
    gsap
      .to(window, {
        ScrollSmoother: {
          scrollProperties: 0,
          frame: 0.04,
        },
        duration: 1,
      });
  },
  methods: {
    scrollToSection(index) {
      // 해당 섹션으로 스크롤
      gsap.to(window, {
        scrollTo: { y: `.${this.$refs.sectionRef[index].classList[0]}`, offsetY: 70 },
        duration: 1,
      });
    }
  }
};
</script>

<style scoped>
.section {
  height: 100vh; /* 섹션의 높이를 화면 높이와 동일하게 설정 */
}
</style>