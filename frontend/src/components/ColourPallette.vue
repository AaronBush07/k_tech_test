<template>
  <v-container>
    <v-btn @click="getList" class="primary">Load New Colours</v-btn>    
  </v-container>
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState({
      list:"list",
    }),
  },
  methods: {
    getList() {
      this.$store.dispatch("fetchList");
    },
  },
};
</script>