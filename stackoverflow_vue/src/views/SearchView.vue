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
                   <div class="mx-auto">Here you can find all the questions for the what you were searching for</div>
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
                   console.log(this.questions)
               })
               .catch(error => {
                   console.log(error)
               })
           this.$store.commit('setIsLoading', false)
       }
   }
}
</script>