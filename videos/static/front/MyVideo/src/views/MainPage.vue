<script setup>
</script>

<template>


<main class="container">
    <div class="row g-3 m-3">
        <div class="col-sm-6" v-for="video in videos">
            <div class="card">
                <img :src="get_url(video.image)" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title" v-text="video.title"></h5>
                    <p class="card-text" v-text="video.description"></p>
                </div>
            </div>
        </div>
    </div>
</main>




</template>

<style>

</style>


<script>
export default {
  data() {
    return { videos: [] }
  },
  async created() {
    const url = "https://8000-denisgr-myvideo-x5gkonzz9sw.ws-eu88.gitpod.io/api/videos.json"
    const response = await fetch(url)
    this.videos = await response.json()
    console.log(this.videos)
  },
  methods: {
    get_url: (url) => "https://8000-denisgr-myvideo-x5gkonzz9sw.ws-eu88.gitpod.io/" + (url || "///").split("/").slice(3).join("/"),
  },
}
</script>