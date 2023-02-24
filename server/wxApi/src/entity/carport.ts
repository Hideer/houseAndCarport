import { Entity, Column, PrimaryGeneratedColumn, OneToOne, JoinColumn } from "typeorm";
import { Length, IsBoolean, ArrayNotEmpty } from "class-validator";
import { Community } from "./community";


export enum TradType {
  SALES = "sales", // 买/卖
  LEASE = "lease", // 租/求租
  IDLE = "idle", // 闲置二手
}

export enum TradRole {
  BUYER = "buyer", // 甲方
  SELLER = "seller", // 乙方
}


@Entity()
export class Carport {
    @PrimaryGeneratedColumn()
    id: number;

    @OneToOne(() => Community)
    @JoinColumn()
    community: Community;

    @Column({
        type: "enum",
        enum: TradType,
    })
    @Length(1,)
    type: TradType;

    @Column({
        type: "enum",
        enum: TradRole,
        default: TradRole.BUYER,
    })
    @Length(1,)
    trad_role: TradRole;

    @Column({length: 100})
    @Length(1,)
    position: string

    @Column({length: 100})
    position_no: string

    @Column({length: 100})
    @Length(1,)
    price: string

    @Column({ default: false })
    @IsBoolean()
    is_charg: boolean

    @Column()
    @IsBoolean()
    remarks: string

    @Column("simple-array")
    @ArrayNotEmpty()
    images: string[]
}

// 车位表
export const userSchema = {
    id: { type: "number", required: true, example: 1 },

    user_id: { type: "number", required: true, example: 1 }, // 关联用户表（姓名，电话）
    community_id: { type: "number", required: true, example: 1 }, // 关联小区表（省，市，区，小区名）

    type: { type: TradType, required: true, example: TradType.SALES }, // 发布交易类型
    trad_role: { type: "string", required: true, example: "卖方/买方" }, // 交易角色
    position: { type: "string", required: true, example: "车位位置" },
    position_no: { type: "string", required: false, example: "车位位置编号" },
    price: { type: "string", required: true, example: "价格" },
    is_charg: { type: "boolean", required: true, example: true }, // 是否有充电桩
    remarks: { type: "string", required: false, example: "备注" },
    images: { type: "array", required: true, example: ["image"] }, // 上传图片
};
