<template>

  <div class="header-banner-wrapper">
    <img class="background" src="/files/banner-bg.png" />
    <div class="inner">
      <div class="header">
        <div class="logo">
          <img src="/files/logo.svg" />
        </div>
        <div class="right-buttons">
          <button @click="handleClick('books')">Explore all Books</button>
          <button @click="handleClick('multimedia')">Explore all multimedia</button>
          <div class="nav-icon theme-icon" v-if="whiteTheme == false" @click="setWhiteTheme(true)"><svg
              xmlns="http://www.w3.org/2000/svg" width="25" height="26" viewBox="0 0 25 26" fill="white">
              <path fill-rule="evenodd" clip-rule="evenodd"
                d="M22.916 21.1391C24.1587 19.879 24.7801 19.249 24.5125 18.63C24.245 18.0111 23.1126 18.038 20.848 18.0917C17.393 18.1737 13.9117 16.8963 11.275 14.2596C8.63833 11.623 7.36096 8.14174 7.4429 4.68675C7.49661 2.42208 7.52346 1.28974 6.90455 1.0222C6.28564 0.754652 5.65559 1.37602 4.39548 2.61877C4.37348 2.64046 4.35154 2.66225 4.32966 2.68414C-0.784745 7.79854 -0.784745 16.0906 4.32966 21.205C9.44406 26.3194 17.7361 26.3194 22.8505 21.205C22.8724 21.1831 22.8943 21.1612 22.916 21.1391Z"
                fill="white" stroke="none" />
            </svg></div>
          <div class="nav-icon" v-else @click="setWhiteTheme(false)"><svg xmlns="http://www.w3.org/2000/svg" width="28"
              height="28" viewBox="0 0 28 28" fill="none">
              <circle cx="13.9998" cy="13.9999" r="4.77778" fill="white" stroke="white" stroke-width="2" />
              <path d="M13.9999 3.88889V1" stroke="white" stroke-width="2" stroke-linecap="round" />
              <path d="M13.9999 26.9997V24.1108" stroke="white" stroke-width="2" stroke-linecap="round" />
              <path d="M21.1498 6.84988L23.1925 4.80713" stroke="white" stroke-width="2" stroke-linecap="round" />
              <path d="M4.8075 23.1931L6.85025 21.1504" stroke="white" stroke-width="2" stroke-linecap="round" />
              <path d="M24.1111 14L26.9999 14" stroke="white" stroke-width="2" stroke-linecap="round" />
              <path d="M1.00003 14L3.88892 14" stroke="white" stroke-width="2" stroke-linecap="round" />
              <path d="M21.1498 21.1501L23.1925 23.1929" stroke="white" stroke-width="2" stroke-linecap="round" />
              <path d="M4.8075 4.80686L6.85025 6.84961" stroke="white" stroke-width="2" stroke-linecap="round" />
            </svg></div>
          <UserIcon />
        </div>
      </div>
      <div class="banner">
        <div class="title">Explore Books, Magazines, Journal and more...</div>
        <Search />
      </div>
    </div>
    <Navigation />
  </div>
  <Navigation :isSticky="true" />

</template>
<script setup>
import Navigation from '../../navigation/Navigation.vue';
import Search from '../../search/Search.vue';</script>
<script>import UserIcon from './UserIcon.vue';



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
    },

  },

};
</script>


<style scoped>
@import "./style.css";
</style>
