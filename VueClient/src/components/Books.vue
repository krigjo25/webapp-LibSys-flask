<template>
        <section  v-for="book in data.books" :key="book.id">
            <div @click="bookInfo(book.id)">
                <img :src="book.path" alt="book cover.jpg" />
                <div>
                    <h3>{{ book.title }}</h3>
                    <span>
                        by <i v-for="author in book.author"> {{ author }} </i>
                    </span>
                </div>
            </div>
            <div v-if="props.nav">
                <Navigation :data="props.data" :id="book.id" />
            </div>
        </section>
</template>

<script setup>
    //  Importing required dependencies
    import { useRouter } from 'vue-router';
    import { defineEmits, onMounted } from 'vue';
    
    import { storedData } from '../stores/sharingdata.js';
    import { Response, data } from '../assets/js/response.js';
    

    //  Importing components
    import Navigation from './misc_components/Navigation.vue';

    const router = useRouter();
    const shareData = storedData();
    const emit = defineEmits(['book-id']);

    const props = defineProps(
        {
            data:
            {
                type: Object,
                required: true
            },
            nav:
            {
                type: Boolean,
                required: false
            }
        }
    );

    //  Function to get the book's information
    function bookInfo(id)
    {
        //  Ensure that the data is not empty
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

    // Initialize the data
    onMounted(Response);

</script>