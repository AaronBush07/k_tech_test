<template>
  <div class="palette" :style="cssVars">
      <div class="col">
        <h3>Hue: {{this.item.hue}}</h3>
        <h3>Saturation: {{this.item.saturation}}</h3>
        <h3>Lightness: {{this.item.lightness}}</h3>
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
      return `background-color: hsl(${this.item.hue}, ${this.item.saturation}%, ${this.item.lightness}%);`;
    },
  },
};
</script>