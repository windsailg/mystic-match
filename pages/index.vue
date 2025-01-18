<script setup>
const data = reactive({
  content: '',
  tab: null,
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
  isOtherRecommand: false,
  // Camera Setting
  usingBackCamera: false,
  canvas: null,
  video: null,
  stream: null,
  isStreaming: false,
  capturedImage: null,
  autoCaptureInterval: null,
  // info message
  snackbar: false,
  message: '',
})
const {
  tab,
  content,
  responseData,
  isFetch,
  isProcessing,
  userInput,
  fitList,
  styleList,
  typeList,
  colorList,
  isOtherRecommand,
  // Camera
  usingBackCamera,
  canvas,
  video,
  stream,
  isStreaming,
  capturedImage,
  autoCaptureInterval,
  snackbar,
  message,
} = toRefs(data)
// # 衣服數據庫 服裝圖片標籤
// # 1.合身 2.寬鬆 Fit
// # 1.日系 2.韓系 Style
// # 1.休閒 2.正式 Type
// # 1.藍 2.白 3.紅 4.綠 5.黑 (五個之前的顏色) (color)

const methods = {
  postData: async () => {
    resetData()
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
      responseData.value = response.result
      isProcessing.value = false
      sendMessage('推薦完成，以下是您的推薦列表')
    } catch (error) {
      console.warn(error)
      sendMessage('影像上傳失敗！')
    } finally {
      isFetch.value = true
    }
  },
  toggleOtherRecommand: () => {
    data.isOtherRecommand = true
  },
  resetData: () => {
    data.isFetch = false
    data.isOtherRecommand = false
  },
  // Camera Function
  openCamera: async () => {
    // stopCamera()
    try {
      const constraints = {
        video: {
          facingMode: data.usingBackCamera ? 'environment' : 'user',
        },
      }
      data.stream = await navigator.mediaDevices.getUserMedia(constraints)
      video.value.srcObject = data.stream
      data.isStreaming = true
      console.warn('相機啟動成功')
    } catch (error) {
      console.error('無法啟動相機', error)
      console.warn('相機啟動失敗，請檢查權限或設備是否支持！')
    }
  },
  stopCamera: () => {
    if (data.stream) {
      const tracks = stream.value.getTracks()
      tracks.forEach((track) => track.stop())
      data.stream = null
    }
    data.isStreaming = false
    console.warn('相機已停止')
  },
  captureImage: () => {
    if (!data.isStreaming) {
      console.warn('相機尚未啟動')
      return
    }
    const context = canvas.value.getContext('2d')
    const size = Math.min(video.value.videoWidth, video.value.videoHeight)
    // 保持1:1比例
    canvas.value.width = size
    canvas.value.height = size
    context.drawImage(
      video.value,
      (video.value.videoWidth - size) / 2,
      (video.value.videoHeight - size) / 2,
      size,
      size,
      0,
      0,
      size,
      size,
    )
    capturedImage.value = canvas.value.toDataURL('image/png')
    console.warn('照片已拍攝')
  },
  captureAndUploadImage: async () => {
    captureImage()
    if (capturedImage.value) {
      await uploadImage()
    }
  },
  uploadImage: async () => {
    try {
      // 將使用者數據包成請求送入後端
      const res = await $fetch('/api/image', {
        method: 'POST',
        body: { image: capturedImage.value },
      })
      responseData.value = res.result
      isProcessing.value = false
      sendMessage('推薦完成，以下是您的推薦列表')
    } catch (error) {
      console.error('影像上傳失敗', error)
      sendMessage('拍照上傳失敗，請聯絡開發人員')
    } finally {
      isProcessing.value = false
      isFetch.value = true
      isStreaming.value = false
    }
  },
  sendMessage: (content) => {
    snackbar.value = true
    message.value = content
    setTimeout(() => {
      snackbar.value = false
    }, 5000)
  },
}
const {
  postData,
  toggleOtherRecommand,
  resetData,
  openCamera,
  stopCamera,
  captureImage,
  captureAndUploadImage,
  uploadImage,
  sendMessage,
} = methods

onMounted(async () => {
  this.$colorMode.preference = 'light'
})
</script>

