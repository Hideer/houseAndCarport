import React, { useState } from "react";
import { Popup, Tabs, Animate, Button, Toast } from '@nutui/nutui-react-taro';
import HousCard from './hous-card.tsx'

import './data-list.scss'

const App = () => {
  const [popupState, setPopupState] = useState('fold');
  const [tabValue, setTabvalue] = useState('0');
  return (
    <>
      <Popup round zIndex={1} overlay={false}
        visible={true} className={'popup-wrap'} style={{ height: popupState === 'expand' ? '80vh' : '40vh' }} position="bottom">
        {/* 展开收起按钮 */}
        <div className="popup-btn-wrap">
          <Animate type="flicker" loop={true} onClick={() => setPopupState(popupState === 'expand' ? 'fold' : 'expand')}>
            <div className="popup-btn"></div>
          </Animate>
        </div>
        <Tabs className="tabs-wrap" value={tabValue} leftAlign titleGutter={10} background={'#FFF'} onChange={({ paneKey }) => {
          setTabvalue(paneKey)
        }}>
          <Tabs.TabPane title="我关注的">
            {
              [1, 2, 3, 4, 5, 6, 7, 8].map(() => {
                return <HousCard></HousCard>
              })
            }
            {/* 查看更多 */}
            <div className="show-more-wrap">
              <Button plain size="small" type="default" onClick={()=>{
                alert('功能开发中!')
              }}>查看更多></Button>
            </div>
          </Tabs.TabPane>
          <Tabs.TabPane title="附近小区">
            {
              [1, 2, 3, 4].map(() => {
                return <HousCard></HousCard>
              })
            }
          </Tabs.TabPane>
        </Tabs>
      </Popup>
    </>
  );
};
export default App;
