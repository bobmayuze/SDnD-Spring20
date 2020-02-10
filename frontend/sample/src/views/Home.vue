<template>
  <div class="home">
    <h1>Dashboard</h1>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->

    <div style="background: #ECECEC; padding: 60px">
      <a-row :gutter="16" type="flex" justify="start">
        <a-col :xs="{ span: 4, offset: 0 }" :lg="{ span: 8, offset: 0 }">
          <div>
            <a-card title="Top 10 Templates" class="grid-Width" bordered = "false" style="width: 300px">
            <p>card content</p>
            <p>card content</p>
            <p>card content</p>
          </a-card>
          </div>
          <br>
          <div>
            <a-card title="Top 10 Templates" class="grid-Width" bordered = "false" style="width: 300px">
            <p>card content</p>
            <p>card content</p>
            <p>card content</p>
          </a-card>
          </div>
        </a-col>
        <a-col :xs="{ span: 4, offset: 0 }" :lg="{ span: 8, offset: 0 }">
          <div>
            <a-card title="Top 10 Templates" class="grid-Width" bordered = "false" style="width: 300px">
            <p>card content</p>
            <p>card content</p>
            <p>card content</p>
          </a-card>
          </div>
          <br>
          <div>
            <a-card title="Top 10 Templates" class="grid-Width" bordered = "false" style="width: 300px">
            <p>card content</p>
            <p>card content</p>
            <p>card content</p>
          </a-card>
          </div>
        </a-col>
        <a-col :xs="{ span: 4, offset: 0.5 }" :lg="{ span: 6, offset: 1 }">
          <a-card title="Top 10 Templates" class="grid-a-Width" bordered = "false" style="width: 300px">
            <p>card content</p>
            <p>card content</p>
            <p>card content</p>
          </a-card>
        </a-col>
      </a-row>                
    </div>
  </div>

</template>

<style scoped>
  .grid-Width {    
    background-color: rgb(163, 167, 166);
    border-radius: 4px;
    min-height: 100px;
  }
  .grid-a-Width {    
    background-color: rgb(81, 145, 131);
    border-radius: 4px;
    min-height: 220px;
  }
</style>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src



export default class Home extends Vue {}
</script>
