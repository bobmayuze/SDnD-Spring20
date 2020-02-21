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
      </a-form-item>


      <a-row>
        <a-col :span="6"></a-col>
        <h2>Step 2 : Choose Regions</h2>
      </a-row>
      <a-form-item
        v-bind="formItemLayout"
        label="China-North"
      >
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
export default {
  data() {
    this.formItemLayout = {
      labelCol: { span: 6 },
      wrapperCol: { span: 10 },
    }
    return {
      data: [],
      value: [],
      fetching: false,
    }
  },
  methods: {
    
  }
}
</script>