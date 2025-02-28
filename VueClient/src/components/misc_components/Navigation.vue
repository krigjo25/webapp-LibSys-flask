<template>
    <nav>
        <Btn v-for="btn in props.data" :key="props.id" :data="btn" :id="props.id"/>
    </nav>
</template>

<script setup>

    //  Importing Components
    import Btn from './Btn.vue';

    const props = defineProps(['data', 'id']);
</script>