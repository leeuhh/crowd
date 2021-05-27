// pages/test/test.js

const db = wx.cloud.database()
Page({
  data: {
    tempImg: [],
    fileIDs: [],
    tmp: {},
    selectArray: [{
      "id": "10",
      "text": "会计类"
    }, {
      "id": "21",
      "text": "工程类"
    }]
  },

  getDate:function(e){
    console.log(e.detail)
    this.data.tmp = e.detail
  },

  uploadImgHandle: function () {
    wx.chooseImage({
      count: 9,
      sizeType: ['original', 'compressed'],
      sourceType: ['album', 'camera'],
      success:res=> {
        // tempFilePath可以作为img标签的src属性显示图片
        const tempFilePaths = res.tempFilePaths
        this.setData({
          tempImg: tempFilePaths
        })
      }
    })
  },

  submit: function () {
    wx.showLoading({
      title: '提交中',
    })
    const promiseArr = []
    //只能一张张上传 遍历临时的图片数组
    for (let i = 0; i < this.data.tempImg.length;i++) {
      let filePath = this.data.tempImg[i]
      let suffix = /\.[^\.]+$/.exec(filePath)[0]; // 正则表达式，获取文件扩展名
      //在每次上传的时候，就往promiseArr里存一个promise，只有当所有的都返回结果时，才可以继续往下执行
      promiseArr.push(new Promise((reslove,reject)=>{
        wx.cloud.uploadFile({
          cloudPath: new Date().getTime() + suffix,
          filePath: filePath, // 文件路径
        }).then(res => {
          // get resource ID
          console.log(res.fileID)
          console.log(this.data.tmp)
          this.setData({
            building: 0,
            room: 1,
            date: 2,
            number: 3,
            no: i,
            fileIDs: this.data.fileIDs.concat(res.fileID)
          })
          reslove()
        }).catch(error => {
          console.log(error)
        })
      }))
    }
    Promise.all(promiseArr).then(res=>{
      for (let i = 0; i < this.data.tempImg.length;i++) {
        db.collection('pics').add({
          data: {

            building: this.data.building,
            room: this.data.room,
            date: this.data.date,
            number: this.data.number,
            no: i,

            fileIDs: this.data.fileIDs[i] //只有当所有的图片都上传完毕后，这个值才能被设置，但是上传文件是一个异步的操作，你不知道他们什么时候把fileid返回，所以就得用promise.all
          }
        })
        .then(res => {
          console.log(res)
          wx.hideLoading()
          wx.showToast({
            title: '提交成功',
          })
        })
        .catch(error => {
          console.log(error)
        })
      }
    })
  }
})












