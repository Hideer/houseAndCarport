import Router from "@koa/router";
import { sign } from "jsonwebtoken";

import { config } from "./config";
import { general } from "./controller";

const unprotectedRouter = new Router();

// Hello World route
unprotectedRouter.get("/", general.helloWorld);
unprotectedRouter.get("/token", async (ctx) => {
    const token = sign({ name: "moyufed" }, config.jwtSecret, { expiresIn: "3h" }); // token 有效期为3小时
    ctx.cookies.set(
        "token",
        token,
        {
            domain: "localhost", //TODO: 设置 cookie 的域
            path: "/", // 设置 cookie 的路径
            maxAge: 3 * 60 * 60 * 1000, // cookie 的有效时间 ms
            // expires: new Date("2021-12-30"), // cookie 的失效日期，如果设置了 maxAge，expires 将没有作用
            httpOnly: true, // 是否要设置 httpOnly
            overwrite: true // 是否要覆盖已有的 cookie 设置
        }
    );
    ctx.body = token;
});


export { unprotectedRouter };
