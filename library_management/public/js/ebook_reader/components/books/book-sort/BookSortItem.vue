<template>
    <div class="item">
        <div class="sort-icon-wrapper">
            <div class="asc-icon"><svg xmlns="http://www.w3.org/2000/svg" width="10" height="13" viewBox="0 0 10 13"
                    fill="none">
                    <path
                        d="M5 1.5L4.29289 0.792893L5 0.0857863L5.70711 0.792893L5 1.5ZM6 11.5C6 12.0523 5.55229 12.5 5 12.5C4.44772 12.5 4 12.0523 4 11.5L6 11.5ZM0.292893 4.79289L4.29289 0.792893L5.70711 2.20711L1.70711 6.20711L0.292893 4.79289ZM5.70711 0.792893L9.70711 4.79289L8.29289 6.20711L4.29289 2.20711L5.70711 0.792893ZM6 1.5L6 11.5L4 11.5L4 1.5L6 1.5Z"
                        fill="#00B0AB" />
                </svg></div>
            <div class="desc-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="10" height="13" viewBox="0 0 10 13" fill="none">
                    <path
                        d="M5 11.5L5.70711 12.2071L5 12.9142L4.29289 12.2071L5 11.5ZM4 1.5C4 0.947715 4.44772 0.5 5 0.5C5.55228 0.5 6 0.947715 6 1.5L4 1.5ZM9.70711 8.20711L5.70711 12.2071L4.29289 10.7929L8.29289 6.79289L9.70711 8.20711ZM4.29289 12.2071L0.292893 8.20711L1.70711 6.79289L5.70711 10.7929L4.29289 12.2071ZM4 11.5L4 1.5L6 1.5L6 11.5L4 11.5Z"
                        fill="#999999" />
                </svg>
            </div>
        </div>
        {{ sortItem.title }}
    </div>
</template>

<script>
export default {
    props: {
        sortItem: {
            type: Object,
            required: true
        },
    },
}
</script>