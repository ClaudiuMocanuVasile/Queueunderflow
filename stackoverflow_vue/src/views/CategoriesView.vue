<template>
    <section class="h-100 gradient-custom-2">
        <div class="container py-5 h-100">

            <!-- Categories Container -->
            <div class="card">

                <div class="rounded-top text-white cover h-50">
                    <div class="m-5 d-flex flex-column">
                        <h1 class="mx-auto">Categories</h1>
                    </div>
                </div>

                <!-- Categories description -->
                <div class="p-3 text-black d-flex flex-column" style="background-color: #f8f9fa;">
                    <div class="mx-auto">Here you can find all available categories. Choose one of the following
                        categories and then you can browse its questions.</div>
                </div>

                <!-- Categories Content -->
                <div class="px-5 py-5">
                    <div class="categories-container d-flex flex-wrap">
                        <div v-for="category in categories" :key="category.id">
                            <!-- Category -->
                            <div class="card m-1 bg-light w-auto">
                                <div class="card-body">
                                    <div><a :href="`/questions/${category.slug}`" class="text-decoration-none text-dark">{{ category.name }}</a></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <!-- Categories Container end -->
        </div>

    </section>
</template>

<script>
import axios from 'axios'

export default {

    name: 'CategoriesView',
    data() {
        return {
            categories: [],
        };
    },
    mounted() {
        axios
            .get('http://localhost:8000/api/v1/categories/')
            .then(response => {
                this.categories = response.data;
            })
            .catch(error => console.error(error));
    },
    methods: {

    }
}
</script>

<style>
.cover {
    /* background: linear-gradient(to right bottom, rgb(50, 36, 80), rgb(79, 69, 128), rgb(105, 94, 161)); */
    background: linear-gradient(to left bottom, rgb(28, 27, 29), rgb(56, 41, 90));
    height: 200px;
}

.gradient-custom-2 {
    /* fallback for old browsers */
    background: #fbc2eb;

    /* Chrome 10-25, Safari 5.1-6 */
    background: -webkit-linear-gradient(to right, rgba(251, 194, 235, 1), rgba(166, 193, 238, 1));

    /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    background: linear-gradient(to right, rgb(194, 217, 251), rgb(185, 166, 238));
}
</style>