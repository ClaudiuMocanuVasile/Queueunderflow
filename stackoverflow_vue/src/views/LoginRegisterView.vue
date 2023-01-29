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

                                    <form class="login-register-form">
                                        <hr>
                                        <h1 class="mx-auto">Sign in</h1>
                                        <hr class="mb-4">
                                        <!-- Email input -->
                                        <div class="form-outline mb-3">
                                            <!-- <label class="form-label" for="login_email" >Email</label> -->
                                            <input type="email" id="login_email" class="form-control shadow-sm"
                                                placeholder="Email" />
                                        </div>

                                        <!-- Password input -->
                                        <div class="form-outline mb-4">
                                            <!-- <label class="form-label" for="login_password">Password</label> -->
                                            <input type="password" id="login_password" class="form-control shadow-sm"
                                                placeholder="Password" />
                                        </div>

                                        <!-- Submit button -->
                                        <button type="button" class="btn btn-dark btn-block mb-4">Sign in</button>

                                        <!-- Register buttons -->
                                        <div class="text-center">
                                            <p>Not a member? <a href="/register">Register here!</a></p>
                                        </div>
                                    </form>
                                </div>

                                <!-- Register Tab -->
                                <div class="tab-pane fade show" id="pills-register" role="tabpanel"
                                    aria-labelledby="pills-register">

                                    <form class="login-register-form">
                                        <hr>
                                        <h1 class="mx-auto">Register</h1>
                                        <hr class="hr mb-4">
                                        <!-- Username input -->
                                        <div class="form-outline mb-4">
                                            <!-- <label class="form-label" for="register_username">Username</label> -->
                                            <input type="text" id="register_username" class="form-control shadow-sm"
                                                placeholder="Username" />
                                        </div>

                                        <!-- Displayed name input -->
                                        <div class="form-outline mb-4">
                                            <!-- <label class="form-label" for="register_displayedName">Displayed Name</label> -->
                                            <input type="text" id="register_displayedName"
                                                class="form-control shadow-sm" placeholder="Displayed name" />
                                        </div>

                                        <!-- Birthday input -->
                                        <div class="form-outline mb-4">
                                            <!-- <label class="form-label" for="register_birthday">Birthday</label> -->
                                            <input type="date" id="register_birthday" class="form-control shadow-sm"
                                                min="1900-01-01" max="2023-12-31" />
                                        </div>

                                        <!-- Email input -->
                                        <div class="form-outline mb-4">
                                            <!-- <label class="form-label" for="register_email">Email</label> -->
                                            <input type="email" id="register_email" class="form-control shadow-sm"
                                                placeholder="Email" />
                                        </div>

                                        <!-- Password input -->
                                        <div class="form-outline mb-4">
                                            <!-- <label class="form-label" for="register_password">Password</label> -->
                                            <input type="password" id="register_password" class="form-control"
                                                placeholder="Password" />
                                        </div>

                                        <!-- Submit button -->
                                        <button type="button" class="btn btn-dark btn-block mb-4">Sign in</button>

                                        <!-- Register buttons -->
                                        <div class="text-center">
                                            <p>Already a member? <a href="/login">Sign in here!</a></p>
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

export default {
    name: 'LoginRegisterView',
    components: {
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
