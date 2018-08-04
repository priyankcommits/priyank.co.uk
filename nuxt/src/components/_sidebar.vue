<script lang="ts">
import Vue from 'vue';
import Component from 'nuxt-class-component';
import { Prop } from 'vue-property-decorator';

@Component
export default class extends Vue{
  @Prop({default: ''}) headline: string;
  @Prop({default: ''}) text: string;
  @Prop({default: ''}) link: string;
}
</script>
<template lang="haml">
%v-layout.ma-1.row.wrap
  %v-flex.xs12
    %v-card.custom-bg-second{"hover": false}
      %v-card-title{"primary-title": true}
        %div
          %h4.headline.mb-0.white--text {{headline}}
          %br
          %h5.white--text {{text}}
      %v-card-actions.custom-bg-second
        %v-spacer
        %v-btn.v-btn--outline.v-btn--small.custom-text-fifth{"flat": true, ":href": 'link', 'target': '_blank'} Read
</template>
<style>
</style>