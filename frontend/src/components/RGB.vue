<template>
  <div class="palette" :style="cssVars">
      <div class="col text-caption text-sm-body-2">
        Red: {{this.item.red}} <br>
        Green: {{this.item.green}} <br>
        Blue: {{this.item.blue}}
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