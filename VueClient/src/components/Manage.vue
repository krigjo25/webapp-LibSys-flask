#  The first Vue project
<template>
  <div>
    <Books :nav="buttons.nav" :data="buttons.data"/>
  </div>
</template>

<script setup>

  //  Importing required dependencies
  import { useRouter } from 'vue-router';
  import { onMounted, reactive, watch } from 'vue';
  import { StoredData } from '../stores/sharingdata.js';
  import {  RemoveBook, UpdateBook, CreateBook } from '../assets/js/crud.js';
  
  //  Importing components
  import Books from './Books.vue';
  
  //  Initializing reactive objects
  const router = useRouter();
  const buffy = StoredData();

  const buttons = reactive(
    { 
      nav : true,
      data:
      [
        {
          id: 1,
          type: 'submit',
          cls: 'bi bi-plus',
          action: UpsertEvent
        },
        {
          id: 2,
          type: 'button',
          cls: 'bi bi-arrow-clockwise',
          action:UpsertEvent
        },
        {
          id: 3,
          type: 'button',
          cls: 'bi bi-trash',
          action:RemoveBook,
        }
    ]});

  //  Router push
  function UpsertEvent()
  {
    
    router.push({name: 'UpsertBook'});
  }

  //  Create or Update a book
  async function UpsertBook(data) 
      {
          console.log('Upsert :', data);
          if (data) 
          {

              //  Ensure the data's integerty
              if (data.id && data.title && data.author) 
              {
                  // Update a book
                  UpdateBook(data);
                  console.log('Upsert :', data);
              } 

              else if (!data.id)
              {
                  CreateBook(data);
              }
          }
  };
onMounted(() => {

  UpsertBook(buffy.data);
  });

</script>