<template>
    <div class="header">
        <div class="left">
            <Search />
        </div>
        <div class="right">
            <div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 25 25"
                    fill="none">
                    <path fill-rule="evenodd" clip-rule="evenodd"
                        d="M22.9161 20.6391C24.1588 19.379 24.7802 18.749 24.5127 18.13C24.2451 17.5111 23.1128 17.538 20.8481 17.5917C17.3931 17.6737 13.9118 16.3963 11.2751 13.7596C8.63845 11.123 7.36108 7.64174 7.44302 4.18675C7.49673 1.92208 7.52358 0.78974 6.90467 0.522196C6.28576 0.254652 5.65571 0.876024 4.3956 2.11877C4.3736 2.14046 4.35166 2.16225 4.32978 2.18414C-0.784623 7.29854 -0.784623 15.5906 4.32978 20.705C9.44418 25.8194 17.7363 25.8194 22.8507 20.705C22.8726 20.6831 22.8944 20.6612 22.9161 20.6391Z"
                        fill="#4B556A" />
                </svg></div>
            <UserIcon :dark="true" />

        </div>
    </div>
</template>

<script setup>
import UserIcon from '../../components/home/header-banner/UserIcon.vue';
import Search from '../../components/search/Search.vue';
</script>
<style scoped>
@import "./style.css";
</style>
