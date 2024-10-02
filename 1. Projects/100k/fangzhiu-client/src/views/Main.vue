<template>
  Main
</template>
<script>
// 导入MainListWrapper组件
import MainListWrapper from "@/components/MainListWrapper.vue";
// 导入MainSidebar组件
import MainSidebar from "@/components/MainSidebar.vue";

export default {
  name: "Main",
  // 注册组件
  components: {
    MainListWrapper,
    MainSidebar
  }
};
</script>