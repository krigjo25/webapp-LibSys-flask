<template>
  <h2>{{ data.title }}</h2>
  <form>
    <Input :data="title" />
    <Input :data="author" />
    <Input :data="genre" />
    <Input :data="published" />
    <Input :data="description" />
    <Input :data="publishedBy" />

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

const buffer = reactive(
  {
    title         :null,
    author        :null,
    genre         :null,
    published     :null,
    description   :null,
    published_by  :null,
});

const data = reactive(
  { 
    btn:
    [
      {
        id: 1,
        type: 'submit',
        cls: 'bi bi-plus',
        action: SubmitFrom
      },
      {
        id: 2,
        type: 'button',
        action:ResetForm,
        cls: 'bi bi-arrow-clockwise',
      },
    ]
});

const title = {
  name: 'title',
  type: 'text',
  placeholder: 'Title',
  value: buffer.title
};

const author = {
  name: 'author',
  type: 'text',
  placeholder: 'Author',
  value: buffer.author
};

const genre = {
  name: 'genre',
  type: 'text',
  placeholder: 'Genre',
  value: buffer.genre
};

const published = {
  name: 'published',
  type: 'text',
  placeholder: 'Published',
  value: buffer.published
};

const description = {
  name: 'description',
  type: 'text',
  placeholder: 'Description',
  value: buffer.description
};

const publishedBy = {
  name: 'published_by',
  type: 'text',
  placeholder: 'Published By',
  value: buffer.published_by
};

function SubmitFrom()
{
  sharedData.setData(buffer);
  router.push({name: 'Mananger'});
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

watch(
  () => buffer,
  (data) =>
  {
    if (data)
    {
      console.log(data);
    }
  });
</script>
