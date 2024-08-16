<!-- template for the slider component -->
<template>
  <div class="container">
    <div class="news-section">

      <div class="title-wrapper">
        <h2>News & Announcement</h2>
        <div class="right">
          <button @click="handleClick('books')" class="link">See all<img src="/files/see-all-arrow.svg" /></button>
        </div>
      </div>
      <div class="news-list-wrapper">
        <template v-for="item in newsstore.news" :key="item.title">
          <div class="item">
            <div class="title">{{ item.title }}</div>
            <div class="description">{{ item.description }}</div>
            <div class="date">{{ item.date }}</div>
          </div>
        </template>


      </div>
    </div>
  </div>

</template>

<script setup>
import { onMounted } from 'vue';
import { useBooksStore } from '../../../../books/store';
// const mediastore = useBooksStore();
const newsstore = {
  news: [
    {
      title: 'Lorem ipsum dolor sit amet',
      description: 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
      date: '6 Jun 2010'
    },
    {
      title: 'Lorem ipsum dolor sit amet',
      description: 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
      date: '6 Jun 2010'
    },
    {
      title: 'Lorem ipsum dolor sit amet',
      description: 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
      date: '6 Jun 2010'
    },
    {
      title: 'Lorem ipsum dolor sit amet',
      description: 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
      date: '6 Jun 2010'
    }
  ]
}
onMounted(() => {
  // mediastore.get_media({ length: 3 });
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
