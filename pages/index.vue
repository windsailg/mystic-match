<script setup>
const data = reactive({
  content: '',
  responseData: {
    comments: '',
    mainRecommand: '',
    recommandList: [],
  },
  isFetch: false,
  isProcessing: false,
})
const { content, responseData, isFetch, isProcessing } = toRefs(data)

const methods = {
  postData: async () => {
    isProcessing.value = true
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
      setTimeout(() => {
        responseData.value = response.result
        isProcessing.value = false
      }, 1500)
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
      <div class="justify-center">
        <h2 class="flex text-4xl md:text-5xl font-sfbold text-center justify-center text-sky-950">
          Welcome to Mystic Match
        </h2>
        <h2 class="flex text-xl md:text-2xl justify-center text-center m-2 text-sky-950">
          Artifical Intellgence Virtual Styling Service
        </h2>
        <h3 class="flex text-xl text-center justify-center text-sky-950">
          ✨ AI 虛 擬 穿 搭 服 務
        </h3>
        <span class="flex text-lg my-4 text-center justify-center text-sky-950">
          點選發送使用者參數，讓 AI 推薦你最適合的穿著
        </span>
        <div class="flex justify-center my-4">
          <v-btn
            class="m-2 rounded-lg green--text lighten-2 "
            color="secondary"
            elevation="0"
            size="x-large"
            append-icon="mdi:mdi-send-circle"
            :loading="isProcessing"
            :disabled="isProcessing"
            @click="postData"
          >
            發送使用者參數
          </v-btn>
        </div>
        <h5 class="my-4">
          <v-card v-show="isFetch">
            <v-card-text>
              <v-list v-if="!isFetch"></v-list>
              <v-list v-else>
                <v-list-item class="text-title my-4" max-width="600">
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
