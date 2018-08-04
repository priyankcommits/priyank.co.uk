<script lang="ts">
import Vue from 'vue';
import Component from 'nuxt-class-component';

@Component
export default class extends Vue {
}
</script>
<template lang="haml">
%div
  %div.hidden-xs-only
    %v-btn{"icon": true}
      %a.white--text{"href": 'mailto:pulumati.priyank@gmail.com', "target": "_blank"}
        %v-icon.v-icon--medium.custom-text-first fa-envelope
    %v-btn{"icon": true}
      %a.white--text{"href": 'https://twitter.com/pulumatipriyank', "target": "_blank"}
        %v-icon.v-icon--medium.custom-text-first fa-twitter
    %v-btn{"icon": true}
      %a.white--text{"href": 'https://www.linkedin.com/in/priyankpulumati', "target": "_blank"}
        %v-icon.v-icon--medium.custom-text-first fa-linkedin
    %v-btn{"icon": true}
      %a.white--text{"href": 'https://github.com/priyankcommits', "target": "_blank"}
        %v-icon.v-icon--medium.custom-text-first fa-github
  %div.hidden-sm-and-up
    %v-btn{"icon": true}
      %a.white--text{"href": 'mailto:pulumati.priyank@gmail.com', "target": "_blank"}
        %v-icon.v-icon--small.custom-text-first fa-envelope
    %v-btn{"icon": true}
      %a.white--text{"href": 'https://twitter.com/pulumatipriyank', "target": "_blank"}
        %v-icon.v-icon--small.custom-text-first fa-twitter
    %v-btn{"icon": true}
      %a.white--text{"href": 'https://www.linkedin.com/in/priyankpulumati', "target": "_blank"}
        %v-icon.custom-text-first fa-linkedin
    %v-btn{"icon": true}
      %a.white--text{"href": 'https://github.com/priyankcommits', "target": "_blank"}
        %v-icon.custom-text-first fa-github
</template>
