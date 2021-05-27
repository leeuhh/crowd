//app.js
App({
  onLaunch(){
    console.log('小程序启动')
    wx.cloud.init({
      env: 'cloud1-1gsabdsx6a087c46'
    })
  },


  globalData: {
     url: 'http://localhost:8080/supership/superadmin/',
  }
})