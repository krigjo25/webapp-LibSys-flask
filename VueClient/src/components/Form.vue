<template>
  <form>
    <legend>{{ title}}</legend>
    <label for="title">Title</label>
    <input type="text" id="title" name="title" placeholder="Title" v-model="Book.title">
    <label for="author">Author</label>
    <input type="text" id="author" name="author" placeholder="Author" v-model="Book.author">
    <div>
      <button type="submit" value="submit" @click="UpdateEvent"><i class="bi bi-plus-circle-fill"></i></button>
      <button type="reset" value= "reset" @click="Reset"><i class="bi bi-arrow-counterclockwise"></i></button>
    </div>
  </form>
</template>
  

<script setup>

//  Importing required dependencies
import { defineProps, defineEmits } from 'vue';
import { reactive, watch, computed, ref } from 'vue';

function UpdateEvent()
{
  emit('shared-data', Book);
}

function Reset()
{
  Book.value.title = "";
  Book.value.author = "";
}

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

const Book = reactive
(
    {
        id: null,
        title: null,
        author: null
    }
);

const title = computed(() => props.formTitle);



watch(
  () => props.book,
  (newVal) =>
  {
    if (newVal)
    {
      Book.value.id = newVal.id;

    }
  }, 
);
</script>
