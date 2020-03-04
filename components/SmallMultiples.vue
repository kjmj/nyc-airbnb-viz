<template>
  <div>
    <h2 class="title is-2">Small Multiples</h2>
    <h3 class="subtitle">Small Multiples will go here</h3>
    <div id="smallMultiples"></div>
  </div>
</template>

<script>
  import * as d3 from 'd3'

  export default {
    name: "SmallMultiples",
    props: {
      smallMultiplesPromise: Promise,
      height: Number,
      width: Number
    },
    mounted() {
      let vm = this

      // load data, then draw graph
      vm.smallMultiplesPromise.then(function(data) {
        // data available here
        console.log(data)

        // set the dimensions and margins of the graph
        var margin = {top: 30, right: 0, bottom: 30, left: 50},
            width = 300 - margin.left - margin.right,
            height = 900 - margin.top - margin.bottom;


          // group the data: I want to draw one line per group
          var sumstat = d3.nest() // nest function allows to group the calculation per level of a factor
            .key(function(d) { return d.Landmark;})
            .entries(data);

          // What is the list of groups?
          allKeys = sumstat.map(function(d){return d.key})

          // Add an svg element for each group. The will be one beside each other and will go on the next row when no more room available
          var svg = d3.select("#my_dataviz")
            .selectAll("uniqueChart")
            .data(sumstat)
            .enter()
            .append("svg")
              .attr("width", width + margin.left + margin.right)
              .attr("height", height + margin.top + margin.bottom)
            .append("g")
              .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");

          // Add X axis --> it is a date format
          var x = d3.scaleLinear()
            .domain(d3.extent(data, function(d) { return d.Distance; }))
            .range([ 0, width ]);
          svg
            .append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x).ticks(3));

          //Add Y axis
          var y = d3.scaleLinear()
            .domain([0, d3.max(data, function(d) { return +d.price; })])
            .range([ height, 0 ]);
          svg.append("g")
            .call(d3.axisLeft(y).ticks(5));

          // color palette
          var color = d3.scaleOrdinal()
            .domain(allKeys)
            .range(['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#ffff33','#a65628','#f781bf','#999999'])

          // Draw the line
          svg
            .append("path")
              .attr("fill", "none")
              .attr("stroke", function(d){ return color(d.key) })
              .attr("stroke-width", 1.9)
              .attr("d", function(d){
                return d3.line()
                  .x(function(d) { return x(d.Distance); })
                  .y(function(d) { return y(+d.price); })
                  (d.values)
              })

          // Add titles
          svg
            .append("text")
            .attr("text-anchor", "start")
            .attr("y", -5)
            .attr("x", 0)
            .text(function(d){ return(d.key)})
            .style("fill", function(d){ return color(d.key) })
      })
    }
  }
</script>

<style scoped>

</style>
