// import Vue from 'vue';
// import App from './App.vue';
// import router from './router';

// Vue.config.productionTip = false;

// new Vue({
//   router,
//   render: (h) => h(App),
// }).$mount('#app');

import router from './router/index';

import Vue from 'vue';
import Antd from 'ant-design-vue';
import Viser from 'viser-vue'
import App from './App.vue';
import 'ant-design-vue/dist/antd.css';
Vue.config.productionTip = false;

Vue.use(Antd);
Vue.use(Viser);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
  router,
  render: (h) => h(App),
}).$mount('#app');