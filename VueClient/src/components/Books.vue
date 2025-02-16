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
            <tr v-for="book in books.books" :key="book.id">
                <td>{{ book.title }}</td>
                <td>{{ book.author }}</td>
                <td>
                  <button @click="BookInfo(book.id)"><i class="bi bi-info-circle"></i></button>
                  <button @click="UpsertEvent(book.id)"><i class="bi bi-arrow-clockwise"></i></button>
                  <button @click="DeleteBook(book.id)"><i class="bi bi-x-circle-fill"></i></button>
            
                    
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script e>

//  Importing required dependencies
import axios from 'axios';
import { reactive, watch, computed, onMounted,ref } from 'vue';


const books = reactive({
    books: ref([]),
});

//  Fetch the books from the server
const Response = async () =>
{
    //  Initialize the path
    const path = 'http://localhost:5000/';
    axios.get(path)
        .then((res) => {

            books.books = res.data.books;
            console.log('Books fetched successfully', books.books);
    })
    .catch((error) => {
        console.error(error);
    });
}

// Create a bok and send a Post Request
async function CreateBook(playload)
{
    // Initialize the path
    const path = 'http://localhost:5000/';

    // Send a post request to the server
    await axios.post(path, playload)
        .then(() => {
            Response();
        })
        .catch((error) => {
            console.error(error);
        });
};

    // Update a book and send Put Request
async function UpdateBook(playload, ID)
{
    //  Initialize the path
    const path = `http://localhost:5000/${ID}`;

    // Send a post request to the server
    await axios.put(path, playload)
        .then(() => {
            Response();
            console.log('Book updated successfully', playload);
        })
        .catch((error) => {
            console.error(error);
        });
};

async function UpsertEvent(data) 
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
            UpdateBook(playload, data.id);
        } 
        else if (data.title && data.author)
        {
            // Add a book
            CreateBook(playload);
        }
        else
        {
            $emit('update-book', data);
        }
      } 

};

    // Delete a book and send a delete request
async function DeleteBook(ID)
    {
        // Initialize the path
        const path = `http://localhost:5000/${ID}`;

        // Send a delete request to the server
        await axios.delete(path)
            .then(() => {
                Response();
                console.log('Book deleted successfully');
            })
            .catch((error) => {
                console.error(error);
            });
    };

export default {

  props:
  {
    data: {
    type    : Object}
  },
  emit : ['update-book'],

  // Initialize the data
  setup(props, { emit }) {

    //  Watch if the data is changed
    watch(props.data)
    {
        if (props.data)
        {
            UpsertEvent(data);
        }
    }

    // Initialize the data
    onMounted(Response);

    return {
        books,

        CreateBook,
        DeleteBook,
        UpdateBook,
        UpsertEvent,
        
    };
  },
};
</script>