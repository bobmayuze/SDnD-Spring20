<template>
  <div>
    <a-row>
      <a-col :span="6"></a-col>
      <h1>New Deployment Jobs</h1>
    </a-row>    
    <a-form>
      <a-row>
        <a-col :span="6"></a-col>
        <h2>Step 1 : Choose Templates to be deployed</h2>
      </a-row>      
      <a-form-item
        v-bind="formItemLayout"
        label="Templates"
      >
      <a-select
          mode="multiple"
          labelInValue
          :value="value"
          placeholder="Select Templates"
          style="width: 100%"
          :filterOption="false"
          @search="fetchUser"
          @change="handleChange"
          :notFoundContent="fetching ? undefined : null"
      >
        <a-spin v-if="fetching" slot="notFoundContent" size="small"/>
        <a-select-option v-for="d in data" :key="d.value">{{d.text}}</a-select-option>
      </a-select>
      </a-form-item>


      <a-row>
        <a-col :span="6"></a-col>
        <h2>Step 2 : Choose Regions</h2>
      </a-row>
      <a-form-item
        v-bind="formItemLayout"
        label="China-North"
      >
      <a-checkbox-group :options="plainOptions" v-model="checkedList" @change="onChange" />
      <br/>
      <a-checkbox-group :options="plainOptions_2" v-model="checkedList" @change="onChange" />
      </a-form-item>

      <!-- Submit Button -->
      <a-row>
        <a-col :span="6"></a-col>
        <a-button @click="buttom_clicked(value, checkedList)" type="primary">Submit</a-button>
      </a-row>      
    </a-form>
  </div>
</template>

<style>

</style>

<script>
import jsonp from 'fetch-jsonp';
import querystring from 'querystring';
import debounce from 'lodash/debounce';
import axios from 'axios';

const plainOptions = ['Hangzhou', 'Beijing', 'Shanghai']
const plainOptions_2 = ['Hongkong', 'German', 'Sydney']
const defaultCheckedList = ['Hangzhou', 'Beijing']

export default {
  data() {
    this.formItemLayout = {
      labelCol: { span: 6 },
      wrapperCol: { span: 10 },
    }
    return {
      checkedList: defaultCheckedList,
      plainOptions,
      plainOptions_2,
      checkAll: false,
      data: [],
      value: [],
      fetching: false,
    }
  },
  methods: {
    onChange (checkedList) {
      console.log('onChange');
      
      this.checkAll = checkedList.length === plainOptions.concat(plainOptions_2).length
    },
    buttom_clicked (templates=[], regions="NOT PICKED YET") {    
      templates.map(template => {
        
        regions.map(region => {
          console.log('New deployment');
          
          console.log(template.key);
          console.log(template.label);
          console.log(region);
          
          fetch('http://localhost:5000/jobs',
            {
              method: 'PUT',    
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify({
                  "template_id" : template.key,
                  "region_id" : region,
                  "target_queue" : "sample_region_1"
                })
            }
          )
          .then(response => response.json())
          .then((body) => {
            console.log(body);
            this.$notification.open({
              message: 'Deployment Job Created',
              description:
                'Template ' + template.label + ' Created on Region ' + region,
              icon: <a-icon type="smile" style="color: #52c41a" />,
            });
            this.$router.push({
              path: `/jobs`
            })                     
          });          
        })
      })   
    },
    fetchUser (value) {
      console.log('fetching user', value);
      this.lastFetchId += 1;
      const fetchId = this.lastFetchId;
      this.data = []
      this.fetching = true
      axios.get('http://localhost:5000/templates',
        {
          params: {customer_id: '1'},
          headers: {'Content-Type': 'application/json'},
        }
      )
        .then((response) => {
          console.log(response.data);
          // if (fetchId !== this.lastFetchId) { // for fetch callback order
          //   return;
          // }
          const data = response.data.map(template => ({
            text: `${template.name}`,
            value: template._id,
          }));
          console.log(data);
          this.data = data
          this.fetching = false
        });
    },
    handleChange (value) {
      Object.assign(this, {
        value,
        data: [],
        fetching: false,
      })
    },
  }
}
</script>