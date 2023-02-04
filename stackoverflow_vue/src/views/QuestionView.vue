<template>
    <div class="home">

    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'QuestionView',
    data() {
        question: {}

    },
    mounted() {
        this.getQuestion()
    },
    methods: {
        async getQuestion() {
            this.$store.commit('setIsLoading', true)
            //const community_slug = this.$route.params.community_slug
            const category_slug = this.$route.params.category_slug
            const question_slug = this.$route.params.question_slug

            await axios
                .get(`/api/v1/questions/${category_slug}/${question_slug}`)
                .then(response => {
                    this.question = response.data

                    document.title = this.product.name + ' | Queueunderflow'
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    },
    components: {
    }
}
</script>
