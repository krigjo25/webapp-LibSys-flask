<template>
  <h2>{{ data.title }}</h2>
  <form>
    <Input :data="inputs" @upsert-form="handleData"/>

    <div>
      <Btn v-for="btn in data.btn" :data="btn" @click="btn.action()"/>
    </div>
  </form>
</template>

<script setup>

import { useRouter } from 'vue-router';
import { reactive, computed } from 'vue';
import { storedData } from '../stores/sharingdata.js';

//  Importing components
import Btn from './misc_components/Btn.vue';
import Input from './misc_components/Inputs.vue';

//  Initializing reactive objects
const router = useRouter();
const buffy = reactive({});
const bufferData = storedData().data;
console.log("bufferData form ", bufferData)

const data = reactive(
  { 
    btn:
    [
      {
        id: 1,
        type: 'submit',
        cls: 'bi bi-plus',
        action: submit
      },
      {
        id: 2,
        type: 'reset',
        action:resetForm,
        cls: 'bi bi-arrow-clockwise',
      },
    ]
});
const inputs = reactive(
  {
    title: computed( () => {'Insert A book'}),
    bookid: computed( () => {bufferData ? bufferData.id : null}),
    data: 
    [
      {
        value: null,
        type: 'file',
        name: 'Upload an image',
        placeholder: computed( () => {bufferData? bufferData.path : 'Upload an image'}),
      },
      {
        
        type: 'text',
        name: 'title',
        placeholder: computed( () => {
          console.log("computing", bufferData.title)
          bufferData.title ? bufferData.title : 'Title'}),
        value: null
      },
      {
        name: 'author',
        type: 'text',
        placeholder: computed( () => {bufferData ? bufferData.author : 'Author'}),
        value: null
      },
      {
        name: 'year',
        type: 'number',
        placeholder: computed( () => {bufferData ? bufferData.year : new Date().getFullYear()}),
        value: null
      },
      {
          name: 'genre',
          type: 'text',
          placeholder: computed( () => {bufferData ? bufferData.genre : 'Genre'}),
          value: null
      },
      {
          name: 'published',
          type: 'text',
          placeholder: computed( () => {bufferData ? bufferData.published : 'Published'}),
          value: null
      },
      {
        name: 'description',
        type: 'text',
        placeholder: computed( () => {bufferData ? bufferData.description : 'Description'}),
        value: null
      },
      {
        name: 'published_by',
        type: 'text',
        placeholder: computed( () => {bufferData ? bufferData.published_by : 'Published By'}),
        value: null
      },
      {
        name: 'review',
        type: 'text',
        placeholder: 'Review',
        value: {
                name:null,
                rating: null, 
                
            }
      },
    ]
});

console.log("inputs ",inputs)
//  Handle  buffer data
const handleData = (data) =>
{
  Object.assign(buffy, data);
}

async function submit()
{

  await bufferData.setData(buffy);
  
  //ResetForm();
  router.push({name: 'Manager'});
  
}

function resetForm()
{
  buffy.title = ''
  buffy.genre = ''
  buffy.author = ''
  buffy.published = ''
  buffy.description = ''
  buffy.published_by = ''
}

</script>
