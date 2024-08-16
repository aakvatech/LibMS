<template>
    <div id="app-container">
        <v-app>
            <v-main>
                <button @click="handleClick('home')">home</button>
                This is aboutpage
            </v-main>
        </v-app>
    </div>
</template>


<script>
export default {
  props: {
    onLinkClick: {
      type: Function,
      required: true
    }
  },
  methods: {
    handleClick(pageName) {
      // Call the function passed via prop
      if (this.onLinkClick) {
        this.onLinkClick(pageName);
      }
    }
  }
};
</script>

<style scoped>
#app-container {
    margin-top: 20px;
    text-align: center;
}

.drawer-open {
    transition: margin-left 0.3s;
    margin-left: 10px;
}

.v-card img {
    object-fit: cover;
}
</style>
