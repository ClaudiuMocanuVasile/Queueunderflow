<template>
    <section class="h-100 gradient-custom-2">
        <div class="container py-5 h-100">

            <!-- Questions Container -->
            <div class="card">

                <div class="rounded-top text-white cover h-50">
                    <div class="m-5 d-flex flex-column">
                        <h1 class="mx-auto">Questions</h1>
                    </div>
                </div>

                <!-- Questions description -->
                <div class="p-3 text-black d-flex flex-column" style="background-color: #f8f9fa;">
                    <div class="mx-auto">Here you can find all the questions for the category {{ categoryName }}</div>
                </div>

                <!-- Questions Content -->
                <div class="px-5 py-5">
                    <div class="categories-container d-flex flex-wrap">
                        <div v-for="question in questions" :key="question.id">
                            <!-- Question -->
                            <div class="card m-1 bg-light w-auto">
                                <div class="card-body">
                                    <div><a :href="`/questions/${categoryName}/${question.slug}`" class="text-decoration-none text-dark">{{ question.question }}</a></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <!-- Questions Container end -->
        </div>

    </section>
</template>

<script>
import axios from 'axios'

export default {
    name: 'QuestionsView',
    data() {
        return {
            categoryName: '',
            questions: [],
        };
    },
    mounted() {
        const categorySlug = this.$route.params.category_slug;
        axios.get(`http://localhost:8000/api/v1/questions/${categorySlug}`)
            .then(response => {
                this.categoryName = response.data.slug;
                this.questions = response.data.questions;
            });

    },
    methods: {
        redirectToQuestion() {
            window.location = `http://localhost:8000/api/v1/questions/${this.categoryName}/${this.question.slug}`;
        }
    }
}
</script>
