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

// Data center location list
let available_regions = [
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
];

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
      task_infor: "SOME INFO"
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
        .then(function(response) {
          element.data.map(region => {
            region.deployment_status = "NO";
          });
          element.template_info = response.data.details;
          console.log("Got sth fron query", element.template_info);
          element.template_info.map(record => {
            element.data.map(region => {
              if (region.name == record.region) {
                // Query the deployment task
                region.deployment_status = "YES";
                const task_url = "http://localhost:5000/jobs";
                axios
                  .get(task_url, {
                    params: {
                      job_id: record.task_id
                    }
                  })
                  .then(function(response) {
                    console.log("second query", response.data);
                    element.task_info = response.data;
                    element.task_info.map(task => {
                      if (task.task_id == task.task_id) {
                        region.created_time = task.create_time;
                        region.task_status = task.status;
                      }
                    });
                  })
                  .catch(function(error) {
                    console.log(error);
                  });
              }
            });
          });
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