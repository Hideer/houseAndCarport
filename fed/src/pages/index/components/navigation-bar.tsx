import React, { useState, useEffect } from "react";
import Taro from '@tarojs/taro';
import { Icon } from "@nutui/nutui-react-taro";
import './navigation-bar.scss';

const App = () => {
  const statusBarHeight = Taro.getStorageSync('statusBarHeight');
  const navigationBarHeight = Taro.getStorageSync('navigationBarHeight');
  const navigationBarAndStatusBarHeight = statusBarHeight + navigationBarHeight + 'px';

  const goSearch = ()=>{
    alert('去搜索')
  }

  return <div className="navigation-comp-wrap" style={{ height: navigationBarAndStatusBarHeight }}>
    {/* 空白来占位状态栏 */}
    <view style={{ height: statusBarHeight }}></view>
    {/* 自定义导航栏 */}
    <div className="content-wrap" style={{ height: navigationBarHeight }} onClick={()=>{goSearch()}}>
      <Icon size={18} name="location2"></Icon>
      <span>融创金城江南府</span>
    </div>
  </div>
};
export default App;
