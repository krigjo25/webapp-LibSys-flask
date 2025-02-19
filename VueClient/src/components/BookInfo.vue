<template>
  <details>
    <img :src="data.image" alt="Book Cover" width="100" height="100">
    
    <summary>{{ data.title }}</summary>
    <small>by 
      <i v-for="author in data.author"> {{ author }} </i> - Published {{ data.published }} by 
      <i v-for="publisher in data.publisher"> {{ publisher }} </i>
    </small>
    <p>{{ data.description }}</p>
    <p v-for="genre in data.genre" > {{ genre }}</p>
  </details>

</template>
  
<script setup>
//  Importing required dependencies
import { defineProps } from 'vue';

//  Initializing reactive objects
const props = defineProps(
  {
    data:{
    type: Array,
    required: true,
    }
  }
);
</script>