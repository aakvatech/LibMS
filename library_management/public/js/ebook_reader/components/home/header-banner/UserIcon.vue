<template>


    <div class="nav-icon" @click="setShowProfileMenu(!showProfileMenu)">
        <svg v-if="dark !== true" xmlns="http://www.w3.org/2000/svg" width="35" height="36" viewBox="0 0 35 36"
            fill="none">
            <circle cx="17.5" cy="15.0834" r="4.375" stroke="white" stroke-width="2" stroke-linecap="round" />
            <circle cx="17.5" cy="18" r="13.125" stroke="white" stroke-width="2" />
            <path
                d="M25.9299 27.9552C26.1153 27.8534 26.203 27.633 26.1246 27.4366C25.5623 26.0274 24.479 24.7863 23.0146 23.8818C21.4325 22.9046 19.4941 22.375 17.5 22.375C15.5059 22.375 13.5675 22.9046 11.9854 23.8818C10.5211 24.7863 9.43775 26.0274 8.87539 27.4366C8.79701 27.633 8.88469 27.8534 9.07008 27.9552C14.3204 30.8377 20.6796 30.8377 25.9299 27.9552Z"
                fill="white" stroke="none" />
            <path v-if="dark == true"
                d="M25.9299 27.9552C26.1153 27.8534 26.203 27.633 26.1246 27.4366C25.5623 26.0274 24.479 24.7863 23.0146 23.8818C21.4325 22.9046 19.4941 22.375 17.5 22.375C15.5059 22.375 13.5675 22.9046 11.9854 23.8818C10.5211 24.7863 9.43775 26.0274 8.87539 27.4366C8.79701 27.633 8.88469 27.8534 9.07008 27.9552C14.3204 30.8377 20.6796 30.8377 25.9299 27.9552Z"
                fill="white" stroke="none" />
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" width="35" height="36" viewBox="0 0 35 36" fill="none">
            <circle cx="17.5" cy="15.0834" r="4.375" stroke="#4B556A" stroke-width="2" stroke-linecap="round" />
            <circle cx="17.5" cy="18" r="13.125" stroke="#4B556A" stroke-width="2" />
            <path
                d="M25.9299 27.9552C26.1153 27.8534 26.203 27.633 26.1246 27.4366C25.5623 26.0274 24.479 24.7863 23.0146 23.8818C21.4325 22.9046 19.4941 22.375 17.5 22.375C15.5059 22.375 13.5675 22.9046 11.9854 23.8818C10.5211 24.7863 9.43775 26.0274 8.87539 27.4366C8.79701 27.633 8.88469 27.8534 9.07008 27.9552C14.3204 30.8377 20.6796 30.8377 25.9299 27.9552Z"
                fill="#4B556A" stroke="none" />
            <path v-if="dark == true"
                d="M25.9299 27.9552C26.1153 27.8534 26.203 27.633 26.1246 27.4366C25.5623 26.0274 24.479 24.7863 23.0146 23.8818C21.4325 22.9046 19.4941 22.375 17.5 22.375C15.5059 22.375 13.5675 22.9046 11.9854 23.8818C10.5211 24.7863 9.43775 26.0274 8.87539 27.4366C8.79701 27.633 8.88469 27.8534 9.07008 27.9552C14.3204 30.8377 20.6796 30.8377 25.9299 27.9552Z"
                fill="#4B556A" stroke="none" />
        </svg>
        <div v-if="showProfileMenu" class="profile-menu">
            <ul>
                <li>test@test.com</li>
                <li>Logout</li>
            </ul>
        </div>
    </div>

</template>

<script>


export default {
    props: {
        onLinkClick: {
            type: Function,
            required: true
        },
        setWhiteTheme: {
            type: Function,
            required: true
        },
        whiteTheme: {
            type: Boolean,
            required: true
        },
        dark: {
            type: Boolean,
            required: false
        }
    },
    methods: {
        handleClick(pageName) {
            // Call the function passed via prop
            if (this.onLinkClick) {
                this.onLinkClick(pageName);
            }
        },
        setShowProfileMenu(value) {
            this.showProfileMenu = value
        }
    },
    data() {
        return {
            showProfileMenu: false
        };
    },
};
</script>


<style scoped>
@import "./style.css";
</style>