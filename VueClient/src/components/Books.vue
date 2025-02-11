<template>
    <table>
        <thead>
            <tr>
                <th>Title</th>
                <th>Author</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="book in books" :key="book.id">
                <td>{{ book.title }}</td>
                <td>{{ book.author }}</td>
                <td>
                  <button @click="BookInfo(book.id)"><i class="bi bi-info-circle"></i></button>
                  <button @click="EditBook(book.id)"><i class="bi bi-arrow-clockwise"></i></button>
                  <button @click="ConfirmDelete()"><i class="bi bi-x-circle-fill"></i></button>
            
                    
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>

//  Importing required dependencies
import axios from 'axios';

export default {
  data() {
    return {
      books: [],
    };
  },

  props: 
  {
    data: 
    {
      type: Object,
      required: true
    }
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

    SubmitEvent(book) 
    {
      // Initialize the playload
      const playload = 
      {
        title: book.title,
        author: book.author,
      }
      console.log(playload, "test")
      
      // Add a book
      this.CreateBook(playload);
      
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
        title: this.book.title,
        author: this.book.author,
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
  },
  created() {
    this.fetchBooks();
  },
};
</script>