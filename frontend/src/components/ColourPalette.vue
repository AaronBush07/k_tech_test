<template>
  <v-container>
      <v-row>
          <v-spacer></v-spacer>
          <div class="col-4 col-md-2"  v-for="item in list" :key="JSON.stringify(item)">
              <v-card >
              <span v-if="item.type === 'RGB'">
                  <RGB :item="item" />
              </span>
              <span v-if="item.type === 'HSL'">
                  <HSL :item="item"/>
              </span>
              <v-card-text>Type: {{item.type}}</v-card-text>
              </v-card>
          </div>
          <v-spacer></v-spacer>
      </v-row>
      <v-row>
        <v-col cols="12" align="center"> 
            <v-btn @click="getList" class="mx-auto primary">Load New Colours</v-btn>    
        </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
import RGB from './RGB'
import HSL from './HSL'
export default {
    components: {
      HSL,
    RGB,
  },
  computed: {
    ...mapState({
      list: "list",
    }),
  },
  methods: {
    getList() {
      this.$store.dispatch("fetchList");
    },
  },
};
</script>

<style scoped>
  .palette {
    width: 100%;
    height: 0;
    padding-bottom: 100%;
    color: white;
  }
</style>