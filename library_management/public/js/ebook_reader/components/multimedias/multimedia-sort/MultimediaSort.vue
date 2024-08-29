<template>
    <div class="icons-wrapper sort">
        <div @click="setShowSortPopup(!showSortPopup)" class="title-icon-wrapper">
            <span class="selected-circle" />
            Sort
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M5 7H19" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                <path d="M5 12H15" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
                <path d="M5 17H11" stroke="#33363F" stroke-width="2" stroke-linecap="round" />
            </svg>
        </div>
        <div v-if="showSortPopup" class="sort-filter-popup">
            <div class="title-wrapper">
                <div class="title">Sort</div>
                <div class="right">
                    <div class="clear">Clear All</div>
                    <div @click="setShowSortPopup(false)" class="close-icon"><svg xmlns="http://www.w3.org/2000/svg"
                            width="24" height="24" viewBox="0 0 24 24" fill="none">
                            <path d="M18 6L6 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M6 6L18 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                        </svg></div>
                </div>
            </div>
            <div class="sort-filter-column-wrapper">
                <div class="column">
                    <template v-for="item in firstHalf" :key="item.title">
                        <MultimediaSortItem :sortItem="item" />
                    </template>
                </div>
                <div class="column">
                    <template v-for="item in secondHalf" :key="item.title">
                        <MultimediaSortItem :sortItem="item" />
                    </template>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import MultimediaSortItem from './MultimediaSortItem.vue';
</script>

<script>
export default {
    data() {
        return {
            array: [
                {
                    title: 'Book Title',
                },
                {
                    title: 'Author',
                },
                {
                    title: 'Language',
                },
                {
                    title: 'Subject',
                },
                {
                    title: 'Publication Year',
                },
                {
                    title: 'Publisher',
                }
            ],
            showSortPopup: false
        };
    },
    methods: {
        setShowSortPopup(value) {
            this.showSortPopup = value
        }
    },
    computed: {
        middleIndex() {
            return Math.floor(this.array.length / 2);
        },
        firstHalf() {
            return this.array.slice(0, this.middleIndex);
        },
        secondHalf() {
            return this.array.slice(this.middleIndex);
        },
    },
};
</script>