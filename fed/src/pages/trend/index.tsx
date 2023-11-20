import { Component, PropsWithChildren } from "react";
import { } from "@nutui/nutui-react-taro";
import './index.scss'

class Index extends Component<PropsWithChildren> {
   constructor(props: any) {
     super(props);
   }

   componentDidMount() {}

   componentWillUnmount() {}

   componentDidShow() {}

   componentDidHide() {}

   render() {
     return (
       <div className="trend-page-wrapper">
         我是趋势页
       </div>
     );
   }
}
export default Index
