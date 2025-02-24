export default {

    data() {
        return {
            book:
            {
                id: '',
                genre: '', release: '',
                title: '', author: '',
                publisher: '', image:'',
            }
        };
    },
    methods:
    {
        UpdateBook(playload, ID)
        {
          //  Initialize the path
          const path = `http://localhost:5000/${ID}`;
    
          // Send a post request to the server
          axios.put(path, playload)
            .then(() => {
              this.fetchBooks();
              console.log('Book updated successfully', playload);
            })
            .catch((error) => {
              console.error(error);
              this.fetchBooks();
            });
        },
    
        SubmitChanges(ID) 
        {
          // Initialize the playload
          const playload = {
            title: this.Book.title,
            author: this.Book.author,
          }
          // Add a book
          this.UpdateBook(playload, ID);
          this.ResetForm();
        },
        // Reset the form
        ResetForm() 
        {
          this.initForm();
          this.fetchBooks();
        },
    },

}