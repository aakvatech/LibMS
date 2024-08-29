<template>
    <div class="video-player-wrapper">
        <div class="left-column">
            <div class="iframe-wrapper">
                <iframe :src="media.media_url"></iframe>
            </div>
            <div class="video-detail">
                <div class="title">{{ media.title }}</div>
                <div class="meta-wrapper">
                    <div class="meta">
                        <div class="label">Date:</div>
                        <div class="value">{{ media.date }}</div>
                    </div>
                    <div class="meta">
                        <div class="label">Category:</div>
                        <div class="value">{{ media.category }}</div>
                    </div>
                </div>
                <div class="description">{{ media.description }}</div>
            </div>
        </div>
        <div class="right-column">
            <div class="related-medias-section">
                <template v-for="item in medias" :key="item.title">
                    <MultimediaHorizonta :onLinkClick="onLinkClick" :media="item" />
                </template>


            </div>
        </div>
    </div>
</template>

<script setup>
import BookField from '../../components/book-field/BookField.vue';
import MultimediaHorizonta from '../../components/multimedias/MultimediaHorizonta.vue';



// import { onMounted } from 'vue';
// import { useBooksStore } from '../../../../books/store';
// const bookstore = useBooksStore();
const mediastore = {
    media:
    // {

    //     book_title: 'મુન્તખબ મીઝાનુલ હિકમા',
    //     author: 'Author'
    // }
    {
        id: "",
        title: 'Media 1',
        date: '19-Sep-2022 4:07 PM',
        category: 'કરબલાના બહાદુરો',
        duration: '00:20:00',
        media_type: 'Video',
        image_url: '',
        media_url: 'https://www.youtube.com/embed/yzqpoVdvdFM?autoplay=0&controls=0&disablekb=1&playsinline=1&cc_load_policy=0&cc_lang_pref=auto&widget_referrer=https%3A%2F%2Fevents.meherlibrary.org%2Fwatch%2F%3Fid%3D66b85622e91ed00a1ddca9f9&rel=0&showinfo=0&iv_load_policy=3&modestbranding=1&customControls=true&noCookie=false&enablejsapi=1&origin=https%3A%2F%2Fevents.meherlibrary.org&widgetid=1',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim  veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate  velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint  occaecat cupidatat non proident, sunt in culpa qui officia deserunt  mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmo.'

    },
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
const media = mediastore.media
const medias = mediastore.medias
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
@import "./video-player.css";
</style>