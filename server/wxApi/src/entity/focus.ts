import { Entity, Column, CreateDateColumn, UpdateDateColumn, PrimaryGeneratedColumn, OneToOne, JoinColumn, ManyToOne,OneToMany } from "typeorm";
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
        default: FocusType.HOUSE,
        comment: '关注类型',
    })
    @Length(10, 80)
    type: FocusType;

    // 多对一关系，多个关注对应一个用户
    @ManyToOne(() => User, user => user.focuss)
    user: User;

    @ManyToOne(() => Community, community => community.id)
    community: Community;

    @CreateDateColumn()
    created_at: Date;

    @UpdateDateColumn()
    updated_at: Date;
}

export const userSchema = {
    id: { type: "number", required: true, example: 1 },
    type: { type: "string", required: true, example: "house/car" }, // 关注类型
    user_id: { type: "string", required: false, example: "用户id" },  // 关联用户表
    community_id: { type: "string", required: false, example: "id" }, // 关注小区表
};
