import Router from "@koa/router";
import { house } from "./../controller";

const router = new Router();

router.get("/index", house.getHouses);
router.get("/distance", house.getHouseByDistance);
router.get("/community", house.getHouseByCommunity);
router.get("/:id", house.getHouse);

export default router;
