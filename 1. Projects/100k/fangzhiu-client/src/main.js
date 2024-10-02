import App from "./App.vue";
import Vue from "vue";
import router from "./router";
import store from "./store";
import "./plugins/element.js";
import "./assets/styles/main.scss";
import CommentList from "@/components/CommentList";


Vue.component("CommentList", CommentList);
Vue.config.productionTip=false;

new Vue({
  router,
  store,
  render:h=>h(App)
}).$mount("#app")