import { createRouter, createWebHistory } from 'vue-router'

import Ping from '../components/Ping.vue'
import Home from '../components/home.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping
    },

  ]
})

export default router
