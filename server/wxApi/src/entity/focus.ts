import { Entity, Column, PrimaryGeneratedColumn, OneToOne, JoinColumn, ManyToOne } from "typeorm";
import { Length, IsEmail, length } from "class-validator";
import { User } from "./user";
import { Community } from "./community";


export enum FocusType {
  HOUSE = "house", // 二手房小区
  CARPORT = "carport", // 车位
  IDLE = "idle", // 闲置
}

@Entity()
export class Focus {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({
        type: "enum",
        enum: FocusType,
        default: FocusType.HOUSE
    })
    @Length(10, 80)
    type: FocusType;

    // 多对一关系，多个关注对应一个用户
    @ManyToOne(() => User, user => user.focuss)
    user: User;

    // 一对一关系, 每个关注都有一个小区
    @OneToOne(() => Community)
    @JoinColumn()
    community: Community;

    // @Column()
    // user_id: string;

    // @Column()
    // community_id: string;
}

export const userSchema = {
    id: { type: "number", required: true, example: 1 },
    type: { type: "string", required: true, example: "house/car" }, // 关注类型
    user_id: { type: "string", required: false, example: "用户id" },  // 关联用户表
    community_id: { type: "string", required: false, example: "id" }, // 关注小区表
};
