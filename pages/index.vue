<template>
  <div>
    <section class="section" id="description">
      <div class="container">
        <description></description>
      </div>
    </section>
    <client-only>
      <visualizations></visualizations>
    </client-only>
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
