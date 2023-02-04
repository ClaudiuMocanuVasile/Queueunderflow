<template>
    <div class="home">
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
    components: {
        QuestionBox
    },
    mounted() {
        document.title = 'Home | Queueunderflow'
    }
}
</script>
