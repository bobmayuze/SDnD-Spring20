<!-- This page display the deployment details of a template -->

<template>
  <a-form id="components-form-demo-validate-other">
    <a-row>
      <a-col :span="6"></a-col>
      <h1>Template Deployment Detail</h1>
    </a-row>

    <!-- {{template_info}} -->

    <br />
    <a-form-item v-bind="formItemLayout" label="Target Region">
      <h2>{{template_info.target_region}}</h2>
    </a-form-item>

    <a-form-item v-bind="formItemLayout" label="Created At">
      <h2>{{template_info.create_time}}</h2>
    </a-form-item>

    <a-form-item v-bind="formItemLayout" label="Status">
      <h2>{{template_info.status}}</h2>
    </a-form-item>

    <br />
    <br />
    <br />
    <br />
    <br />
    <a-row>
      <a-col :span="6" />

      <!-- <a-col :span="8">              
      </a-col>-->

      <a-col :span="6">
        <a-button type="primary" html-type="button" v-on:click="$router.go(-1)">Go Back</a-button>
      </a-col>
    </a-row>
    <!-- {{template_info}} -->
  </a-form>
</template>

<script>
import axios from "axios";
export default {
  mounted() {
    this.fetch(this.$route.query.job_id, this);
  },
  data() {
    return {
      template_info: "SOME INFO",
      formItemLayout: {
        labelCol: { span: 6 },
        wrapperCol: { span: 14 }
      }
    };
  },
  methods: {
    // GET methods, endpoint: jobs
    // Get the deplyment jobs list
    fetch(job_id, element) {
      console.log("Feting detail for", job_id);
      const url = "http://localhost:5000/jobs";
      axios
        .get(url, {
          params: {
            job_id: job_id
          }
        })
        .then(function(response) {
          element.template_info = response.data;
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    buttonClieked() {
      console.log("Clicked");
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