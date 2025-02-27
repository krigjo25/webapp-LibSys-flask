#  The first Vue project
<template>
  <div>
    <Books :nav="buttons.nav" :data="buttons.data"/>
  </div>
</template>

<script setup>

  //  Importing required dependencies
  import { reactive, onMounted } from 'vue';
  import { Response, data } from '../assets/js/response.js';
  import { CreateBook, RemoveBook, UpdateBook } from '../assets/js/crud.js';
  //  Importing components
  import Books from './Books.vue';
  
const buttons = reactive(
  { 
    nav : true,
    data:
    [
      {
        id: 1,
        type: 'submit',
        cls: 'bi bi-plus',
        action: CreateBook
      },
      {
        id: 2,
        type: 'button',
        cls: 'bi bi-arrow-clockwise',
        action:() => {}
      },
      {
        id: 3,
        type: 'button',
        cls: 'bi bi-trash',
        action:RemoveBook,
      }
    ]});
    console.log("manage id:", buttons.data[2].action);

// Initialize the data
onMounted(Response);
</script>