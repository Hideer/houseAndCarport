import Router from "@koa/router";
import { community } from "./../controller";

const router = new Router();

router.get("/index", community.getCommunity);
router.get("/distance", community.getCommunityByDistance);
router.get("/:id", community.getCommunityDetail);

export default router;
