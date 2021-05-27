// pages/people/people.js
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad() {
    //es6写法
    wx.cloud.database().collection('test')
    .where({
      id_building: 1,
      id_date: 1,
      id_room: 2,
      id_time: 0
    })
    .get()
    .then(res => {
      console.log('返回的数据', res)
      console.log('返回的人数', res.data[0].id_number)
      this.setData({
        list: res.data
      })
    })
    .catch(err => {
      console.log('请求失败', err)
    })

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})