<<<<<<< HEAD
<template>
  <div class="flex">

    <section class="flex max-w-7xl mx-auto p-5 justify-center h-screen items-center">

=======
<script setup>
const data = reactive({
  content: '',
  responseData: {
    comments: '',
    mainRecommand: '',
    recommandList: [],
  },
  isFetch: false,
})
const { content, responseData, isFetch } = toRefs(data)

const methods = {
  postData: async () => {
    try {
      const data = {
        content: 'something',
      }
      const options = {
        method: 'POST',
        body: data,
      }
      const res = await fetch('/api/data', options)
      const response = await res.json()
      responseData.value = response.result
    } catch (error) {
      console.warn(error)
    } finally {
      isFetch.value = true
    }
  },
}
const { postData } = methods

onMounted(async () => {})
</script>

<template>
  <div class="flex">
    <section
      class="flex mt-20 py-10 max-w-7xl mx-auto p-5 justify-center items-center"
    >
>>>>>>> 8ca2512 (mv all dev to web_src/)
      <div>
        <span class="flex text-xl md:text-3xl justify-center">
          Welcome to
        </span>
        <h1 class="flex text-4xl md:text-7xl font-sfbold justify-center">
<<<<<<< HEAD
          {{ $t('title') }}
        </h1>
        <h2 class="flex text-xl md:text-2xl justify-center m-2">
          {{ $t('subtitle') }}
        </h2>
        <div class="flex justify-center">
          <libraryButtonNuxt value="About" to='/about' class="m-2"/>
        </div>
      </div>

    </section>
  </div>
</template>

=======
          Mystic Match
        </h1>
        <h2 class="flex text-xl md:text-2xl justify-center m-2">
          Artifical Intellgence Virtual Styling Service
        </h2>
        <h3 class="flex text-xl justify-center">
          ✨ AI 虛 擬 穿 搭 服 務
        </h3>
        <div class="flex justify-center my-4">
          <v-btn
            class="m-2"
            color="primary"
            variant="outlined"
            @click="postData"
          >
            發送使用者數據
          </v-btn>
        </div>
        <h5 class="my-4">
          <v-card v-show="isFetch">
            <v-card-text>
              <v-list v-if="!isFetch"></v-list>
              <v-list v-else>
                <v-list-item class="text-title" max-width="600">
                  {{ responseData.comments }}
                </v-list-item>
                <v-list-item>
                  <v-img max-width="600" :src="responseData.mainRecommand" />
                </v-list-item>
                <v-list-item
                  v-for="img in responseData.recommandList"
                  :key="img"
                >
                  <v-img max-width="600" :src="img" />
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
        </h5>
      </div>
    </section>
  </div>
</template>
>>>>>>> 8ca2512 (mv all dev to web_src/)
