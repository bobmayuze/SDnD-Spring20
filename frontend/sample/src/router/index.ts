import Vue from 'vue';
import Router from 'vue-router';
import Home from '../views/Home.vue';
import Templates from '../views/Templates.vue';

Vue.use(Router);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/templates',
    name: 'template',
    component: Templates,
  }
];

const router = new Router({
  routes,
});

export default router;
