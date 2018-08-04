const express = require('express');
const {Nuxt} = require('nuxt');
const path = require('path');
const awsServerlessExpressMiddleware = require('aws-serverless-express/middleware');

const app = express();

app.use(awsServerlessExpressMiddleware.eventContext());

app.use('/_nuxt', express.static(path.join(__dirname, '.nuxt', 'dist')));

let config = require('./nuxt.config.js');
const nuxt = new Nuxt(config);
app.use(nuxt.render);


module.exports = app;
