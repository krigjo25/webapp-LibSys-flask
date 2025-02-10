<template>
  <form>
    <legend>Modify a Book</legend>
    <label for="title">Title</label>
    <input type="text" id="title" name="title" v-model="Book.title" placeholder="Title">
    <label for="author">Author</label>
    <input type="text" id="author" name="author" v-model="Book.author" placeholder="Author">
    <div>
      <button type="submit" value="submit" @click="SubmitBook"><i class="bi bi-plus-circle-fill"></i></button>
      <button type="reset" value= "reset"  @click="ResetBook"><i class="bi bi-arrow-counterclockwise"></i></button>
    </div>
  </form>
  
    <table>
        <thead>
          <h2>Books</h2>
            <tr>
                <th>Name</th>
                <th>Author</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(book, i) in books" :key="i">
                <td>{{ book.title }}</td>
                <td>{{ book.author }}</td>
                <td>
                    <button type="submit" value="submit" @click="SubmitChanges(book.id)"><i class="bi bi-arrow-clockwise"></i></button>
                    <button type="reset" value= "reset" @click="ConfirmDelete(book.id)"><i class="bi bi-x-circle-fill"></i></button>
                    <button @click="View(book.id)"><i class="bi bi-info-circle"></i></button>

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