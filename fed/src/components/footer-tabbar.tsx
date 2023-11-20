import React, { useState } from "react";
import Taro from '@tarojs/taro';
import { Tabbar, TabbarItem } from '@nutui/nutui-react-taro';

const App = (props) => {
  const { activeIndex = 0 } = props;
  const blackBarHight = Taro.getStorageSync('blackBarHight');
  const [curActiveIndex, setCurActiveIndex] = useState(activeIndex)

  const onSwitch = (params)=>{
    const { index } = params.props;
    let url = '/pages/index/index';
    switch (index) {
      case 0:
        break;
      case 1:
        url = '/pages/trend/index'
        break;
      case 2:
        url = '/pages/mine/index'
        break;
      default:
        break;
    }
    setCurActiveIndex(index)
    Taro.redirectTo({
      url,
    })
  }

  return <div className="footer-wrap" style={{ bottom: blackBarHight + 'px' }}>
    <Tabbar activeVisible={curActiveIndex} onSwitch={onSwitch}>
      <TabbarItem tabTitle="首页" icon="home" index={0} />
      <TabbarItem tabTitle="趋势" icon="location" index={1} />
      {/* <TabbarItem tabTitle="发布" icon="find" /> */}
      <TabbarItem tabTitle="我的" icon="my" index={2} />
    </Tabbar>
  </div>
}


export default App;
