<!-- template for the slider component -->
<template>
  <div class="container">
    <div class="new-book-section media-section">

      <div class="title-wrapper">
        <h2>New Multimedia</h2>
        <div class="right">
          <button @click="handleClick('books')" class="link">See all<img src="/files/see-all-arrow.svg" /></button>
        </div>
      </div>
      <div class="book-list-wrapper">
        <template v-for="item in mediastore.media" :key="item.title">
          <div class="item">
            <div class="image-wrapper">
              <v-img :src="item.image ? item.image
                : '/files/default-media.png'">
              </v-img>
              <div class="player-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30" fill="none">
                  <circle cx="15" cy="15" r="15" fill="#00B0AB" />
                  <path
                    d="M23.2111 14.1055L10.07 7.53495C9.27211 7.13601 8.33333 7.71621 8.33333 8.60827V21.3917C8.33333 22.2837 9.27211 22.8639 10.07 22.465L23.2111 15.8944C23.9482 15.5259 23.9482 14.4741 23.2111 14.1055Z"
                    fill="white" />
                </svg>
              </div>
            </div>
            <div class="book-detail">
              <div class="title">{{ item.title }}</div>
              <div class="meta-wrapper">
                <div class="meta"><span class="label">Date:</span> {{ item.date
                  }}</div>
                <div class="meta"><span class="label">Category:</span> {{ item.category
                  }}</div>
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
// const mediastore = useBooksStore();
const mediastore = {
  media: [
    {
      title: 'Media 1',
      date: '19-Sep-2022 4:07 PM',
      category: 'કરબલાના બહાદુરો'
    },
    {
      title: 'Media 2',
      date: '19-Sep-2022 4:07 PM',
      category: 'કરબલાના બહાદુરો'
    },
    {
      title: 'Media 3',
      date: '19-Sep-2022 4:07 PM',
      category: 'કરબલાના બહાદુરો'
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
