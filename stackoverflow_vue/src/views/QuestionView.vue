<template>
    <section class="h-100 gradient-custom-2">
        <div class="container py-5 h-100">

            <!-- Question Details Container -->
            <div class="card">

                <!-- Question description -->
                <div class="pt-3 pb-4 ps-5 text-black d-flex flex-column" style="background-color: #f8f9fa;">
                    <h4 class="mt-3">{{ question.question }}</h4>

                    <div class="mt-3 d-flex">
                        <div><button class="btn btn-danger ms-2"
                                style="max-width: fit-content;" @click="redirectToCategory">{{ categoryName }}</button></div>
                        <div class="py-1 ms-4">Question posted by: {{ username }}</div>
                        <div class="py-1 ms-4">Asked: {{ formattedDate }} {{ formattedTime }}</div>
                    </div>

                    <hr>

                    <!-- Add comment -->
                    <div class="pt-3 text-danger" @click="showTextarea = !showTextarea">
                        <a style="cursor: pointer;">Add a comment</a>
                    </div>

                    <!-- Comment textarea -->
                    <div v-if="showTextarea">
                        <textarea class="form-control w-75" rows="5"></textarea>
                        <button class="btn btn-dark mt-3">Submit</button>
                    </div>
                </div>

                <!-- Questions Content -->
                <div class="px-5 py-5">
                    <div class="categories-container d-flex flex-wrap">
                        <div v-for="answer in answers" :key="answer.id">
                            <!-- Question -->
                            <div class="card m-1 bg-light w-auto">
                                <div class="card-body">
                                    <div>{{ answer.answer }}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <!-- Question Details Container end -->
        </div>

    </section>
</template>

<script>
import axios from 'axios'

export default {
    name: 'QuestionView',
    data() {
        return {
            categoryName: '',
            question: [],
            answers: [],
            username: '',
            date_posted: '',
            showTextarea: false
        }

    },
    mounted() {
        this.getQuestion()

        const token = localStorage.getItem('token');
        axios.post("/api/v1/profile/", { "token": token })
            .then(response => {
                this.username = response.data.username
            })
            .catch(error => {
                console.log(JSON.stringify(error))
            })
    },
    methods: {
        async getQuestion() {
            this.$store.commit('setIsLoading', true)
            const category_slug = this.$route.params.category_slug
            const question_slug = this.$route.params.question_slug
            this.categoryName = category_slug

            await axios
                .get(`http://localhost:8000/api/v1/questions/${category_slug}/${question_slug}`)
                .then(response => {
                    this.question = response.data
                    this.date_posted = this.question.date_posted
                    this.answers = this.question.answers
                });

            this.$store.commit('setIsLoading', false)
        },

        redirectToCategory() {
            window.location = `/questions/${this.categoryName}/`;
        }
    },
    computed: {
        formattedDate() {
            return new Date(this.date_posted).toLocaleDateString();
        },
        formattedTime() {
            return new Date(this.date_posted).toLocaleTimeString();
        }
    }
}
</script>
