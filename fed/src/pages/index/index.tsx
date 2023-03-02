import { Component, PropsWithChildren } from "react";
import {
	Tabbar,
	TabbarItem,
  Watermark,
  Button,
	Cell,
} from "@nutui/nutui-react-taro";
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
        <Watermark
          className="mark1"
          zIndex={1}
          content="water-mark"
        />
        <div className="test">
          <div className="index">
            欢迎使用 NutUI React 开发 Taro 多端项目。
          </div>
          <div className="index">
            <Button type="primary" className="btn">
              NutUI React Button
            </Button>
          </div>
        </div>
        <div className="footer-wrap">
          <Tabbar>
            <TabbarItem tabTitle="首页" icon="home" dot />
            <TabbarItem tabTitle="分类" icon="category" />
            <TabbarItem tabTitle="发现" icon="find" />
            <TabbarItem tabTitle="购物车" icon="cart" dot />
            <TabbarItem tabTitle="我的" icon="my" />
          </Tabbar>
        </div>
			</div>
		);
	}
}
export default Index
