<template>
    <a-form id="components-form-demo-validate-other" :form="form" @submit="handleSubmit">
    <a-row>
      <a-col :span="6"></a-col>
      <h1>New Template</h1>
    </a-row>

    <a-form-item v-bind="formItemLayout" label="Template Name">
    </a-form-item>

    <a-form-item v-bind="formItemLayout" label="Experiment ID">
    </a-form-item>

    <a-form-item v-bind="formItemLayout" label="Template Description">
    </a-form-item>

    <a-form-item v-bind="formItemLayout" label="Tag">
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
      </a-row>      
    </a-form-item>
    
    <a-form-item :wrapper-col="{ span:16, offset:6}">
        <a-row type="flex" justify="space-between">
            <a-col :span="8">
            <a-button type="primary" html-type="submit">
            Submit
            </a-button>
            </a-col>

            <a-col :span="8">
            <a-button 
                type="primary" 
                html-type="button"
                v-on:click="$router.go(-1)"
                style="margin-top: 24px"
            >
            Discard
            </a-button>
            </a-col>
        </a-row>   
    </a-form-item>
    </a-form>
</template>


<script>
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
        }
    },
  };
</script>

<style>
#components-form-demo-validate-other .dropbox {
  height: 180px;
  line-height: 1.5;
}
</style>