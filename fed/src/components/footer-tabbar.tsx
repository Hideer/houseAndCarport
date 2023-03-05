import React, { useState } from "react";
import { Tabbar, TabbarItem } from '@nutui/nutui-react-taro';

const App = (props) => {
  const { activeIndex = 0 } = props;
  return <div className="footer-wrap">
    <Tabbar activeVisible={activeIndex}>
      <TabbarItem tabTitle="首页" icon="home" dot />
      <TabbarItem tabTitle="趋势" icon="location" />
      {/* <TabbarItem tabTitle="发布" icon="find" /> */}
      <TabbarItem tabTitle="我的" icon="my" />
    </Tabbar>
  </div>
}

export default App;
