<template>
    <div class="media-table-wrapper">
        <table>
            <thead>
                <tr class="t-header-row">
                    <th>Image</th>
                    <th>
                        <div class="sort-title">
                            Title<div class="sort-icon-wrapper">
                                <div class="asc-icon"><svg xmlns="http://www.w3.org/2000/svg" width="10" height="13"
                                        viewBox="0 0 10 13" fill="none">
                                        <path
                                            d="M5 1.5L4.29289 0.792893L5 0.0857863L5.70711 0.792893L5 1.5ZM6 11.5C6 12.0523 5.55229 12.5 5 12.5C4.44772 12.5 4 12.0523 4 11.5L6 11.5ZM0.292893 4.79289L4.29289 0.792893L5.70711 2.20711L1.70711 6.20711L0.292893 4.79289ZM5.70711 0.792893L9.70711 4.79289L8.29289 6.20711L4.29289 2.20711L5.70711 0.792893ZM6 1.5L6 11.5L4 11.5L4 1.5L6 1.5Z"
                                            fill="#999999" />
                                    </svg></div>
                                <div class="desc-icon">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="10" height="13" viewBox="0 0 10 13"
                                        fill="none">
                                        <path
                                            d="M5 11.5L5.70711 12.2071L5 12.9142L4.29289 12.2071L5 11.5ZM4 1.5C4 0.947715 4.44772 0.5 5 0.5C5.55228 0.5 6 0.947715 6 1.5L4 1.5ZM9.70711 8.20711L5.70711 12.2071L4.29289 10.7929L8.29289 6.79289L9.70711 8.20711ZM4.29289 12.2071L0.292893 8.20711L1.70711 6.79289L5.70711 10.7929L4.29289 12.2071ZM4 11.5L4 1.5L6 1.5L6 11.5L4 11.5Z"
                                            fill="#999999" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </th>
                    <th>
                        <div class="sort-title">
                            Date<div class="sort-icon-wrapper">
                                <div class="asc-icon"><svg xmlns="http://www.w3.org/2000/svg" width="10" height="13"
                                        viewBox="0 0 10 13" fill="none">
                                        <path
                                            d="M5 1.5L4.29289 0.792893L5 0.0857863L5.70711 0.792893L5 1.5ZM6 11.5C6 12.0523 5.55229 12.5 5 12.5C4.44772 12.5 4 12.0523 4 11.5L6 11.5ZM0.292893 4.79289L4.29289 0.792893L5.70711 2.20711L1.70711 6.20711L0.292893 4.79289ZM5.70711 0.792893L9.70711 4.79289L8.29289 6.20711L4.29289 2.20711L5.70711 0.792893ZM6 1.5L6 11.5L4 11.5L4 1.5L6 1.5Z"
                                            fill="#999999" />
                                    </svg></div>
                                <div class="desc-icon">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="10" height="13" viewBox="0 0 10 13"
                                        fill="none">
                                        <path
                                            d="M5 11.5L5.70711 12.2071L5 12.9142L4.29289 12.2071L5 11.5ZM4 1.5C4 0.947715 4.44772 0.5 5 0.5C5.55228 0.5 6 0.947715 6 1.5L4 1.5ZM9.70711 8.20711L5.70711 12.2071L4.29289 10.7929L8.29289 6.79289L9.70711 8.20711ZM4.29289 12.2071L0.292893 8.20711L1.70711 6.79289L5.70711 10.7929L4.29289 12.2071ZM4 11.5L4 1.5L6 1.5L6 11.5L4 11.5Z"
                                            fill="#999999" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </th>
                    <th>
                        <div class="sort-title">
                            Duration<div class="sort-icon-wrapper">
                                <div class="asc-icon"><svg xmlns="http://www.w3.org/2000/svg" width="10" height="13"
                                        viewBox="0 0 10 13" fill="none">
                                        <path
                                            d="M5 1.5L4.29289 0.792893L5 0.0857863L5.70711 0.792893L5 1.5ZM6 11.5C6 12.0523 5.55229 12.5 5 12.5C4.44772 12.5 4 12.0523 4 11.5L6 11.5ZM0.292893 4.79289L4.29289 0.792893L5.70711 2.20711L1.70711 6.20711L0.292893 4.79289ZM5.70711 0.792893L9.70711 4.79289L8.29289 6.20711L4.29289 2.20711L5.70711 0.792893ZM6 1.5L6 11.5L4 11.5L4 1.5L6 1.5Z"
                                            fill="#999999" />
                                    </svg></div>
                                <div class="desc-icon">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="10" height="13" viewBox="0 0 10 13"
                                        fill="none">
                                        <path
                                            d="M5 11.5L5.70711 12.2071L5 12.9142L4.29289 12.2071L5 11.5ZM4 1.5C4 0.947715 4.44772 0.5 5 0.5C5.55228 0.5 6 0.947715 6 1.5L4 1.5ZM9.70711 8.20711L5.70711 12.2071L4.29289 10.7929L8.29289 6.79289L9.70711 8.20711ZM4.29289 12.2071L0.292893 8.20711L1.70711 6.79289L5.70711 10.7929L4.29289 12.2071ZM4 11.5L4 1.5L6 1.5L6 11.5L4 11.5Z"
                                            fill="#999999" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </th>
                    <th>
                        <div class="sort-title">
                            Type<div class="sort-icon-wrapper">
                                <div class="asc-icon"><svg xmlns="http://www.w3.org/2000/svg" width="10" height="13"
                                        viewBox="0 0 10 13" fill="none">
                                        <path
                                            d="M5 1.5L4.29289 0.792893L5 0.0857863L5.70711 0.792893L5 1.5ZM6 11.5C6 12.0523 5.55229 12.5 5 12.5C4.44772 12.5 4 12.0523 4 11.5L6 11.5ZM0.292893 4.79289L4.29289 0.792893L5.70711 2.20711L1.70711 6.20711L0.292893 4.79289ZM5.70711 0.792893L9.70711 4.79289L8.29289 6.20711L4.29289 2.20711L5.70711 0.792893ZM6 1.5L6 11.5L4 11.5L4 1.5L6 1.5Z"
                                            fill="#999999" />
                                    </svg></div>
                                <div class="desc-icon">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="10" height="13" viewBox="0 0 10 13"
                                        fill="none">
                                        <path
                                            d="M5 11.5L5.70711 12.2071L5 12.9142L4.29289 12.2071L5 11.5ZM4 1.5C4 0.947715 4.44772 0.5 5 0.5C5.55228 0.5 6 0.947715 6 1.5L4 1.5ZM9.70711 8.20711L5.70711 12.2071L4.29289 10.7929L8.29289 6.79289L9.70711 8.20711ZM4.29289 12.2071L0.292893 8.20711L1.70711 6.79289L5.70711 10.7929L4.29289 12.2071ZM4 11.5L4 1.5L6 1.5L6 11.5L4 11.5Z"
                                            fill="#999999" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </th>
                    <th>
                        <div class="sort-title">
                            Category<div class="sort-icon-wrapper">
                                <div class="asc-icon"><svg xmlns="http://www.w3.org/2000/svg" width="10" height="13"
                                        viewBox="0 0 10 13" fill="none">
                                        <path
                                            d="M5 1.5L4.29289 0.792893L5 0.0857863L5.70711 0.792893L5 1.5ZM6 11.5C6 12.0523 5.55229 12.5 5 12.5C4.44772 12.5 4 12.0523 4 11.5L6 11.5ZM0.292893 4.79289L4.29289 0.792893L5.70711 2.20711L1.70711 6.20711L0.292893 4.79289ZM5.70711 0.792893L9.70711 4.79289L8.29289 6.20711L4.29289 2.20711L5.70711 0.792893ZM6 1.5L6 11.5L4 11.5L4 1.5L6 1.5Z"
                                            fill="#999999" />
                                    </svg></div>
                                <div class="desc-icon">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="10" height="13" viewBox="0 0 10 13"
                                        fill="none">
                                        <path
                                            d="M5 11.5L5.70711 12.2071L5 12.9142L4.29289 12.2071L5 11.5ZM4 1.5C4 0.947715 4.44772 0.5 5 0.5C5.55228 0.5 6 0.947715 6 1.5L4 1.5ZM9.70711 8.20711L5.70711 12.2071L4.29289 10.7929L8.29289 6.79289L9.70711 8.20711ZM4.29289 12.2071L0.292893 8.20711L1.70711 6.79289L5.70711 10.7929L4.29289 12.2071ZM4 11.5L4 1.5L6 1.5L6 11.5L4 11.5Z"
                                            fill="#999999" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </th>
                </tr>
            </thead>
            <tbody>
                <template v-for="item in medias" :key="item.title">
                    <tr @click="handleClick('media-detail')">
                        <td>
                            <div class="image-wrapper">
                                <img :src="item.image ? item.image
                                    : '/files/default-media.png'" />
                                <div class="player-icon">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30"
                                        fill="none">
                                        <circle cx="15" cy="15" r="15" fill="#00B0AB" />
                                        <path
                                            d="M23.2111 14.1055L10.07 7.53495C9.27211 7.13601 8.33333 7.71621 8.33333 8.60827V21.3917C8.33333 22.2837 9.27211 22.8639 10.07 22.465L23.2111 15.8944C23.9482 15.5259 23.9482 14.4741 23.2111 14.1055Z"
                                            fill="white" />
                                    </svg>
                                </div>
                            </div>
                        </td>
                        <td>
                            <h2>{{ item.title }}</h2>
                        </td>
                        <td>{{ item.date
                            }}</td>
                        <td>{{ item.duration }}</td>
                        <td>{{ item.media_type }}</td>
                        <td>{{ item.category }}</td>
                    </tr>
                </template>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    props: {
        medias: {
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
@import "./multimediaList.css";
</style>
