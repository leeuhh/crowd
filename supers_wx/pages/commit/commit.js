const app = getApp();
const url = app.globalData.url;
Page({

  /**
   * 页面的初始数据
   */
  data: {
    imagepath: "",
    address: "",
    number: 0


  },
  tap: function () {
    var that = this
    wx.chooseImage({
      count: 1, // 默认9
      sizeType: ['compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: res => {
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        that.setData({
          imagepath: res.tempFilePaths,
        })
      }
    })

  },

  showimage: function () {
    wx.previewImage({
      urls: this.data.imagepath
    })

  },
  setAddress: function (e) {
    this.setData({
      address: e.detail.value
    })
  },

  tosubmit: function () {
    if (this.data.address == "" || this.data.imagepath == "") {
      wx.showToast({
        title: '信息不完整',
        icon: "none"
      })
    } else {

      this.upload()

    }
  },

  upload: function () {
    var that = this

    wx.uploadFile({
      filePath: that.data.imagepath[0],
      name: 'file',
      url: "http://localhost:8080/supership/superadmin/photos",
      header: {
        "Content-Type": "multipart/form-data"
      },
      success: function (res) {

        var path = JSON.parse(res.data).target;
        wx.request({
          url: "http://localhost:8080/supership/superadmin/getcontent",
          method: "get",
          data: {
            address: that.data.address,
            imagepath: path
          },
          success: function (res) {
            console.log(res.data)
            that.setData({
              number: res.data.number
            })
          }
        })

      },
    })

  }


})