<template>
    <button>
        <i :class="data.cls"></i>
    </button>
</template>

<script setup>
    //  Importing required dependencies
    import axios from 'axios';
    import { defineProps } from 'vue';

    //  Importing Components
    const props = defineProps(['data']);
</script>