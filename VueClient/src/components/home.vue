<template>
  <form>
    <legend>Add a Book</legend>
    <label for="title">Title</label>
    <input type="text" id="title" name="title" v-model="cBook.title" placeholder="Title">
    <label for="author">Author</label>
    <input type="text" id="author" name="author" v-model="cBook.author" placeholder="Author">
    <div>
      <button @click="SubmitBook">Add Book</button>
      <button @click="ResetBook">Reset Book</button>
    </div>
  </form>
  <form>
    <legend>Modify a Book</legend>
    <label for="title">Title</label>
    <input type="text" id="title" name="title" v-model="Book.title" placeholder="Title">
    <label for="author">Author</label>
    <input type="text" id="author" name="author" v-model="Book.author" placeholder="Author">
    <div>
      <button @click="ResetBook">Reset Book</button>
    </div>
  </form>
  <h2>Books</h2>
    <table>
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
                <td>
                    <button @click="SubmitChanges(book.id)">Update</button>
                    <button @click="ConfirmDelete(book.id)">Delete</button>

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
        title: '',
        author: '',
      },
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
        title: this.cBook.title,
        author: this.cBook.author,
      }
      console.log(playload)
      
      // Add a book
      this.CreateBook(this.cBook);
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