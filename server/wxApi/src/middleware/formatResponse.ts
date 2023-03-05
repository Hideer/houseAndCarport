import { Context } from "koa";

export const MESSAGE_CODE_TEXT:{[propName: number]: string} = {
    200: "成功",
    300: "参数校验失败",
    301: "操作过于频繁",
};

export const routerResponse = ()=> {
    return async (ctx: Context, next: () => Promise<void>): Promise<void> => {
        ctx.fail = function (code: number = 300, msg?:string) {
            ctx.status = 200;
            ctx.body = {
                code,
                msg: msg || MESSAGE_CODE_TEXT[code],
            };
        };

        ctx.success = <T>(data: T, msg?: string) => {
            const code = 200;
            ctx.status = 200;
            ctx.body = {
                code,
                msg: msg || MESSAGE_CODE_TEXT[code],
                data: data
            };
        };

        // 分页数据结构
        ctx.pagSuccess = <T>(data: T, total:number, msg?: string) => {
            const code = 200;
            ctx.status = 200;
            ctx.body = {
                code,
                msg: msg || MESSAGE_CODE_TEXT[code],
                data: {
                    list:data,
                    total
                }
            };
        };
        await next();
    };
};
