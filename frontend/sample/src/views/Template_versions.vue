<!-- This page display the version list of a template -->
<template>
  <div class="Templates">
    <h1>Template Versions</h1>

    <a-table
      :columns="columns"
      :rowKey="record => record.version_id"
      :dataSource="data"
      :pagination="pagination"
      :loading="loading"
      @change="handleTableChange"
      size="middle"
    >
      <span slot="Activated" slot-scope="d">
        <div v-if="d">True</div>
        <div v-else>False</div>
      </span>

      <span slot="operation" slot-scope="record">
        <div v-if="record.is_activated">
          <a-button @click="activate_version(record)" type="primary">Activate</a-button>
          <a-divider type="vertical" />
          <a-button @click="delete_version(record)" type="danger" disabled>Delete</a-button>
        </div>
        <div v-else>
          <a-button @click="activate_version(record)" type="primary">Activate</a-button>
          <a-divider type="vertical" />
          <a-button @click="delete_version(record)" type="danger">Delete</a-button>
        </div>
      </span>
    </a-table>

    <a-button type="primary" html-type="button" v-on:click="$router.go(-1)">Go Back</a-button>
  </div>
</template>



<script>
import reqwest from "reqwest";
import axios from "axios";

// set up the display table values
const columns = [
  {
    title: "Version Id",
    dataIndex: "version_id",
    width: "15%"
  },
  {
    title: "Name",
    dataIndex: "name",
    width: "15%"
  },
  {
    title: "Activated",
    dataIndex: "is_activated",
    width: "10%",
    scopedSlots: { customRender: "Activated" }
  },
  {
    title: "Created At",
    dataIndex: "created_at",
    width: "20%"
  },
  {
    title: "Action",
    key: "operation",
    scopedSlots: { customRender: "operation" }
  }
];

export default {
  mounted() {
    this.fetch();
  },
  data() {
    return {
      data: [],
      pagination: {
        pageSize: 10
      },
      loading: false,
      columns
    };
  },
  methods: {
    handleTableChange(pagination, filters, sorter) {
      console.log(pagination);
    },
    activate_version(record) {// activate other version template
      console.log("Activating", record);// endpoint: versions, method: put
      const activate_url = "http://localhost:5000/versions";
      axios({
        method: "put",
        url: activate_url,
        data: {
          'origin_id': record.origin_id,
          'version_id': record.version_id
        }
      })
        .then(function(response) {
          console.log(response);
          window.location.reload();
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    delete_version(record) {// delete a certain version in the database
      console.log("Deleting", record);// endpoint: versions, method: delete
      const delete_url = "http://localhost:5000/versions";
      axios
        .delete(delete_url, {
          data: {
            'origin_id': record.origin_id,
            'version_id': record.version_id
          }
        })
        .then(function(response) {
          console.log(response);
          window.location.reload();
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    fetch(params = {}) {// get the version list of a template
      console.log("fetch triggered", this.$route.query.origin_id);

      this.loading = true;
      reqwest({// endpoint: versions, method: get
        url: "http://localhost:5000/versions",
        method: "get",
        data: {
          origin_id: this.$route.query.origin_id
        },
        type: "json"
      }).then(data => {
        console.log(data);
        this.loading = false;
        this.data = data;
      });
    }
  }
};
</script>
