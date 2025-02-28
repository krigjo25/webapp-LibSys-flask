
<template>
    <label :for="data.name">{{ data.name}} :</label>
    <input :type="data.type" :id="data.name" :name="data.name" :placeholder="data.name" v-model="data.value"/>
</template>

<script setup>

    //  Importing required dependencies
    import {reactive, watch, ref } from 'vue';


    //  Initializing reactive objects
    const props = defineProps(
    {
        data:{
            type: Object,
            required: true,
        }
    }
    );
    const buffer = reactive(
        {
            id: null,
            title: null,
            author: null
        }
    );

    const data = ref(props.data);

    function Reset()
    {
        buffer.title = "";
        buffer.author = "";
    }
    console.log(data)
</script>