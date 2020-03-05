<template>
  <div>
    <h2 class="title is-2">Some expensive airbnb's</h2>
    <p class="subtitle">We did a bit of searching to find some expensive airbnb's in the city. They say NYC has it all -
      and we agree. You can rent a boat, book a huge home on a film location, or even hit the hay in a 1 bedroom
      apartment in chinatown for a reasonable $9,999 / night</p>
    <div style="max-width: 800px">
      <b-carousel
        class="column"
        :autoplay="false"
        :indicator="indicator"
        :indicator-background="indicatorBackground"
        :indicator-inside="indicatorInside"
        :indicator-mode="indicatorMode"
        :indicator-position="indicatorPosition"
        :indicator-style="indicatorStyle">
        <b-carousel-item v-for="(carousel, i) in carousels" :key="i">
          <card :title="carousel.title" :link="carousel.link" :image="carousel.image" :borough="carousel.borough"
                :neighborhood="carousel.neighborhood" :price="carousel.price">
          </card>
        </b-carousel-item>
      </b-carousel>
    </div>
  </div>
</template>

<script>
  import Card from './Card'

  export default {
    name: "Carousel",
    data() {
      return {
        autoplay: false,
        indicator: true,
        indicatorBackground: true,
        indicatorInside: true,
        indicatorMode: 'click',
        indicatorPosition: 'is-bottom',
        indicatorStyle: 'is-dots',
        carousels: [
          {
            title: 'Greenwich Village Townhome with Private Garden!',
            link: 'https://www.airbnb.com/rooms/20692563?source_impression_id=p3_1583387651_iq%2FaHQq8pMMRjMyc',
            image: 'https://a0.muscache.com/im/pictures/5d3b16c4-5de6-439c-bceb-a0fafe3411cf.jpg?aki_policy=x_large',
            borough: 'Manhattan',
            neighborhood: 'Greenwich Village',
            price: '$1000 / night'
          },
          {
            title: 'West Chelsea Studios - Penthouse 12',
            link: 'https://www.airbnb.com/rooms/18071399?source_impression_id=p3_1583387936_WA4pxUakiyBP9OH4',
            image: 'https://a0.muscache.com/im/pictures/dfa06cca-d8b1-4dd0-9816-e4dd129ae3ef.jpg?aki_policy=xx_large',
            borough: 'Manhattan',
            neighborhood: 'Chelsea',
            price: '$2800 / night'
          },
          {
            title: '70 Luxury MotorYacht on the Hudson',
            link: 'https://www.airbnb.com/rooms/33007610?source_impression_id=p3_1583387311_GSQaQzx47UFNzQAm',
            image: 'https://a0.muscache.com/im/pictures/84830680/93103707_original.jpg?aki_policy=xx_large',
            borough: 'Manhattan',
            neighborhood: 'Battery Park City',
            price: '$6500 / night'
          },
          {
            title: 'Quiet, Clean, Lit @ LES & Chinatown',
            link: 'https://www.airbnb.com/rooms/9528920?source_impression_id=p3_1583297472_bCFqu%2BAlJNg9Wjuo',
            image: 'https://a0.muscache.com/im/pictures/fb030ec8-4e8f-4243-8cbe-99a89b226878.jpg?aki_policy=xx_large',
            borough: 'Manhattan',
            neighborhood: 'Lower East Side',
            price: '$9999 / night'
          },
          {
            title: 'Film Location',
            link: 'https://www.airbnb.com/rooms/2953058?source_impression_id=p3_1583297523_pHzrzMLoXIaeZAyF',
            image: 'https://a0.muscache.com/im/pictures/46691333/a6d03b8a_original.jpg?aki_policy=xx_large',
            borough: 'Brooklyn',
            neighborhood: 'Clinton Hill',
            price: '$8000 / night'
          },
        ]
      }
    },
    components: {
      Card
    }
  }
</script>

<style scoped>

</style>
