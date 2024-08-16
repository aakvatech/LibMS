<template>
    <div id="app-container">
        <v-app>
            <v-main>
                This is homepage.132456
                <nav>
    <a href="/app/books">About</a>
  </nav>
            </v-main>
        </v-app>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useBooksStore } from './store';
import Sidebar from '../ebook_reader/components/Sidebar.vue';
import EpubReader from '../ebook_reader/components/EpubReader.vue';
import PdfReader from '../ebook_reader/components/PdfReader.vue';


const bookstore = useBooksStore();
const selectedBook = ref(null);
const isReaderOpen = ref(false);
const drawer = ref(true);

const selectBook = (book) => {
    selectedBook.value = book;
    isReaderOpen.value = true;
}

const toggleDrawer = () => {
    drawer.value = !drawer.value;
};

onMounted(() => {
    bookstore.get_books();
    bookstore.get_book_categories();
});
</script>

<style>
#freeze{
    display: none;
}
#app-container {
    margin-top: 20px;
    text-align: center;
}
</style>
<style scoped>

#app-container {
    margin-top: 400px;
    text-align: center;
}

.drawer-open {
    transition: margin-left 0.3s;
    margin-left: 10px;
}

.v-card img {
    object-fit: cover;
}
</style>
