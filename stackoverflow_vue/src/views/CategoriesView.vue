<template>
    <div class="category">

    </div>
</template>

<script>
import axios from 'axios'

export default {

    name: 'CategoriesView',
    data() {
        return {
            category: {
                questions: {}
            }
        }
    },
    components: {
    },
    mounted() {
        this.getCategories()

        document.title = 'Categories | Queueunderflow'
    },
    methods: {
        
    }
}
</script>

<style>

</style>