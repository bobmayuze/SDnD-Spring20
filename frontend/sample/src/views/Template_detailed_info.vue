<template>
    <a-form id="components-form-demo-validate-other">
        <a-row>
            <a-col :span="6"></a-col>
            <h1>Template Detail</h1>
        </a-row>
        <br/>

        <a-form-item
            v-bind="formItemLayout"
            label="Name"
        >
            <h2>{{template_info.name}}</h2>
        </a-form-item>

        <a-form-item
            v-bind="formItemLayout"
            label="Activated Version"
        >
            <h2 style="inline">{{template_info._id}}</h2>
            <a-button 
                type="primary" 
                html-type="button"
                v-on:click="$router.push(`/templates/template_versions/?template_id=${$route.query.template_id}`)"
            >
                View All Versions
            </a-button>      
        </a-form-item>

        <a-form-item
            v-bind="formItemLayout"
            label="Created At"
        >
            <h2>{{template_info.created_at}}</h2>
        </a-form-item> 

        <a-form-item
            v-bind="formItemLayout"
            label="Description"
        >
            {{template_info.description}}
        </a-form-item> 

        <a-form-item
            v-bind="formItemLayout"
            label="Tags"
        >
            <a-tag
                :color="Math.ceil(Math.random()*10) > 5 ? 'green' : 'pink'"
            >
                {{template_info.key_words}}
            </a-tag>
        </a-form-item> 

        <br/>
        <br/>
        <br/>        
        <br/>        
        <br/>      
        <a-row>
            <a-col :span="6"/>

            <a-col :span="8">
                <a-button 
                    type="primary" 
                    html-type="button"
                    v-on:click="$router.push(`/templates/template_update/?template_id=${$route.query.template_id}`)"
                >
                    New Version
                </a-button>                

            </a-col>

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


export default {
    mounted() {
        this.fetch(this.$route.query.template_id, this);
    },
    data() {
        return {
            template_info : 'SOME INFO',
            formItemLayout: {
                labelCol: { span: 6 },
                wrapperCol: { span: 14 },
            },       
        }
    },
    methods : {
        fetch(template_id, element){
            console.log('Feting detail for', template_id);
            const url = 'http://localhost:5000/getTemplateByID'
            axios.post(url, {
                'template_id' : template_id
            })
            .then(function (response) {
                element.template_info = response.data
            })
            .catch(function (error) {
                console.log(error);
            });         

        },
        buttonClieked(){
            console.log('Clicked');
        }
    }
}
</script>

<style>
#components-form-demo-validate-other .dropbox {
    height: 180px;
    line-height: 1.5;
}
</style>
