import React, { useState } from "react";
import Taro from '@tarojs/taro';
import { Tabbar, TabbarItem } from '@nutui/nutui-react-taro';

const App = (props) => {
  const { activeIndex = 0 } = props;
  const blackBarHight = Taro.getStorageSync('blackBarHight');

  return <div className="footer-wrap" style={{ bottom: blackBarHight + 'px' }}>
    <Tabbar activeVisible={activeIndex}>
      <TabbarItem tabTitle="首页" icon="home" dot />
      <TabbarItem tabTitle="趋势" icon="location" />
      {/* <TabbarItem tabTitle="发布" icon="find" /> */}
      <TabbarItem tabTitle="我的" icon="my" />
    </Tabbar>
  </div>
}

export default App;
