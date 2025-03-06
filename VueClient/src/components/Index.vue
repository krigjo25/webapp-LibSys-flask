<template>
    <BookTable :data="data" @book-id="UpdateEvent"/>
</template>

<script setup>

  //  Importing Components
  import BookTable from './Books.vue';


  //  Importing required dependencies
  import { reactive, watch } from 'vue';

  //  Initializing reactive objects
  const Book = reactive
  (
      {
        id    :null,
        title :null,
        author:null,
      }
  );

  const data = reactive(  
    {
      title: null,
      author: null,
  });

  watch(Book, (data) => {
    console.log("Data: ", data);
  },
  );
</script>