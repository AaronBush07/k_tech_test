<template>
    <span class="rgb"></span>
</template>

<script>
export default {
    name: "RGB", 
    props: {
        type: String, 
        red: Number,
        blue: Number, 
        green: Number
    },
    computed: {
        cssVars() {
            return {
                '--red': this.red,
                '--blue': this.blue,
                '--green': this.green
            } 
        }
    }
}
</script>

<style scoped>
    .rgb {
        background-color: rgb(var(--red), var(--blue), var(--green));
        width:100%;
        height: 0;
        padding-bottom:100%; 
    }
</style>