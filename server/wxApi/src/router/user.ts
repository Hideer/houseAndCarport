import Router from "@koa/router";
import { user } from "./../controller";


const router = new Router();

router.get("/index", ()=>{});
router.post("/signin_wx", user.signinWx);
router.get("/signin-ok", () => {});
router.get("/signin-failed", () => {});

export default router;
