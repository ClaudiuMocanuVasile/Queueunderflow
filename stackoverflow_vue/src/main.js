import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// My imports

import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-icons/font/bootstrap-icons.css"
import "bootstrap/dist/js/bootstrap.js"
import axios from 'axios'

axios.defaults.baseURL = "http://127.0.0.1:8000"

createApp(App).use(store).use(router, axios).mount('#app')

