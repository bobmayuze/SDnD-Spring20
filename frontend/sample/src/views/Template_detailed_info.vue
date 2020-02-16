<template>
    <div>
        <h1>Template Detail</h1>
        <div>{{template_info}}</div>
    </div>
    
</template>

<script>
import axios from 'axios';


export default {
    mounted() {
        this.fetch(this.$route.query.template_id, this);
    },
    data() {
        return {
            template_info : 'SOME INFO'
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
            
            
        }
    }
}
</script>
 No newline at end of file
