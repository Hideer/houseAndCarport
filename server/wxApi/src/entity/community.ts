import { Entity, Column, PrimaryGeneratedColumn } from "typeorm";
import { Length, ArrayNotEmpty } from "class-validator";

@Entity()
export class Community {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({ length: 80 })
    @Length(1, 20)
    province: string;

    @Column({ length: 80 })
    @Length(1, 20)
    city: string;

    @Column({ length: 80 })
    @Length(1, 20)
    district: string;

    @Column({ length: 80 })
    @Length(1, 20)
    area: string;

    @Column({ length: 80 })
    @Length(1, 40)
    name: string;


    @Column("simple-array")
    @ArrayNotEmpty()
    logo: string[];
}

// 小区表
export const userSchema = {
    id: { type: "number", required: true, example: 1 },
    province: { type: "string", required: true, example: "杭州" }, // 所属省份
    city: { type: "string", required: true, example: "杭州" }, // 所属城市
    district: { type: "string", required: true, example: "余杭区" }, // 所属区
    area: { type: "string", required: false, example: "未来科技城" }, // 所属板块
    name: { type: "string", required: true, example: "江南府" }, // 小区名称
    logo: { type: "string", required: true, example: "logo" }, // 小区图

    // 车位出售均价、车位出租均价、出售数、出租数、求租数、求购数
    // 挂牌均价、成交均价、最近成交记录
};
