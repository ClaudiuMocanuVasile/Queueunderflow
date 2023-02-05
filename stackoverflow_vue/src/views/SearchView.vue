<template>
    <div class="search">
        <QuestionBox
            v-for = "question in questions"
            v-bind:key="question.id"
            v-bind:question="question"/>
        </div>
</template>

<script>
import axios from 'axios'
import QuestionBox from '@/components/QuestionBox.vue'

export default {
    name: 'SearchView',
    components: {
        QuestionBox
    },
    data() {
        return {
            questions: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Search | Queueunderflow'

        if(window.location.search)
        {
            var uri = window.location.search.substring(1)
        }
        let params = new URLSearchParams(uri)
        if(params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true)
            
            await axios
                .post('/api/v1/search/', {'query': this.query})
                .then(response => {
                    this.questions = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>
