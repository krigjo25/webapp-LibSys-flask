<template>
  <form>
    <legend></legend>
    <label for="title">Title</label>
    <input type="text" id="title" name="title" placeholder="Title" v-model="book.title">
    <label for="author">Author</label>
    <input type="text" id="author" name="author" placeholder="Author" v-model="book.author">
    <div>
      <button type="submit" value="submit" @click="SubmitBook()"><i class="bi bi-plus-circle-fill"></i></button>
      <button type="reset" value= "reset" @click="Reset"><i class="bi bi-arrow-counterclockwise"></i></button>
    </div>
  </form>
</template>

<script>
export default {
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  watch: {
    book: function(book, oldBook) {
      if (book) {
        this.book = book;
        this.SubmitBook();
      }
      console.log(book);
    }
  },
  methods: {
    Reset() {
      this.$emit('Reset');
    },
    SubmitBook()
    {
      const book = this.book;
      this.$emit('upsert-book', book);
    },
        // Reset the form
    Reset() 
    {
      this.initForm();
      this.fetchBooks();
    },

    initForm() 
    {
      // Reset the form
      this.Book.title = '';
      this.Book.author = '';
    },
  },
};
</script>