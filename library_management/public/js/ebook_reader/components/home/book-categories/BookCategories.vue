<!-- template for the slider component -->
<template>
  <div class="book-category-section">
    <div class="container">
      <div class="title-wrapper">
        <h2>Books Categories</h2>
        <div class="right">
          <button @click="handleClick('book-categories')" class="link">See all<img
              src="/files/see-all-arrow.svg" /></button>
        </div>
      </div>
      <div class="category-list-wrapper">
        <template v-for="item in bookCategoryStore.book_categories" :key="item.category">
          <div class="item">
            <div class="icon-wrapper" style="background-image: url(/files/round.png);"><img src="/files/image.png">
            </div>
            <div class="title">{{ item.category }}</div>
          </div>
        </template>


      </div>
    </div>
  </div>

</template>
<script setup>
import { onMounted } from 'vue';
import { useBooksStore } from '../../../../books/store';
const bookCategoryStore = useBooksStore();

onMounted(() => {
  bookCategoryStore.get_book_categories({ length: 5 });
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
