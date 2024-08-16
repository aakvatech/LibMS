<template>

    <div class="books-wrapper">
        <div class="inner-container">
            <div class="page-header">
                <h1>Books</h1>
                <div class="right">
                    <div class="icon-wrapper">
                        <svg width="31" height="24" viewBox="0 0 31 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect x="6" y="6" width="5" height="5" fill="#33363F" />
                            <rect x="13" y="6" width="5" height="5" fill="#33363F" />
                            <rect x="20" y="6" width="5" height="5" fill="#33363F" />
                            <rect x="6" y="13" width="5" height="5" fill="#33363F" />
                            <rect x="13" y="13" width="5" height="5" fill="#33363F" />
                            <rect x="20" y="13" width="5" height="5" fill="#33363F" />
                        </svg>
                        <svg width="25" height="18" viewBox="0 0 25 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect x="3" y="3" width="5" height="5" fill="#33363F" />
                            <rect x="10" y="4" width="12" height="3" fill="#33363F" />
                            <rect x="3" y="10" width="5" height="5" fill="#33363F" />
                            <rect x="10" y="11" width="12" height="3" fill="#33363F" />
                        </svg>
                    </div>
                    <div class="icon-wrapper">
                        Sort
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                            <path d="M5 7H19" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <path d="M5 12H15" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <path d="M5 17H11" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                        </svg>
                    </div>
                    <div class="icon-wrapper">
                        Filters
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                            <path d="M5 12L5 4" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <path d="M19 20L19 18" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <path d="M5 20L5 16" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <path d="M19 12L19 4" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <path d="M12 7L12 4" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <path d="M12 20L12 12" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <circle cx="5" cy="14" r="2" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <circle cx="12" cy="9" r="2" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                            <circle cx="19" cy="15" r="2" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                        </svg>
                    </div>
                </div>
            </div>
            <div class="book-table-wrapper">
                <table>
                    <tr class="t-header-row">
                        <th>Image</th>
                        <th>Title</th>
                        <th>Author</th>
                        <th>Language</th>
                        <th>Book type</th>
                        <th>Sec</th>
                        <th>Available</th>
                    </tr>
                    <template v-for="item in bookstore.books" :key="item.book_title">
                        <tr>
                            <td class="image-wrapper"><img :src="item.image ? item.image
                                : 'https://placehold.co/150?text=Item'" />
                            </td>
                            <td>
                                <h2>{{ item.book_title }}</h2>
                            </td>
                            <td>{{ item.author
                                }}</td>
                            <td>Gujarati</td>
                            <td>E-Book</td>
                            <td>Shia</td>
                            <td><span class="availability yes">Yes</span></td>
                        </tr>
                    </template>
                </table>
            </div>
        </div>
    </div>
</template>
<script setup>
// import { onMounted } from 'vue';
// import { useBooksStore } from '../../../../books/store';
// const bookstore = useBooksStore();
const bookstore = {
    books: [
        {
            book_title: 'Book1',
            author: 'Author'
        },
        {
            book_title: 'Book2',
            author: 'Author'
        },
        {
            book_title: 'Book3',
            author: 'Author'
        },
        {
            book_title: 'Book4',
            author: 'Author'
        },
        {
            book_title: 'Book5',
            author: 'Author'
        }
    ]
}
</script>
<style scoped>
@import "./style.css";
</style>
