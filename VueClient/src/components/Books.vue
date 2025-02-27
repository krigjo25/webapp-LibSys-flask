<template>
        <section  v-for="book in data.books" :key="book.id">
            <div @click="BookInfo(book.id)">
                <img :src="book.path" alt="book cover.jpg" />
                <div>
                    <h3>{{ book.title }}</h3>
                    <span>
                        by <i v-for="author in book.author"> {{ author }} </i>
                    </span>
                </div>
            </div>
            <div v-if="props.nav">
                <Navigation :data="props.data"/>
            </div>
        </section>
</template>

<script setup>
    //  Importing required dependencies
    import { useRouter } from 'vue-router';
    import { watch, defineEmits, onMounted } from 'vue';
    import { Response, data } from '../assets/js/response.js';
    import { StoredData } from '../stores/sharingdata.js';
    
    //  Importing components
    import Navigation from './misc_components/Navigation.vue';

    const router = useRouter();
    const shareData = StoredData();
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