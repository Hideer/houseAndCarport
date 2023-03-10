import { Context } from "koa";
import { getManager, getRepository, Repository, Not, Equal, Like } from "typeorm";
import { validate, ValidationError } from "class-validator";
import { request, summary, path, body, responsesAll, tagsAll } from "koa-swagger-decorator";
import { House, houseSchema } from "./../entity/house";
import { Community, communitySchema } from "./../entity/community";


@responsesAll({ 200: { description: "success" }, 400: { description: "bad request" }, 401: { description: "unauthorized, missing/wrong jwt token" } })
@tagsAll(["User"])
export default class TrendController {

    @request("get", "/trend/city_area")
    @summary("按城市获取所有板块")
    public static async getCityAllArea(ctx: Context): Promise<void> {
        const { city = "杭州" } = ctx.query;
        // TODO: 这里typeorm不知道为啥
        // const res =  await getManager()
        //     .createQueryBuilder(Community, "community")
        //     .select("distinct community.area")
        //     // .select("distinct area")
        //     .where("community.city = :city", {
        //         city: "杭州"
        //     })
        //     .getMany();
        const res = await getManager().query(`SELECT distinct  community.area FROM community WHERE community.city = '${city}'`);
        const res_data = res.map((i: { area: string; })=>{
            return i.area;
        });
        ctx.success(res_data);
    }

    @request("get", "/trend/community/price")
    @summary("小区按月获取成交均价趋势")
    public static async getCommunityPrice(ctx: Context): Promise<void> {
        const { id  } = ctx.query;
        const sql = "SELECT house.*,TIME AS community_time_key,community.province AS community_province,community.city AS community_city,community.district AS community_district,community.area AS community_area,community.`name` AS community_name,community.lng AS community_lng,community.lat AS community_lat,community.logo AS community_logo FROM (house,(SELECT DATE_FORMAT(deal_date, '%Y-%m') AS TIME, GROUP_CONCAT(house.id ORDER BY house.id DESC) AS ids FROM house WHERE`house`.`communityId` = " + id + " GROUP BY TIME) AS b) LEFT JOIN`community` `community` ON`community`.`id` = `house`.`communityId` WHERE FIND_IN_SET(house.id, b.ids) ";

        const res = await getManager().query(sql);

        // 将数据按月分组并分组
        const map:{[key:string]:any} = {};
        res.map((item:any)=>{
            if (!map[item.community_time_key]){
                map[item.community_time_key] = [item];
            }else{
                map[item.community_time_key].push(item);
            }
        });
        const res_data: { time: string;average_price: number, data: any; }[] = [];
        Object.keys(map).forEach(key => {
            let average_price = 0;
            let total_price = 0;
            map[key].map((it: { unit_price: string; }) => {
                const unit_prict = Number(it.unit_price.split(" ")[0] || 0);
                total_price += unit_prict;
            });
            average_price = total_price / map[key].length;
            res_data.push({
                time: key,
                average_price,
                data: map[key],
            });
        });
        // res = await getManager()
        //     .createQueryBuilder(House, "house")
        //     .where("house.communityId = :communityId", {
        //         communityId: id
        //     })
        //     .leftJoinAndSelect("house.community", "community")
        //     // .groupBy("house.deal_date")
        //     // .skip(skip)
        //     // .take(take)
        //     // .getSql();
        //     .getManyAndCount();
        ctx.success(res_data);
    }

