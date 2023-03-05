import React, { useState, useEffect } from "react";
import Taro from '@tarojs/taro';
import { Icon } from "@nutui/nutui-react-taro";
import { Map } from '@tarojs/components';
import './map.scss'

const App = () => {
  const [curLocation, setCurLocation] = useState({
    latitude: 0,
    longitude: 0,
  })
  const statusBarHeight = Taro.getStorageSync('statusBarHeight');
  const navigationBarHeight = Taro.getStorageSync('navigationBarHeight');
  const navigationBarAndStatusBarHeight = statusBarHeight + navigationBarHeight + 'px';

  const goLocal = () => {
    let mpCtx = Taro.createMapContext('home-map')
    // 将地图中心移置当前定位点，此时需设置地图组件 show-location 为true。'2.8.0' 起支持将地图中心移动到指定位置。
    mpCtx.moveToLocation({})
  }

  useEffect(() => {
    // Taro.getSetting();
    Taro.getLocation({
      isHighAccuracy: true, // 开启高精度定位
      type: 'gcj02', // wgs84 返回 gps 坐标，gcj02 返回可用于 openLocation 的坐标
      highAccuracyExpireTime: 3000, // 高精度定位超时时间(ms)，指定时间内返回最高精度，该值3000ms以上高精度定位才有效果
      success: function (res) {
        console.log('获取地图信息', res);
        setCurLocation({
          latitude: res.latitude,
          longitude: res.longitude,
        })
      }
    })
  }, [])
  return <div className="map-comp-wrap" style={{ height: `calc(50vh + 25px - ${navigationBarAndStatusBarHeight})` }}>
    {/**
         * longitude 中心经度
         * latitude 中心纬度
         * scale 缩放级别，取值范围为5-18
         * onMarkertap marker 点击事件
         * onRegionchange 视野发生变化触发事件
         * show-location 显示带有方向的当前定位点
         * cover-view 覆盖在原生组件之上的文本视图
         */}
    <Map
      id="home-map"
      className="map-dom-wrap"
      // subkey={this.state.qMapKey}
      longitude={curLocation?.longitude}
      latitude={curLocation?.latitude}
      // scale={18}
      // markers={this.state.markers}
      // onMarkertap={this.handleMarkerClick.bind(this)}
      // onRegionchange={this.handleRegionChange.bind(this)}
      showLocation
    >
      {/* <cover-view class="cover-view" bindtap="controltap">
        <cover-image class="station" src="https://linli-oss.vecommunity.com/xchx/icon/position.jpg"></cover-image>
      </cover-view> */}
    </Map>
    <div className="current-position-btn" onClick={() => goLocal()}>
      <Icon size={28} name="location"></Icon>
    </div>
  </div>
};
export default App;
