<template>
  <div>
    <h2 class="title is-2">Comparing Average Price to Distance from Popular Landmarks</h2>
    <p class="subtitle"> When you go to a specific area, you usually want to be closer to the places you want to visit.
      Unless you like driving I guess. Below you will see an array of line charts depicting the average price of an
      airbnb compared to how far that listing (in miles) is from a landmark. In this case we chose 9 different locations
      to preform our calculation on.</p>
    <p class="subtitle">We have found that airbnb average prices generally decrease as you move further away from
      landmarks. However, the further you get, the less options you have. If you look at any of the lines graphs below,
      you will see some sudden spikes, especially the further away you are. These are cause by there only being a
      couple of listing at this distance, causing the average price to fluctuate quite a bit. Please note that most of
      the landmarks we chose were in Manhattan, which is the most expensive borough. One aspect we are totally sure
      about is if prices go down because you're leaving manhattan, or if they really are just more expensive near the
      landmarks.</p>
    <div id="smallMultiplesViz"></div>
  </div>
</template>

<style> /* set the CSS */

.grid line {
  stroke: lightgrey;
  stroke-opacity: 0.7;
  shape-rendering: crispEdges;
}

.grid path {
  stroke-width: 0;
}

</style>

<script>
  import * as d3 from 'd3'

  export default {
    name: "SmallMultiples",
    props: {
      smallMultiplesPromise: Promise,
      tooltip: Object
    },
    mounted() {
      let vm = this

      // load data, then draw graph
      vm.smallMultiplesPromise.then(function (data) {

        var margin = {top: 30, right: 0, bottom: 30, left: 50},
          width = 900 - margin.left - margin.right,
          height = 300 - margin.top - margin.bottom;
        var temp = 0

        // group the data: I want to draw one line per group
        var sumstat = d3.nest() // nest function allows to group the calculation per level of a factor
          .key(function (d) {
            return d.Landmark;
          })
          .entries(data);

        // What is the list of groups?
        var allKeys = sumstat.map(function (d) {
          return d.key
        })

        // Add an svg element for each group. The will be one beside each other and will go on the next row when no more room available
        var svg = d3.select("#smallMultiplesViz")
          .selectAll("uniqueChart")
          .data(sumstat)
          .enter()
          .append("svg")
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
          .append("g")
          .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


        // Add X axis
        var x = d3.scaleLinear()
          .domain([0, 15])
          .range([0, width]);

        svg.append("g")
          .attr("transform", "translate(" + temp + "," + height + ")")
          .call(d3.axisBottom(x).ticks(8));


        // Add X axis label:
        svg.append("text")
          .attr("text-anchor", "start")
          .attr("x", width / 2)
          .attr("y", height + margin.top)
          .text("Distance (miles)");

        //Add Y axis
        var y = d3.scaleLinear()
          .domain([0, 650])
          .range([height, 0]);

        // Y axis label:
        svg.append("text")
          .attr("text-anchor", "end")
          .attr("transform", "rotate(-90)")
          .attr("y", -margin.left + 15)
          .attr("x", -margin.top - 30)
          .text("Average Price")

        svg.append("g")
          .call(d3.axisLeft(y).ticks(5));

        var xscale = x;
        var yscale = y;

        svg.append("g")
          .attr("class", "grid")
          .call(
            d3.axisLeft(y)
              .tickSize(-width)
              .tickFormat("")
          );

        // color palette
        var color = d3.scaleOrdinal()
          .domain(allKeys)
          .range(['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', 'black', '#a65628', '#f781bf', '#999999'])

        // Draw the line
        svg
          .append("path")
          .attr("fill", "none")
          .attr("stroke", function (d) {
            return color(d.key)
          })
          .attr("stroke-width", 1.9)
          .attr("d", function (d) {
            return d3.line()
              .x(function (d) {
                return x(d.RoundedDistance);
              })
              .y(function (d) {
                return y(d.Average);
              })
              (d.values)
          })
          .on('mouseover', function (d) {
            vm.tooltip.style('visibility', 'visible')
          })
          .on('mousemove', function (d) {

            vm.tooltip
              .html(
                'Distance (Miles): ' +
                (xscale.invert(d3.mouse(this)[0])).toFixed(2) +
                '<br>' +
                'Average Price: $' +
                ((yscale.invert(d3.mouse(this)[1] - 10)) - 30).toFixed(2)
              )
              .style('top', event.pageY - 10 + 'px')
              .style('left', event.pageX + 10 + 'px')

          })
          .on('mouseout', function (d) {
            vm.tooltip.style('visibility', 'hidden')
          })

        // Add titles
        svg
          .append("text")
          .attr("text-anchor", "start")
          .attr("y", -5)
          .attr("x", 0)
          .text(function (d) {
            return (d.key)
          })
          .style("fill", function (d) {
            return color(d.key)
          })
      })
    }
  }
</script>


<style scoped>


</style>
