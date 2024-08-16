<template>
  <div id="app-container" :class="homepageClass">
    <HeaderBanner :onLinkClick="onLinkClick" :setWhiteTheme="setWhiteTheme" :whiteTheme="whiteTheme" />
    <div class="main-content">

      <BannerSlider />
      <BookCategories :onLinkClick="onLinkClick" />
      <NewBooks :onLinkClick="onLinkClick" />
      <MediaCategories />
      <NewMedia />
      <NewsAnnouncements />
    </div>
    <Footer />
    <!-- <v-app> -->

    <!-- <button @click="handleClick('about')">About</button>
                This is homepage -->

    <!-- </v-app> -->
  </div>
</template>
<script setup>
import HeaderBanner from '../../components/home/header-banner/HeaderBanner.vue'
import BannerSlider from '../../components/home/banner-slider/BannerSlider.vue'
import BookCategories from '../../components/home/book-categories/BookCategories.vue'
import NewBooks from '../../components/home/new-books/NewBooks.vue';
import MediaCategories from '../../components/home/media-categories/MediaCategories.vue';
import NewMedia from '../../components/home/new-media/NewMedia.vue';
import NewsAnnouncements from '../../components/home/news-announcements/NewsAnnouncements.vue';
import Footer from '../../components/home/footer/Footer.vue';
</script>
<script>
export default {
  props: {
    onLinkClick: {
      type: Function,
      required: true
    },
    setWhiteTheme: {
      type: Function,
      required: true
    },
    whiteTheme: {
      type: Boolean,
      required: true
    },
  },
  methods: {
    handleClick(pageName) {
      // Call the function passed via prop
      if (this.onLinkClick) {
        this.onLinkClick(pageName);
      }
    }
  },
  computed: {
    homepageClass() {
      return [
        'homepage',  // Static class
        {
          white: this.whiteTheme,
          black: !this.whiteTheme
        }
      ];
    }
  }
};
</script>

<style>
.sticky-top {
  display: none;
}
</style>

<style scoped>
.drawer-open {
  transition: margin-left 0.3s;
  margin-left: 10px;
}

.v-card img {
  object-fit: cover;
}
</style>

<style scoped>
@import "./home.css";
</style>
