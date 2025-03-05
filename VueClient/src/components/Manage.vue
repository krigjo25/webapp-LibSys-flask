#  The first Vue project
<template>

  <nav>
    <Btn :data="{
          type: 'submit',
          cls: 'bi bi-plus',
          action: upsertEvent
        }"/>
  </nav>
  <div>
    <Books :nav="buttons.nav" :data="buttons.data"/>
  </div>
</template>

<script setup>

  //  Importing required dependencies
  import { useRouter } from 'vue-router';
  import { onMounted, reactive, watch} from 'vue';
  import { storedData } from '../stores/sharingdata.js';
  import { removeBook, updateBook, createBook } from '../assets/js/crud.js';
  
  //  Importing components
  import Books from './Books.vue';
  import Btn from './misc_components/Btn.vue';
  
  //  Initializing reactive objects
  const router = useRouter();
  const buffy = storedData();

  const buttons = reactive(
    { 
      nav : true,
      data:
      [
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
  function upsertEvent(book = null)
  {

    buffy.setData(book);
    router.push({name: 'UpsertBook'});
  }

  //  Create or Update a book
  async function upsertBook(data) 
      {
          if (data) 
          {

              //  Ensure the data's integerty
              if (data.id) 
              {
                  // Update a book
                  updateBook(data);
              } 

              else if (!data.id)
              {
                  createBook(data);
              }
          }
  };

watch(buffy, (n, o) => {
  console.log("buffy", n)
  upsertBook(n.data);
});

</script>