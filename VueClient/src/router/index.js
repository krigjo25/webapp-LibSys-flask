import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../components/Index.vue')
    },
    {
      
      name: 'BookDetails',
      path: '/Details',
      component: () => import('../components/BookInfo.vue')
    },
    {
      path: '/bookMananger',
      name: 'Manager',
      component: () => import('../components/Manage.vue')
    },
    {
      path: '/upsert',
      name: 'UpsertBook',
      component: () => import('../components/Form.vue')
    },

  ]
})

export default router
