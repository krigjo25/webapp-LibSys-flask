<template>

    <h2>Books</h2>
      <table>
          <thead>
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
                    <tr v-for="(info, j) in books.info" :key="j">
                        <td>{{ info.title }}</td>
                        <td>{{ info.author }}</td>
                        <td>{{ info.genre }}</td>
                        <td>{{ info.year }}</td>
                        <td>{{ info.publisher }}</td>
                        <td>{{ info.rating }}</td>
                        <td>{{ info.description }}</td>
                    </tr>
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
        
        Book:
        {
          title: "",
          author: "",
        },
        books: [],
      };
    },
    methods: {
  
      // Update a book and send Put Request
      UpdateBook(playload, ID)
      {
        //  Initialize the path
        const path = `http://localhost:5000/${ID}`;
  
        // Send a post request to the server
        axios.put(path, playload)
          .then(() => {
            this.fetchBooks();
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
        this.info.year = '';
        this.Book.title = '';
        this.Book.author = '';
        this.info.rating = '';
        this.info.publisher = '';
        this.Book.info.genre = '';
        this.info.description = '';
      },
    },
    created() {
      this.fetchBooks();
    },
  };
  </script>