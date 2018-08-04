<script lang="ts">
import { apiUrl } from '../../globals';

import axios from 'axios';
import Vue from 'vue';
import VueCookies from 'vue-cookies';
import { State } from "vuex-class";
import Component from 'nuxt-class-component';

Vue.use(VueCookies as any);

@Component
export default class extends Vue {
  @State filteredPosts;
  previouslyLikedPostIds: String[] = [];

  public mounted() {
    const posts: any = VueCookies.get('posts') || '';
    this.$store.commit('commitUpvotePreviouslyLikedPosts', posts.split(","));
  }
  private upvote(postId: string) {
    axios.post(apiUrl, {
      query: `mutation PostUpdate($input: PostUpdateInput!) {
                update(input: $input) {
                update{
                  id
                }
              }
            }`,
      variables: `{"input": {"post": {"id": "${postId}" }}}`,
    }).then(() => {
      this.$store.commit("commitUpvotePost", postId);
      let newPosts: any = VueCookies.get('posts') || '';
      newPosts = newPosts + ',' + postId;
      VueCookies.set('posts', newPosts, 60 * 60 * 24 * 30);
    }).catch(() => {
      console.log('Oops, Something went wrong.');
    });
  }

}
</script>
<template lang="haml">
%div
  %h2.white--text.ml-1.mb-1.mt-4.font-weight-thin Posts
  %template{"v-for": 'post in filteredPosts'}
    %transition{"name": "fade"}
      %v-flex.xs12
        %v-card.mb-1.white{"hover": false}
          %v-card-media{":src": 'post.node.image', "height": "200px"}
          %v-card-title{"primary-title": true}
            %p.headline.ma-0.custom-text-first {{post.node.headline}}
          %v-card-text
            %p.subheading.custom-text-first {{post.node.subheadline}}
          %v-divider.custom-text-first
          %v-card-actions.ma-0.white
            %v-btn.v-btn--round.custom-text-first.mr-4.ml-2{"flat": true, "icon": true, "v-on:click": '$store.commit("commitShowPost", post.node.id)'}
              %v-icon.v-icon--medium.grey--text.text--darken-3{"flat": true, "v-if": '!post.node.show'} fa-chevron-down
              %v-icon.v-icon--medium.grey--text.text--darken-3{"flat": true, "v-else": 'v-else'} fa-chevron-up
            %v-spacer
            %v-btn.v-btn--round.custom-text-first.mr-4{"flat": true, "icon": true}
            %v-btn.v-btn--round.custom-text-first.mr-4{"v-on:click": 'upvote(post.node.id)', "flat": true, "icon": true}
              %v-badge{"color": "red"}
                %span{"slot": "badge"} {{post.node.likes}}
                %v-icon.v-icon--medium{"flat": true, 'v-bind:class': 'post.node.likedClass'} fa-thumbs-up
          %v-slide-y-transition
            %v-card-text.preline{"v-show": 'post.node.show', "v-html": 'post.node.content'}
</template>
<style>
.preline {
  white-space: pre-line;
}
</style>
