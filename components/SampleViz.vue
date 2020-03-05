<template>
  <div>
    <h2 class="title is-2">Sample Viz</h2>
    <h3 class="subtitle">Sample Viz will go here</h3>
    <div id="sampleViz"></div>
  </div>
</template>

<script>
  import * as d3 from 'd3'

  export default {
    name: "SampleViz",
    props: {
      datasetPromise: Promise,
      height: Number,
      width: Number
    },
    mounted() {
      let vm = this

      // load data, then draw graph
      vm.datasetPromise.then(function (data) {
        // data available here
        console.log(data)

        var height = vm.height
        var width = vm.width

        // draw a quick svg for show
        var svg = d3
          .select('#sampleViz')
          .append('svg')
          .attr('height', height)
          .attr('width', width)

        svg.append("rect")
          .attr("width", "100%")
          .attr("height", "100%")
          .attr("fill", "#4099FF");
      })
    }
  }
</script>

<style scoped>

</style>
