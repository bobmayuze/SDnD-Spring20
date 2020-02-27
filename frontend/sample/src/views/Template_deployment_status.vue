<template>
    <a-form id="components-form-demo-validate-other">
        <a-row>
            <a-col :span="6"></a-col>
            <h1>Tempalte Deployment Status</h1>
        </a-row>

        <br/>
        <br/>
        <br/>

        <a-row>
            <a-col :span="6"/>
            <a-col :span="6">
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
        
        <br/>
        <br/>
        <br/>
                
        <a-row>
            <a-col :span="6"/>

            <a-col :span="6">
                <a-button 
                    type="primary" 
                    html-type="button"
                    v-on:click="$router.go(-1)"
                >
                    Go Back
                </a-button>
            </a-col>            
            
        </a-row>        

    </a-form>

</template>


<script>
import axios from 'axios';

let available_regions = [
]

export default {
    mounted() {
        this.fetch(this.$route.query.origin_id, this);
    },
    data() {
        return {
            available_regions,
            template_info : 'SOME INFO',
            formItemLayout: {
                labelCol: { span: 6 },
                wrapperCol: { span: 14 },
            },            
        }
    },
    methods : {
    }
}
</script>

<style>
#components-form-demo-validate-other .dropbox {
  height: 180px;
  line-height: 1.5;
}
</style>