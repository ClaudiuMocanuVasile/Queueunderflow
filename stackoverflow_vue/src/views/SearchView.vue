<template>
    <div class="search">
        <QuestionBox
            v-for = "question in category.questions"
            v-bind:key="question.id"
            v-bind:question="question"/>
        </div>
</template>

<script>
import QuestionBox from '@/components/QuestionBox.vue'

export default {
    name: 'SearchView',
    components: {
        QuestionBox
    },
    data() {
        return {
            products: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Search | Queueunderflow'

        let uri = window.Geolocation.search.substring(1)
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
                .post('/api/v1/questions/search', {'query': this.query})
                .then(response => {
                    this.products = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>
