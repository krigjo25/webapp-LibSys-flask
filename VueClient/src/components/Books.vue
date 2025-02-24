<template>
    <main>
        <section>
            <div v-for="book in data.books" :key="book.id" @click="BookInfo(book.id)">
                <img :src="book.img" alt="book cover.jpg" />
                <div>
                    <h3>{{ book.title }}</h3>
                    <span>
                        by <i v-for="author in book.author"> {{ author }} </i>
                    </span>
                </div>
            </div>
        </section>
        
    </main>
</template>

<script setup>
    //  Importing required dependencies
    import axios from 'axios';
    import { useRouter } from 'vue-router';
    import { Response, data } from '../utils/response.js';
    import { StoredData } from '../stores/sharingdata.js';
    import { reactive, watch, defineEmits, onMounted, ref } from 'vue';

    const router = useRouter();
    const shareData = StoredData();
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

    //  Show book
    function BookInfo(id)
    {
        if (!data.books) 
        {return;}
        for (let i = 0; i < data.books.length; i++) 
        {
            const book = data.books[i];
            if (book.id === id) 
            {

            shareData.setData(book);
            
             router.push({name: 'BookDetails'});
            }
        }
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