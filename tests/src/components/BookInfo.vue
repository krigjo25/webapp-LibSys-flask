<template>
    <Header />
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
  import { reactive } from 'vue';
  import { useRoute } from 'vue-router';

  //  Importing components
  import Header from './header_components/Header.vue';

  //  Initializing reactive objects
  const data = history.state.data;
  console.log(data);
</script>