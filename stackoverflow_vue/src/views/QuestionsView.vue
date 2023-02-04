<template>
    <div class="questions">
        <QuestionBox
            v-for = "question in category.questions"
            v-bind:key="question.id"
            v-bind:question="question"/>
    </div>
</template>

<script>
import QuestionBox from '@/components/QuestionBox.vue'

export default {
    name: 'QuestionsView',
    components: {
        QuestionBox
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        $route(to, from) {
            if(to.name === 'Category') {
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory() {
            //const community_slug = this.$route.params.community_slug
            const category_slug = this.$route.params.category_slug

            this.$store.commit('setIsLoading', true)

            await axios
                .get(`/api/v1/questions/${categorySlug}/`)
                .then(response => {
                    this.category = response.data

                    document.title = this.category.name + ' | Queueunderflow'
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>
