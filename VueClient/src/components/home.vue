<template>
    <button> ADD</button>
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
                    <button>Update</button>
                    <button>Modify</button>
                    <button>Delete</button>

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
      books: [],
    };
  },
  methods: {
    fetchBooks() {
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