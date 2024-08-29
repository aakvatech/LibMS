<template>
    <div class="book-categories-page">
        <h1>Book Categories</h1>
        <div class="category-list-wrapper">
            <template v-for="item in bookCategoryStore.book_categories" :key="item.category">
                <div class="item" @click="handleClick('books')">
                    <div class="icon-wrapper" style="background-image: url(/files/round.png);"><img
                            src="/files/image.png">
                    </div>
                    <div class="title">{{ item.category }}</div>
                </div>
            </template>
        </div>

    </div>
</template>


<script setup>
// import { onMounted } from 'vue';
// import { useBooksStore } from '../../../../books/store';
// const bookCategoryStore = useBooksStore();
const bookCategoryStore = {
    book_categories: [
        {
            category: 'Category 1',
        },
        {
            category: 'Category 2',
        },
        {
            category: 'Category 3',
        },
        {
            category: 'Category 4',
        },
        {
            category: 'Category 5',
        },
        {
            category: 'Category 6',
        },
        {
            category: 'Category 7',
        },
        {
            category: 'Category 8',
        },
        {
            category: 'Category 9',
        },
        {
            category: 'Category 10',
        }
    ]
}
// onMounted(() => {
//   bookCategoryStore.get_book_categories({ length: 5 });
// });
</script>

<script>
export default {
    props: {
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
    },
}
</script>

<style scoped>
@import "./bookCategories.css";
</style>
