<template>
  <div class="palette" :style="cssVars">
      <div class="col">
        <h3>Red: {{this.item.red}}</h3>
        <h3>Green: {{this.item.green}}</h3>
        <h3>Blue: {{this.item.blue}}</h3>
      </div>
  </div>
</template>

<script>
export default {
  name: "RGB",
  props: {
    item: Object
  },
  computed: {
    cssVars() {
      return `background-color: rgb(${this.item.red}, ${this.item.green}, ${this.item.blue});`;
    },
  },
};
</script>