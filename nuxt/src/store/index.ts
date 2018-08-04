import { apiUrl } from '../../globals';

export const state = () => ({
  users: [],
  articles: [],
  posts: [],
  filteredPosts: [],
});

export const mutations = {
  setUsers(state, users) {
    state.users = users;
  },
  setArticles(state, articles) {
    state.articles = articles;
  },
  setPosts(state, posts) {
    posts.forEach((element: any) => {
      element.node.show = false;
      element.node.likedClass = 'blue-grey--text';
    });
    state.posts = posts;
    state.filteredPosts = state.posts;
  },
  commitShowPost(state, postId) {
    state.posts.forEach(element => {
      if (element.node.id === postId) {
        element.node.show = !element.node.show;
      }
    });
  },
  commitUpvotePost(state, postId) {
    state.posts.forEach(element => {
      if (element.node.id === postId) {
        element.node.likedClass = 'blue--text';
      }
    });
  },
  commitUpvotePreviouslyLikedPosts(state, postIds) {
    state.posts.forEach(element => {
      postIds.forEach(postId => {
        if (element.node.id == postId) {
          element.node.likedClass = 'blue--text';
        }
      });
    });
    state.filteredPosts = state.posts;
  },
  commitShowFilteredPosts(state, postKind) {
    state.filteredPosts = [];
    if (postKind == 0) {
      state.filteredPosts = state.posts;
    } else {
      state.posts.forEach(element => {
        if (element.node.kind === postKind) {
          state.filteredPosts.push(element);
        }
      });
    }
  }
};

export const actions = {
  async nuxtServerInit({ commit }, { app }) {
    const response = await app.$axios.post(apiUrl, {
      query: `{
        allProfiles {edges { node { id, firstName, lastName }}}
        allArticles {edges { node { headline, text, link }}}
        allPosts {edges { node { id, headline, content, image, likes, subheadline, kind }}}
      }`,
    });
    commit("setUsers", response.data.data.allProfiles.edges);
    commit("setArticles", response.data.data.allArticles.edges);
    commit("setPosts", response.data.data.allPosts.edges);
 },
};
