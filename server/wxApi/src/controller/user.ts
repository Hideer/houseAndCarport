import { Context } from "koa";
import https from "https";
import { getManager, Repository, Not, Equal, Like } from "typeorm";
import { validate, ValidationError } from "class-validator";
import { request, summary, path, body, responsesAll, tagsAll } from "koa-swagger-decorator";
import { User, userSchema } from "../entity/user";
import { WXBizDataCrypt } from "./../utils/wx";

@responsesAll({ 200: { description: "success"}, 400: { description: "bad request"}, 401: { description: "unauthorized, missing/wrong jwt token"}})
@tagsAll(["User"])
export default class UserController {

    @request("get", "/users")
    @summary("Find all users")
    public static async getUsers(ctx: Context): Promise<void> {

        // get a user repository to perform operations with user
        const userRepository: Repository<User> = getManager().getRepository(User);

        // load all users
        const users: User[] = await userRepository.find();

        // return OK status code and loaded users array
        ctx.status = 200;
        ctx.body = users;
    }

    @request("post", "/signin_wx")
    @summary("微信小程序鉴权登录")
    public static async signinWx(ctx: Context): Promise<void> {
        const params = ctx.params;
        const encryptedData = params.encryptedData; // 获取小程序传来的encryptedData
        const iv = params.iv; // 获取小程序传来的iv
        const code = params.code;
        const appid = "xxxxxxx"; // 自己小程序后台管理的appid，可登录小程序后台查看
        const secret = "xxxxxxx"; // 小程序后台管理的secret，可登录小程序后台查看
        const grant_type = "authorization_code"; // 授权（必填）默认值

        //请求获取openid
        const url = "https://api.weixin.qq.com/sns/jscode2session?grant_type=" + grant_type + "&appid=" + appid + "&secret=" + secret + "&js_code=" + code;

        let openid, sessionKey;

        https.get(url, (res) => {
            res.on("data", (d) => {
                console.log("返回的信息: ", JSON.parse(d));
                openid = JSON.parse(d).openid; // 得到openid
                sessionKey = JSON.parse(d).session_key; // 得到session_key
                const pc = new WXBizDataCrypt({ appId:appid, sessionKey }); // 这里的sessionKey 是上面获取到的
                const decodeData = pc.decryptData(encryptedData, iv); // encryptedData 是从小程序获取到的
                console.log("解密后 data: ", decodeData);
            }).on("error", (e) => {
                console.error(e);
            });
        });

    }
}
