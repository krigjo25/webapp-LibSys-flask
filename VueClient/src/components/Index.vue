<template>
  <Form :books ="books" />
  <BookTable :books="books" @deleteBook="ConfirmDelete" @updateBook="SubmitChanges" />
  </template>

<script>

//  Importing Components
import Form from './Form.vue';
import BookTable from './Books.vue';

//  Importing required dependencies
import axios from 'axios';

export default {
  data() {
    return {
      
      Book:
      {
        title: "",
        author: "",
      },
      books: [],
    };
  },
  methods: {

    // Create a bok and send a Post Request
    CreateBook(playload)
    {
      // Initialize the path
      const path = 'http://localhost:5000/';

      // Send a post request to the server
      axios.post(path, playload)
        .then(() => {
          this.fetchBooks();
          console.log('Book added successfully');
        })
        .catch((error) => {
          console.error(error);
          this.fetchBooks();
        });
    },
    SubmitBook() 
    {
      // Initialize the playload
      const playload = 
      {
        title: this.Book.title,
        author: this.Book.author,
      }
      console.log(playload)
      
      // Add a book
      this.CreateBook(this.Book);
      
      this.initForm();
    },

    // Update a book and send Put Request
    UpdateBook(playload, ID)
    {
      //  Initialize the path
      const path = `http://localhost:5000/${ID}`;

      // Send a post request to the server
      axios.put(path, playload)
        .then(() => {
          this.fetchBooks();
          console.log('Book updated successfully', playload);
        })
        .catch((error) => {
          console.error(error);
          this.fetchBooks();
        });
    },

    SubmitChanges(ID) 
    {
      // Initialize the playload
      const playload = {
        title: this.Book.title,
        author: this.Book.author,
      }
      // Add a book
      this.UpdateBook(playload, ID);
      this.initForm();
    },

    // Delete a book and send a delete request
    DeleteBook(ID)
    {
      // Initialize the path
      const path = `http://localhost:5000/${ID}`;

      // Send a delete request to the server
      axios.delete(path)
        .then(() => {
          this.fetchBooks();
          console.log('Book deleted successfully');
        })
        .catch((error) => {
          console.error(error);
          this.fetchBooks();
        });
    },

    ConfirmDelete(ID)
    {
      this.DeleteBook(ID);
      
    },

    // Fetch all books and send a get request
    fetchBooks() 
    {
      //  Initialize the path
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
          console.log(this.books);
        })
        .catch((error) => {
          console.error(error);
        });
    },

    // Reset the form
    ResetForm() 
    {
      this.initForm();
      this.fetchBooks();
    },

    initForm() 
    {
      // Reset the form
      this.Book.title = '';
      this.Book.author = '';
    },
  },
  components: {
    
    Form,
    BookTable,
  },
};
</script>