<template>
    <div class="book-field">
        <div class="label">{{ label }}</div>
        <div class="value">{{ value }}</div>
    </div>
</template>

<script>
export default {
    props: {
        label: {
            type: String,
            required: true
        },
        value: {
            type: String,
            required: true
        }
    },
}
</script>