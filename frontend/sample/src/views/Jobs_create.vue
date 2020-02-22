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
      </a-row>      
    </a-form>
  </div>
</template>

<style>

</style>

<script>
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
      data: [],
      value: [],
      fetching: false,
    }
  },
  methods: {
    onChange (checkedList) {
      console.log('onChange');
      
      this.indeterminate = !!checkedList.length && (checkedList.length < plainOptions.length)
      this.checkAll = checkedList.length === plainOptions.concat(plainOptions_2).length
    },
  }
}
</script>