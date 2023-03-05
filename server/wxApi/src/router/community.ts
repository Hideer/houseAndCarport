import Router from "@koa/router";
import { community } from "./../controller";

const router = new Router();

router.get("/index", community.getCommunity);
router.get("/signin", () => { });
router.get("/signin-ok", () => { });
router.get("/signin-failed", () => { });

export default router;
