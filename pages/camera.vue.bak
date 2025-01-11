<template>
  <div class="camera-page">
    <h1>影像串流與拍照功能</h1>
    <div class="video-container">
      <video ref="video" autoplay playsinline></video>
      <canvas ref="canvas" style="display: none;"></canvas>
    </div>
    <div class="controls">
      <button class="bg-white border-black" @click="startCamera">開始串流</button>
      <button class="bg-white border-black" @click="stopCamera" :disabled="!isStreaming">停止串流</button>
      <button class="bg-white border-black" @click="switchCamera" :disabled="!hasMultipleCameras">切換鏡頭</button>
      <button class="bg-white border-black" @click="captureAndUploadImage" :disabled="!isStreaming">拍照並上傳</button>
      <!-- <button class="bg-white border-black" @click="startAutoCapture" :disabled="!isStreaming || isAutoCapturing">每秒拍照一次</button>
      <button class="bg-white border-black" @click="stopAutoCapture" :disabled="!isAutoCapturing">停止自動拍照</button> -->
    </div>
    <div v-if="message" class="message-box">
      <p class="text-red-600">{{ message }}</p>
    </div>
    <div v-if="capturedImage">
      <h3>拍攝結果</h3>
      <img :src="capturedImage" alt="Captured Image" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const video = ref(null);
const canvas = ref(null);
const capturedImage = ref(null);
const isStreaming = ref(false);
const hasMultipleCameras = ref(false);
const usingBackCamera = ref(false);
const isAutoCapturing = ref(false);
const message = ref(null);
let stream = null;
let autoCaptureInterval = null;

const displayMessage = (text) => {
  message.value = text;
  setTimeout(() => {
    message.value = null;
  }, 3000);
};

const checkCameraAvailability = async () => {
  try {
    const devices = await navigator.mediaDevices.enumerateDevices();
    const videoDevices = devices.filter(device => device.kind === 'videoinput');
    hasMultipleCameras.value = videoDevices.length > 1;
  } catch (error) {
    console.error('無法檢查相機可用性', error);
  }
};

const startCamera = async () => {
  stopCamera();

  try {
    const constraints = {
      video: {
        facingMode: usingBackCamera.value ? 'environment' : 'user',
      },
    };
    stream = await navigator.mediaDevices.getUserMedia(constraints);
    video.value.srcObject = stream;
    isStreaming.value = true;
    displayMessage('相機啟動成功');
  } catch (error) {
    console.error('無法啟動相機', error);
    displayMessage('相機啟動失敗，請檢查權限或設備是否支持！');
  }
};

const stopCamera = () => {
  if (stream) {
    const tracks = stream.getTracks();
    tracks.forEach(track => track.stop());
    stream = null;
  }
  isStreaming.value = false;
  displayMessage('相機已停止');
};

const switchCamera = () => {
  usingBackCamera.value = !usingBackCamera.value;
  startCamera();
};

const captureImage = () => {
  if (!video.value || !isStreaming.value) {
    displayMessage('相機尚未啟動');
    return;
  }

  const context = canvas.value.getContext('2d');
  const size = Math.min(video.value.videoWidth, video.value.videoHeight); // 保持1:1比例
  canvas.value.width = size;
  canvas.value.height = size;
  context.drawImage(
    video.value,
    (video.value.videoWidth - size) / 2,
    (video.value.videoHeight - size) / 2,
    size,
    size,
    0,
    0,
    size,
    size
  );
  capturedImage.value = canvas.value.toDataURL('image/png');
  displayMessage('照片已拍攝');
};

const uploadImage = async () => {
  if (!capturedImage.value) {
    displayMessage('請先拍照！');
    return;
  }
  try {
    const response = await $fetch('/api/upload', {
      method: 'POST',
      body: { image: capturedImage.value },
    });
    displayMessage('影像已成功上傳！');
    console.log('上傳路徑:', response.path);
  } catch (error) {
    console.error('影像上傳失敗', error);
    displayMessage('影像上傳失敗！');
  }
};

const captureAndUploadImage = async () => {
  captureImage();
  if (capturedImage.value) {
    await uploadImage();
  }
};

const startAutoCapture = () => {
  isAutoCapturing.value = true;
  autoCaptureInterval = setInterval(() => {
    captureImage();
    uploadImage();
  }, 1000);
  displayMessage('開始每秒自動拍照');
};

const stopAutoCapture = () => {
  isAutoCapturing.value = false;
  clearInterval(autoCaptureInterval);
  autoCaptureInterval = null;
  displayMessage('已停止自動拍照');
};

onMounted(() => {
  checkCameraAvailability();
  startCamera();
});

onBeforeUnmount(() => {
  stopCamera();
  stopAutoCapture();
});
</script>

<style>
.camera-page {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 20px;
}

.video-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  max-width: 600px;
  height: auto;
  position: relative;
  border: 1px solid #ccc;
  background-color: #000;
}

video {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
}

.controls {
  margin-top: 20px;
}

button {
  margin: 5px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

button:disabled {
  background-color: #ddd;
  cursor: not-allowed;
}

.message-box {
  margin-top: 20px;
  padding: 10px;
  /* background-color: #f0f8ff; */
  border: 1px solid #fff;
  border-radius: 5px;
  font-size: 16px;
}
</style>