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
  userInput: {
    fit: 1,
    style: 1,
    type: 1,
    color: 3,
    // height: 170,
    // weight: 60,
  },
  fitList: [
    { title: '合身', value: 1 },
    { title: '寬鬆', value: 2 },
  ],
  styleList: [
    { title: '日系', value: 1 },
    { title: '韓系', value: 2 },
  ],
  typeList: [
    { title: '休閒', value: 1 },
    { title: '正式', value: 2 },
  ],
  colorList: [
    { title: '藍', value: 1 },
    { title: '白', value: 2 },
    { title: '紅', value: 3 },
    { title: '綠', value: 4 },
    { title: '黑', value: 5 },
  ],
})
const {
  content,
  responseData,
  isFetch,
  isProcessing,
  userInput,
  fitList,
  styleList,
  typeList,
  colorList,
} = toRefs(data)
// # 衣服數據庫 服裝圖片標籤
// # 1.合身 2.寬鬆 Fit
// # 1.日系 2.韓系 Style
// # 1.休閒 2.正式 Type
// # 1.藍 2.白 3.紅 4.綠 5.黑 (五個之前的顏色) (color)

const methods = {
  postData: async () => {
    isProcessing.value = true
    try {
      // 將使用者數據包成請求送入後端
      const data = userInput.value
      const options = {
        method: 'POST',
        body: JSON.stringify(data),
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
  <div class="flex mt-20 py-10 mx-auto p-2 justify-center items-center w-2/3">
    <div class="w-100">
      <h2
        class="flex text-4xl md:text-5xl font-sfbold text-center justify-center text-sky-950"
      >
        Welcome to Mystic Match
      </h2>
      <h2
        class="flex text-xl md:text-2xl justify-center text-center m-2 text-sky-950"
      >
        Artifical Intellgence Virtual Styling Service
      </h2>
      <h3 class="flex text-xl text-center justify-center text-sky-950">
        ✨ AI 虛 擬 穿 搭 服 務
      </h3>
      <span class="flex text-lg my-4 text-center justify-center text-sky-950">
        點選發送使用者參數，讓 AI 推薦你最適合的穿著
      </span>
      <div v-show="false" class="flex justify-center my-4">
        <!-- 設定使用者數據 -->
        <!-- <v-text-field></v-text-field> -->
      </div>
      <v-row class="justify-center text-center pt-8 pb-6">
        <div class="mx-4 sm:w-screen md:w-2/3 lg:w-1/2">
          <v-stepper :items="['Step 1', 'Step 2', 'Step 3', 'Step 4']">
            <v-stepper-header></v-stepper-header>

            <template #[`item.1`]>
              <v-card title="選擇喜好版型" flat>
                <v-select
                  v-model="userInput.fit"
                  :items="fitList"
                  item-title="title"
                  item-value="value"
                  label="選擇喜歡的版型"
                  persistent-hint
                  variant="outlined"
                  return-value
                  single-line
                ></v-select>
              </v-card>
            </template>

            <template #[`item.2`]>
              <v-card title="選擇喜好風格" flat>
                <v-select
                  v-model="userInput.style"
                  :items="styleList"
                  item-title="title"
                  item-value="value"
                  label="選擇喜歡的風格"
                  persistent-hint
                  variant="outlined"
                  return-value
                  single-line
                ></v-select>
              </v-card>
            </template>

            <template #[`item.3`]>
              <v-card title="選擇穿著場域" flat>
                <v-select
                  v-model="userInput.type"
                  :items="typeList"
                  item-title="title"
                  item-value="value"
                  label="選擇穿著場域"
                  persistent-hint
                  variant="outlined"
                  return-value
                  single-line
                ></v-select>
              </v-card>
            </template>

            <template #[`item.4`]>
              <v-card title="選擇喜好色彩" flat>
                <v-select
                  v-model="userInput.color"
                  :items="colorList"
                  item-title="title"
                  item-value="value"
                  label="選擇喜歡的色彩"
                  persistent-hint
                  variant="outlined"
                  return-value
                  single-line
                ></v-select>
                <v-btn
                  class="m-2 rounded-lg green--text lighten-2"
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
              </v-card>
            </template>

            <!-- <v-stepper-actions
              :disabled="disabled"
              @click:next="下一步"
              @click:prev="上一步"
            ></v-stepper-actions> -->

          </v-stepper>
        </div>
      </v-row>
      <v-row class="justify-center text-center pb-2">
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
      </v-row>
    </div>
  </div>
</template>

<style lang="sass">
.v-stepper-header
  display: none !important
</style>
