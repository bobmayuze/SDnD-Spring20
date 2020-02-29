<template>
  <div class="Templates">
    <h1>Templates</h1>

    <a-button @click="new_template()" type="primary">New Template</a-button>
    
    <a-table 
      :columns="columns"
      :rowKey="record => record._id"
      :dataSource="data"
      :pagination="pagination"
      :loading="loading"
      @change="handleTableChange"
      size="middle"
    >

      <span slot="key_words" slot-scope="key_words">
        <a-tag
          v-for="tag in key_words"
          :key="tag"
          :color="Math.ceil(Math.random()*10) > 5 ? 'green' : 'pink'"
        >
          {{tag.toUpperCase()}}
        </a-tag>
      </span>

      <span slot="operation" slot-scope="record">
        <div v-if="record.status=='REVOKED'">
          <a-button type="primary" disabled>Revoke</a-button>
        </div>
        <div v-else>
          <a-button @click="get_details(record._id)" type="primary">Details</a-button>
          <a-divider type="vertical" />
          <a-button @click="get_deployment_status(record)" type="primary">Deployment Status</a-button>
        </div>        
      </span>    

    </a-table>
    
  </div>
</template>



<script>
import reqwest from 'reqwest';
import axios from 'axios';

const columns = [{
  title: 'Template Id',
  dataIndex: 'origin_id',
  width: '15%',
}, {
  title: 'Name',
  dataIndex: 'name',
  width: '15%',
}, {
  title: 'Tags',
  dataIndex: 'tags',
  width: '25%',
}, {  
  title: 'Created At',
  dataIndex: 'created_at',
  width: '20%',
}, {  
  title: 'Action', 
  key: 'operation', 
  scopedSlots: { customRender: 'operation' }  
}];

export default {
  mounted() {
    this.fetch();
  },
  data() {
    return {
      data: [],
      pagination: {
        'pageSize' : 10
      },
      loading: false,
      columns,
    }
  },
  methods: {
    get_details (record) {
      console.log('Clicked', record);
      this.$router.push({
         path: `/templates/template_detailed_info/?template_id=${record}`
      })      
    },    
    get_deployment_status (record) {
      console.log('Origin', record.origin_id);
      this.$router.push({
        path: `/templates/deployment_status/?origin_id=${record.origin_id}`
      })
    },
    new_template () {
      window.location.assign('#/templates/templates_create')
    },    
    handleTableChange (pagination, filters, sorter) {
      console.log(pagination);
    },
    fetch (params = {}) {
      console.log('fetch triggered');
      this.loading = true
      reqwest({
        url: 'http://localhost:5000/templates',
        method: 'get',
        type: 'json',
      }).then((data) => {
        console.log(data);
        this.loading = false;
        this.data = data;
      });      

    }
  },
}
</script>
