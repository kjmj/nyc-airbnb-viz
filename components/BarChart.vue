<template>
  <div>
    <h2 class="title is-2">Price by Borough - A Quick Overview</h2>
    <p class="subtitle">Before we jump into the specific neighborhoods, lets try to understand the most expensive
      boroughs. Taking a look at the graph, we can see that Manhattan is definitely the most expensive borough. The
      other four are reasonably close to each other.</p>
    <div id="barViz"></div>
  </div>
</template>

<script>
  import * as d3 from 'd3'

  export default {
    name: "Bar",
    props: {
      priceByBoroughPromise: Promise,
      tooltip: Object
    },
    mounted() {
      let vm = this

      var margin = {top: 30, right: 30, bottom: 70, left: 60},
        width = 600 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

      // draw a quick svg for show
      var svg = d3
        .select('#barViz')
        .append('svg')
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");


      // wait for data to load and create a bar chart
      vm.priceByBoroughPromise.then(function (data) {

          // sort data
          data.sort(function (b, a) {
            return a.avgPrice - b.avgPrice;
          });

          // X axis
          var x = d3.scaleBand()
            .range([0, width])
            .domain(data.map(function (d) {
              return d.neighbourhood_group;
            }))
            .padding(0.2);
          svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x))
            .selectAll("text")
            .attr("transform", "translate(17,0)rotate(0)")
            .style("text-anchor", "end");

        // Add X axis label:
        svg.append("text")
          .attr("text-anchor", "start")
          .attr("x", width / 2)
          .attr("y", height + margin.top + 5)
          .text("Borough");

          // Add Y axis
          var y = d3.scaleLinear()
            .domain([0, 225])
            .range([height, 0]);
          svg.append("g")
            .call(d3.axisLeft(y));

          // Y axis label:
          svg.append("text")
            .attr("text-anchor", "end")
            .attr("transform", "rotate(-90)")
            .attr("y", -margin.left + 20)
            .attr("x", -margin.top - 60)
            .text("Average Price")

          // Bars
          svg.selectAll("mybar")
            .data(data)
            .enter()
            .append("rect")
            .attr("x", function (d) {
              return x(d.neighbourhood_group);
            })
            .attr("y", function (d) {
              return y(d.avgPrice);
            })
            .attr("width", x.bandwidth())
            .attr("height", function (d) {
              return height - y(d.avgPrice);
            })
            .attr("fill", "#4099FF")
            .on('mouseover', function (d) {
              vm.tooltip.style('visibility', 'visible')

              d3.select(this)
                .style('stroke', 'black')
            })
            .on('mousemove', function (d) {
              // var avg = (parseFloat(d.avgPrice)).toFixed(2)
              vm.tooltip
                .html(
                  'Borough: ' +
                  d.neighbourhood_group +
                  '<br>' +
                  'Average price: $' +
                  parseFloat(d.avgPrice).toFixed(2)
                )
                .style('top', event.pageY - 10 + 'px')
                .style('left', event.pageX + 10 + 'px')

            })
            .on('mouseout', function (d) {
              vm.tooltip.style('visibility', 'hidden')

              d3.select(this)
                .style('stroke', 'none')
            })

          // Add title
          svg
            .append("text")
            .attr("text-anchor", "start")
            .attr("y", -10)
            .attr("x", 0)
            .text(function (d) {
              return ("Price by Borough")
            })
        }
      )

    }
  }
</script>

<style scoped>

</style>
