<script lang="ts">
import DefaultLeftSidebarComponent from '../components/_default-left-sidebar.vue';
import DefaultRightSidebarComponent from '../components/_default-right-sidebar.vue';
import CoverComponent from '../components/_cover.vue';
import { apiUrl } from '../../globals';

import Vue from 'vue';
import VueCookie from 'vue-cookie';
import Vuetify from 'vuetify';
import Component from 'nuxt-class-component';
import { State } from 'vuex-class';
import axios from 'axios';

Vue.use(Vuetify, {
  iconfont: 'fa4'
})
Vue.use(VueCookie);


@Component({
  components: {
    DefaultLeftSidebarComponent,
    DefaultRightSidebarComponent,
    CoverComponent,
  },
})
export default class extends Vue{
  @State articles;
  @State users;
  private subscriberEmail: string = '';
  private subscriberName: string = '';
  private alert: boolean = false;
  private alertMessage: string = '';

  private createSubscriber() {
    if (this.subscriberEmail !== '' && this.subscriberName !== '') {
      axios.post(apiUrl, {
        query: `mutation SubscribersCreate($input: SubscribersCreateInput!) {
                create(input: $input) {
                  create {
                    name, email
                  }
                }
              }`,
        variables: `{"input": {"subscriber": {"name": "${this.subscriberName}", "email": "${this.subscriberEmail}" }}}`,
      }).then(() => {
        this.alert = true;
        this.alertMessage = 'Subscribed !!';
        setTimeout(() => {
          this.alert = false;
        }, 5000);
      }).catch(() => {
        this.alert = true;
        this.alertMessage = 'Failed :(';
        setTimeout(() => {
          this.alert = false;
        }, 5000);
      });
    } else {
        this.alert = true;
        this.alertMessage = 'Name and Email are required.';
        setTimeout(() => {
          this.alert = false;
        }, 5000);
    }
  }

}
</script>
<template lang="haml">
%div
  %cover-component{"cover": false, ":coverHeight": 60}
  %v-content
    %v-container.grid-list-xs.fluid
      %v-layout.row.wrap.mt-1
        %v-flex.md3.hidden-xs-only
          %default-left-sidebar-component{":articles": 'articles'}
        %v-flex.xs12.md6
          %nuxt
        %v-flex.md3.hidden-xs-only
          %default-right-sidebar-component{":users": 'users'}
        %v-flex.xs12.hidden-sm-and-up
          %default-left-sidebar-component{":articles": 'articles'}
        %v-flex.xs12.hidden-sm-and-up
          %default-right-sidebar-component{":users": 'users'}
  %v-divider.white
  %v-footer.pa-3.custom-bg-first{"height": "auto", "width": '100%'}
    %v-layout.row.wrap.justify-center
      %v-flex.xs12.md6.text-xs-center
        %h4.mt-4.white--text
          = 'Copyright  Priyank Pulumati   © {{ new Date().getFullYear() }} built using'
          %a.strong.white--text{"href": 'https://vuejs.org/', "target": "_blank"} VueJS
          = ' and '
          %a.strong.white--text{"href": "https://vuetifyjs.com", "target": "_blank"} Vuetify
          = ' and '
          %a.strong.white--text{"href": 'https://nuxtjs.org/', "target": "_blank"} Nuxt
      %v-flex.xs12.md6.text-xs-center
        %v-text-field.d-inline-block.white--text.mt0.mr-2{"label": "Name", "color": "red", "v-model": 'subscriberName'}
        %v-text-field.d-inline-block.white--text.mt0{"label": "Email", "color": "red", "v-model": 'subscriberEmail'}
        %v-btn{"flat": true, "round": true, "color": "white", "v-on:click.native": 'createSubscriber' } Subscribe
    %v-flex.xs6.custom-alert{"v-if": 'alert'}
      %div.white--text {{alertMessage}}
</template>