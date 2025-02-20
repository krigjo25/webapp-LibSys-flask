<template>
  <form>
    <!--Field v-for="fm in forms" :data="fm"\-->
    <legend>{{ title }}</legend>
    <label for="title">Title</label>
    <input type="text" id="title" name="title" placeholder="Title" v-model="buffer.title">
    <label for="author">Author</label>
    <input type="text" id="author" name="author" placeholder="Author" v-model="buffer.author">
    <div>
      <Btn v-for="btn in buttons":data="btn" @click="btn.action"/>
    </div>
  </form>
</template>
  

<script setup>

  //  Importing required dependencies
  import { defineProps, defineEmits } from 'vue';
  import { reactive, watch, computed, ref } from 'vue';

  //  Importing Components
  import Btn from './misc_components/Btn.vue';
  import Entry from './misc_components/Inputs.vue';

  const buttons = reactive([
          {
              type: 'submit',
              action: UpdateEvent,
              cls: 'bi bi-plus-circle-fill',
          },
          {
              type: 'reset',
              action: Reset,
              cls: 'bi bi-arrow-counterclockwise',
          },

  ]);

  const form = reactive(
    {
      type: 'text',
      modal: false,
      label: "title",
    },
    {
      type: 'text',
      modal: false,
      label: "author",
    },
  );

  const props = defineProps(
    {
      book: 
      {
        type: Object,
        required: true
      },
      formTitle: 
      {
        type: String,
        default: "Add a book",
      }
    }
  );

  const emit = defineEmits(['shared-data']);

  const buffer = reactive(
      {
          id: null,
          title: null,
          author: null
      }
  );

  function Reset()
  {
    buffer.title = "";
    buffer.author = "";
  }

  function UpdateEvent()
  {
    emit('shared-data', buffer);
  }



  const title = computed(() => props.formTitle);

  //  Watch if the book ID is changed
  watch(
    () => props.book.id,
    (book) =>
    {
      console.log("Data: ", book);
      if (book)
      {
        buffer.id = book;
        console.log("Book ID: ", buffer.id);
        emit('shared-data', buffer);

      }
    },
    {
      deep: true
    }
  );
</script>
