import { Context } from "koa";
import { getManager, getRepository, Repository, Not, Equal, Like } from "typeorm";
import { validate, ValidationError } from "class-validator";
import { request, summary, path, body, responsesAll, tagsAll } from "koa-swagger-decorator";
import { House, houseSchema } from "./../entity/house";
import { Community, communitySchema } from "./../entity/community";

@responsesAll({ 200: { description: "success" }, 400: { description: "bad request" }, 401: { description: "unauthorized, missing/wrong jwt token" } })
@tagsAll(["User"])
export default class CommunityController {

    @request("get", "/community/index")
    @summary("Find all community and support filters")
    public static async getCommunity(ctx: Context): Promise<void> {
        const { limit = 0, offset = 20 } = ctx.query;
        const skip = Number(limit);
        const take = Number(offset);
        const [list, total] = await getManager()
            .createQueryBuilder(Community, "community")
            // .orderBy({ "house.deal_date": "DESC" })
            // .leftJoinAndSelect("house.community", "community")
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
    @summary("Find house by distance")
    public static async getHouseByDistance(ctx: Context): Promise<void> {
        const { limit = 0, offset = 20 } = ctx.query;
        const skip = Number(limit);
        const take = Number(offset);
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
    @summary("Find house by community")
    public static async getHouseByCommunity(ctx: Context): Promise<void> {
        const { id, limit = 0, offset = 20 } = ctx.query;
        const skip = Number(limit);
        const take = Number(offset);
        const [list, total] = await getManager()
            .createQueryBuilder(House, "house")
            .where("house.communityId = :communityId", { communityId: id })
            .leftJoinAndSelect("house.community", "community")
            .skip(skip)
            .take(take)
            .getManyAndCount();
        ctx.pagSuccess(list, total);
    }
}
