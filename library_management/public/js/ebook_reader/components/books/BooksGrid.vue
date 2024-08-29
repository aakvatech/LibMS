<template>
    <div class="book-grid-section">
        <div class="book-list-wrapper">
            <template v-for="item in books" :key="item.book_title">
                <Book :onLinkClick="onLinkClick" :book="item" />
            </template>


        </div>
    </div>
</template>

<script setup>
import Book from './Book.vue';
</script>

<script>


export default {
    props: {
        books: {
            type: Array,
            required: true
        },
        onLinkClick: {
            type: Function,
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
    }
}
</script>

<style scoped>
@import './booksGrid.css'
</style>
