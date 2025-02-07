import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Overview',
      component: () => import('../components/BooksOverview.vue')
    },
    {
      path: '/BookInfo/:id',
      name: 'Info',
      component: () => import('../components/BookInfo.vue')
    },
    {
      path: '/ping',
      name: 'Ping',
      component: () => import('../components/Ping.vue')
    },

  ]
})

export default router
