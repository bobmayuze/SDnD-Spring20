import Vue from 'vue';
import Router from 'vue-router';
import Home from '../views/Home.vue';
import Templates from '../views/Templates.vue';
import Templates_create from '../views/Templates_create.vue';
import Template_detailed_info from '../views/Template_detailed_info.vue';
// import Template_update from '../views/Template_update.vue';
// import Template_deployment_detail from '../views/Template_deployment_detail.vue';
// import Template_deployment_status from '../views/Template_deployment_status.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/templates',
      name: 'template',
      component: Templates,
    },
    {
      path: '/templates/templates_create',
      name: 'templates_create',
      component: Templates_create,
    },
  {
    path: '/templates/template_detailed_info',
    name: 'template_detailed_info',
    component: Template_detailed_info,
  },
  // {
  //   path: '/templates/template_update',
  //   name: 'Template_update',
  //   component: Template_update,
  // },
  // {
  //   path: '/templates/deployment_detail',
  //   name: 'deployment_detail',
  //   component: Template_deployment_detail,
  // },
  // {
  //   path: '/templates/deployment_status',
  //   name: 'deployment_status',
  //   component: Template_deployment_status,
  // }
  ],
});

