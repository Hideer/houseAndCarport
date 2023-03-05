import { Component, PropsWithChildren } from "react";
import { Avatar, Icon } from '@nutui/nutui-react-taro';
import FooterBabar from './../../components/footer-tabbar'

import './index.scss'

class Index extends Component<PropsWithChildren> {
  constructor(props: any) {
    super(props);
  }

  componentDidMount() { }

  componentWillUnmount() { }

  componentDidShow() { }

  componentDidHide() { }

  render() {
    return (
      <div className="mine-page-wrapper">
        <div className="header-bg"></div>
        <div className="interval">
          <div className="user-info-wrap">
            <Avatar size="large" icon="https://img12.360buyimg.com/imagetools/jfs/t1/143702/31/16654/116794/5fc6f541Edebf8a57/4138097748889987.png"
            />
            <div className="info">
              <div className="base">
                <div className="name">
                  微信用户
                </div>
                <div className="phone">
                  <Icon name="issue"></Icon>
                  <span>178****8199</span>
                </div>
              </div>
              <div className="setting">
                <Icon name="arrow-right"></Icon>
              </div>
            </div>
          </div>
          {/* 基础数据 */}
          <div className="basic-data-wrap">
            <div className="item">
              <div className="num">0</div>
              <div className="text">消息</div>
            </div>
            <div className="item">
              <div className="num">0</div>
              <div className="text">收藏</div>
            </div>
            <div className="item">
              <div className="num">0</div>
              <div className="text">订阅</div>
            </div>
          </div>
          {/* 我的服务 */}
          <div className="my-service-wrap">
            <div className="title">我的服务</div>
            <div className="wrap">
              <div className="item">
                <div className="icon">
                  <Icon size="50" name="https://img11.360buyimg.com/imagetools/jfs/t1/137646/13/7132/1648/5f4c748bE43da8ddd/a3f06d51dcae7b60.png" />
                </div>
                <span className="text">联系客服</span>
              </div>
              <div className="item">
                <div className="icon">
                  <Icon size="50" name="https://img11.360buyimg.com/imagetools/jfs/t1/137646/13/7132/1648/5f4c748bE43da8ddd/a3f06d51dcae7b60.png" />
                </div>
                <span className="text">用户反馈</span>
              </div>
              <div className="item">
                <div className="icon">
                  <Icon size="50" name="https://img11.360buyimg.com/imagetools/jfs/t1/137646/13/7132/1648/5f4c748bE43da8ddd/a3f06d51dcae7b60.png" />
                </div>
                <span className="text">隐私协议</span>
              </div>
            </div>
          </div>
          {/* 出品方 */}
          <p className="source-text">
            - 可行技术圈出品 -
          </p>
        </div>
        <FooterBabar activeIndex={2} />
      </div>
    );
  }
}
export default Index
