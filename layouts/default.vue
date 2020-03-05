<template>
  <div>
    <b-navbar class="navbar header has-shadow is-primary" :fixed-top="true">
      <template slot="brand">
        <b-navbar-item v-scroll-to="{ el: '#description', offset: -10 }">
          <img src="../assets/logo.png"/>
        </b-navbar-item>
      </template>
      <template slot="start">
        <b-navbar-item v-scroll-to="{ el: '#carousel', offset: -10 }">
          Carousel
        </b-navbar-item>
        <b-navbar-item v-scroll-to="{ el: '#smallMultiples', offset: -10 }">
          Small Multiples
        </b-navbar-item>
        <b-navbar-item v-scroll-to="{ el: '#map', offset: -10 }">
          Map
        </b-navbar-item>
      </template>
    </b-navbar>

    <!--Here is our content from index.vue-->
    <div>
      <nuxt/>
    </div>

    <footer class="footer">
      <div class="content has-text-centered">
        <p>
          <strong>NYC airbnb viz</strong> by <a href="https://github.com/kjmj/" target="_blank">Ken Morton</a> and <a
          href="https://github.com/NeerJariwala/" target="_blank">Neer Jariwala</a> for Lane Harrison's Data
          Visualization course at <a href="https://www.wpi.edu/" target="_blank">WPI</a>. Find our source code on
          <a href="https://github.com/kjmj/final/" target="_blank">GitHub</a>.
        </p>
        <p>
          Made with <a href="https://vuejs.org/" target="_blank">vue.js</a> and <a href="https://d3js.org/"
                                                                                   target="_blank">d3.js</a>. Here is
          our <a href="https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data/" target="_blank">dataset</a> on
          Kaggle.
        </p>
      </div>
    </footer>
  </div>
</template>

<!--Override some of bulmas defaults-->
<style lang="scss">
  // Import Bulma's core
  @import "~bulma/sass/utilities/_all";

  // Set your colors
  $primary: #4099FF;
  $primary-invert: findColorInvert($primary);

  // Setup $colors to use as bulma classes (e.g. 'is-twitter')
  $colors: (
    "white": ($white, $black),
    "black": ($black, $white),
    "light": ($light, $light-invert),
    "dark": ($dark, $dark-invert),
    "primary": ($primary, $primary-invert),
    "info": ($info, $info-invert),
    "success": ($success, $success-invert),
    "warning": ($warning, $warning-invert),
    "danger": ($danger, $danger-invert),
  );

  // Font
  $family-primary: Roboto, sans-serif;
  $family-secondary: Roboto, sans-serif;

  // Links
  $link: $primary;
  $link-invert: $primary-invert;
  $link-focus-border: $primary;

  // Import Bulma and Buefy styles
  @import "~bulma";
  @import "~buefy/src/scss/buefy";
</style>
