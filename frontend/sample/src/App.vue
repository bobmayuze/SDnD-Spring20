<template>
  <div id="app">
    <a-layout id="components-layout-demo-custom-trigger">
      <a-layout-sider :trigger="null" collapsible v-model="collapsed">
        <div class="logo">
          <h1>CMS</h1>
        </div>

        <a-menu theme="dark" mode="inline">
          <a-menu-item key="1">
            <a-icon type="dashboard" />
            <span>Home</span>
            <a href="#/"></a>
          </a-menu-item>

          <a-menu-item key="2">
            <a-icon type="rocket" />
            <span>Templates</span>
            <a href="#/templates"></a>
          </a-menu-item>

          <a-menu-item key="3">
            <a-icon type="schedule" />
            <span>Deployment Jobs</span>
            <a href="#/jobs"></a>
          </a-menu-item>

          <!-- <a-menu-item key="4">
            <a-icon type="global" />
            <span>Regions</span>
            <a href="#/regions"></a>
          </a-menu-item> -->
        </a-menu>
      </a-layout-sider>
      <a-layout>
        <a-layout-header style="background: #fff; padding: 0">
          <a-icon
            class="trigger"
            :type="collapsed ? 'menu-unfold' : 'menu-fold'"
            @click="()=> collapsed = !collapsed"
          />
        </a-layout-header>
        <a-layout-content
          :style="{ margin: '24px 16px', padding: '24px', background: '#fff', minHeight: '280px' }"
        >
          <router-view />
        </a-layout-content>
      </a-layout>
    </a-layout>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        collapsed: false,
      };
    },
  };
</script>
<style>
  #components-layout-demo-custom-trigger .trigger {
    font-size: 18px;
    line-height: 64px;
    padding: 0 24px;
    cursor: pointer;
    transition: color 0.3s;
  }

  #components-layout-demo-custom-trigger .trigger:hover {
    color: #1890ff;
  }

  #components-layout-demo-custom-trigger .logo {
    height: 32px;
    background: rgba(255, 255, 255, 0.2);
    margin: 16px;
  }

  #components-layout-demo-custom-trigger .logo h1 {
    color: rgba(255, 255, 255, 0.85);
  }

  #components-layout-demo-custom-trigger .ant-layout-sider-children {
    height: 100vh;
  }
</style>