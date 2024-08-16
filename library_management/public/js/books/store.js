import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

export const useBooksStore = defineStore('books', {
    state: () => {
        return {
            books: ref([]),
            search_book: ref(""),
            book_category: ref(""),
            book_categories: ref([]),
            book_author: ref(""),
            book_subject: ref(""),
            book_tag: ref(""),
            book_edition: ref(""),
            year_of_publication: ref(""),

        }
    },
    getters: {

    },
    actions: {
        get_books({ length = null }) {
            frappe.call({
                method: "library_management.api.api.get_books",
                args: {},
                callback: (r) => {
                    if (r.message.length > 0) {
                        if (length !== null) {
                            this.books = r.message.slice(0, length);
                        } else {
                            this.books = r.message;
                        }


                    } else {
                        this.books = [];
                    }
                }
            });
        },

        get_media({ length = null }) {
            frappe.call({
                method: "library_management.api.api.get_books",
                args: {},
                callback: (r) => {
                    if (r.message.length > 0) {
                        if (length !== null) {
                            this.media = r.message.slice(0, length);
                        } else {
                            this.media = r.message;
                        }


                    } else {
                        this.media = [];
                    }
                }
            });
        },

        get_book_categories({ length = null }) {
            frappe.call({
                method: "library_management.api.api.get_book_categories",
                args: {},
                callback: (r) => {
                    if (r.message.length > 0) {
                        if (length !== null) {
                            this.book_categories = r.message.slice(0, length);
                        } else {
                            this.book_categories = r.message;
                        }
                    } else {
                        this.book_categories = [];
                    }
                }
            });
        },

        search_books() {
            frappe.call({
                method: "library_management.api.api.search_books",
                args: {
                    book_title: this.search_book
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        },

        get_books_by_category() {
            frappe.call({
                method: "library_management.api.api.get_books_by_category",
                args: {
                    book_category: this.book_category
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        },

        get_books_by_author() {
            frappe.call({
                method: "library_management.api.api.get_books_by_author",
                args: {
                    author: this.book_author
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        },

        get_books_by_subject() {
            frappe.call({
                method: "library_management.api.api.get_books_by_subject",
                args: {
                    subject: this.book_subject
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        },

        get_books_by_tag() {
            frappe.call({
                method: "library_management.api.api.get_books_by_book_tag",
                args: {
                    book_tag: this.book_tag
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        },

        get_books_by_edition() {
            frappe.call({
                method: "library_management.api.api.get_books_by_book_edition",
                args: {
                    edition: this.book_edition
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        },

        get_books_by_year_of_publication() {
            frappe.call({
                method: "library_management.api.api.get_books_by_publication_year",
                args: {
                    year_of_publication: this.year_of_publication
                },
                callback: (r) => {
                    if (r.message.length > 0) {
                        this.books = r.message;
                    } else {
                        this.books = [];
                    }
                }
            });
        }
    }
})
