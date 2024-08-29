<template>
    <div class="medias-wrapper">
        <div class="inner-container">
            <div class="page-header">
                <h1>Multimedia</h1>
                <div class="right">
                    <div class="icons-wrapper">
                        <div :class="gridActiveClass" @click="setShowGrid(true)">
                            <svg width="31" height="24" viewBox="0 0 31 24" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <rect x="6" y="6" width="5" height="5" fill="#33363F" />
                                <rect x="13" y="6" width="5" height="5" fill="#33363F" />
                                <rect x="20" y="6" width="5" height="5" fill="#33363F" />
                                <rect x="6" y="13" width="5" height="5" fill="#33363F" />
                                <rect x="13" y="13" width="5" height="5" fill="#33363F" />
                                <rect x="20" y="13" width="5" height="5" fill="#33363F" />
                            </svg>
                        </div>
                        <div :class="listActiveClass" @click="setShowGrid(false)">
                            <svg width="25" height="18" viewBox="0 0 25 18" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <rect x="3" y="3" width="5" height="5" fill="#33363F" />
                                <rect x="10" y="4" width="12" height="3" fill="#33363F" />
                                <rect x="3" y="10" width="5" height="5" fill="#33363F" />
                                <rect x="10" y="11" width="12" height="3" fill="#33363F" />
                            </svg>
                        </div>
                    </div>
                    <MultimediaSort />
                    <MultimediaFilter />
                </div>
            </div>

            <MultimediaGrid :onLinkClick="onLinkClick" v-if="showGrid" :medias="mediastore.medias" />
            <MultimediaList :onLinkClick="onLinkClick" v-else :medias="mediastore.medias" />
        </div>
    </div>
</template>
<script setup>
import MultimediaGrid from '../../components/multimedias/MultimediaGrid.vue';
import MultimediaList from '../../components/multimedias/MultimediaList.vue';
import MultimediaSort from '../../components/multimedias/multimedia-sort/MultimediaSort.vue';
import MultimediaFilter from '../../components/multimedias/multimedia-filter/MultimediaFilter.vue';

// const mediastore = useBooksStore();
const mediastore = {
    medias: [
        {
            title: 'Media 1',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Video',
        },
        {
            title: 'Media 2',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Audio',
        },
        {
            title: 'Media 3',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Video',
        },
        {
            title: 'Media 4',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Audio',
        },
        {
            title: 'Media 5',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Video',
        },
        {
            title: 'Media 6',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Audio',
        },
        {
            title: 'Media 7',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Video',
        },
        {
            title: 'Media 8',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Audio',
        },
        {
            title: 'Media 9',
            date: '19-Sep-2022 4:07 PM',
            category: 'કરબલાના બહાદુરો',
            duration: '00:20:00',
            media_type: 'Video',
        }
    ]
}
</script>
<script>
let showGridValue = localStorage.getItem('showGrid')
if (showGridValue == null) {
    showGridValue = true
} else {
    showGridValue = JSON.parse(showGridValue)
}
export default {
    props: {
        onLinkClick: {
            type: Function,
            required: true
        },
    },
    methods: {
        setShowGrid(value) {
            this.showGrid = value
            localStorage.setItem('showGrid', value)
        },

    },
    data() {
        return {
            showGrid: showGridValue,
            showSortPopup: false
        };
    },
    computed: {
        gridActiveClass() {
            return [
                'icon-wrapper',  // Static class
                {
                    active: this.showGrid,
                }
            ];
        },
        listActiveClass() {
            return [
                'icon-wrapper',  // Static class
                {
                    active: !this.showGrid,
                }
            ];
        },

    }
}
</script>
<style scoped>
@import "./style.css";
</style>
