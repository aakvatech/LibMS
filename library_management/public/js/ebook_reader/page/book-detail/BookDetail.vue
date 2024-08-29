<template>

    <div class="book-detail-wrapper">
        <div class="inner-container">
            <div class="book-image-title-wrapper">
                <div class="image-wrapper"><v-img :src="book.image ? book.image
                    : 'https://placehold.co/150?text=Item'">
                    </v-img></div>
                <div class="title-wrapper">
                    <h1>{{ book.book_title }}</h1>
                    <div class="subtitle">અનુવાદક & પ્રકાશક: મેહેર લાઇબ્રેરી & જાફરી સેમિનરી</div>
                </div>

            </div>
            <div class="book-detail-section">
                <div class="description-wrapper">
                    <div class="description">{{ book.description }} </div>
                    <div class="button-wrapper">
                        <div class="primary-button" @click="handleClick('book-reader')"><svg
                                xmlns="http://www.w3.org/2000/svg" width="19" height="20" viewBox="0 0 19 20"
                                fill="none">
                                <path
                                    d="M18.2111 9.10557L1.73666 0.868328C0.938776 0.469388 0 1.04958 0 1.94164V18.0584C0 18.9504 0.938776 19.5306 1.73666 19.1317L18.2111 10.8944C18.9482 10.5259 18.9482 9.4741 18.2111 9.10557Z"
                                    fill="white" />
                            </svg>Start reading</div>
                    </div>
                </div>
                <div class="book-desc-columns">
                    <div class="book-desc-column">
                        <h2>Bibliographic Info</h2>
                        <div class="book-fields">
                            <BookField :label="'Subject Code'" :value="book.subjectCode" />
                            <BookField :label="'Author'" :value="book.author" />
                            <BookField :label="'Subject'" :value="book.subject" />
                            <BookField :label="'Language'" :value="book.language" />
                            <BookField :label="'Document Type'" :value="book.documentType" />
                            <BookField :label="'Publication'" :value="book.publication" />
                            <BookField :label="'Translator'" :value="book.translator" />
                            <BookField :label="'Publication Year'" :value="book.publicationYear" />
                            <BookField :label="'Volume'" :value="book.volume" />
                            <BookField :label="'ISBN'" :value="book.ISBN" />
                            <BookField :label="'Pages'" :value="book.pages" />
                            <BookField :label="'Category'" :value="book.category" />

                        </div>
                    </div>
                    <div class="book-desc-column">
                        <h2>Availability</h2>
                        <div class="book-access-fields">
                            <div class="book-access-header">
                                <div class="access-number">Access number</div>
                                <div class="status">Status</div>
                            </div>
                            <template v-for="item in book.accessNumber" :key="item.id">
                                <div class="book-access-item">
                                    <div class="access-number">{{ item.id }}</div>
                                    <div class="status" :class="{ active: item.avaiblity }">{{
                                        item.avaiblity?'Available':'Not available' }}
                                    </div>
                                </div>
                            </template>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>
<script setup>
import BookField from '../../components/book-field/BookField.vue';



// import { onMounted } from 'vue';
// import { useBooksStore } from '../../../../books/store';
// const bookstore = useBooksStore();
const bookstore = {
    book:
    // {

    //     book_title: 'મુન્તખબ મીઝાનુલ હિકમા',
    //     author: 'Author'
    // }
    {
        id: "",
        book_title: 'મુન્તખબ મીઝાનુલ હિકમા',
        imageUrl: '',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim  veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate  velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint  occaecat cupidatat non proident, sunt in culpa qui officia deserunt  mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmo.',
        subjectCode: '297.13',
        subject: 'Tafseer',
        documentType: 'Tafseer',
        translator: 'Tafseer',
        volume: '2',
        pages: '100',
        author: 'author',
        language: 'Gujarati',
        publication: 'Meher Library & Seminar',
        publicationYear: '2020',
        ISBN: '0000',
        category: 'Tafseer',
        accessNumber:
            [{
                id: '0000',
                avaiblity: true
            }, {
                id: '0001',
                avaiblity: false
            }]

    }

}
const book = bookstore.book
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
    }
}
</script>
<style scoped>
@import "./bookDetail.css";
</style>
