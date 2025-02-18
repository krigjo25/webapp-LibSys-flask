<template>
  <Form :book="Book" @shared-data="SubmitBook"/>
  <BookTable :data="data" @book-id="UpdateEvent"/>
</template>

<script setup>

  //  Importing Components
import Form from './Form.vue';
import BookTable from './Books.vue';

//  Importing required dependencies
import { ref, watch } from 'vue';

function SubmitBook(payload)
{
  console.log("Submitting :", payload.value);
  if (payload.value.id)
  {
      data.value.id = payload.value.id;
  }
  data.value.title = payload.value.title;
  data.value.author = payload.value.author;
}
function UpdateEvent(payload)
{
    Book.value.id = payload;
}

//  Initializing reactive objects
const Book = ref
(
    {
      id    :null,
      title :null,
      author:null,
    }
);

const data = ref(  
  {
    title: null,
    author: null,
});

watch(Book, (data) => {
  console.log("Data: ", data);
},
);
</script>