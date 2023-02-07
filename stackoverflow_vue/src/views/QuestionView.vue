<template>
    <section class="h-100 gradient-custom-2">
        <div class="container py-5 h-100">

            <!-- Question Details Container -->
            <div class="card">

                <!-- Question description -->
                <div class="pt-3 pb-4 ps-5 text-black d-flex flex-column">
                    <h4 class="mt-3">{{ question.question }}</h4>

                    <div class="mt-3 d-flex">
                        <div><button class="btn btn-danger ms-2" style="max-width: fit-content;"
                                @click="redirectToCategory">{{ categoryName }}</button></div>
                        <div class="py-1 ms-4">Question posted by: {{ question.queue_user }}</div>
                        <div class="py-1 ms-4">Asked: {{ formattedDate }}</div>
                        <div class="py-1 ms-4">{{ formattedTime }}</div>
                    </div>

                    <!-- <hr> -->

                    <!-- Add comment -->
                    <div class="pt-5 pb-3 text-danger" @click="showTextareaAnswer = !showTextareaAnswer">
                        <a style="cursor: pointer;">Answer this question</a>
                    </div>

                    <!-- Comment textarea -->
                    <div v-if="showTextareaAnswer">
                        <textarea class="form-control w-75" rows="5" v-model="answer_text"></textarea>
                        <button class="btn btn-dark mt-3" @click="sendAnswerData">Submit</button>
                    </div>
                </div>

                <hr>
                <h4 class="ps-5 py-4">Answers:</h4>

                <!-- Answer Content -->
                <div class="px-5 py-4">
                    <div class="d-flex flex-wrap">
                        <div v-for="answer in answers" :key="answer.id">
                            <!-- Answer -->
                            <div class="p-4 m-1 w-auto">
                                <div class="card-body">

                                    <div class="my-3 d-flex bg-danger text-white p-2">
                                        <div>Answered: </div>
                                        <div class="ms-4">User {{ answer.queue_user }}</div>
                                        <div class="ms-4">{{ new Date(answer.date_posted).toLocaleDateString() }}</div>
                                        <div class="ms-4">{{ new Date(answer.date_posted).toLocaleTimeString() }}</div>
                                    </div>

                                    <div>{{ answer.answer }}</div>


                                    <div>
                                        <!-- Add comment -->
                                        <div class="pt-2 pb-3 text-danger"
                                            @click="showTextareaComment = !showTextareaComment">
                                            <a style="cursor: pointer;">Add comment</a>
                                        </div>

                                        <!-- Comment textarea -->
                                        <div v-if="showTextareaComment">
                                            <textarea class="form-control w-75" rows="5"></textarea>
                                            <button class="btn btn-dark mt-3">Submit</button>
                                        </div>
                                        <hr>
                                    </div>
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
            posted_by: '',
            username: '',
            logged_user_id: '',
            date_posted: '',
            showTextareaAnswer: false,
            showTextareaComment: false,
            answer_text: ''
        }

    },
    mounted() {
        this.getQuestion()

        const token = localStorage.getItem('token');
        axios.post("/api/v1/profile/", { "token": token })
            .then(response => {
                this.username = response.data.username
                this.logged_user_id = response.data.id

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
                    this.posted_by = this.question.queue_user
                    console.log(this.question)
                    console.log(this.answers)
                });

            this.$store.commit('setIsLoading', false)
        },

        redirectToCategory() {
            window.location = `/questions/${this.categoryName}/`;
        },

        async sendAnswerData() {
            const endpoint = '/answer/';
            const payload = {
                question: this.question.id,
                answer: this.answer_text,
                queue_user: this.logged_user_id
            };

            axios
                .post('http://localhost:8000/api/v1/answer/', payload)
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.error(error);
                });
        },
        
        async sendCommentData() {
            const endpoint = '/answer/';
            const payload = {
                answer: this.answer.id,
                comment: this.answer_text,
                queue_user: this.logged_user_id
            };
            console.log(payload)
            axios
                .post('http://localhost:8000/api/v1/comment/', payload)
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.error(error);
                });
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
