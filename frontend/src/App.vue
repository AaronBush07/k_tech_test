<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <h2>Random Colour Generator</h2>
      </div>
    </v-app-bar>

    <v-main>
      <ColourPalette/>
    </v-main>
  </v-app>
</template>

<script>
import ColourPalette from './components/ColourPalette';

export default {
  name: 'App',

  components: {
    ColourPalette,
  },

  data: () => ({
    //
  }),
};
</script>
