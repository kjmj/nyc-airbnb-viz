<template>
  <div>
    <section class="section" id="description">
      <description></description>
    </section>
    <client-only>
      <visualizations></visualizations>
    </client-only>

    <!--this is here temporarily so clicking navbar items scrolls-->
    <div style="height: 1000px"></div>
  </div>
</template>

<script>
  import Description from '~/components/Description'
  import Visualizations from "../components/Visualizations";

  export default {
    name: 'HomePage',

    components: {
      Visualizations,
      Description,
    }
  }
</script>
