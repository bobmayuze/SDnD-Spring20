<template>
  <div class="Jobs">
    <h1>Jobs</h1>



    <a-button type="primary">New Deployment Jobs</a-button>
    
    <a-table 
      :columns="columns"
      :rowKey="record => record.task_id"
      :dataSource="data"
      :pagination="pagination"
      :loading="loading"
      size="middle"
    >

            

    </a-table>
    
  </div>


</template>



<script>

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
    
  },
}
</script>