    @request("get", "/trend/community/amount")
    @summary("小区按月获取成交量趋势")
    public static async getCommunityAmount(ctx: Context): Promise<void> {
        const { id } = ctx.query;

        const sql = "SELECT house.*,TIME AS community_time_key,community.province AS community_province,community.city AS community_city,community.district AS community_district,community.area AS community_area,community.`name` AS community_name,community.lng AS community_lng,community.lat AS community_lat,community.logo AS community_logo FROM (house,(SELECT DATE_FORMAT(deal_date, '%Y-%m') AS TIME, GROUP_CONCAT(house.id ORDER BY house.id DESC) AS ids FROM house WHERE`house`.`communityId` = " + id + " GROUP BY TIME) AS b) LEFT JOIN`community` `community` ON`community`.`id` = `house`.`communityId` WHERE FIND_IN_SET(house.id, b.ids) ";

        const res = await getManager().query(sql);

        // 将数据按月分组并分组
        const map: { [key: string]: any } = {};
        res.map((item: any) => {
            if (!map[item.community_time_key]) {
                map[item.community_time_key] = [item];
            } else {
                map[item.community_time_key].push(item);
            }
        });
        const res_data: { time: string; total_number: number, data: any; }[] = [];
        Object.keys(map).forEach(key => {
            res_data.push({
                time: key,
                total_number: map[key].length,
                data: map[key],
            });
        });
        ctx.success(res_data);
    }

    @request("get", "/trend/area/price")
    @summary("板块月成交均价趋势(默认近三年)")
    public static async getAreaPrice(ctx: Context): Promise<void> {
        const { city="杭州", area="武林", step = 3 } = ctx.query;
        const sql = "SELECT house.*,b.*,DATE_FORMAT(house.deal_date,'%Y-%m') AS house_time_key FROM (house,( SELECT * FROM community WHERE community.city = '" + city + "' AND community.area = '" + area +"') AS b) WHERE FIND_IN_SET(house.communityId, b.id) AND(DATE_SUB(CURDATE(), INTERVAL " + step + " YEAR) <= house.deal_date) ";

        const res = await getManager().query(sql);

        // 将数据按月分组并分组
        const map: { [key: string]: any } = {};
        res.map((item: any) => {
            if (!map[item.house_time_key]) {
                map[item.house_time_key] = [item];
            } else {
                map[item.house_time_key].push(item);
            }
        });
        const res_data: { time: string; average_price: number, data: any; }[] = [];
        Object.keys(map).forEach(key => {
            let average_price = 0;
            let total_price = 0;
            map[key].map((it: { unit_price: string; }) => {
                const unit_prict = Number(it.unit_price.split(" ")[0] || 0);
                total_price += unit_prict;
            });
            average_price = total_price / map[key].length;
            res_data.push({
                time: key,
                average_price,
                data: map[key],
            });
        });
        ctx.success(res_data);
    }

    @request("get", "/trend/area/amount")
    @summary("板块月成交量趋势(默认近三年)")
    public static async getAreaAmount(ctx: Context): Promise<void> {
        const { city = "杭州", area = "武林", step = 3 } = ctx.query;
        const sql = "SELECT house.*,b.*,DATE_FORMAT(house.deal_date,'%Y-%m') AS house_time_key FROM (house,( SELECT * FROM community WHERE community.city = '" + city + "' AND community.area = '" + area + "') AS b) WHERE FIND_IN_SET(house.communityId, b.id) AND(DATE_SUB(CURDATE(), INTERVAL " + step + " YEAR) <= house.deal_date) ";

        const res = await getManager().query(sql);

        // 将数据按月分组并分组
        const map: { [key: string]: any } = {};
        res.map((item: any) => {
            if (!map[item.house_time_key]) {
                map[item.house_time_key] = [item];
            } else {
                map[item.house_time_key].push(item);
            }
        });
        const res_data: { time: string; total_number: number, data: any; }[] = [];
        Object.keys(map).forEach(key => {
            res_data.push({
                time: key,
                total_number: map[key].length,
                data: map[key],
            });
        });
        ctx.success(res_data);
    }

    @request("get", "/area_all/amount")
    @summary("各板块成交量占比")
    public static async getAllAreaAmount(ctx: Context): Promise<void> {
        // const { city = "杭州", area = "武林", step = 3 } = ctx.query;

        const sql = "SELECT house.*,b.area AS community_area,b.district AS community_district,b.city AS community_city,b.province AS community_province FROM (house,( SELECT community.province, community.city, community.district, community.area, GROUP_CONCAT(DISTINCT id ORDER BY id ASC) AS ids FROM community GROUP BY community.area) AS b) WHERE FIND_IN_SET(house.communityId, b.ids) ";

        const res = await getManager().query(sql);

        ctx.success(res);
    }
}
