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
                  <button @click="BookInfo(book)"><i class="bi bi-info-circle"></i></button>
                  <button @click="UpsertEvent(book.id)"><i class="bi bi-arrow-clockwise"></i></button>
                  <button @click="DeleteBook(book.id)"><i class="bi bi-x-circle-fill"></i></button>
            
                    
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script setup>
    //  Importing required dependencies
    import axios from 'axios';
    import { reactive, watch, computed, defineEmits, onMounted,ref } from 'vue';

    //  Fetch the books from the server
    const Response = async () =>
    {
        //  Initialize the path
        const path = 'http://localhost:5000/';
        axios.get(path)
            .then((res) => {

                books.books = res.data.books;

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
    async function UpdateBook(payload)
    {
        //  Initialize the path
        const path = `http://localhost:5000/${payload.id}`;

        // Send a post request to the server
        await axios.put(path, payload)
            .then(() => {
                console.log('Book updated successfully', payload);
            })
            .catch((error) => {
                console.error(error);
            });
        
        Response();
    };

    async function UpsertEvent(data) 
    {
        
        if (data) 
        {
            const playload = 
            {
                id: data.id,
                title: data.title,
                author: data.author,
            }

            //  Ensure the data's integerty
            if (data.id && data.title && data.author) 
            {
                // Update a book
                UpdateBook(playload);
                console.log('Data:', data);
            } 

            else if (data.title && data.author && !data.id)
            {
                CreateBook(playload);
            }

            else
            {
                emit('book-id', data);
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

    const emit = defineEmits(['book-id']);

    const books = reactive({books: []});

    const props = defineProps(
        {
            data:
            {
                type: Object,
                required: true
            }
        }
    );
    //  Watch if the data is changed
    watch(
        () => props.data, 
        (data) => 
        {
            if (data) {
                UpsertEvent(data);
        }
    },
    {
        deep: true
    }
    );

    // Initialize the data
    onMounted(Response);

</script>