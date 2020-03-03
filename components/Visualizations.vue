<template>
  <div>
    <sample-viz :datasetPromise="datasetPromise"></sample-viz>
  </div>
</template>

<script>
  import SampleViz from "./SampleViz";
  import * as d3 from 'd3'

  export default {
    name: "Visualizations",
    components: {SampleViz},
    data() {
      return {
        datasetPromise: 'hello'
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
    }
  }
</script>

<style scoped>

</style>
