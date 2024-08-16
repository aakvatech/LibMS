<template>
  <div id="app-container">
    <v-app>
      <v-main>

        <!-- <button @click="setCurrentComponent('home')">home</button> ???
              <button @click="setCurrentComponent('about')">about</button>??
              <button @click="setCurrentComponent('books')">books</button>??
              <button @click="setCurrentComponent('contact')">contact</button> -->

        <component v-if="page == 'home'" :onLinkClick="setCurrentComponent" :is="currentComponent"
          :setWhiteTheme="setWhiteTheme" :whiteTheme="whiteTheme"></component>
        <Layout v-else :customComponent="currentComponent" :onLinkClick="setCurrentComponent" />
      </v-main>
    </v-app>
  </div>
</template>

<script setup>
import Home from '../ebook_reader/page/home/Home.vue'
import About from '../ebook_reader/page/About.vue'
import Books from '../ebook_reader/page/books/Books.vue'
import Contact from '../ebook_reader/page/Contact.vue'
import Layout from '../ebook_reader/layout/Layout.vue'
import BookCategories from '../ebook_reader/page/BookCategories.vue'
</script>
<script>
const url = new URL(window.location.href);
const params = new URLSearchParams(url.search);
const pageValue = params.get('page');

export default {

  data() {
    return {
      page: pageValue == null ? 'home' : pageValue,
      currentComponent: Home,
      whiteTheme: true
    };
  },
  methods: {
    setCurrentComponent(pageName) {
      this.page = pageName
      let url = `/app/books`
      if (pageName !== 'home') {
        url = `/app/books?page=${pageName}`
      }
      window.history.pushState('', '', url);
      switch (pageName) {
        case 'home':
          this.currentComponent = Home
          break;
        case 'about':
          this.currentComponent = About
          break;
        case 'books':
          this.currentComponent = Books
        case 'book-categories':
          this.currentComponent = BookCategories
          break;
        case 'contact':
          this.currentComponent = Contact
          break;
        default:
          this.currentComponent = Home
          break;
      }
    },
    setWhiteTheme(flag) {
      this.whiteTheme = flag
    }
  },
  computed: {
    currentComponent() {
      switch (this.page) {
        case 'home':
          return Home
        case 'about':
          return About
        case 'books':
          return Books
        case 'contact':
          return Contact
        case 'book-categories':
          return BookCategories
        default:
          return Home
      }
    },
  },
};
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap');
@import "./reset.css";
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
<style>
#freeze {
  display: none;
}
</style>
