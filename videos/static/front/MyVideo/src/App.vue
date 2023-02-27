<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <RouterLink class="nav-link" to="/">Главная страница</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/">О сайте</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <RouterView />
  <div class="footer text-center bg-light">
    <span>Вход для админа: </span>
    <a class="link me-1">Wagtail</a>
    <a class="link">Django</a>
  </div>
</template>

<style>

</style>
