<template>
    <div :class="navigationClass">
        <button @click="handleClick('book-categories')">Book categories</button>
        <button @click="handleClick('about')">Multimedia Categories</button>
        <button @click="handleClick('about')">Apply Membership</button>
        <button @click="handleClick('about')">Fees</button>
        <button @click="handleClick('about')">News & Announcements</button>
        <button @click="handleClick('about')">Holidays</button>
        <button @click="handleClick('about')">Contact us</button>
        <button @click="handleClick('about')">Feedback</button>
    </div>
</template>
<script>


export default {
    props: {

        isSticky: {
            type: Boolean,
            required: false
        },
    },
    computed: {
        navigationClass() {
            return [
                'navigation',  // Static class
                {
                    sticky: this.isSticky,
                }
            ];
        }
    }
}
</script>
<style scoped>
@import "./style.css";
</style>
