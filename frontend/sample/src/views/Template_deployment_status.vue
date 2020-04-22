<!-- This page display the deployment status of a template -->
<template>
  <div class="Templates">
    <h1>Template Deployment Status</h1>
    <a-table :columns="columns" :dataSource="data">
      <a slot="name" slot-scope="text">{{ text }}</a>
      <span slot="customTitle">
        <a-icon type="smile-o" />Region
      </span>
    </a-table>
    <a-button type="primary" html-type="button" v-on:click="$router.go(-1)">Go Back</a-button>
  </div>
</template>


<script>
import axios from "axios";

const columns = [
  {
    dataIndex: "name",
    key: "name",
    slots: { title: "customTitle" },
    scopedSlots: { customRender: "name" },
    width: "5%"
  },
  {
    title: "Deployment Status",
    dataIndex: "deployment_status",
    key: "deployment_status",
    width: "5%"
  },
  {
    title: "Create At",
    dataIndex: "created_time",
    key: "created_time",
    width: "10%"
  },
  {
    title: "Deployment Task Status",
    dataIndex: "task_status",
    key: "task_status",
    width: "10%"
  }
];

export default {
  mounted() {
    this.fetch(this.$route.query.origin_id, this);
  },
  data() {
    return {
      data: [
        {
          name: "Hangzhou",
          deployment_status: "",
          created_time: "",
          task_status: ""
        },
        {
          name: "Beijing",
          deployment_status: "",
          created_time: "",
          task_status: ""
        },
        {
          name: "Shanghai",
          deployment_status: "",
          created_time: "",
          task_status: ""
        },
        {
          name: "Hongkong",
          deployment_status: "",
          created_time: "",
          task_status: ""
        },
        {
          name: "German",
          deployment_status: "",
          created_time: "",
          task_status: ""
        },
        {
          name: "Sydney",
          deployment_status: "",
          created_time: "",
          task_status: ""
        }
      ],
      columns,
      template_info: "SOME INFO",
      task_info: "SOME INFO"
    };
  },
  methods: {
    // get the template info by the origin id
    // display the activated version template deployment status
    fetch(origin_id, element) {
      console.log("Feting detail for", origin_id);
      const url = "http://localhost:5000/templates";
      axios
        .get(url, {
          params: {
            template_id: origin_id,
            deployed_regions_required: "True"
          }
        })
        .then((response) => {
          console.log('here', response.data.details);
          let deployment_tasks_status = response.data.details;
          element.data.map(region => {
            deployment_tasks_status.map(regional_task => {
              
              if( region.name == regional_task.region){
                console.log(region.name, regional_task);
                region.task_status = regional_task.status;
                region.deployment_status = (regional_task.status == 'SUCCESS') ? 'YES' : 'NO';
                region.created_time = regional_task.create_time;
              }
              
            })
          })
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    buttonClieked(info) {
      console.log("Clicked", info);
      this.$router.push({
        path: `/templates/deployment_detail/?task_id=${info}`
      });
    }
  }
};
</script>

<style>
#components-form-demo-validate-other .dropbox {
  height: 180px;
  line-height: 1.5;
}
</style>