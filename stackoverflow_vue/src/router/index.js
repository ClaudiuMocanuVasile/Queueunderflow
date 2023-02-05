import { createRouter, createWebHistory } from 'vue-router'

import store from '@/store'


import HomeView from '../views/HomeView.vue'
import LoginRegisterView from '../views/LoginRegisterView.vue'
import ProfileView from '../views/ProfileView.vue'
import QuestionView from '@/views/QuestionView.vue'
import QuestionsView from '@/views/QuestionsView.vue'
import CategoriesView from '@/views/CategoriesView.vue'
import SearchView from '@/views/SearchView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginRegisterView
  },
  {
    path: '/:category_slug/:question_slug/',
    name: 'Question',
    component: QuestionView
  },
  {
    path: '/:category_slug/',
    name: 'Questions',
    component: QuestionsView
  },
  {
    path: '/categories',
    name: 'Categories',
    component: CategoriesView
  },
  {
    path: '/search/',
    name: 'Search',
    component: SearchView
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
    meta: {
        requireLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
    if(to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
        next({name: 'Login', query: {to: to.path}})
    } else {
        next()
    }
})

export default router