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
import DataList from './components/data-list'
import Map from './components/map'
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
      <div className="index-page-wrapper">
        {/* <WaterMark
          className="mark1"
          zIndex={1}
          content="water-mark"
        /> */}
        <Map></Map>
        <DataList />
        <FooterBabar />
      </div>
    );
  }
}
export default Index
