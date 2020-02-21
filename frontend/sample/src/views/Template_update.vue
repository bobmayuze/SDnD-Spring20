<template>

  <a-form id="components-form-demo-validate-other" :form="form" @submit="handleSubmit">
    <a-row>
      <a-col :span="6"></a-col>
      <h1>Update Template</h1>
    </a-row>

    <a-form-item
      v-bind="formItemLayout"
      label="Template Name"
    >
      <a-input
        v-decorator="[
          'template_name',
          { rules: [{ required: true, message: 'Please input template tag' }] },
        ]"
        placeholder="Please input template Name"
      />
    </a-form-item>

    <a-form-item
      v-bind="formItemLayout"
      label="Template Tags"
    >
      <a-input
        v-decorator="[
          'template_tags',
          { rules: [{ required: true, message: 'Please input template tags' }] },
        ]"
        placeholder="Please input template tags"
      />
    </a-form-item>    

    <a-form-item
      v-bind="formItemLayout"
      label="Template Desciption"
    >
      <a-textarea
        placeholder="Autosize height with minimum and maximum number of lines"
        :autosize="{ minRows: 3, maxRows: 10 }"
        v-decorator="[
          'template_desc',
          { rules: [{ required: true, message: 'Please input template description' }] },
        ]"
      />      
    </a-form-item>

    <a-form-item v-bind="formItemLayout" label="Template json">
      <a-row>
      <a-upload :fileList="fileList" :remove="handleRemove" :beforeUpload="beforeUpload">
        <a-button> <a-icon type="upload" /> Select File </a-button>
      </a-upload>
      </a-row>
      
      <a-row>
        <a-col :span="20">
          <a-button
            type="primary"
            @click="handleUpload"
            :disabled="fileList.length === 0"
            :loading="uploading"
            style="margin-top: 24px"
          >
            {{uploading ? 'Uploading' : 'Start Upload' }}
          </a-button>
        </a-col>

      <a-button 
          type="primary" 
          html-type="button"
          v-on:click="$router.go(-1)"
          style="margin-top: 24px"
      >
          Go Back
      </a-button>  
      </a-row>      
    </a-form-item>

  </a-form>
</template>

<script>
import reqwest from 'reqwest';

export default {
  data: () => ({
    formItemLayout: {
      labelCol: { span: 6 },
      wrapperCol: { span: 14 },
    },
    fileList: [],
    uploading: false,    
  }),
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: 'validate_other' });
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log('Received values of form: ', values);
        }
      });
    },
  },
};
</script>

<style>
#components-form-demo-validate-other .dropbox {
  height: 180px;
  line-height: 1.5;
}
</style>