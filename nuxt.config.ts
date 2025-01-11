const siteTitle = 'Mystic Match - AI 穿搭服務'

/*
 * Nuxt 3 Config File
 Usage: https://nuxt.com/docs/api/configuration/nuxt-config
 */
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'
export default defineNuxtConfig({
  experimental: { appManifest: false},
  ssr: false,
  build: {
    transpile: ['vuetify']
  },
  nitro: { output: { publicDir: 'dist' } },
  app: {
    head: {
      title: siteTitle, // App window nav title

      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'theme-color', content: '#353535' }
        // ...
      ],
      link: [
        { rel: 'manifest', href: 'pwa/manifest.json' },
        { rel: 'apple-touch-icon', href: 'pwa/icons/apple-touch-icon.png' }
      ]
    },
    pageTransition: { name: 'page', mode: 'out-in' }
  },

  modules: [
    (_options, nuxt) => {
      nuxt.hooks.hook('vite:extendConfig', config => {
        // @ts-expect-error
        config.plugins.push(vuetify({ autoImport: true }))
      })
    },
    'nuxt-icon',
    '@nuxtjs/i18n',
    '@nuxt/content',
    '@nuxtjs/color-mode',
    '@nuxtjs/tailwindcss'
  ],
  components: {
    dirs: ['~/components', '~/components/library']
  },

  tailwindcss: {
    cssPath: '~/assets/tailwind.css',
    configPath: 'tailwind.config',
    exposeConfig: true, // true to resolve the tailwind config in runtime. https://tailwindcss.nuxt.dev/getting-started/options/#exposeconfig
    injectPosition: 0,
    viewer: true // set up the /_tailwind/ route. (Disable in production) https://tailwindcss.nuxt.dev/getting-started/options/#viewer
  },

  i18n: {
    defaultLocale: 'en',
    detectBrowserLanguage: false,
    langDir: 'lang/',
    lazy: true,
    locales: [
      {
        code: 'es',
        file: 'es.json',
        iso: 'es-ES',
        name: 'Español'
      },
      {
        code: 'en',
        file: 'en.json',
        iso: 'en-US',
        name: 'English'
      }
    ]
  },

  colorMode: {
    classSuffix: ''
  },

  vite: {
    vue: {
      // template: {
      //   transformAssetUrls
      // }
    }
  },

  runtimeConfig: {
    // The private keys which are only available server-side
    apiSecret: '123',
    // Keys within public are also exposed client-side
    public: {
      apiBase: '/api'
    }
  },

  compatibilityDate: '2025-01-01'
})
