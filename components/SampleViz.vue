<template>
  <div>
    <h2 class="title is-2">Sample Viz</h2>
    <h3 class="subtitle">Sample Viz will go here</h3>
  </div>
</template>

<script>
  export default {
    name: "SampleViz",
    props: {
      datasetPromise: Promise
    },
    mounted() {
      let vm = this

      vm.datasetPromise.then(function(data) {
        console.log(data)
      })

    }
  }
</script>

<style scoped>

</style>
