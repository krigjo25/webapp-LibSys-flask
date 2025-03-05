<template>
    <section v-if="data.data" class="book-info">
      <div>
        <img :src="data.data.path" alt="book cover" />
      </div>
      <div>
        <h2>{{ data.data.title }}</h2>
        <small>by 
          <i v-for="author in data.data.author"> {{ author }} </i> - Published {{ data.data.published }} by 
          <i v-for="publisher in data.data.publisher"> {{ publisher }} </i>
        </small>
        <span v-for="review in data.data.review">| rating:{{review.rating}} by {{review.name}} </span>
        <section class="description">
          <p>{{ data.data.description }}</p>
          <div>
            <p v-for="genre in data.data.genre.split(',')">{{ genre }}</p>
          </div>
        </section>
      </div>
    </section>
    <section v-else>
      <h2>The data is not available at the moment</h2>
    </section>
</template>
  
<script setup>

  
  //  Importing required dependencies
  import { storedData } from '../stores/sharingdata.js';
  import { onMounted, onUnmounted, reactive } from 'vue';
  
  //  Initializing reactive objects
  const book = storedData();
  const data = reactive({
    data: null,
  });

  onUnmounted(() => {
    book.clearData(null);
  });
  onMounted(() => {
    data.data = book.data;
  });
</script>