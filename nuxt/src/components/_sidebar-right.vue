<script lang="ts">
import Vue from 'vue';
import Component from 'nuxt-class-component'

@Component
export default class extends Vue{
  private mounted() {
  }
}
</script>
<template lang="haml">
%v-layout.ma-1.row.wrap
  %v-flex.xs12
    %v-card.custom-bg-fourth{"hover": false}
      %slot{"name": "card-media"}
      %v-card-title{"primary-title": true}
        %div
          %h3.headline.mb-0.white--text
            %slot{"name": "card-title"} Title
          %div.white--text.font-weight-light
            %slot{"name": "card-body"}
      %v-card-media
</template>
<style>
</style>