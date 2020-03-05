<template>
  <div>
    <h2 class="title is-2">Description</h2>
    <p class="subtitle">New York is one of the coolest cities in the world (sorry, LA). We found a cool dataset on
      Kaggle with
      airbnb listings from all over NYC. After looking through the dataset, we wanted to answer three main
      questions.</p>
    <div class="content">
      <ol type="1">
        <li>What are some of the most expensive airbnb listings in NYC?</li>
        <li>Do airbnb's get cheaper as you get further from popular landmarks?</li>
        <li>Which neighborhoods have the most expensive airbnbs?</li>
      </ol>
    </div>
    <p class="subtitle">The data was pretty clean straight from Kaggle. We did some preprocessing to get the data into a
      format
      that was usable with d3.js. After the data was good and organized, we put our heads down and started to create
      some visualizations in d3.js. We were able to create a small multiples graph, which depicts airbnb prices by
      distance from popular landmarks. We also created an interactive map which shows airbnb prices by neighborhood.
      Check out our gallery below for a fun exploration of the most expensive airbnb's in the city. Some really aren't
      worth it</p>
  </div>
</template>

<script>
  export default {
    name: "Description"
  }
</script>

<style scoped>

</style>
