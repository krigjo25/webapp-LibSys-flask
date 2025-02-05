<template>
  <form>
    <legend>Add a Book</legend>
    <label for="title">Title</label>
    <input type="text" id="title" name="title" v-model="cBook.title" placeholder="Title">
    <label for="author">Author</label>
    <input type="text" id="author" name="author" v-model="cBook.author" placeholder="Author">
    <div>
      <button @click="SubmitChanges">Add Book</button>
      <button @click="ResetBook">Reset Book</button>
    </div>
  </form>
  <form>
    <legend>Modify a Book</legend>
    <label for="title">Title</label>
    <input type="text" id="title" name="title" v-model="uBook.title" placeholder="Title">
    <label for="author">Author</label>
    <input type="text" id="author" name="author" v-model="uBook.author" placeholder="Author">
    <div>
      <button @click="SubmitChanges">Modify Book</button>
      <button @click="ResetBook">Reset Book</button>
    </div>
  </form>
    <table>
        <thead>
          <h1>Books</h1>
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
      
      cBook: 
      {
        id: '',
        title: '',
        author: '',
      },
      uBook: 
      {
        id: '',
        title: '',
        author: '',
      },
      dBook:{},
      books: [],
    };
  },
  methods: {

    // Add a book
    CreateBook(playload)
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
    DeleteBook(ID)
    {},
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

    ResetForm() 
    {
      this.initForm();
      this.fetchBooks();
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

    SubmitChanges() 
    {
      // Initialize the playload
      const playload = {
        title: this.uBook.title,
        author: this.uBook.author,
      }
      // Add a book
      this.UpdateBook(playload, this.uBook.id);
      this.initForm();
    },
    
    initForm() 
    {
      // Reset the form
      this.cBook.title = '';
      this.cBook.author = '';
      this.uBook.title = '';
      this.uBook.author = '';
    },
  },
  created() {
    this.fetchBooks();
  },
};
</script>