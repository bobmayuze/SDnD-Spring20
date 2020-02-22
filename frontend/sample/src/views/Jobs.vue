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

            

    </a-table>
    
  </div>


</template>



<script>
import reqwest from 'reqwest';
import axios from 'axios';

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
    new_template () {
      window.location.assign('#/jobs/create_deployment_jobs')
    },
    handleTableChange (pagination, filters, sorter) {
      console.log(pagination);
    },
    // FIXME: problem loading
    fetch (params = {}) {
      console.log('fetch triggered');
      this.loading = true
      reqwest({
        url: 'http://localhost:5000/get_deployment_jobs',
        method: 'get',
        data: {
          results : 10,
        },
        type: 'json',
      }).then((data) => {
        console.log(data);
        this.loading = false;
        this.data = data;
        // this.pagination = pagination;
      });
    }
  },
}
</script>
