<template>
  <h2>{{ data.title }}</h2>
  <form>
    <Input :data="inputs" @upsert-form="handleData"/>

    <div>
      <Btn v-for="btn in data.btn" :data="btn" @click="btn.action"/>
    </div>
  </form>
</template>

<script setup>

import { reactive, watch } from 'vue';
import { StoredData } from '../stores/sharingdata.js';

//  Importing components
import Btn from './misc_components/Btn.vue';
import Input from './misc_components/Inputs.vue';

const data = reactive(
  { 
    btn:
    [
      {
        id: 1,
        type: 'submit',
        cls: 'bi bi-plus',
        action: Submit
      },
      {
        id: 2,
        type: 'button',
        action:ResetForm,
        cls: 'bi bi-arrow-clockwise',
      },
    ]
});
const handleData = (data) =>
{
  Object.assign(buffer, data);
}
const buffer = reactive({});
const inputs = reactive(
  {
    title: 'Insert a Book',
    data: 
    [
    {
        name: 'Upload an image',
        type: 'file',
        value: null
      },
      {
        name: 'title',
        type: 'text',
        placeholder: 'Title',
        value: null
      },
      {
        name: 'author',
        type: 'text',
        placeholder: 'Author',
        value: null
      },
      {
          name: 'genre',
          type: 'text',
          placeholder: 'Genre',
          value: null
      },
      {
          name: 'published',
          type: 'text',
          placeholder: 'Published',
          value: null
      },
      {
        name: 'description',
        type: 'text',
        placeholder: 'Description',
        value: null
      },
      {
        name: 'published_by',
        type: 'text',
        placeholder: 'Published By',
        value: null
      },
      {
        name: 'review',
        type: 'text',
        placeholder: 'Review',
        value: {
                name: null,
                rating: null, 
                
            }
      },
    ]
  });

const title = {
  name: 'title',
  type: 'text',
  placeholder: 'Title',
  value: buffer.title
};

const sharedData = StoredData();
function Submit()
{
  sharedData.setData(buffer);
  router.push({name: 'Mananger'});
  console.log(sharedData.data);
}

function ResetForm()
{
  buffer.title = ''
  buffer.genre = ''
  buffer.author = ''
  buffer.published = ''
  buffer.description = ''
  buffer.published_by = ''
}

</script>
