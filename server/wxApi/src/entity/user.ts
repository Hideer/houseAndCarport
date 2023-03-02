import { Entity, Column, CreateDateColumn, UpdateDateColumn, PrimaryGeneratedColumn, OneToMany } from "typeorm";
import { Length, IsEmail, IsPhoneNumber } from "class-validator";
import { Focus } from "./focus";

@Entity()
export class User {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({
        type: 'varchar',
        length: 80,
        comment: '用户名',
    })
    @Length(10, 80)
    name: string;

    @Column({
        type: 'varchar',
        length: 100,
        nullable: true,
        comment: '用户邮箱',
    })
    @Length(10, 100)
    @IsEmail()
    email: string;

    @Column({
        type: 'int',
        nullable: true,
        comment: '用户手机',
    })
    @Length(11)
    @IsPhoneNumber()
    phone: number;

    @Column({
        type: 'varchar',
        length: 100,
        comment: '微信token',
    })
    @Length(8, 100)
    @IsPhoneNumber()
    access_token: string;

    @Column({
        length: 100,
        nullable: true,
        comment: '用户地址',
    })
    @Length(8, 100)
    @IsPhoneNumber()
    address: string;

    // 一对多的关系
    @OneToMany(() => Focus, focus => focus.user)
    focuss: Focus[];

    @CreateDateColumn()
    created_at: Date;

    @UpdateDateColumn()
    updated_at: Date;
}

export const userSchema = {
    id: { type: "number", required: true, example: 1 },
    name: { type: "string", required: true, example: "Javier" },
    email: { type: "string", required: false, example: "avileslopez.javier@gmail.com" },
    phone: { type: "number", required: true, example: "17899999999" },
    access_token: { type: "string", required: true, example: "access_token" },
    address: { type: "string", required: false, example: "浙江杭州" }
};
