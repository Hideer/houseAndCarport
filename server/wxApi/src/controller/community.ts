import { Context } from "koa";
import axios from "axios";
import { getManager, getRepository, Repository, Not, Equal, Like } from "typeorm";
import { validate, ValidationError } from "class-validator";
import { request, summary, path, body, responsesAll, tagsAll } from "koa-swagger-decorator";
import { House, houseSchema } from "./../entity/house";
import { Community, communitySchema } from "./../entity/community";


/**
   * 附近位置最大最小经纬度计算
   * @param   longitude  经度
   * @param   latitude   纬度
   * @param   distince    距离（千米）
   * @returns 格式：经度最小值-经度最大值-纬度最小值-纬度最大值
   */
const getMaxMinLongitudeLatitude = (longitude: number, latitude: number, distince: number)=>{
    console.log("MaxMinLongitudeLatitude", longitude, latitude);
    const r = 6371.393;    // 地球半径千米
    const lng = longitude;
    const lat = latitude;
    let dlng = 2 * Math.asin(Math.sin(distince / (2 * r)) / Math.cos(lat * Math.PI / 180));
    dlng = dlng * 180 / Math.PI;// 角度转为弧度
    let dlat = distince / r;
    dlat = dlat * 180 / Math.PI;
    const minlat = lat - dlat;
    const maxlat = lat + dlat;
    const minlng = lng - dlng;
    const maxlng = lng + dlng;
    return {
        minlng,
        maxlng,
        minlat,
        maxlat
    };
};


@responsesAll({ 200: { description: "success" }, 400: { description: "bad request" }, 401: { description: "unauthorized, missing/wrong jwt token" } })
@tagsAll(["User"])
export default class CommunityController {

    @request("get", "/community/index")
    @summary("查找所有小区信息按名称排序并分页，可按名称模糊查询")
    public static async getCommunity(ctx: Context): Promise<void> {
        const { limit = 20, offset = 0, community_name="" } = ctx.query;
        const skip = Number(offset);
        const take = Number(limit);
        let res = null;
        if (community_name){
            // 按名字模糊查询
            console.log(community_name);
            res = await getManager()
                .createQueryBuilder(Community, "community")
                .where("community.name LIKE :community_name")
                .setParameters({
                    community_name: "%" + community_name + "%"
                })
                .orderBy({ "community.name": "DESC" })
                .skip(skip)
                .take(take)
                .getManyAndCount();
        }else{
            res = await getManager()
                .createQueryBuilder(Community, "community")
                .orderBy({ "community.name": "DESC" })
                // .leftJoinAndSelect("house.community", "community")
                .skip(skip)
                .take(take)
                .getManyAndCount();
        }
        const [list, total] = res;
        ctx.pagSuccess(list, total);
    }

    @request("get", "/community/{id}")
    @summary("按小区id返回小区基础信息，可返回所有成交房源信息")
    @path({
        id: { type: "number", required: true, description: "id of community" }
    })
    public static async getCommunityDetail(ctx: Context): Promise<void> {
        const { id } = ctx.params;
        const { limit = 20, offset = 0 } = ctx.query;
        const data_community = await getManager()
            .createQueryBuilder(Community, "community")
            .where("community.id = :id", { id })
            .printSql()
            .getMany();
        const skip = Number(offset);
        const take = Number(limit);
        const data_house = await getManager()
            .createQueryBuilder(House, "house")
            .where("house.communityId = :id", { id })
            .orderBy({ "house.deal_date": "DESC" })
            .skip(skip)
            .take(take)
            .getMany();

        const dataMerge = {
            ...data_community[0],
            "house_lists": data_house
        };
        ctx.success(dataMerge);
    }

    @request("get", "/community/distance")
    @summary("查询周边小区")
    public static async getCommunityByDistance(ctx: Context): Promise<void> {
        // 方案一：通过地图接口获取数据后匹配本地数据
        // axios.get("https://apis.map.qq.com/ws/geocoder/v1/?location=30.40147,120.289711&key=K7ZBZ-XJY6U-3IZVA-BNMJY-7UGCO-NFFZM&get_poi=1")
        //     .then(res => {
        //         console.log(res);
        //     })
        //     .catch(err => {
        //         console.log("Error: ", err.message);
        //     });
        // 方案二：利用空间数据库玩法
        // 方案三 利用方法判断距离内的经纬度的区间
        let { lng = 119.966309, lat = 30.243301, dist= 4 } = ctx.query;
        lng = Number(lng);
        lat = Number(lat);
        dist = Number(dist);
        const { minlng,
            maxlng,
            minlat,
            maxlat } = getMaxMinLongitudeLatitude(lng, lat, dist);
        const data = await getManager()
            .createQueryBuilder(Community, "community")
            .where("lng BETWEEN :start AND :end AND lat BETWEEN :start2 AND :end2", {
                start: minlng,
                end: maxlng,
                start2: minlat,
                end2: maxlat
            })
            .getMany();
        ctx.success(data);
    }
}
