import { Entity, Column, CreateDateColumn, UpdateDateColumn, PrimaryGeneratedColumn, ManyToOne, OneToOne, JoinColumn } from "typeorm";
import { Length, IsEmail } from "class-validator";
import { Community } from "./community";

@Entity()
export class House {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({
        length: 80,
        comment: '数据收集日期',
    })
    @Length(1,)
    collection_date: string;

    @Column({
        length: 80,
        comment: '小区编码',
    })
    @Length(1,)
    code: string;

    @Column({
        length: 80,
        nullable: true,
        comment: '成交周期',
    })
    deal_time: string;

    @Column({
        length: 80,
        nullable: true,
        comment: '成交日期',
    })
    @Length(1,)
    deal_date: string;

    @Column({
        length: 80,
        nullable: true,
        comment: '户型',
    })
    @Length(1,)
    door_model: string;

    @Column({
        length: 1000,
        nullable: true,
        comment: '户型图',
    })
    door_model_img: string;

    @Column({
        length: 1000,
        comment: '详情地址',
    })
    desc_url: string;

    @Column({
        length: 80,
        comment: '面积',
    })
    size: string;

    @Column({
        length: 80,
        nullable: true,
        comment: '挂牌价格',
    })
    @Length(1,)
    original_price: string;

    @Column({
        length: 80,
        comment: '成交价格',
    })
    @Length(1,)
    real_price: string;

    @Column({
        length: 80,
        nullable: true,
        comment: '成交单价',
    })
    @Length(1,)
    unit_price: string;

    @Column({
        length: 80,
        nullable: true,
        comment: '朝向',
    })
    @Length(1,)
    toward: string;

    @Column({
        length: 80,
        nullable: true,
        comment: '装修情况',
    })
    @Length(1,)
    decorate_situation: string;

    @Column({
        length: 80,
        nullable: true,
        comment: '楼层',
    })
    @Length(1,)
    high: string;

    @Column({
        length: 80,
        nullable: true,
        comment: '房屋构造',
    })
    structure: string;

    @Column({
        length: 80,
        nullable: true,
        comment: '是否满五满二',
    })
    tax_status: string;

    @Column({
        length: 80,
        nullable: true,
        comment: '最近交通',
    })
    recently_subway: string;

    // TODO: 是否关联小区,关联小区需要清洗数据
    // @Column({ length: 80 })
    // @Length(1,)
    // community_name: string;
    // 一对多关系, 小区有多个房子
    @ManyToOne(() => Community, community => community.id)
    community: Community;

    @CreateDateColumn()
    created_at: Date;

    @UpdateDateColumn()
    updated_at: Date;
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
    desc_url:{ type: "string", required: false, example: "详情页url" },
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
