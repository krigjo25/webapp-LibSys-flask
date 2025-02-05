<template>
  <form>
    <label for="title">Title</label>
    <input type="text" id="title" name="title" v-model="Book.title" placeholder="Title">
    <label for="author">Author</label>
    <input type="text" id="author" name="author" v-model="Book.author" placeholder="Author">
    <div>
      <button @click="SubmitBook">Add Book</button>
      <button @click="ResetBook">Reset Book</button>
    </div>
  </form>
    
    <table>
        <h1>Books</h1>
        <thead>
            <tr>
                <th>Name</th>
                <th>Author</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(book, index) in books" :key="index">
                <td>{{ book.title }}</td>
                <td>{{ book.author }}</td>
                <td> {{ book.Read }}</td>
                <td>
                    <button @click="UpdateBook">Update</button>
                    <button @click="RemoveBook">Delete</button>
                </td>
            </tr>
        </tbody>
    </table>
  </template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      
      Book: 
      {
        title: '',
        author: '',
      },
      books: [],
    };
  },
  methods: {

    // Add a book
    addBook(playload)
    {
      // Initialize the path
      const path = 'http://localhost:5000/';

      // Send a post request to the server
      axios.post(path, playload)
        .then(() => {
          this.fetchBooks();
          console.log('Book added successfully', playload);
        })
        .catch((error) => {
          console.error(error);
          this.fetchBooks();
        });
    },
    fetchBooks() 
    {
      //  Initialize the path
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          console.error(error);
        });
    },

    ResetBook() 
    {
      this.initForm();
    },
    SubmitBook() 
    {
      // Initialize the playload
      const playload = {
        title: this.Book.title,
        author: this.Book.author,
      }
      // Add a book
      this.addBook(this.Book);
      this.initForm();
    },
    initForm() 
    {
      this.Book = {
        title: '',
        book: '',
      };
    },
  },
  created() {
    this.fetchBooks();
  },
};
</script>