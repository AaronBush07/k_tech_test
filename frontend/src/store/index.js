import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    list: [],
  },
  mutations: {
    updateList(state, payload) {
      state.list = payload;
    },
  },
  actions: {
    async fetchList({ commit }) {
      axios
        .request({
          url: `http://localhost:8000/colours`,
          method: "GET",
        })
        .then((response) => {
          commit("updateList", response.data);
        })
        .catch(() => {
          console.log("Server error");
        });
    },
  },
  modules: {},
});
