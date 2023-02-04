<template>

    <!-- Section: Login -->
    <section class="background-radial-gradient overflow-hidden">

        <div class="container px-4 py-5 px-md-5 text-center text-lg-start my-5">
            <div class="row gx-lg-5 align-items-center mb-5">
                <div class="col-lg-6 mb-5 mb-lg-0" style="z-index: 10">
                    <h1 class="my-5 display-5 fw-bold ls-tight" style="color: hsl(218, 81%, 95%)">
                        The best platform <br />
                        <span style="color: hsl(218, 81%, 75%)">for answering questions</span>
                    </h1>
                    <p class="mb-4 opacity-70" style="color: hsl(218, 81%, 85%)">
                        Queueunderflow is a platform that wishes to accomplish knowledge exchange on a scale
                        unbeforeseen.
                        Users can post questions, interact with each other and reply with their own approach.
                    </p>
                </div>

                <div class="col-lg-6 mb-5 mb-lg-0 position-relative">
                    <div id="radius-shape-1" class="position-absolute rounded-circle shadow-5-strong"></div>
                    <div id="radius-shape-2" class="position-absolute shadow-5-strong"></div>

                    <div class="card bg-glass">
                        <div class="card-body px-4 py-5 px-md-5">

                            <!-- Pills navs -->
                            <ul class="nav nav-pills mb-3" id="ex1" role="tablist">
                                <li class="nav-item" role="presentation">
                                    <a class="nav-link active" id="ex1-tab-1" data-bs-toggle="pill" href="#pills-login"
                                        role="tab" aria-controls="pills-login" aria-selected="true">Sign in</a>
                                </li>
                                <li class="nav-item" role="presentation">
                                    <a class="nav-link" id="ex1-tab-2" data-bs-toggle="pill" href="#pills-register"
                                        role="tab" aria-controls="pills-register" aria-selected="false">Register</a>
                                </li>
                            </ul>
                            <!-- Pills navs -->

                            <!-- Pills content -->
                            <div class="tab-content" id="ex1-content">

                                <!-- Login Tab -->
                                <div class="tab-pane fade show active" id="pills-login" role="tabpanel"
                                    aria-labelledby="pills-login">

                                    <form @submit.prevent="submitFormLogin" class="login-register-form">
                                        <hr>
                                        <h1 class="mx-auto">Sign in</h1>
                                        <hr class="mb-4">
                                        <!-- Email input -->
                                        <div class="form-floating form-outline mb-3">
                                           
                                            <input type="email" id="login_email" v-model="username_login" class="form-control shadow-sm"
                                                placeholder="Email" /><label class="form-label" for="login_email" >Email</label>
                                        </div>

                                        <!-- Password input -->
                                        <div class="form-floating mb-4">
                                           
                                            <input type="password" id="login_password" v-model="password_login" class="form-control shadow-sm"
                                                placeholder="Password" /> <label class="form-label" for="login_password">Password</label>
                                        </div>

                                        <div v-if="errors_login.length">
                                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                                        </div>

                                        <!-- Submit button -->
                                        <button type="button" class="btn btn-dark btn-block mb-4">Sign in</button>

                                        <!-- Register buttons -->
                                        <div class="text-center">
                                            <p>Not a member? <a href="#" @click="switchTabToRegister">Register here!</a></p>
                                        </div>
                                    </form>
                                </div>

                                <!-- Register Tab -->
                                <div class="tab-pane fade show" id="pills-register" role="tabpanel"
                                    aria-labelledby="pills-register">

                                    <form @submit.prevent="submitFormRegister" class="login-register-form">
                                        <hr>
                                        <h1 class="mx-auto">Register</h1>
                                        <hr class="hr mb-4">
                                        <!-- Username input -->
                                        <div class="form-floating mb-4">
                                           
                                            <input type="text" id="register_username" v-model="username" class="form-control shadow-sm"
                                                placeholder="Username" /> <label class="form-label" for="register_username">Username</label>
                                        </div>

                                        <!-- Displayed name input -->
                                        <div class="form-floating mb-4">
                                            
                                            <input type="text" id="register_displayedName" v-model="displayed_name"
                                                class="form-control shadow-sm" placeholder="Displayed name" /><label class="form-label" for="register_displayedName">Displayed Name</label> 
                                        </div>

                                        <!-- Birthday input -->
                                        <div class="form-floating mb-4">
                                            
                                            <input type="date" id="register_birthday" v-model="birthday" class="form-control shadow-sm"
                                                min="1900-01-01" max="2023-12-31" /><label class="form-label" for="register_birthday">Birthday</label> 
                                        </div>

                                        <!-- Email input -->
                                        <div class="form-floating mb-4">
                                            
                                            <input type="email" id="register_email" v-model="email" class="form-control shadow-sm"
                                                placeholder="Email" /><label class="form-label" for="register_email">Email</label> 
                                        </div>

                                        <!-- Password input -->
                                        <div class="form-floating mb-4">
                                             
                                            <input type="password" id="register_password" v-model="password" class="form-control"
                                                placeholder="Confirm password" /><label class="form-label" for="register_password">Confirm password</label>
                                        </div>

                                        <!-- Confirm password input -->
                                        <div class="form-floating mb-4">
                                            
                                            <input type="password" id="confirm_password" v-model="confirm_password" class="form-control shadow-sm"
                                                placeholder="Confirm assword" /><label class="form-label" for="login_password">Password</label>
                                        </div>

                                        <div v-if="errors.length">
                                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                                        </div>

                                        <!-- Submit button -->
                                        <button type="button" class="btn btn-dark btn-block mb-4">Sign in</button>

                                        <!-- Register buttons -->
                                        <div class="text-center">
                                            <p>Already a member? <a href="#" @click="switchTabToLogin">Sign in here!</a></p>
                                        </div>
                                    </form>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Section: Login -->

