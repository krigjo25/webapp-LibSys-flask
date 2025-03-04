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
import { reactive} from 'vue';
import { useRouter } from 'vue-router';
import { storedData } from '../stores/sharingdata.js';

//  Importing components
import Btn from './misc_components/Btn.vue';
import Input from './misc_components/Inputs.vue';

//  Initializing reactive objects
const router = useRouter();
const buffy = reactive({});
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
        name: 'year',
        type: 'number',
        placeholder: '2025',
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


//  Handle  buffer data
const handleData = (data) =>
{
  Object.assign(buffy, data);
}

async function submit()
{
  const bufferData = storedData();

  await bufferData.setData(buffy);
  console.log("Shared data",bufferData.data);
  
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
