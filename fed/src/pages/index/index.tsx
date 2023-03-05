import { Component, PropsWithChildren } from "react";
import {
  Tabbar,
  TabbarItem,
  WaterMark,
  Button,
  Popup,
  Cell,
  Tabs
} from "@nutui/nutui-react-taro";
import Taro from '@tarojs/taro';
import NavigationBar from './components/navigation-bar'
import DataList from './components/data-list'
import Map from './components/map'
import FooterBabar from './../../components/footer-tabbar'

import './index.scss'

class Index extends Component<PropsWithChildren> {
  constructor(props: any) {
    super(props);
    this.state = {
      blackBarHight: 0,
      navigationBarAndStatusBarHeight: 0,
    }
  }

  componentDidMount() {
    this.initBar();

  }

  componentWillUnmount() { }

  componentDidShow() { }

  componentDidHide() { }

  initBar() {
    const { statusBarHeight, platform, screenHeight, safeArea } = Taro.getSystemInfoSync()
    const { top, height } = Taro.getMenuButtonBoundingClientRect()
    const blackBarHight = screenHeight - safeArea!.bottom

    // 状态栏高度
    Taro.setStorageSync('statusBarHeight', statusBarHeight)
    // 胶囊按钮高度 一般是32 如果获取不到就使用32
    Taro.setStorageSync('menuButtonHeight', height ? height : 32)
    // 底部黑条的高度
    Taro.setStorageSync('blackBarHight', blackBarHight)
    // 判断胶囊按钮信息是否成功获取
    if (top && top !== 0 && height && height !== 0) {
      const navigationBarHeight = (top - statusBarHeight!) * 2 + height
      // 导航栏高度
      Taro.setStorageSync('navigationBarHeight', navigationBarHeight)
    } else {
      Taro.setStorageSync(
        'navigationBarHeight',
        platform === 'android' ? 48 : 40
      )
    }
    const navigationBarAndStatusBarHeight = Taro.getStorageSync('statusBarHeight') + Taro.getStorageSync('navigationBarHeight')

    this.setState({
      ...this.state,
      blackBarHight,
      navigationBarAndStatusBarHeight
    })
  }

  render() {
    return (
      <div className="index-page-wrapper" style={{ paddingBottom: this.state.blackBarHight + 50 + 'px', paddingTop: this.state.navigationBarAndStatusBarHeight + 'px' }}>
        {/* <WaterMark
          className="mark1"
          zIndex={1}
          content="water-mark"
        /> */}
        <NavigationBar/>
        <Map></Map>
        <DataList style={{ paddingBottom: this.state.blackBarHight + 50 + 'px' }}/>
        <FooterBabar />
      </div>
    );
  }
}
export default Index
