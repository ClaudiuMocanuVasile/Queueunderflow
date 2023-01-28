<template>
    <div class="container-fluid px-0">

        <!-- Header -->

        <div id="header">

            <nav class="navbar navbar-dark navbar-expand-xl fixed-top bg-dark text-white">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">
                        <img src="data:image/jpeg;base64,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"
                            alt="Logo" width="30" height="24" class="d-inline-block align-text-top">
                        Queueunderflow
                    </a>

                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                        data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                        aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse text-end" id="navbarSupportedContent">
                        <div class="navbar-nav">
                            <router-link to="" class="nav-link nav-link-white-gray mx-3 mx-xl-0 p-0" href="#">
                                <div class="mx-2 d-flex justify-content-end d-xl-none mt-xl-0 mt-2">
                                    <div>
                                        <span class="me-2">
                                            Hello, Cermergatorul
                                        </span>
                                        <i class="bi bi-person" style="font-size: 1.5rem;"></i>
                                    </div>
                                </div>
                            </router-link>
                        </div>

                        <ul class="navbar-nav">

                            <li class="nav-item dropdown">
                                <router-link to="" class="nav-link nav-link-white-gray dropdown-toggle mx-3 mx-xl-0"
                                    href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Categories
                                </router-link>
                                <ul class="dropdown-menu dropdown-menu-dark">
                                    <li class="text-end mx-2 mx-xl-0"><router-link to="" class="dropdown-item"
                                            href="#">Favorite
                                            categories</router-link></li>
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                    <li class="text-end mx-2 mx-xl-0"><router-link to="" class="dropdown-item"
                                            href="#">Random category</router-link>
                                    </li>
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                    <li class="text-end mx-2 mx-xl-0"><router-link to="" class="dropdown-item"
                                            href="#">All categories</router-link>
                                    </li>
                                </ul>
                            </li>
                            <li class="nav-item dropdown">
                                <router-link to="" class="nav-link nav-link-white-gray dropdown-toggle mx-3 mx-xl-0"
                                    href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Communities
                                </router-link>
                                <ul class="dropdown-menu dropdown-menu-dark">
                                    <li class="text-end mx-2 mx-xl-0">
                                        <router-link to="" class="dropdown-item" href="#">Create a
                                            community!</router-link>
                                    </li>
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                    <li class="text-end mx-2 mx-xl-0">
                                        <router-link to="" class="dropdown-item" href="#">Your communities</router-link>
                                    </li>
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                    <li class="text-end mx-2 mx-xl-0">
                                        <router-link to="" class="dropdown-item" href="#">Random community</router-link>
                                    </li>
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                    <li class="text-end mx-2 mx-xl-0">
                                        <router-link to="" class="dropdown-item" href="#">All communities</router-link>
                                    </li>
                                </ul>
                            </li>
                            <li class="nav-item">
                                <router-link to="" class="nav-link nav-link-white-gray mx-3 mx-xl-0" href="#">Post your
                                    own
                                    question!</router-link>
                            </li>
                        </ul>
                        <div class="d-flex flex-grow-1">
                            <div class="container-fluid px-0">
                                <div class="d-flex flex-md-row flex-column justify-content-between">
                                    <div class="flex-grow-1">
                                        <form class="d-flex" role="search">

                                            <input class="form-control me-2" type="search"
                                                placeholder="Search topic or question..." aria-label="Search">
                                            <button class="btn btn-outline-light mx-2" type="submit">Search</button>


                                        </form>
                                    </div>
                                    <div class="navbar-nav">
                                        <router-link to="" class="nav-link nav-link-white-gray mx-3 mx-xl-0 p-0"
                                            href="#">
                                            <div class="mx-2 d-flex justify-content-center d-none d-xl-block">

                                                <span class="me-2">
                                                    Hello, Cermergatorul
                                                </span>
                                                <i class="bi bi-person" style="font-size: 1.5rem;"></i>

                                            </div>
                                        </router-link>
                                    </div>

                                </div>
                            </div>
                        </div>


                    </div>
                </div>


            </nav>
        </div>

        <!-- Main content -->
        <div id="main">
            <router-view />
        </div>

        <!-- Footer -->
        <div id="footer">
            <!-- Footer -->
            <footer class="text-center text-lg-start bg-dark text-white">
                <!-- Section: Social media -->
                <section class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom">
                    <!-- Left -->
                    <div class="me-5 d-none d-lg-block">
                        <span>Get connected with us on social networks:</span>
                    </div>
                    <!-- Left -->

                    <!-- Right -->
                    <div>
                        <a href="" class="me-4 text-reset">
                            <i class="fab fa-facebook-f"></i>
                        </a>
                        <a href="" class="me-4 text-reset">
                            <i class="fab fa-twitter"></i>
                        </a>
                        <a href="" class="me-4 text-reset">
                            <i class="fab fa-google"></i>
                        </a>
                        <a href="" class="me-4 text-reset">
                            <i class="fab fa-instagram"></i>
                        </a>
                        <a href="" class="me-4 text-reset">
                            <i class="fab fa-linkedin"></i>
                        </a>
                        <a href="" class="me-4 text-reset">
                            <i class="fab fa-github"></i>
                        </a>
                    </div>
                    <!-- Right -->
                </section>
                <!-- Section: Social media -->

                <!-- Section: Links  -->
                <section class="">
                    <div class="container text-center text-md-start mt-5">
                        <!-- Grid row -->
                        <div class="row mt-3">
                            <!-- Grid column -->
                            <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
                                <!-- Content -->
                                <h6 class="text-uppercase fw-bold mb-4">
                                    <i class="fas fa-gem me-3"></i>Queueunderflow
                                </h6>
                                <p>
                                    Queueunderflow is a platform made by programmers, for programmers, that wishes to
                                    accomplish knowledge exchange on a scale unbeforeseen. Users can post questions,
                                    interact with each other and reply with their own approach.
                                </p>
                            </div>
                            <!-- Grid column -->

                            <!-- Grid column -->
                            <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
                                <!-- Links -->
                                <h6 class="text-uppercase fw-bold mb-4">
                                    Products
                                </h6>
                                <p>
                                    <a href="#!" class="text-reset">Angular</a>
                                </p>
                                <p>
                                    <a href="#!" class="text-reset">React</a>
                                </p>
                                <p>
                                    <a href="#!" class="text-reset">Vue</a>
                                </p>
                                <p>
                                    <a href="#!" class="text-reset">Laravel</a>
                                </p>
                            </div>
                            <!-- Grid column -->

                            <!-- Grid column -->
                            <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
                                <!-- Links -->
                                <h6 class="text-uppercase fw-bold mb-4">
                                    Useful links
                                </h6>
                                <p>
                                    <a href="#!" class="text-reset">FAQ</a>
                                </p>
                                <p>
                                    <a href="#!" class="text-reset">Cookie policy</a>
                                </p>
                                <p>
                                    <a href="#!" class="text-reset">Terms of Service</a>
                                </p>
                                <p>
                                    <a href="#!" class="text-reset">Help</a>
                                </p>
                            </div>
                            <!-- Grid column -->

                            <!-- Grid column -->
                            <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
                                <!-- Links -->
                                <h6 class="text-uppercase fw-bold mb-4">Contact</h6>
                                <p><i class="fas fa-home me-3"></i> Bucharest, 030018, Romania</p>
                                <p>
                                    <i class="fas fa-envelope me-3"></i>
                                    m.v.claudiu99@gmail.com
                                </p>
                                <p>
                                    <i class="fas fa-envelope me-3"></i>
                                    petrache.larisa@gmail.com
                                </p>
                                <p><i class="fas fa-phone me-3"></i> +40 765 099 203</p>
                            </div>
                            <!-- Grid column -->
                        </div>
                        <!-- Grid row -->
                    </div>
                </section>
                <!-- Section: Links  -->

                <!-- Copyright -->
                <div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
                    © 2023 Copyright:
                    <span class="text-reset fw-bold">Mocanu-Vasile Claudiu</span>
                    <span class="text-reset fw-bold"> & </span>
                    <span class="text-reset fw-bold">Petrache Larisa-Stefania</span>
                </div>
                <!-- Copyright -->
            </footer>
            <!-- Footer -->
        </div>
    </div>

</template>

<script>
export default {
    data() {
        return {

        }
    }
}
</script>

<style lang="scss">
.nav-link-white-gray {
    color: white !important;
}

.nav-link-white-gray:hover {
    color: rgba(255, 255, 255, 0.75) !important;
}
</style>
