#  The first Vue project
<template>
  <div>
    <Books :nav="buttons.nav" :data="buttons.data"/>
  </div>
</template>

<script setup>

  //  Importing required dependencies
  import { reactive, onMounted } from 'vue';
  import { CreateBook, RemoveBook, UpdateBook } from '../assets/js/crud.js';
  
  //  Importing components
  import Books from './Books.vue';
  
  //  Initializing reactive objects

const buttons = reactive(
  { 
    nav : true,
    data:
    [
      {
        id: 1,
        type: 'submit',
        cls: 'bi bi-plus',
        action: () => {}
      },
      {
        id: 2,
        type: 'button',
        cls: 'bi bi-arrow-clockwise',
        action:UpdateBook
      },
      {
        id: 3,
        type: 'button',
        cls: 'bi bi-trash',
        action:RemoveBook,
      }
    ]});

// Initialize the data
</script>