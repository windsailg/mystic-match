<template>
    <header class="fixed w-full top-0 z-10 backdrop-blur-md">
      <nav class="max-w-7xl mx-auto flex p-5 justify-between">
        <div class="flex">
          <NuxtLink to="/">
            <img src="/logo.png" class="w-30 h-8">
          </NuxtLink>
          
        </div>
        <!-- <Switch class="flex"/> -->
      </nav>

      <!-- <MobileMenu class="hidden mobile-menu" /> -->

    </header>
  </template>

<script>

  export default {

    methods: {
      toggleMobileMenu(){
        // Toggle mobile menu
        document.querySelector('.mobile-menu').classList.toggle('hidden')
        
      }
    }
  }

</script>
  
<style>

</style>