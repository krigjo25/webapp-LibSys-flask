<template>
    <Header />
    <section v-if="data.data" class="book-info">
      <div>
        <img :src="data.data.img" alt="book cover" />
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
            <p v-for="genre in data.data.genre">{{ genre }}</p>
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
  import { useRouter } from 'vue-router';
  import { StoredData } from '../stores/sharingdata.js';

  //  Importing components
  import Header from './header_components/Header.vue';
  import { onMounted, onUnmounted, reactive } from 'vue';
  
  //  Initializing reactive objects
  const sds = StoredData();
  const data = reactive({
    data: null,
  });

  onUnmounted(() => {
    sds.clearData(null);
  });
  onMounted(() => {
    data.data = sds.data;
  });

  console.log(data.data);
</script>