import { Entity, Column, PrimaryGeneratedColumn, OneToMany } from "typeorm";
import { Length, IsEmail } from "class-validator";

@Entity()
export class House {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({ length: 80 })
    @Length(1,)
    code: string;

    // TODO: 是否关联小区,关联小区需要清洗数据
    // @Column({ length: 80 })
    // @Length(1,)
    // community_name: string;

    @Column({ length: 80 })
    deal_time: string;

    @Column({ length: 80 })
    @Length(1,)
    deal_date: string;

    @Column({ length: 80 })
    @Length(1,)
    door_model: string;

    @Column({ length: 100 })
    door_model_img: string;

    @Column({ length: 80 })
    size: string;

    @Column({ length: 80 })
    @Length(1,)
    original_price: string;

    @Column({ length: 80 })
    @Length(1,)
    real_price: string;

    @Column({ length: 80 })
    @Length(1,)
    unit_price: string;

    @Column({ length: 80 })
    @Length(1,)
    toward: string;

    @Column({ length: 80 })
    @Length(1,)
    decorate_situation: string;

    @Column({ length: 80 })
    @Length(1,)
    high: string;

    @Column({ length: 80 })
    structure: string;

    @Column({ length: 80 })
    tax_status: string;

    @Column({ length: 80 })
    recently_subway: string;
}

export const userSchema = {
    id: { type: "number", required: true, example: 1 },

    community_name: { type: "string", required: true, example: "Javier" }, // 小区名字community
    city: { type: "string", required: true, example: "杭州" }, // 所属城市
    district: { type: "string", required: true, example: "余杭区" }, // 所属区
    area: { type: "string", required: true, example: "未来科技城" }, // 所属板块

    code: { type: "string", required: true, example: "123456789" }, // 交易编码
    deal_time: { type: "string", required: false, example: "100天" }, // 成交周期
    deal_date: { type: "string", required: true, example: "2011-12-12" }, // 成交日期
    door_model: { type: "string", required: true, example: "几室几厅" },
    door_model_img: { type: "string", required: false, example: "户型图片" },
    size: { type: "string", required: false, example: "136平方米" },
    original_price: { type: "string", required: true, example: "1000万" },
    real_price: { type: "string", required: true, example: "890万" },
    unit_price: { type: "string", required: true, example: "6000元/米" }, // 单价
    toward: { type: "string", required: false, example: "南北" }, // 朝向
    decorate_situation: { type: "string", required: false, example: "精装" }, // 装修情况
    high: { type: "string", required: true, example: "低楼层(共32层)" }, // 楼层高度
    structure: { type: "string", required: false, example: "板楼" },  // 楼房结构
    tax_status: { type: "string", required: false, example: "房屋满五年" }, // 满5满2
    recently_subway: { type: "string", required: false, example: "距地铁6号线(杭富线)伟业路1009米" }, // 最近地铁
};
