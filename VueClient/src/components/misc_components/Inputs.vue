<template>
    <label :for="data.name">{{ data.name}}</label>
    <input :type="data.type" :id="data.name" :name="data.name" :placeholder="data.name" v-model="buffer"/>
</template>

<script setup>

    //  Importing required dependencies
    import { defineProps, defineEmits } from 'vue';


    //  Initializing reactive objects
    const props = defineProps(
    {
        data:{
        type: Array,
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

    function Reset()
    {
    buffer.title = "";
    buffer.author = "";
    }

    function UpdateEvent()
    {
    emit('shared-data', buffer);
    }
</script>