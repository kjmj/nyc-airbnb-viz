<template>
  <div>
    <h2 class="title is-2">Map Viz</h2>
    <h3 class="subtitle">Here is a map showing the average airbnb price by neighborhood in NYC</h3>
    <div id="sampleViz"></div>
  </div>
</template>

<script>
  import * as d3 from 'd3'

  export default {
    name: "Map",
    props: {
      neighborhoodsPromise: Promise,
      priceByNeighbourhoodPromise: Promise,
    },
    mounted() {
      let vm = this

      var height = 600
      var width = 900

      // draw a quick svg for show
      var svg = d3
        .select('#sampleViz')
        .append('svg')
        .attr('height', 600)
        .attr('width', 900)

      // use a map to store our data
      var data = d3.map();

      // tooltip that will show when mouse hovers over a neighborhood
      var tooltip = d3
        .select('body')
        .append('div')
        .style('position', 'absolute')
        .style('z-index', '10')
        .style('visibility', 'hidden')
        .style('background-color', 'white')
        .style('border', 'solid')
        .style('border-width', '2px')
        .style('border-radius', '5px')
        .style('padding', '5px')


      // wait for data to load and create a map
      Promise.all([vm.neighborhoodsPromise, vm.priceByNeighbourhoodPromise]).then(
        ([neighborhoods, priceByNeighbourhood]) => {

          // we want to map neighborhood to avg price
          priceByNeighbourhood.forEach(function (d) {
            data.set(d.neighbourhood, +d.avgPrice)
          })

          // a bunch of color scales i am testing
          var maxVal = Math.max(...data.values())
          var color_scale1 = d3.scaleLinear().domain([0, maxVal]).range(['#40ff46', '#ff4640']);
          var color_scale2 = d3.scaleLinear().domain([0, maxVal]).range(['#4099FF', '#ff4640']);
          var color_scale3 = d3.scaleQuantile().domain(data.values()).range(['#8dc2ff', '#4099ff', '#0071f3']);
          var color_scale4 = d3.scaleQuantile().domain(data.values()).range(['#40ffa6', '#4099ff', '#ffa640', '#ff4099']);
          var color_scale5 = d3.scaleQuantile().domain([0, maxVal]).range(['#40ff46', '#4640ff', '#ff4640']);
          var color_scale6 = d3.scaleQuantile().domain([0, maxVal]).range(['#c9e2ff', '#54a3ff', '#057aff', '#004ca2', '#001e40']);
          var color_scale7 = d3.scaleQuantile().domain([0, maxVal]).range(['#4099ff', '#c685ee', '#ff74b8', '#ff8177', '#ffa640']);
          var color_scale8 = d3.scaleQuantile().domain([0, maxVal]).range(['#4099ff', '#ff74b8', '#ffa640']);
          var color_scale9 = d3.scaleQuantile().domain([0, maxVal]).range(['#4099ff', '#e27edf', '#ff798c', '#ffa640']);

          // fit map to nyc
          var path = d3.geoPath()
            .projection(d3.geoConicConformal()
              .parallels([33, 45])
              .rotate([96, -39])
              .fitSize([width, height], neighborhoods));

          // draw map
          svg.selectAll("path")
            .data(neighborhoods.features)
            .enter()
            .append("path")
            .attr("d", path)
            .style('stroke', '#D3D3D3')
            .attr("fill", function (d) {
              d.total = data.get(d.properties.neighborhood) || 'No data';
              return d.total == 'No data' ? 'white' : color_scale6(d.total);
            })
            .on('mouseover', function (d) {
              tooltip.style('visibility', 'visible')

              d3.select(this)
                .style('stroke', 'black')
            })
            .on('mousemove', function(d) {
              tooltip
                .html(
                  'Borough: ' +
                  d.properties.borough +
                  '<br>' +
                  'Neighborhood: ' +
                  d.properties.neighborhood +
                  '<br>' +
                  'Average price: $' +
                  d.total.toFixed(2)
                )
                .style('top', event.pageY - 10 + 'px')
                .style('left', event.pageX + 10 + 'px')

            })
            .on('mouseout', function (d) {
              tooltip.style('visibility', 'hidden')

              d3.select(this)
                .style('stroke', 'none')
            })
        }
      )

    }
  }
</script>

<style scoped>

</style>
