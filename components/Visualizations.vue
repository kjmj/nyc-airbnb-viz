<template>
  <div>
    <sample-viz :datasetPromise="datasetPromise" :height="height" :width="width"></sample-viz>
    <section class="section">
      <small-multiples :smallMultiplesPromise="smallMultiplesPromise" :height="height" :width="width"></small-multiples>
    </section>
  </div>
</template>

<script>
  import SampleViz from "./SampleViz";
  import SmallMultiples from "./SmallMultiples"
  import * as d3 from 'd3'

  export default {
    name: "Visualizations",
    components: {SampleViz, SmallMultiples},
    data() {
      return {
        datasetPromise: null,
        height: 900,
        width: 600
      }
    },
    created() {
      // load in our dataset
      this.datasetPromise = new Promise(function (resolve, reject) {
        d3.csv('AB_NYC_2019.csv')
          .then(function (data) {
            resolve(data)
          })
          .catch(function (e) {
            reject(Error(e))
          })
      })

      this.smallMultiplesPromise = new Promise(function (resolve, reject) {
        d3.csv('AB_NYC_2019_calculated_smallMultiples.csv')
          .then(function (data) {
            resolve(data)
          })
          .catch(function (e) {
            reject(Error(e))
          })
      })
    }
  }
</script>

<style scoped>

</style>
