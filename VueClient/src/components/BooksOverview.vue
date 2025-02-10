<template>
  <form>
    <legend>{{Book.Form}}</legend>
    <label for="title">Title</label>
    <input type="text" id="title" name="title" v-model="Book.title" placeholder="Title">
    <label for="author">Author</label>
    <input type="text" id="author" name="author" v-model="Book.author" placeholder="Author">
    <div>
      <button type="reset" value= "reset"  @click="ResetBook">Reset Book</button>
    </div>
  </form>
  <table>
        <thead>
          <h2>Books</h2>
          <button type="submit" value="submit" @click="SubmitBook"><i class="bi bi-plus-circle-fill"></i>Add a Book</button>
            <tr>
              <th>Title</th>
              <th>Author</th>
              <th>Genre</th>
              <th>Release</th>
              <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(book, i) in books" :key="i" @click="View(book.id)">
                <td>{{ book.title }}</td>
                <td>{{ book.author }}</td>
                
                <td>{{ book.genre }}</td>
                <td>{{ book.release }}</td>
                
                <td>
                  <button @click="ShowInfo(book.id)"><i class="bi bi-info-circle"></i></button>
                    <button type="submit" value="submit" @click="SubmitChanges(book.id)"><i class="bi bi-arrow-clockwise"></i></button>
                    <button type="reset" value= "reset" @click="ConfirmDelete(book.id)"><i class="bi bi-x-circle-fill"></i></button>
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
  created() {
    this.fetchBooks();
  },
};
</script>