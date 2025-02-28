#  The first Vue project
<template>
  <div>
    <Books :nav="buttons.nav" :data="buttons.data"/>
  </div>
</template>

<script setup>

  //  Importing required dependencies
  import { useRouter } from 'vue-router';
  import { reactive } from 'vue';
  import { StoredData } from '../stores/sharingdata.js';
  import {  RemoveBook, UpdateBook } from '../assets/js/crud.js';
  
  //  Importing components
  import Books from './Books.vue';
  
  //  Initializing reactive objects

const buttons = reactive(
  { 
    nav : true,
    data:
    [
      {
        id: 1,
        type: 'submit',
        cls: 'bi bi-plus',
        action: UpsertBook
      },
      {
        id: 2,
        type: 'button',
        cls: 'bi bi-arrow-clockwise',
        action:UpdateBook
      },
      {
        id: 3,
        type: 'button',
        cls: 'bi bi-trash',
        action:RemoveBook,
      }
  ]});

  const router = useRouter();
  const shareData = StoredData();

function UpsertBook(arg)
{
  if (arg)
  {
    router.push({name: 'UpsertBook'});
  }
  router.push({name: 'UpsertBook'});
}
</script>