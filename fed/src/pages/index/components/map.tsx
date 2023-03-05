import React, { useState, useEffect } from "react";
import Taro from '@tarojs/taro';
import { Map } from '@tarojs/components';
import './map.scss'

const App = () => {
  const [curLocation, setCurLocation] = useState({
    latitude: 0,
    longitude: 0,
  })

  useEffect(() => {
    console.log('我是测试一下');
    Taro.getSetting({
      success: res => {
        // 通过scope.userLocation的值是否为true判断是否授权使用地理位置
        console.log(res.authSetting)
        // res.authSetting = {
        //   "scope.userInfo": true,
        //   "scope.userLocation": true
        // }
      }
    })
    Taro.getLocation({
      isHighAccuracy: true, // 开启高精度定位
      altitude: true, // 传入 true 会返回高度信息，由于获取高度需要较高精确度，会减慢接口返回速度
      type: 'gcj02', // wgs84 返回 gps 坐标，gcj02 返回可用于 openLocation 的坐标
      highAccuracyExpireTime: 3000, // 高精度定位超时时间(ms)，指定时间内返回最高精度，该值3000ms以上高精度定位才有效果
      success: function (res) {
        setCurLocation({
          latitude: res.latitude,
          longitude: res.longitude,
        })
        // console.log('获取地图信息', res);
        // this.curLatitude = res.latitude
        // this.curLongitude = res.longitude
      }
    })
  }, [])
  return <>
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
      className="map-dom-wrap"
      // subkey={this.state.qMapKey}
      longitude={curLocation?.longitude}
      latitude={curLocation?.latitude}
      // scale={18}
      // markers={this.state.markers}
      // onMarkertap={this.handleMarkerClick.bind(this)}
      // onRegionchange={this.handleRegionChange.bind(this)}
      showLocation
    />
  </>
};
export default App;
