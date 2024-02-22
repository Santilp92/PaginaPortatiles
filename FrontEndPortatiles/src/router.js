import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import LogIn from "./components/LogIn.vue";
import SignUp from "./components/SignUp.vue";
import Home from './components/Home.vue'
import Account from './components/Account.vue'
import Portatil from './components/Portatil.vue'
import NewPc from './components/NewPc.vue'


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
    path: '/user/home',
    name: 'user-home',
    component: Home,
    meta: { requiresAuth: true }, 
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
  },
  {
    path: '/user/newpc',
    name: "newPc",
    component: NewPc
  },

];



const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
