<template>
  <div>
    <b-navbar class="navbar header has-shadow is-primary" :fixed-top="true">
      <template slot="brand">
        <b-navbar-item v-scroll-to="{ el: '#description', offset: -10 }">
          <img src="../assets/buefy.png"/>
        </b-navbar-item>
      </template>
      <template slot="start">
        <b-navbar-item v-scroll-to="{ el: '#carousel', offset: -10 }">
          Carousel
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
  </div>
</template>

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

  // Links
  $link: $primary;
  $link-invert: $primary-invert;
  $link-focus-border: $primary;

  // Images
  @import "./image";

  // Import Bulma and Buefy styles
  @import "~bulma";
  @import "~buefy/src/scss/buefy";
</style>
