import React, { useState } from "react";
import { Card, Tag } from '@nutui/nutui-react-taro';

import './hous-card.scss'

const App = () => {
  const state = {
    imgUrl:
      '//img10.360buyimg.com/n2/s240x240_jfs/t1/210890/22/4728/163829/6163a590Eb7c6f4b5/6390526d49791cb9.jpg!q70.jpg',
    title: '融创金成江南府  (三室两厅)',
    price: '823万',
    vipPrice: '204万',
    shopDesc: '自营',
    delivery: '厂商配送',
    shopName: '距9号线南苑553米',
  }
  const footerTpl = <div className="footerTpl-time">2022-12-12</div>
  const originTpl = <div className="originTpl-price">
    <span className="total-price">单价:34123元/平</span>
    {/* <span className="origin-price">挂:400万</span> */}
  </div>
  const shopTagTpl = <>
    <Tag plain>高楼层(共18层)</Tag>
    <Tag plain>朝南</Tag>
    <Tag plain>精装</Tag>
    <Tag type="danger">满五</Tag>
  </>
  return (
    <Card
      className="card-wrap"
      imgUrl={state.imgUrl}
      title={state.title}
      price={state.price}
      shopName={state.shopName}
      footerTpl={footerTpl}
      shopTagTpl={shopTagTpl}
      originTpl={originTpl}
    > </Card>
  );
};
export default App;
