<!-- This page is the interface for the update of template
Only update the template name and files, keep the origin tags and descriptions -->
<template>
  <a-form id="components-form-demo-validate-other" :form="form" @submit="handleSubmit">
    <a-row>
      <a-col :span="6"></a-col>
      <h1>Update Template</h1>
    </a-row>

    <a-form-item v-bind="formItemLayout" label="Template Name">
      <a-input
        v-decorator="[
          'template_name',
          { rules: [{ required: true, message: 'Please input template tag' }] },
        ]"
        placeholder="Please input template Name"
      />
    </a-form-item>

    <a-form-item v-bind="formItemLayout" label="Template Tags">
      <a-input
        v-decorator="[
          'template_tags',
          { rules: [{ required: true, message: 'Please input template tags' }] },
        ]"
        placeholder="Please input template tags"
      />
    </a-form-item>

    <a-form-item v-bind="formItemLayout" label="Template Desciption">
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
          <a-button>
            <a-icon type="upload" />Select File
          </a-button>
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
          >{{uploading ? 'Uploading' : 'Start Upload' }}</a-button>
        </a-col>

        <a-button
          type="primary"
          html-type="button"
          v-on:click="$router.go(-1)"
          style="margin-top: 24px"
        >Go Back</a-button>
      </a-row>
    </a-form-item>
  </a-form>
</template>

<script>
import reqwest from "reqwest";
import axios from "axios";

export default {
  data: () => ({
    template_info: "SOME INFO",
    formItemLayout: {
      labelCol: { span: 6 },
      wrapperCol: { span: 14 }
    },
    fileList: [],
    uploading: false
  }),
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "validate_other" });
  },
  mounted() {
    // this.fetch(this.$route.query.origin_id, this);
    console.log(this.$route.query.origin_id);
  },
  methods: {
    fetch(template_id, element) {
      console.log("Feting detail for", template_id);
      const url = "http://localhost:5000/templates";
      axios
        .get(url, {
          params: {
            template_id: template_id
          }
        })
        .then(response => {
          element.template_info = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    handleSubmit(e) {
      // validate the form input
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log("Received values of form: ", values);
        }
      });
    },
    normFile(e) {
      console.log("Upload event:", e);
      if (Array.isArray(e)) {
        return e;
      }
      return e && e.fileList;
    },

    handleRemove(file) {
      const index = this.fileList.indexOf(file);
      const newFileList = this.fileList.slice();
      newFileList.splice(index, 1);
      this.fileList = newFileList;
    },

    beforeUpload(file) {
      this.fileList = [...this.fileList, file];
      console.log(this.fileList);
      console.log(file);

      return false;
    },

    handleUpload() {
      let { fileList } = this;
      let formData = new FormData();
      fileList.forEach(file => {
        formData.append("files", file);
      });
      this.uploading = true;
      // formData.append('username', 'Chris');

      this.form.validateFields((err, values) => {
        formData.append("name", values.template_name);
        formData.append("description", values.template_desc);
        formData.append("tags[]", values.template_tags);
        formData.append("origin_id", this.$route.query.origin_id);
      });

      console.log(formData);

      // Display the key/value pairs
      for (var pair of formData.entries()) {
        console.log(pair[0] + ", " + pair[1]);
      }

      // You can use any AJAX library you like
      reqwest({
        url: "http://localhost:5000/versions",
        method: "post",
        processData: false,
        data: formData,
        success: () => {
          this.fileList = [];
          this.uploading = false;
          this.$notification.open({
            message: "Template Updated",
            description: "Template successfully updated",
            icon: <a-icon type="smile" style="color: #52c41a" />
          });
          this.$router.push({
            path: `/templates`
          });
        },
        error: () => {
          this.uploading = false;
          this.$message.error("upload failed.");
        }
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