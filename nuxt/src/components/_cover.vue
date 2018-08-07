<script lang="ts">
import SocialLinksComponent from './_social-links.vue';
import { staticUrl } from '../../globals';

import Vue from 'vue';
import Component from 'nuxt-class-component';
import { Prop } from 'vue-property-decorator';
import jquery from 'jquery';

@Component({
  components: {
    SocialLinksComponent,
  },
})
export default class extends Vue {
  @Prop({default: false}) cover: Boolean;
  @Prop({default: 0})  coverHeight: Number;
  private showCoverImage: boolean = true;
  private staticUrl: string = staticUrl;

  private mounted() {
    if (this.cover) {
      jquery(window).on('scroll', () => {
        if (jquery(window).scrollTop() > 200) {
          this.showCoverImage = false;
        } else {
          this.showCoverImage = true;
        }
      });
    }
  }
}
</script>
<template lang="haml">
%div{":style": '"margin-bottom:" + (coverHeight + 10) + "px;"'}
  %v-toolbar.hidden-xs-only.toolbar.white{"tabs": true, "dark": true, ":class": 'cover ? "opacity-cover" : ""'}
    %v-toolbar-side-icon
      %img.right.mr-3.profile-photo-toolbar.custom-bg-first{":src": 'staticUrl + "/img/favicon.png"'}
    %v-toolbar-title.font-weight-regular.custom-text-first Priyank Pulumati
    %v-spacer
    %social-links-component
    %v-tabs{"color": "white", "slot": "extension", "centered": true, "slider-color": "red"}
      %v-tab{"color": "blue", "v-on:click": '$store.commit("commitShowFilteredPosts", 0)'}
        %span.custom-text-first All
      %v-tab{"color": "blue", "v-on:click": '$store.commit("commitShowFilteredPosts", 1)'}
        %span.custom-text-first Tech - Bits and Bytes
      %v-tab{"color": "blue", "v-on:click": '$store.commit("commitShowFilteredPosts", 2)'}
        %span.custom-text-first Thoughts of an Evanascence
  %v-toolbar.hidden-sm-and-up.toolbar.white{"tabs": true, "dark": true, ":class": 'cover ? "opacity-cover" : ""'}
    %v-toolbar-side-icon
      %img.right.ml-1.profile-photo-toolbar.custom-bg-first{":src": 'staticUrl + "/img/favicon.png"'}
    %v-layout.row.wrap.mt-3.ml-2
      %v-flex.xs12
        %h2.custom-text-first.ml-2 Priyank Pulumati
      %v-flex.xs12.mb-1
        %social-links-component
    %v-tabs{"color": "white", "slot": "extension", "centered": true, "slider-color": "red"}
      %v-tab{"color": "blue", "v-on:click": '$store.commit("commitShowFilteredPosts", 0)'}
        %span.custom-text-first All
      %v-tab{"color": "blue", "v-on:click": '$store.commit("commitShowFilteredPosts", 1)'}
        %span.custom-text-first Tech - Bits and Bytes
      %v-tab{"color": "blue", "v-on:click": '$store.commit("commitShowFilteredPosts", 2)'}
        %span.custom-text-first Thoughts of an Evanascence
  %template{"v-if": 'cover'}
    %transition{"name": "fade"}
      %img.hidden-md-and-down.custom-bg-first.cover-photo{"v-if": 'showCoverImage', ":src": 'staticUrl + "/img/cover.jpg"', "style": "height: 300;"}
    %transition{"name": "fade"}
      %img.profile-photo{"v-if": 'showCoverImage', ":src": 'staticUrl + "/img/favicon.png"'}
</template>
<style>
.opacity-cover {
  opacity: 0.5;
}
.toolbar {
  position: fixed;
  top: 0;
  z-index: 300;
}
.cover-photo {
  position: absolute;
  top: 0;
  width: 100%;
  height: 450px;
  z-index: 100;
}
.profile-photo {
  position: absolute;
  top: 350px;
  left: 10%;
  width: 200px;
  height: 200px;
  z-index: 200;
  padding: 5px;
  border-radius: 50%;
}
.profile-photo-toolbar {
  width: 45px !important;
  height: 45px !important;
  border-radius: 50%;
}
</style>
