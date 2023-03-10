import { Context } from "koa";
import { getManager, getRepository, Repository, Not, Equal, Like } from "typeorm";
import { validate, ValidationError } from "class-validator";
import { request, summary, path, body, responsesAll, tagsAll } from "koa-swagger-decorator";
import { House, houseSchema } from "./../entity/house";

@responsesAll({ 200: { description: "success"}, 400: { description: "bad request"}, 401: { description: "unauthorized, missing/wrong jwt token"}})
@tagsAll(["User"])
export default class HouseController {

    @request("get", "/house/index")
    @summary("查找所有二手成交房源并分页")
    public static async getHouses(ctx: Context): Promise<void> {
        const { limit = 20, offset = 0 } = ctx.query;
        const skip = Number(offset);
        const take = Number(limit);
        const [list, total] = await getManager()
                                    .createQueryBuilder(House, "house")
                                    .orderBy({"house.deal_date": "DESC"})
                                    .leftJoinAndSelect("house.community", "community")
                                    .skip(skip)
                                    .take(take)
                                    .getManyAndCount();

        ctx.pagSuccess(list, total);
    }

    @request("get", "/house/{id}")
    @summary("Find house by id")
    @path({
        id: { type: "number", required: true, description: "id of house" }
    })
    public static async getHouse(ctx: Context): Promise<void> {
        const { id } = ctx.params;
        const data = await getManager()
                                    .createQueryBuilder(House, "house")
                                    .where("house.id = :id", { id })
                                    .leftJoinAndSelect("house.community", "community")
                                    .getMany();
        ctx.success(data);
    }

    @request("get", "/house/distance")
    @summary("按距离查找二手成交")
    // TODO: 未实现
    public static async getHouseByDistance(ctx: Context): Promise<void> {
        const { limit = 20, offset = 0 } = ctx.query;
        const skip = Number(offset);
        const take = Number(limit);
        const data = await getManager()
                            .createQueryBuilder(House, "house")
                            .orderBy({ "house.deal_date": "DESC" })
                            .leftJoinAndSelect("house.community", "community")
                            .skip(skip)
                            .take(take)
                            .getManyAndCount();
        ctx.success(data);
    }

    @request("get", "/house/community")
    @summary("查询指定小区的二手成交房并分页")
    public static async getHouseByCommunity(ctx: Context): Promise<void> {
        const { id, limit = 20, offset = 0 } = ctx.query;
        const skip = Number(offset);
        const take = Number(limit);
        const [list,total] = await getManager()
                    .createQueryBuilder(House, "house")
                    .where("house.communityId = :communityId", { communityId:id })
                    .leftJoinAndSelect("house.community", "community")
                    .skip(skip)
                    .take(take)
                    .getManyAndCount();
        ctx.pagSuccess(list, total);
    }
}
