import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import LogIn from "./components/LogIn.vue";
import SignUp from "./components/SignUp.vue";
import Home from './components/Home.vue'
import Account from './components/Account.vue'
import Portatil from './components/Portatil.vue'

const routes = [
  {
    path: '/',
    name: "root",
    component: App,
  },
  {
    path: '/logIn',
    name: "logIn",
    component: LogIn,
  },
  {
    path: '/signUp',
    name: "signUp",
    component: SignUp,
  },
  {
    path: '/home',
    name: "home",
    component: Home,
  },
  {
    path: '/user/account',
    name: "account",
    component: Account,
  },
  {
    path: '/portatil',
    name: "portatil",
    component: Portatil
  }
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
