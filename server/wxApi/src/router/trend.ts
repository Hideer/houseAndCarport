import Router from "@koa/router";
import { trend } from "./../controller";

const router = new Router();

router.get("/city_area", trend.getCityAllArea);
router.get("/community/price", trend.getCommunityPrice);
router.get("/community/amount", trend.getCommunityAmount);
router.get("/area/price", trend.getAreaPrice);
router.get("/area/amount", trend.getAreaAmount);
router.get("/area_all/amount", () => { });

export default router;

// 趋势：
// 1. 小区月成交均价趋势
// 2. 板块月成交均价趋势
// 3. 小区月成交量趋势
// 4. 板块月成交量趋势
// 5. 各板块成交量占比
// 6. 城市月(成交均价/成交量)趋势 （需要开通多城市后）
