<template>
    <div class="home">
        <div class="card text-bg-dark">
            <img src="https://www.brookings.edu/wp-content/uploads/2017/11/metro_20171121_tech-empowers-tech-polarizes-mark-muro.jpg"
                class="card-img" alt="...">
            <div class="card-img-overlay text-center" style="background:rgba(0,0,0,0.5)">
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>
                <h1 class="card-title">Queueunderflow</h1>
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>

                <p class="card-text w-50 m-auto">Queueunderflow is a platform made by programmers, for programmers, that
                    wishes to accomplish knowledge exchange on a scale unbeforeseen. Users can post questions, interact
                    with each other and reply with their own approach.</p>
            </div>
            <p class="card-text" v-for="question in latestQuestions.slice(0, 4)" v-bind:key="question.id" v-bind:question="question">
                cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos cos
            </p >
        </div>
    </div>

</template>

<script>
import axios from 'axios'

import QuestionBox from '@/components/QuestionBox.vue'

export default {
    name: 'HomeView',
    data() {
        return {
            latestQuestions: []
        }
    },
    components: {
        QuestionBox
    },
    mounted() {
        document.title = 'Home | Queueunderflow'
        axios
            .get('http://localhost:8000/api/v1/questions/')
            .then(response => {
                this.latestQuestions = response.data
            })
            .catch(error => {
                console.log(error)
            })
    },
}
</script>
