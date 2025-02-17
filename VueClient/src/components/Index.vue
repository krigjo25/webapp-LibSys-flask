<template>
  <Form :book="Book" @shared-data="SubmitBook"/>
  <BookTable :data="data" @book-id="UpdateEvent"/>
</template>

<script setup>
  //  Importing Components
  import Form from './Form.vue';
import BookTable from './Books.vue';

//  Importing required dependencies
import { reactive, ref } from 'vue';

const Book = ref
(
    {
      id:null,
      title: null,
      author: null,
    }
);

const data = 
ref(  
  {
    title: null,
    author: null,
  });

function SubmitBook(payload)
{
  console.log("Submitting :", payload.value);
  
  if (payload.id)
  {
      data.value.id = payload.value.id;
  }
  data.value.title = payload.value.title;
  data.value.author = payload.value.author;
}
function UpdateEvent(payload)
{
    data.value.id = payload;

    console.log("updating :", Book.value.id);
}
</script>