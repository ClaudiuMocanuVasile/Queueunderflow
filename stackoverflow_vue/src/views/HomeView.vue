<template>
    <div class="home">
        <div class="card text-bg-dark">
  <img src="https://www.brookings.edu/wp-content/uploads/2017/11/metro_20171121_tech-empowers-tech-polarizes-mark-muro.jpg" class="card-img" alt="...">
  <div class="card-img-overlay">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
    <p class="card-text"><small>Last updated 3 mins ago</small></p>
  </div>
</div>
        <QuestionBox
            v-for = "question in latestQuestions"
            v-bind:key="question.id"
            v-bind:question="question"/>
    </div>
</template>

<script>
import axios from 'axios'

import QuestionBox from '@/components/QuestionBox.vue'

export default {
    name: 'HomeView',
    data() {
        return {
            latestQuestions: {}
        }
    },
    components: {
        QuestionBox
    },
    mounted() {
        document.title = 'Home | Queueunderflow'
        
    }
}
</script>
