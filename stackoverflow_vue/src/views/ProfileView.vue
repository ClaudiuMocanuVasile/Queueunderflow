<template>

    <section class="h-100 gradient-custom-2">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col col-lg-9 col-xl-7">
                    <div class="card">
                        <div class="rounded-top text-white d-flex flex-row cover">
                            <div class="ms-4 mt-5 d-flex flex-column" style="width: 150px;">
                                <!-- Profile image -->
                                <img src="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/626fd8140423801.6241b91e24d9c.png"
                                    alt="Generic placeholder image" class="img-fluid img-thumbnail mt-4 mb-2"
                                    style="width: 150px; z-index: 1">

                                <!-- Edit profile button -->
                                <button type="button" class="btn btn-outline-dark" data-mdb-ripple-color="dark"
                                    style="z-index: 1;">
                                    Edit profile
                                </button>
                            </div>

                            <!-- Displayed name and username -->
                            <div class="ms-3" style="margin-top: 130px;">
                                <h5>Displayed Name</h5>
                                <p>@username</p>
                            </div>
                        </div>
                        <div class="p-4 text-black" style="background-color: #f8f9fa;">
                            <div class="d-flex justify-content-end text-center py-1">
                                <div>
                                    <p class="mb-1 h5">17</p>
                                    <p class="small text-muted mb-0">Questions posted</p>
                                </div>
                                <div class="px-3">
                                    <p class="mb-1 h5">40</p>
                                    <p class="small text-muted mb-0">Answers given</p>
                                </div>
                                <div>
                                    <p class="mb-1 h5">18</p>
                                    <p class="small text-muted mb-0">Best answer</p>
                                </div>
                                <div class="px-4">
                                    <p class="mb-1 h5">361</p>
                                    <p class="small text-muted mb-0">Score</p>
                                </div>
                                
                            </div>
                        </div>
                        <div class="card-body p-4 text-black">
                            <div class="mb-5">
                                <p class="lead fw-normal mb-1">About</p>
                                <div class="p-4" style="background-color: #f8f9fa;">
                                    <p class="font-italic mb-1"> [Aci campul "description" de la fiecare user] --- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Perferendis magnam laborum iure neque enim accusantium vero. Laudantium nisi itaque ipsam delectus beatae maiores eveniet perferendis. Delectus velit minima temporibus. Adipisci!</p>
                                    <hr>
                                    <p class="font-italic mb-1">Birthday: 10/04/2000</p>
                                </div>
                            </div>
                            <!-- <div class="d-flex justify-content-between align-items-center mb-4">
                                <p class="lead fw-normal mb-0">Recent photos</p>
                                <p class="mb-0"><a href="#!" class="text-muted">Show all</a></p>
                            </div> -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

</template>

<script>

export default {
    name: 'ProfileView',
    components: {
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
background: linear-gradient(to right, rgb(194, 217, 251), rgb(185, 166, 238))
}

</style>
