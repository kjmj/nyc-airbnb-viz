<template>
  <div>
    <!--    <sample-viz :datasetPromise="datasetPromise" :height="height" :width="width"></sample-viz>-->
    <section class="section" id="carousel">
      <carousel></carousel>
    </section>
    <section class="section">
      <small-multiples :smallMultiplesPromise="smallMultiplesPromise" :height="height" :width="width" :tooltip="tooltip"></small-multiples>
    </section>
    <section class="section" id='map'>
      <Map :neighborhoods-promise="neighborhoodsPromise"
           :price-by-neighbourhood-promise="priceByNeighbourhoodPromise"
      :tooltip="tooltip"></Map>
    </section>
  </div>
</template>

<script>
  import SampleViz from "./SampleViz";
  import SmallMultiples from "./SmallMultiples"
  import Map from "./Map";
  import * as d3 from 'd3'
  import Carousel from "./Carousel";

  export default {
    name: "Visualizations",
    components: {Carousel, Map, SampleViz, SmallMultiples},
    data() {
      return {
        datasetPromise: null,
        smallMultiplesPromise: null,
        neighborhoodsPromise: null,
        priceByNeighbourhoodPromise: null,
        height: 900,
        width: 600,
        tooltip: d3
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

      this.neighborhoodsPromise = new Promise(function (resolve, reject) {
        d3.json('nyc_neighborhoods.geojson')
          .then(function (data) {
            resolve(data)
          })
          .catch(function (e) {
            reject(Error(e))
          })
      })

      this.priceByNeighbourhoodPromise = new Promise(function (resolve, reject) {
        d3.csv('priceByNeighbourhood.csv')
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
