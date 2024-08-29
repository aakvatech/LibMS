<template>
    <div class="inner-layout">
        <Sidebar :onLinkClick="onLinkClick" />
        <div class="right-column">
            <Header />
            <component :onLinkClick="onLinkClick" :is="customComponent" />
        </div>
    </div>
</template>

<script setup>
import Header from './header/Header.vue';
import Sidebar from './sidebar/Sidebar.vue';
</script>

<script>
export default {
    props: {
        onLinkClick: {
            type: Function,
            required: true
        },
        customComponent: {
            type: Object, // The prop type should be a component definition (an object)
            required: true,
        },
    }

};
</script>

<style scoped>
@import "./style.css";
</style>