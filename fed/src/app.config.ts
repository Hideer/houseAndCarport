export default defineAppConfig({
  pages: [
    'pages/index/index',
    'pages/mine/index',
  ],
  window: {
    backgroundTextStyle: 'light',
    navigationBarBackgroundColor: '#fff',
    navigationBarTitleText: 'WeChat',
    navigationBarTextStyle: 'black'
  },
  permission: {
    "scope.userLocation": {
      desc: '需要用到你的位置信息'
    }
  },
  requiredPrivateInfos: ["getLocation", "choosePoi"]
})
