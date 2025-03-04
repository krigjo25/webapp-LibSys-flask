#  The first Vue project
<template>
  <div>
    <Books :nav="buttons.nav" :data="buttons.data"/>
  </div>
</template>

<script setup>

  //  Importing required dependencies
  import { useRouter } from 'vue-router';
  import { onMounted, reactive} from 'vue';
  import { storedData } from '../stores/sharingdata.js';
  import { removeBook, updateBook, createBook } from '../assets/js/crud.js';
  
  //  Importing components
  import Books from './Books.vue';
  
  //  Initializing reactive objects
  const router = useRouter();
  const buffy = storedData();

  const buttons = reactive(
    { 
      nav : true,
      data:
      [
        {
          id: 1,
          type: 'submit',
          cls: 'bi bi-plus',
          action: upsertEvent
        },
        {
          id: 2,
          type: 'button',
          cls: 'bi bi-arrow-clockwise',
          action:upsertEvent
        },
        {
          id: 3,
          type: 'button',
          cls: 'bi bi-trash',
          action:removeBook,
        }
    ]});

  //  Router push
  function upsertEvent()
  {
    
    router.push({name: 'UpsertBook'});
  }

  //  Create or Update a book
  async function upsertBook(data) 
      {
          console.log('Upsert :', data);
          if (data) 
          {

              //  Ensure the data's integerty
              if (data.id && data.title && data.author) 
              {
                  // Update a book
                  updateBook(data);
                  console.log('Upsert :', data);
              } 

              else if (!data.id)
              {
                  createBook(data);
              }
          }
  };
onMounted(() => {

  upsertBook(buffy.data);
  });

</script>