<template>

    <div class="media-detail-wrapper">
        <div class="inner-container">
            <div class="media-image-title-wrapper">

                <div class="image-wrapper">
                    <v-img :src="media.image_url !== '' ? media.image_url
                        : '/files/default-media.png'">
                    </v-img>
                    <div class="player-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="70" height="70" viewBox="0 0 70 70" fill="none">
                            <ellipse cx="35.2552" cy="35.2557" rx="34.4193" ry="34.5229" fill="#00B0AB" />
                            <path
                                d="M56.4188 34.3617L21.6955 16.9478C20.8975 16.5476 19.9575 17.1278 19.9575 18.0205V52.4908C19.9575 53.3834 20.8975 53.9636 21.6955 53.5634L56.4188 36.1495C57.1544 35.7806 57.1544 34.7306 56.4188 34.3617Z"
                                fill="white" />
                        </svg>
                    </div>
                </div>
                <div class="title-wrapper">
                    <h1>{{ media.title }}</h1>
                </div>

            </div>
            <div class="media-detail-section">
                <div class="description-wrapper">
                    <div class="description">{{ media.description }} </div>
                    <div class="button-wrapper">
                        <div v-if="media_type" class="primary-button" @click="handleClick('video-player')"><svg
                                xmlns="http://www.w3.org/2000/svg" width="19" height="20" viewBox="0 0 19 20"
                                fill="none">
                                <path
                                    d="M18.2111 9.10557L1.73666 0.868328C0.938776 0.469388 0 1.04958 0 1.94164V18.0584C0 18.9504 0.938776 19.5306 1.73666 19.1317L18.2111 10.8944C18.9482 10.5259 18.9482 9.4741 18.2111 9.10557Z"
                                    fill="white" />
                            </svg>Play Video</div>
                        <div v-else class="primary-button" @click="togglePlay">
                            <div class="icon-wrapper"><svg v-if="isPlaying" xmlns="http://www.w3.org/2000/svg"
                                    width="24" height="24" viewBox="0 0 24 24" fill="none">
                                    <rect x="6" y="5" width="4" height="14" rx="1" stroke="#fff" stroke-width="2"
                                        stroke-linecap="round" />
                                    <rect x="14" y="5" width="4" height="14" rx="1" stroke="#fff" stroke-width="2"
                                        stroke-linecap="round" />
                                </svg>
                                <svg v-else xmlns="http://www.w3.org/2000/svg" width="17" height="17"
                                    viewBox="0 0 17 17" fill="none">
                                    <path
                                        d="M15.2111 7.60557L2.73666 1.36833C1.93878 0.969388 1 1.54958 1 2.44164V14.5584C1 15.4504 1.93878 16.0306 2.73666 15.6317L15.2111 9.39443C15.9482 9.0259 15.9482 7.9741 15.2111 7.60557Z"
                                        stroke="white" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round" />
                                </svg>
                            </div>Play Audio
                        </div>
                    </div>
                </div>

                <div class="audio-player">
                    <audio ref="audio" @timeupdate="updateProgress" @ended="resetPlayer">
                        <source :src="audioSrc" type="audio/mpeg" />
                        Your browser does not support the audio element.
                    </audio>

                    <div class="controls">
                        <button @click="togglePlay">
                            <div class="icon-wrapper">
                                <svg v-if="isPlaying" xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                                    viewBox="0 0 24 24" fill="none">
                                    <rect x="6" y="5" width="4" height="14" rx="1" stroke="#fff" stroke-width="2"
                                        stroke-linecap="round" />
                                    <rect x="14" y="5" width="4" height="14" rx="1" stroke="#fff" stroke-width="2"
                                        stroke-linecap="round" />
                                </svg>
                                <svg v-else xmlns="http://www.w3.org/2000/svg" width="17" height="17"
                                    viewBox="0 0 17 17" fill="none">
                                    <path
                                        d="M15.2111 7.60557L2.73666 1.36833C1.93878 0.969388 1 1.54958 1 2.44164V14.5584C1 15.4504 1.93878 16.0306 2.73666 15.6317L15.2111 9.39443C15.9482 9.0259 15.9482 7.9741 15.2111 7.60557Z"
                                        stroke="white" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round" />
                                </svg>
                            </div>

                        </button>
                        <input class="range-slider" type="range" min="0" :max="duration" step="0.1"
                            v-model="currentTime" @input="seekAudio">
                        <span class="time">{{ formatTime(currentTime) }} / {{ formatTime(duration) }}</span>
                        <div class="volume-control">
                            <label for="volume"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="25"
                                    viewBox="0 0 24 25" fill="none">
                                    <path
                                        d="M4.15838 14.4306C3.44537 13.2423 3.44537 11.7577 4.15838 10.5694C4.37596 10.2067 4.73641 9.95272 5.1511 9.86978L6.84413 9.53117C6.94499 9.511 7.03591 9.45691 7.10176 9.37788L9.17085 6.89498C10.3534 5.47592 10.9447 4.76638 11.4723 4.95742C12 5.14846 12 6.07207 12 7.91928L12 17.0807C12 18.9279 12 19.8515 11.4723 20.0426C10.9447 20.2336 10.3534 19.5241 9.17085 18.105L7.10176 15.6221C7.03591 15.5431 6.94499 15.489 6.84413 15.4688L5.1511 15.1302C4.73641 15.0473 4.37596 14.7933 4.15838 14.4306Z"
                                        fill="white" />
                                    <path
                                        d="M14.5355 8.96447C15.4684 9.89732 15.9948 11.1611 16 12.4803C16.0052 13.7996 15.4888 15.0674 14.5633 16.0076"
                                        stroke="white" stroke-width="2" stroke-linecap="round" />
                                </svg></label>
                            <input id="volume" class="volume-range-slider" type="range" min="0" max="1" step="0.01"
                                v-model="volume" @input="adjustVolume">
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
        media_url: '',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim  veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate  velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint  occaecat cupidatat non proident, sunt in culpa qui officia deserunt  mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmo.'

    }

}
const media = mediastore.media
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
        },
        togglePlay() {
            const audio = this.$refs.audio;
            this.isPlaying = !this.isPlaying;

            if (this.isPlaying) {
                audio.play();
            } else {
                audio.pause();
            }
        },
        updateProgress() {
            this.currentTime = this.$refs.audio.currentTime;
        },
        setDuration() {
            this.duration = this.$refs.audio.duration;
        },
        seekAudio() {
            this.$refs.audio.currentTime = this.currentTime;
        },
        formatTime(time) {
            const minutes = Math.floor(time / 60);
            const seconds = Math.floor(time % 60);
            return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
        },
        resetPlayer() {
            this.isPlaying = false;
            this.currentTime = 0;
        },
        adjustVolume() {
            this.$refs.audio.volume = this.volume;
        },
    },
    data() {
        return {
            audioSrc: 'https://file-examples.com/storage/fed4cf5e5466cf5da9e984e/2017/11/file_example_MP3_700KB.mp3',  // Replace with your audio file path
            isPlaying: false,
            duration: 0,
            currentTime: 0,
            volume: 1  // Default volume (100%)
        };
    },
    mounted() {
        this.$refs.audio.addEventListener('loadedmetadata', this.setDuration);
        this.$refs.audio.volume = this.volume;  // Set initial volume
    },
}
</script>
<style scoped>
@import "./mediaDetail.css";
</style>
