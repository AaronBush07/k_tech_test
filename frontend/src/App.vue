<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <h1>Random Colour Generator</h1>
      </div>
    </v-app-bar>

    <v-main>
      <ColourPallette/>
    </v-main>
  </v-app>
</template>

<script>
import ColourPallette from './components/ColourPallette';

export default {
  name: 'App',

  components: {
    ColourPallette,
  },

  data: () => ({
    //
  }),
};
</script>
