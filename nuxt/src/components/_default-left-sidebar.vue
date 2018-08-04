<script lang="ts">
import SidebarComponent from './_sidebar.vue';

import Vue from 'vue';
import Component from 'nuxt-class-component';
import { Prop } from 'vue-property-decorator';

@Component({
  components: {
    SidebarComponent,
  },
})
export default class extends Vue{
  @Prop({default: []}) articles: Array<{}>;
}
</script>
<template lang="haml">
%div
  %h2.white--text.ml-1.mt-4.mb-1.font-weight-thin Good Reads
  %template{"v-for": 'article in articles'}
    %sidebar-component{':headline': 'article.node.headline', ':text': 'article.node.text', ':link': 'article.node.link'}
</template>