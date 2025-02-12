<template>
  <Form :book ="Book" @upsert-book="SubmitEvent" />
  <BookTable :data="data"  @update-book="UpdateEvent"/>
</template>

<script>

//  Importing Components
import Form from './Form.vue';
import BookTable from './Books.vue';

export default {
  components: {
    
    Form,
    BookTable,
  },
  data() {
    return {
      
      Book:
      {
        title: "",
        author: "",

      },
      data: null,

    };
  },
  methods:
  {
    SubmitEvent(book) 
    {
      this.data = book;
    },

    UpdateEvent(book)
    {
      this.Book.id = book;
      this.data = this.Book;
    },

    

  },
};
</script>