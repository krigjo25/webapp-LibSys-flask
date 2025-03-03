
<template>
    <legend>{{ props.data.title }}</legend>
    <div v-for="dt in data">
        
        <label :for="dt.name">{{ dt.name}} :</label>
        <input :type="dt.type" :id="dt.id" :name="dt.name" :placeholder="dt.name" v-model="dt.value"/>
    </div>
</template>

<script setup>

    //  Importing required dependencies
    import {reactive, watch, ref, defineEmits } from 'vue';

    const emit = defineEmits(['upsert-form']);

    //  Initializing reactive objects
    const props = defineProps(
    {
        data:{
            type: Object,
            required: true,
        }
    });
    
    const data = props.data.data;
    const buffer = reactive({});

    console.log("Inputs", data.value);

    watch(data, (n, o) => {

        //  Initialize variables
        
        const genre = 'genre';
        const rewiew = 'rewiew';
        const file = 'Upload an image';
        const array = ['.jpg', '.png', '.jpeg', '.gif'];
        //  Loop through the new data
        for (let i = 0; i < n.length; i++) 
        {
            //  Ensure that no genre or rewiews is pushed to the buffer
            if (genre != n[i].name  && n[i].name != rewiew && n[i].name != file) 
            {
                //  Push the data to the buffer
                buffer[n[i].name] = n[i].value;
                
            }
            else if (n[i].name == file)
            {

                //  Ensure that the file includes an acceptable image
                for (let j = 0; j < array.length; j++) 
                {
                    const element = n[i].value || 'null';
                    if (element.includes('jpg')) 
                    {
                        buffer.path = n[i].value;
                    }
                    else {
                        n[i].value = null;
                    }
                }
            }
            


        }
        emit('upsert-form', buffer);
    });
</script>