<template>
  <div class="column">
    <div class="card">
      <header class="card-header">
      </header>

      <div class="card-content columns">
        <div class="column is-narrow">
          <img :src="image" style="width: 256px; display: block">
        </div>

        <div class="column">
          <p class="title is-4">
            <a
              :href="link"
              target="_blank"
            >{{title}}</a
            >
          </p>
          <p class="title is-6">{{neighborhood}}, {{borough}}</p>
          <p class="subtitle is-6">{{price}}</p>
        </div>
      </div>

      <footer clas="card-footer"></footer>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      title: {
        type: String,
        required: true
      },
      link: {
        type: String,
        required: true
      },
      image: {
        type: String,
        required: true
      },
      borough: {
        type: String,
        required: true
      },
      neighborhood: {
        type: String,
        required: true
      },
      price: {
        type: String,
        required: true
      }
    }
  }
</script>
