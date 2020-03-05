<template>
  <div>
    <h2 class="title is-2">Some expensive places...</h2>
    <h3 class="subtitle">We hand picked some expensive places in NYC</h3>
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
            title: 'Luxury 1 bedroom apt. -stunning Manhattan views',
            link: 'https://www.airbnb.com/rooms/13894339?source_impression_id=p3_1583297353_H%2F4qsqKVYqY2qB2k',
            image: 'https://a0.muscache.com/im/pictures/4938ff43-2416-48bd-b4c6-3c38f4115fb4.jpg?aki_policy=xx_large',
            borough: 'Brooklyn',
            neighborhood: 'Greenpoint',
            price: '$10000 / night'
          },
          {
            title: '1-BR Lincoln Center',
            link: 'https://www.airbnb.com/rooms/22436899?source_impression_id=p3_1583297398_lBhjvGDuV5nkwy0v',
            image: 'https://a0.muscache.com/im/pictures/e3571de1-a97b-447e-9ada-6b83eddb8700.jpg?aki_policy=xx_large',
            borough: 'Manhattan',
            neighborhood: 'Upper West Side',
            price: '$10000 / night'
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
            title: '2br - The Heart of NYC: Manhattans Lower East Side',
            link: 'https://www.airbnb.com/rooms/31340283?source_impression_id=p3_1583297490_HBgNLABgp%2B3I6fI%2B',
            image: 'https://a0.muscache.com/im/pictures/643f3d26-61a6-4d7a-9c08-4647c9674a09.jpg?aki_policy=xx_large',
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
