<template>
  <Form :book ="this.Book" @add-book="SubmitEvent" />
  <BookTable :data="Book"  />
  </template>

<script>

//  Importing Components
import Form from './Form.vue';
import BookTable from './Books.vue';

export default {
  data() {
    return {
      
      Book:
      {
        title: "",
        author: "",
        form : "Add Book",
      },

    };
  },
  methods:
  {
    SubmitEvent(book) 
    {

      this.Book = book;
      CreateBook(book);
    },
    CreateBook(playload)
    {
    },
  },
  components: {
    
    Form,
    BookTable,
  },
};
</script>