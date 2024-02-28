// src/store.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    selectedPc: null,
    isAuthorized:false,
  },
  mutations: {
    setSelectedPc(state, pc) {
      state.selectedPc = pc;
    },
    setIsAuth(state,isAuth){
      state.isAuthorized = isAuth;
    }
  },
});
