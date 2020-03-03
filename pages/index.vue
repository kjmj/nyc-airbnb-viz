<template>
  <div>
    <section class="section" id="description">
      <description></description>
    </section>
    <section class="section" id="sampleViz">
      <sample-viz></sample-viz>
    </section>
    <div style="height: 1000px"></div>
  </div>
</template>

<script>
import Description from '~/components/Description'
import SampleViz from '~/components/SampleViz'

export default {
  name: 'HomePage',

  components: {
    Description,
    SampleViz
  }
}
</script>
