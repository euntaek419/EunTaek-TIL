module.exports = {
  pwa: {
    name: 'vuesta',
    themeColor: '#4DBA87',
    msTileColor: '#000000',
    workboxOptions: {
      exclude: [/\.map$/, /manifest\.json$/, 'index.html']
    }
  }
}

const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
