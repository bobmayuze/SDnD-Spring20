<!-- This page display the deployment status of a template -->
<template>
  <a-form id="components-form-demo-validate-other">
    <a-row>
      <a-col :span="6"></a-col>
      <h1>Template Deployment Status</h1>
    </a-row>

    <br />
    <br />
    <br />

    <a-row>
      <a-col :span="6" />
      <a-col :span="8">
        <a-list :grid="{ gutter: 6, column: 3 }" :dataSource="available_regions">
          <a-list-item slot="renderItem" slot-scope="item">
            <div v-if="item.task_id">
              <a-button type="primary" @click="buttonClieked(item.task_id)">{{item.name}}</a-button>
            </div>
            <div v-else>
              <a-button type="primary" @click="buttonClieked(item.task_id)" disabled>{{item.name}}</a-button>
            </div>
          </a-list-item>
        </a-list>
      </a-col>
      <a-col :span="6"></a-col>
      <a-col :span="6"></a-col>
    </a-row>

    <br />
    <br />
    <br />

    <a-row>
      <a-col :span="6" />

      <a-col :span="6">
        <a-button type="primary" html-type="button" v-on:click="$router.go(-1)">Go Back</a-button>
      </a-col>
    </a-row>
  </a-form>
</template>


<script>
import axios from 'axios';

// Data center location list
// let available_regions = [
//     {'name' : 'Hangzhou'},
//     {'name' : 'Beijing'},
//     {'name' : 'Shanghai'},
//     {'name' : 'Hongkong'},
//     {'name' : 'German'},
//     {'name' : 'Sydney'}
// ]

export default {
    mounted() {
        this.fetch(this.$route.query.origin_id, this);
    },
    data() {
        return {
            available_regions: [
                                    {'name' : 'Hangzhou'},
                                    {'name' : 'Beijing'},
                                    {'name' : 'Shanghai'},
                                    {'name' : 'Hongkong'},
                                    {'name' : 'German'},
                                    {'name' : 'Sydney'}
                                ],
            template_info : 'SOME INFO',
            formItemLayout: {
                labelCol: { span: 6 },
                wrapperCol: { span: 14 },
            },            
        }
    },
    methods : {
        // get the template info by the origin id
        // display the activated version template deployment status
        fetch(origin_id, element){
            console.log('Feting detail for', origin_id);
            const url = 'http://localhost:5000/templates'
            axios.get(url, {
                params: {
                    'template_id': origin_id,
                    'deployed_regions_required': 'True'
                }
            })
            .then(function (response) {
                // console.log("Got sth here", response);
                element.template_info = response.data.details;
                console.log(element.template_info);
                response.data.details.map(record => {
                    element.available_regions.map(region => {
                        if (region.name == record.region) {
                            region.task_id = record.task_id
                            element.$forceUpdate()
                        }
                    })
                    
                })
            })
            .catch(function (error) {
                console.log(error);
            });         
        },
        buttonClieked(info){
            console.log('Clicked',info);
            this.$router.push({
                path: `/templates/deployment_detail/?task_id=${info}`
            })            
        },
    }
}
</script>

<style>
#components-form-demo-validate-other .dropbox {
  height: 180px;
  line-height: 1.5;
}
</style>