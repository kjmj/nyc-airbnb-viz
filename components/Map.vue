<template>
  <div>
    <h2 class="title is-2">Map Viz</h2>
    <h3 class="subtitle">Here is a map showing the average airbnb price by neighborhood in NYC</h3>
    <div id="mapViz"></div>
  </div>
</template>

<script>
  import * as d3 from 'd3'

  export default {
    name: "Map",
    props: {
      neighborhoodsPromise: Promise,
      priceByNeighbourhoodPromise: Promise,
      tooltip: Object
    },
    mounted() {
      let vm = this

      var height = 600
      var width = 900

      // draw a quick svg for show
      var svg = d3
        .select('#mapViz')
        .append('svg')
        .attr('height', 600)
        .attr('width', 900)

      // use a map to store our data
      var data = d3.map();

      // tooltip that will show when mouse hovers over a neighborhood


      // wait for data to load and create a map
      Promise.all([vm.neighborhoodsPromise, vm.priceByNeighbourhoodPromise]).then(
        ([neighborhoods, priceByNeighbourhood]) => {

          // we want to map neighborhood to avg price
          priceByNeighbourhood.forEach(function (d) {
            data.set(d.neighbourhood, +d.avgPrice)
          })

          // a bunch of color scales i am testing
          var minVal = Math.min(...data.values())
          var maxVal = Math.max(...data.values())
          var color_scale1 = d3.scaleLinear().domain([minVal, maxVal]).range(['#40ff46', '#ff4640']);
          var color_scale2 = d3.scaleLinear().domain([minVal, maxVal]).range(['#4099FF', '#ff4640']);
          var color_scale3 = d3.scaleQuantile().domain(data.values()).range(['#8dc2ff', '#4099ff', '#0071f3']);
          var color_scale4 = d3.scaleQuantile().domain(data.values()).range(['#40ffa6', '#4099ff', '#ffa640', '#ff4099']);
          var color_scale5 = d3.scaleQuantile().domain([minVal, maxVal]).range(['#40ff46', '#4640ff', '#ff4640']);
          var color_scale6 = d3.scaleQuantile().domain([minVal, maxVal]).range(['#c9e2ff', '#54a3ff', '#057aff', '#004ca2', '#001e40']);
          console.log(color_scale6)
          var color_scale7 = d3.scaleQuantile().domain([minVal, maxVal]).range(['#4099ff', '#c685ee', '#ff74b8', '#ff8177', '#ffa640']);
          var color_scale8 = d3.scaleQuantile().domain([minVal, maxVal]).range(['#4099ff', '#ff74b8', '#ffa640']);
          var color_scale9 = d3.scaleQuantile().domain([minVal, maxVal]).range(['#4099ff', '#e27edf', '#ff798c', '#ffa640']);

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
              vm.tooltip.style('visibility', 'visible')

              d3.select(this)
                .style('stroke', 'black')
            })
            .on('mousemove', function (d) {
              var total = d.total == 'No data' ? 'No data' : d.total.toFixed(2)

              vm.tooltip
                .html(
                  'Borough: ' +
                  d.properties.borough +
                  '<br>' +
                  'Neighborhood: ' +
                  d.properties.neighborhood +
                  '<br>' +
                  'Average price: $' +
                  total
                )
                .style('top', event.pageY - 10 + 'px')
                .style('left', event.pageX + 10 + 'px')

            })
            .on('mouseout', function (d) {
              vm.tooltip.style('visibility', 'hidden')

              d3.select(this)
                .style('stroke', 'none')
            })


          // this will contain information when building our legend
          var legendKeys = []

          // my attempt at using our color scale to create different ranges for the legend
          color_scale6.quantiles().forEach(function (item, index) {
            var curr = item
            var next = null

            if (index < color_scale6.quantiles().length - 1) {
              next = color_scale6.quantiles()[index + 1]
            }

            if (index == 0) {
              legendKeys.push({
                color: 'white',
                label: 'No data'
              })

              legendKeys.push({
                color: color_scale6((minVal + curr) / 2),
                label: '$' + minVal.toFixed(2) + '-' + '$' + curr.toFixed(2)
              })

              legendKeys.push({
                color: color_scale6((curr + next) / 2),
                label: '$' + curr.toFixed(2) + '-' + '$' + next.toFixed(2)
              })
            } else if (index == color_scale6.quantiles().length - 1) {
              legendKeys.push({
                color: color_scale6((curr + maxVal) / 2),
                label: '$' + curr.toFixed(2) + '-' + '$' + maxVal.toFixed(2)
              })
            } else {
              legendKeys.push({
                color: color_scale6((curr + next) / 2),
                label: '$' + curr.toFixed(2) + '-' + '$' + next.toFixed(2)
              })
            }
          });

          // Add one dot in the legend for each name.
          svg.selectAll("mydots")
            .data(legendKeys)
            .enter()
            .append("circle")
            .attr("cx", 100)
            .attr("cy", function (d, i) {
              return 100 + i * 25
            }) // 100 is where the first dot appears. 25 is the distance between dots
            .attr("r", 7)
            .style("fill", function (d) {
              return d.color
            })
            .style('stroke', 'black')

          // Add one dot in the legend for each name.
          svg.selectAll("mylabels")
            .data(legendKeys)
            .enter()
            .append("text")
            .attr("x", 120)
            .attr("y", function (d, i) {
              return 100 + i * 25
            }) // 100 is where the first dot appears. 25 is the distance between dots
            // .style("fill", function(d){
            //   return color_scale6(d.avg)})
            .text(function (d) {
              return d.label
            })
            .attr("text-anchor", "left")
            .style("alignment-baseline", "middle")
        }
      )

    }
  }
</script>

<style scoped>

</style>
