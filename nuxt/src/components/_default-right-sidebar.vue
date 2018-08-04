<script lang="ts">
import SidebarRightComponent from './_sidebar-right.vue';
import { staticUrl } from '../../globals';

import Vue from 'vue';
import Component from 'nuxt-class-component';
import { Prop } from 'vue-property-decorator';
import axios from 'axios';

@Component({
  components: {
    SidebarRightComponent,
  },
})
export default class extends Vue{
  @Prop({default: []}) users: Array<{}>;
  private qod: string = '';
  private qodImageUrl: string = '';
  private qodAuthor: string = '';
  private staticUrl: string = staticUrl;

  private getQod() {
    axios.get('https://quotes.rest/qod.json?category=inspire').then((response: any) => {
      this.qod = response.data.contents.quotes[0].quote;
      this.qodImageUrl = response.data.contents.quotes[0].background;
      this.qodAuthor = response.data.contents.quotes[0].author;
    }).catch(() => {
      this.qod = 'The bigger the challenges in life, the bigger the reward!';
      this.qodImageUrl = staticUrl + '/img/inspire.png';
      this.qodAuthor = 'Myself';
    });
  }

  private mounted() {
    this.getQod();
  }
}
</script>
<template lang="haml">
%div
  %h2.white--text.ml-1.mt-4.mb-1.font-weight-thin Info
  %sidebar-right-component
    %div{"slot": "card-media"}
      %v-card-media{":src": 'staticUrl + "/img/about-alt.jpg"', "height": "200px"}
    %div{"slot": "card-title"} About
    %div{"slot": "card-body"}
      %br
      %h4 Ola, this is Priyank,
      %br
      %h4 Currently, a Full Stack Web Developer at a startup.
      %h4 I will be microblogging mostly about tech related to Application Engineering and also pen down my thoughts as a stringent Cancerian.
      %br
      %h4 Free time: Playing Chess, Football and enjoy swinging my hands on the guitar.
      %br
      %h4 Current Musings: Learning Spanish
      %br
  %sidebar-right-component.hidden
    %div{"slot": "card-title"} Contributors
    %div{"slot": "card-body"}
      %template{"v-for": 'user in users'}
        %br
        %h4 {{user.node.firstName}} {{user.node.lastName}}
  %sidebar-right-component
    %div{"slot": "card-title"} Last Meetup Hosted
    %div{"slot": "card-body"}
      %br
      %h4 VueJS Meetup 05 March 2018
      %br
      %h5
        = 'Intro to VueJS at '
        %a.custom-text-third{'href': 'http://beautifulcode.co', 'target': "_blank"} beautifulcode.co
  %sidebar-right-component
    %div{"slot": "card-title"} Next Meetup
    %div{"slot": "card-body"}
      %br
      %h4 TBD
      %br
      %h5
        = 'Email me at'
        %a.custom-text-third{'href': 'mailto:pulumati.priyank@gmail.com'} pulumati.priyank@gmail.com
        = ' for any ideas'
  %sidebar-right-component
    %div{"slot": "card-media"}
      %v-card-media{":src": 'qodImageUrl', "height": "200px"}
    %div{"slot": "card-title"} Quote of the day
    %div{"slot": "card-body"}
      %br
      %h4 {{qod}}
      %br
      %h4.text-xs-right - {{qodAuthor}}
</template>
