<template>
    <img :src="data.image" alt="Book Cover" width="100" height="100">
    
    <div>
      <h3>{{ data.title }}</h3>
      <small>by 
        <i v-for="author in data.author"> {{ author }} </i> - Published {{ data.published }} by 
        <i v-for="publisher in data.publisher"> {{ publisher }} </i>
      </small>
      <span v-for="review in data.review">| rating:{{review.rating}} by {{review.name}} </span>
      <p>{{ data.description }}</p>
      <div>
        <p v-for="genre in data.genre">{{ genre }}</p>
      </div>
    </div>
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