<template>
  <div
    class="flex mt-20 py-10 mx-auto p-2 justify-center items-center sm:w-100 md:1/2 lg:max-w-4xl"
  >
    <div class="w-100">
      <h2
        class="flex text-4xl md:text-5xl font-sfbold text-center justify-center text-sky-950"
      >
        Welcome to Mystic Match
      </h2>
      <h2
        class="flex text-l md:text-2xl justify-center text-center mx-2 text-sky-950"
      >
        Artifical Intellgence Virtual Styling Service
      </h2>
      <h3 class="flex text-2xl text-center justify-center my-2 text-sky-950">
        ✨ AI 虛 擬 穿 搭 服 務
      </h3>
      <span class="flex text-lg my-4 text-center justify-center text-sky-950">
        選擇喜好風格，或拍照上傳，來讓 AI 推薦你最適合的穿著
      </span>
      <v-row class="justify-center text-center pt-8 pb-6">
        <div class="mx-6 w-100 text-center user__input">
          <!-- 選擇操作類型 -->
          <v-card class="elevation-20 rounded-xl">
            <v-overlay
              :model-value="isProcessing"
              class="align-center justify-center"
              contained
            >
              <v-progress-circular
                color="secondary"
                size="64"
                indeterminate
              ></v-progress-circular>
            </v-overlay>
            <v-tabs v-model="tab" bg-color="secondary" class="" fixed-tabs>
              <v-tab value="one">
                <v-icon icon="mdi-heart" class="text-sky-900"></v-icon>
                <div class="font-bold text-lg text-sky-900 py-2">
                  選取風格喜好
                </div>
              </v-tab>
              <v-tab value="two">
                <v-icon icon="mdi-camera" class="text-sky-900"></v-icon>
                <div class="font-bold text-lg text-sky-900 py-2">拍照上傳</div>
              </v-tab>
            </v-tabs>

            <v-card-text>
              <v-tabs-window v-model="tab" fixed-tabs>
                <v-tabs-window-item value="one">
                  <v-stepper
                    :items="['Step 1', 'Step 2', 'Step 3', 'Step 4']"
                    class="elevation-1"
                  >
                    <v-stepper-header></v-stepper-header>
                    <!-- class="font-black text-sky-600" -->
                    <template #[`item.1`]>
                      <v-card flat>
                        <v-card-title class="font-sfbold text-sky-800">
                          選擇喜好版型
                        </v-card-title>
                        <v-card-text class="flex justify-center">
                          <v-select
                            v-model="userInput.fit"
                            :items="fitList"
                            class="user__input__field"
                            hide-details
                            item-title="title"
                            item-value="value"
                            label="選擇喜歡的版型"
                            variant="outlined"
                            return-value
                            single-line
                          ></v-select>
                        </v-card-text>
                      </v-card>
                    </template>

                    <template #[`item.2`]>
                      <v-card flat>
                        <v-card-title class="font-sfbold text-sky-800">
                          選擇喜好風格
                        </v-card-title>
                        <v-select
                          v-model="userInput.style"
                          :items="styleList"
                          class="user__input__field"
                          hide-details
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
                      <v-card flat>
                        <v-card-title class="font-sfbold text-sky-800">
                          選擇穿著場域
                        </v-card-title>
                        <v-select
                          v-model="userInput.type"
                          :items="typeList"
                          class="user__input__field"
                          hide-details
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
                      <v-card flat>
                        <v-card-title class="font-bold text-sky-800">
                          選擇喜好色彩
                        </v-card-title>
                        <v-select
                          v-model="userInput.color"
                          :items="colorList"
                          class="user__input__field"
                          hide-details
                          item-title="title"
                          item-value="value"
                          label="選擇喜歡的色彩"
                          persistent-hint
                          variant="outlined"
                          return-value
                          single-line
                        ></v-select>
                        <v-btn
                          class="mt-6 rounded-lg green--text lighten-2"
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
                </v-tabs-window-item>

                <v-tabs-window-item value="two">
                  <div v-show="isStreaming" class="video-container w-100">
                    <video
                      ref="video"
                      class="w-100 video__main"
                      autoplay
                      playsinline
                    ></video>
                    <canvas ref="canvas" style="display: none;"></canvas>
                  </div>
                  <v-btn
                    v-show="!isStreaming"
                    class="my-6 rounded-lg green--text lighten-2"
                    color="secondary"
                    elevation="0"
                    size="x-large"
                    block
                    append-icon="mdi:mdi-camera"
                    :loading="isProcessing"
                    :disabled="isProcessing"
                    @click="openCamera"
                  >
                    開啟相機
                  </v-btn>
                  <v-btn
                    v-show="isStreaming"
                    class="my-4 rounded-lg green--text lighten-2"
                    color="grey"
                    elevation="0"
                    size="x-large"
                    block
                    append-icon="mdi:mdi-close-circle"
                    :loading="isProcessing"
                    :disabled="isProcessing"
                    @click="stopCamera"
                  >
                    關閉相機
                  </v-btn>
                  <v-btn
                    v-show="isStreaming"
                    class="my-4 rounded-lg green--text lighten-2"
                    color="secondary"
                    elevation="0"
                    size="x-large"
                    block
                    append-icon="mdi:mdi-send-circle"
                    :loading="isProcessing"
                    :disabled="!isStreaming"
                    @click="captureAndUploadImage"
                  >
                    拍照並上傳
                  </v-btn>
                </v-tabs-window-item>
              </v-tabs-window>
            </v-card-text>
          </v-card>
        </div>
      </v-row>
      <v-row class="justify-center text-center pb-2 mx-2 mb-10">
        <h5 class="my-4 w-100">
          <v-card v-show="isFetch" class="rounded-xl elevation-20">
            <v-overlay
              :model-value="isProcessing"
              class="align-center justify-center"
              contained
            >
              <v-progress-circular
                color="secondary"
                size="64"
                indeterminate
              ></v-progress-circular>
            </v-overlay>
            <v-card-text class="pb-10">
              <v-list v-if="!isFetch"></v-list>
              <v-list v-else class="text-center">
                <v-list-item class="text-lg my-4">
                  {{ responseData.comments }}
                </v-list-item>
                <v-list-item class="my-10">
                  <v-img
                    class="elevation-1 rounded-xl"
                    max-width="600"
                    :src="responseData.mainRecommand"
                  />
                </v-list-item>
                <v-btn
                  v-show="!isOtherRecommand"
                  class="rounded-lg green--text lighten-2 mb-8"
                  color="secondary"
                  elevation="0"
                  size="x-large"
                  append-icon="mdi:mdi-account-search"
                  :loading="isProcessing"
                  :disabled="isProcessing"
                  @click="toggleOtherRecommand"
                >
                  查看其他推薦穿搭列表
                </v-btn>
                <v-list-item
                  v-show="isOtherRecommand"
                  v-for="img in responseData.recommandList"
                  :key="img"
                >
                  <v-img
                    class="elevation-1 rounded-xl my-6"
                    max-width="600"
                    :src="img"
                  />
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
        </h5>
      </v-row>
    </div>
    <v-snackbar v-model="snackbar" multi-line>
      <div class="text-lg font-bold">{{ message }}</div>
      <template v-slot:actions>
        <v-btn @click="snackbar = false">
          <v-icon color="white" size="large">mdi:mdi-close-circle</v-icon>
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<style lang="sass">
.v-slide-group
  height: 70px !important
  align-items: center
.v-slide-group__content
  .v-btn
    height: 70px !important
.v-stepper-header
  display: none !important
.user__input
  .v-field__input
    display: block !important

.v-list-item__content
  display: flex !important
  justify-content: center !important
.user__input__field
  display: flex !important
  justify-content: center !important
  .v-input__control
    width: 60%

// Camera Page
.camera-page
  text-align: center
  display: flex
  flex-direction: column
  align-items: center
  justify-content: center
  min-height: 100vh
  padding: 20px

.video-container
  display: flex
  justify-content: center
  align-items: center
  width: 100%
  position: relative
  border: 1px solid #ccc
  background-color: #000

video
  max-width: 100%
  max-height: 350px
  object-fit: contain

.controls
  margin-top: 20px

button
  margin: 5px
  padding: 10px 20px
  font-size: 16px
  cursor: pointer

  &:disabled
    background-color: #ddd
    cursor: not-allowed

.message-box
  margin-top: 20px
  padding: 10px

  /* background-color: #f0f8ff;
  border: 1px solid #fff
  border-radius: 5px
  font-size: 16px
</style>
