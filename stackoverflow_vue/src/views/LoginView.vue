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
                            <form class="login-form">
                                <h1 class="mx-auto">Sign in</h1>
                                <hr class="mb-4">
                                <!-- Email input -->
                                <div class="form-outline mb-3">
                                    <!-- <label class="form-label" for="login_email" >Email</label> -->
                                    <input type="email" id="login_email" class="form-control shadow-sm" placeholder="Email" />
                                </div>

                                <!-- Password input -->
                                <div class="form-outline mb-4">
                                    <!-- <label class="form-label" for="login_password">Password</label> -->
                                    <input type="password" id="login_password" class="form-control shadow-sm" placeholder="Password" />
                                </div>

                                <!-- Submit button -->
                                <button type="button" class="btn btn-dark btn-block mb-4">Sign in</button>

                                <!-- Register buttons -->
                                <div class="text-center">
                                    <p>Not a member? <a href="/register">Register here!</a></p>
                                </div>
                            </form>
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
    name: 'LoginView',
    components: {
    }
}
</script>

<style>
@media (min-width: 1000px) {
    .background-radial-gradient {
        padding-top: 150px;
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

.login-form {
    display: flex;
    justify-content: center;
    flex-direction: column;
    text-align: left;
}
</style>
