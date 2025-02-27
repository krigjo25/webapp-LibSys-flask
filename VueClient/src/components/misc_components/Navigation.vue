<template>
    <nav>
        <Btn v-for="btn in props.data" :key="btn.id" :data="btn"/>
    </nav>
</template>

<script setup>

    //  Importing Components
    import Btn from './Btn.vue';

    const props = defineProps(['data']);
</script>