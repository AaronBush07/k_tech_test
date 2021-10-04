<template>
  <div class="palette" :style="cssVars">
      <div class="col text-caption text-sm-body-2" >
        Hue: {{this.item.hue}}<br>
        Saturation: {{this.item.saturation}}<br>
        Lightness: {{this.item.lightness}}
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