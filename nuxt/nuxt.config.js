module.exports = {
  env: {
    baseUrl: '',
    ENVIRONMENT: process.env.ENVIRONMENT || '',
  },
  head: {
    title: 'Priyank\'s Humble Adobe',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Nuxt.js project' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/img/favicon.png' },
      { href: "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css", rel: "stylesheet", integrity: "sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN", crossorigin: "anonymous" },
    ],
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#3B8070' },
  /*
  ** Build configuration
  */
  css: ['./assets/css/main.css'],
  build: {
    vendor: ['vuex-class', 'nuxt-class-component', 'vue-cookies']
  },
  plugins: [
    {src: './plugins/vuetify'},
    {src: './plugins/ga', ssr: false},
  ],
  modules: ['./modules/typescript', '@nuxtjs/axios'],
  router: {
    base: '/',
  },
  axios: {},
  srcDir: 'src/',
  performance: {
    gzip: false
  },
  dev: false,
};