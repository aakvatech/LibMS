<template>
    <div class="search-wrapper">
        <div class="search-input-wrapper">
            <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="19" height="19" viewBox="0 0 19 19" fill="none">
                <path
                    d="M7.9427 14.8416C11.5009 14.8416 14.3854 11.855 14.3854 8.1708C14.3854 4.48662 11.5009 1.5 7.9427 1.5C4.38449 1.5 1.5 4.48662 1.5 8.1708C1.5 11.855 4.38449 14.8416 7.9427 14.8416Z"
                    stroke="#818098" stroke-width="2.31353" stroke-linecap="round" stroke-linejoin="round" />
                <path d="M16.9531 17.5L12.4955 12.8846" stroke="#818098" stroke-width="2.31353" stroke-linecap="round"
                    stroke-linejoin="round" />
            </svg>
            <input v-model="message" @click="setShowSearchSuggestions(true)"
                placeholder="Looking for specific book? Enter Book Title here.." />
            <div v-if="message !== ''" @click="clearSearchInput()" class="close-btn">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M18 6L6 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M6 6L18 18" stroke="#222222" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
            </div>
        </div>
        <div v-if="showSearchSuggestions" class="search-dropdown">
            <ul class="tab-wrapper">
                <li class="active">All<span>14</span></li>
                <li>Books<span>8</span></li>
                <li>Magazines<span>8</span></li>
                <li>E-books<span>8</span></li>
                <li>Video<span>8</span></li>
                <li>Audio<span>8</span></li>
            </ul>
            <ul class="results">
                <li>
                    <div class="result-title">The Keys of understanding <span>qur</span>an</div>
                    <div class="category">Book</div>
                </li>
                <li>
                    <div class="result-title">The Keys of understanding quran</div>
                    <div class="category">Book</div>
                </li>
            </ul>
        </div>
    </div>
</template>
<script>
export default {
    methods: {
        handleClick(pageName) {
            // Call the function passed via prop
            if (this.onLinkClick) {
                this.onLinkClick(pageName);
            }
        },
        setShowSearchSuggestions(value) {
            this.showSearchSuggestions = value
        },
        clearSearchInput() {
            this.message = ""
            this.showSearchSuggestions = false
        }
    },
    data() {
        return {
            showSearchSuggestions: false,
            message: ''
        };
    },
}
</script>
<style scoped>
@import "./style.css";
</style>
