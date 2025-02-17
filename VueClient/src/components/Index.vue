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

const Book = reactive
(
    {
        title: null,
        author: null,
    }
);

const data = reactive
(
  {
      title: null,
      author: null,
  }
);
function SubmitBook(payload)
{
  data.id = payload.id;
  data.title = payload.title;
  data.author = payload.author;
  console.log("Submitting :", data);
}
function UpdateEvent(payload)
{
    Book.id = payload.id;
    console.log("Submitting :", Book);
}
</script>