</template>

<script>
import axios from 'axios'


export default {
    name: 'LoginRegisterView',
    components: {
    },
    data() {
        return {
            username: '',
            displayed_name: '',
            password: '',
            confirm_password: '',
            birthday: '',
            email: '',
            errors: [],
            errors_login: [],
            username_login: '',
            password_login: ''
        }
    },
    mounted() {
        document.title = 'Log In | Queueunderflow'
    },
    methods: {
        // switchTabToRegister() {
        // document.querySelector('#ex1-tab-2').click();
        // },
        // switchTabToLogin() {
        // document.querySelector('#ex1-tab-1').click();
        // }

        async submitFormLogin() {

        },

        submitFormRegister()
        {
            this.errors = []
            if(this.username === '') {
                this.errors.push('The username is missing')
            }

            if(this.password === '') {
                this.errors.push('The password is too short')
            }

            if(this.password !== this.confirm_password) {
                this.errors.push('The passwords do not match')
            }

            if(!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password,
                    email: this.email
                }

                axios
                    .post("/api/v1/users/", formData)
                    .then(response => {
                        toast({
                            message: 'Account created, you can now log in.',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right'
                        })

                        this.$router.push('/login')
                    })
                    .catch(error => {
                        if(error.response) {
                            for(const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if(PerformanceResourceTiming.message) {
                            this.errors.push('Something went wrong. Please try again')

                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }

}
</script>

<style>
@media (min-width: 1000px) {
    .background-radial-gradient {
        padding-top: 100px;
        padding-bottom: 100px;
    }
}

.background-radial-gradient {
    background-color: hsl(218, 41%, 15%);
    background-image: radial-gradient(650px circle at 0% 0%,
            hsl(218, 41%, 35%) 15%,
            hsl(218, 41%, 30%) 35%,
            hsl(218, 41%, 20%) 75%,
            hsl(218, 41%, 19%) 80%,
            transparent 100%),
        radial-gradient(1250px circle at 100% 100%,
            hsl(218, 41%, 45%) 15%,
            hsl(218, 41%, 30%) 35%,
            hsl(218, 41%, 20%) 75%,
            hsl(218, 41%, 19%) 80%,
            transparent 100%);
}

#radius-shape-1 {
    height: 220px;
    width: 220px;
    top: -60px;
    left: -130px;
    background: radial-gradient(#44006b, #ad1fff);
    overflow: hidden;
}

#radius-shape-2 {
    border-radius: 38% 62% 63% 37% / 70% 33% 67% 30%;
    bottom: -60px;
    right: -110px;
    width: 300px;
    height: 300px;
    background: radial-gradient(#44006b, #ad1fff);
    overflow: hidden;
}

.bg-glass {
    background-color: hsla(0, 0%, 100%, 0.9) !important;
    backdrop-filter: saturate(200%) blur(25px);
}

.login-register-form {
    display: flex;
    justify-content: center;
    flex-direction: column;
    text-align: left;
}
</style>
