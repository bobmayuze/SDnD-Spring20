<template>
  <div class="Jobs">
    <h1>Jobs</h1>



    <a-button @click="new_template()" type="primary">New Deployment Jobs</a-button>
    
    <a-table 
      :columns="columns"
      :rowKey="record => record.task_id"
      :dataSource="data"
      :pagination="pagination"
      :loading="loading"
      @change="handleTableChange"
      size="middle"
    >

      <span slot="status" slot-scope="record">
        <div v-if="record=='SUCCESS'">
          <a-tag color="green">SUCCESS</a-tag>
        </div>
        <div v-else-if="record=='FAILED'">
          <a-tag color="red">FAILED</a-tag>
        </div>                
        <div v-else>
          <a-tag color="orange">PENDING</a-tag>
        </div>        
      </span>  

      <span slot="operation" slot-scope="record">
        <div v-if="record.status=='REVOKED'">
          <a-button type="primary" disabled>Revoke</a-button>
        </div>
        <div v-else-if="record.status=='SUCCESS'">
          <a-button type="primary" disabled>Revoke</a-button>
        </div>        
        <div v-else>
          <a-button @click="revoke_task(record)" type="primary">Revoke</a-button>
        </div>        
        <!-- <a-button @click="revoke_task(record.task_id)" type="primary">Revoke</a-button> -->
      </span> 

    </a-table>
    
  </div>


</template>



<script>
import reqwest from 'reqwest';
import axios from 'axios';
// const axios = require('axios');

const columns = [{
  title: 'Task Id',
  dataIndex: 'task_id',
  width: '20%',
}, {
  title: 'Region',
  dataIndex: 'target_region',
  width: '10%',
}, {
  title: 'Teamplate',
  dataIndex: 'template_name',
  width: '10%',  
}, {
  title: 'Status',
  dataIndex: 'status',
  width: '15%', 
  scopedSlots: { customRender: 'status' }
}, {
  title: 'Created At',
  dataIndex: 'create_time',
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
    revoke_task (record) {
      console.log('Clicked', record.task_id);
      const revoke_url = 'http://localhost:5000/jobs'
      axios.delete(revoke_url, {
        data: {'task_id' : record.task_id}
      })
      .then(function (response) {
        record.status = 'REVOKED'
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });

      
    },
    new_template () {
      window.location.assign('#/jobs/create_deployment_jobs')
    },    
    handleTableChange (pagination, filters, sorter) {
      console.log(pagination);
    },
    fetch (params = {}) {
      console.log('fetch triggered');
      this.loading = true
      reqwest({
        url: 'http://localhost:5000/jobs',
        method: 'GET',
        data: {
          results : 10,
        },
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
