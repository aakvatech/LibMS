<template>

    <div id="app-container">
        <v-app>
            <v-main>
                <Sidebar :drawer="drawer" :bookstore="bookstore" @toggle-drawer="toggleDrawer" />
                <v-container fluid class="pa-0 ma-0" :class="{ 'drawer-open': drawer }">
                    <v-row class="align-center pa-0 ma-0">
                        <v-col cols="11" class="rounded-shaped">
                            <v-card outlined class="rounded-shaped">
                                <v-divider></v-divider>
                                <v-container class="overflow-y-auto" style="max-height: calc(100vh - 112px);">
                                    <v-row align="center" class="fill-height" justify="center">
                                        <template v-for="item in bookstore.books" :key="item.book_title">
                                            <v-col cols="12" sm="6" md="4" lg="3">
                                                <v-hover v-slot="{ isHovering, props }">
                                                    <v-card :class="{ 'on-hover': isHovering }"
                                                        :elevation="isHovering ? 12 : 2" v-bind="props"
                                                        @click="selectBook(item)">
                                                        <v-img :src="item.image ? item.image
                                                            : 'https://placehold.co/150?text=Item'" height="300px"
                                                            class="white--text align-end">
                                                        </v-img>
                                                        <v-card-subtitle
                                                            class="text-h6 text-center text-body-3 text-sm-left text-dark d-flex flex-column">
                                                            <p class="mt-1 text-center">
                                                                {{ item.book_title }}
                                                            </p>
                                                        </v-card-subtitle>
                                                        <v-card-text class="pa-1">
                                                            <p class="ma-0 text-body-6 text-sm-left">
                                                                By: <span class="font-weight-medium">{{ item.author
                                                                    }}</span>
                                                            </p>
                                                            <p class="text-caption text-sm-left">
                                                                Subject: <span class="font-weight-medium">
                                                                    {{ item.subject }}
                                                                </span>
                                                            </p>
                                                            <div class="text-center justify-content"
                                                                v-show="isHovering">
                                                                <v-btn @click.stop="selectBook(item)" class="mt-2"
                                                                    :class="{ 'show-btns': isHovering }"
                                                                    color="primary">
                                                                    <span class="mdi mdi-read"></span>
                                                                    Read
                                                                </v-btn>
                                                            </div>
                                                        </v-card-text>
                                                    </v-card>
                                                </v-hover>
                                            </v-col>
                                        </template>
                                    </v-row>
                                </v-container>
                            </v-card>
                        </v-col>
                    </v-row>
                    <v-dialog v-model="isReaderOpen" fullscreen hide-overlay transition="dialog-bottom-transition">
                        <EpubReader v-if="selectedBook.digital_file_type === 'epub'" :book="selectedBook"
                            :show="isReaderOpen" @close-reader="isReaderOpen = false" />
                        <PdfReader v-if="selectedBook.digital_file_type === 'pdf'" :book="selectedBook"
                            :show="isReaderOpen" @close-reader="isReaderOpen = false" />
                    </v-dialog>
                </v-container>
            </v-main>
        </v-app>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useBooksStore } from '../../books/store';
import Sidebar from '../components/Sidebar.vue';
import EpubReader from '../components/EpubReader.vue';
import PdfReader from '../components/PdfReader.vue';
import Layout from '../layout/Layout.vue';


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
    bookstore.get_books({ length: null });
    bookstore.get_book_categories({ length: null });
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
#app-container {
    margin-top: 20px;
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
