// src/store.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    selectedPc: null,
  },
  mutations: {
    setSelectedPc(state, pc) {
      state.selectedPc = pc;
    },
  },
});
