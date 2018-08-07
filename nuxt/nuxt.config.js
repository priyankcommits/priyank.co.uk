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
      { hid: 'description', name: 'description', content: 'Nuxt.js project' },
      {content: "IE=edge", "http-equiv": "X-UA-Compatible"},
      {content: "width=device-width, initial-scale=1", "name": "viewport"},
      {content: "https://priyank.co.uk", "name": "application-name"},
      {content: "Priyank Pulumati", "name": "author"},
      {content: "https://priyank.co.uk", "name": "distributor"},
      {content: "share alike", "name": "copyright"},
      {content: "All", "name": "robots"},
      {content: "Priyank.co.uk is a micro blogging website about application engineering, web apps, mobile app and also sometimes about life :)", "name": "description"},
      {content: "web,apps,javascript,python,mobile,tech,tech life,life,cancer,evanascence,blog,micro", "name": "keywords"},
      {content: "General", "name": "rating"},
      {content: "Priyank.co.uk", "name": "dcterms.title"},
      {content: "Priyank Pulumati", "name": "dcterms.contributor"},
      {content: "Priyank Pulumati", "name": "dcterms.creator"},
      {content: "Priyank Pulumati", "name": "dcterms.publisher"},
      {content: "Priyank.co.uk is a micro blogging website about application engineering, web apps, mobile app and also sometimes about life :)", "name": "dcterms.description"},
      {content: "priyank.co.yk", "name": "dcterms.rights"},
      {content: "website", "property": "og:type"},
      {content: "priyank.co.yk", "property": "og:title"},
      {content: "Priyank.co.uk is a micro blogging website about application engineering, web apps, mobile app and also sometimes about life :)", "property": "og:description"},
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/img/favicon.png' },
      { href: "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css", rel: "stylesheet", integrity: "sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN", crossorigin: "anonymous" },
    ],
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#44B5DC' },
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