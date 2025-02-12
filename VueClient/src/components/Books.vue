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
                  <button @click="UpsertEvent(book.id)"><i class="bi bi-arrow-clockwise"></i></button>
                  <button @click="ConfirmDelete(book.id)"><i class="bi bi-x-circle-fill"></i></button>
            
                    
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

  props:{
    data: {
      type: Object,
      required: true,}

  },
  watch:
  {
    data: function(data, oldData)
    {
      if (data)
      {
        this.UpsertEvent(data);
      }

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

    UpsertEvent(data) 
    {
      // Initialize the playload
      if (data) 
      {
          const playload = 
        {
          title: data.title,
          author: data.author,
        }

        if (data.id && data.title && data.author) 
        {
          // Update a book
          this.UpdateBook(playload, data.id);
        } 
        else if (data.title && data.author)
        {
          // Add a book
          this.CreateBook(playload);
        }
        else
        {
          this.$emit('update-book', data);
        }
      } 

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
  },
  created() {
    this.fetchBooks();
  },
};
</script>