<template>
    <button :type="props.data.type" @click="props.data.action(props.id)">
        <i :class="props.data.cls"></i>
    </button>
</template>

<script setup>
    //  Importing Components
    const props = defineProps(['data', 'id']);
    
</script>