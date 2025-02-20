<template>
    <main>
        <section>
            <div v-for="book in data.books" :key="book.id" @click="BookInfo(book.id)">
                <img osrc="https://mrjoes.github.io/shared/posts/flask-admin-120/cb3.jpg" alt="book cover.jpg" />
                <h3>{{ book.title }} | {{book.rating[0]}} </h3>
            </div>
        </section>
    </main>
    <div v-for="book in data.books" :key="book.id">
        <Bookinfo v-if="book.selected" :data="book"/>
    </div>
</template>

<script setup>
    //  Importing required dependencies
    import axios from 'axios';
    import { reactive, watch, computed, defineEmits, onMounted,ref } from 'vue';

    //  Importing Components
    import Bookinfo from './BookInfo.vue';
    import Btn from './misc_components/Btn.vue';

    const emit = defineEmits(['book-id']);

    const props = defineProps(
        {
            data:
            {
                type: Object,
                required: true
            }
        }
    );

    const data = reactive(
        {
        headings: ['Title', 'Author', 'Actions'],
        books:null
    });

    const buttons = reactive([
        {
            type: 'button',
            book: data.books,
            action: BookInfo,
            cls: 'bi bi-info-circle',
        },
        {
            type: 'button',
            book: data.books,
            action: UpsertEvent,
            cls: 'bi bi-arrow-clockwise',
        },
        {
            type: 'button',
            book: data.books,
            action: DeleteBook,
            cls: 'bi bi-x-circle-fill',
        }
    ]);

        //  Fetch the books from the server
    const Response = async () =>
    {
        //  Initialize the path
        const path = 'http://localhost:5000/';
        axios.get(path)
            .then((res) => {

                data.books = res.data.books;
                console.log('Books:', data.books);

        })
        .catch((error) => {
            console.error(error);
        });
    };

    //  Show book
    function BookInfo(id)
    {
        for (let i = 0; i < data.books.length; i++) 
        {
            const book = data.books[i];

            book.selected = (book.id === id) ? ref(true) : ref(false);

        }
    };

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