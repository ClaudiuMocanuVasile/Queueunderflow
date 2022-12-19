import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// My imports

import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-icons/font/bootstrap-icons.css"

createApp(App).use(store).use(router).mount('#app')

import "bootstrap/dist/js/bootstrap.js"