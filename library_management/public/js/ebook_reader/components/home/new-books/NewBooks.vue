<!-- template for the slider component -->
<template>
  <div class="container">
    <div class="new-book-section">

      <div class="title-wrapper">
        <h2>New Books</h2>
        <div class="right">
          <button @click="handleClick('books')" class="link">See all<img src="/files/see-all-arrow.svg" /></button>
        </div>
      </div>
      <div class="book-list-wrapper">
        <template v-for="item in bookstore.books" :key="item.book_title">
          <div class="item">
            <div class="image-wrapper"><v-img :src="item.image ? item.image
              : 'https://placehold.co/150?text=Item'">
              </v-img></div>
            <div class="book-detail">
              <div class="title">{{ item.book_title }}</div>
              <div class="meta-wrapper">
                <div class="meta"><span class="label">Author:</span> {{ item.author
                  }}</div>
                <div class="meta"><span class="label">Language:</span> Gujarati</div>
                <div class="meta"><span class="label">Sect:</span> Shia</div>
                <div class="meta"><span class="label">Book type:</span> E-book</div>
                <div class="meta"><span class="label">Availability:</span> <span class="avail-value">Yes</span></div>
              </div>
            </div>
          </div>
        </template>


      </div>
    </div>
  </div>

</template>

<script setup>
import { onMounted } from 'vue';
import { useBooksStore } from '../../../../books/store';
// const bookstore = useBooksStore();
const bookstore = {
  books: [
    {
      book_title: 'Book1',
      author: 'Author'
    },
    {
      book_title: 'Book2',
      author: 'Author'
    },
    {
      book_title: 'Book3',
      author: 'Author'
    },
    {
      book_title: 'Book4',
      author: 'Author'
    },
    {
      book_title: 'Book5',
      author: 'Author'
    }
  ]
}
onMounted(() => {

  // bookstore.get_books({ length: 5 });
});
</script>

<script>
export default {
  props: {
    onLinkClick: {
      type: Function,
      required: true
    }
  },
  methods: {
    handleClick(pageName) {
      // Call the function passed via prop
      if (this.onLinkClick) {
        this.onLinkClick(pageName);
      }
    }
  }
};
</script>

<style scoped>
@import "./style.css";
</style>
