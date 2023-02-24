import { Entity, Column, PrimaryGeneratedColumn, OneToMany } from "typeorm";
import { Length, IsEmail, IsPhoneNumber } from "class-validator";
import { Focus } from "./focus";

@Entity()
export class User {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({
        length: 80
    })
    @Length(10, 80)
    name: string;

    @Column({
        length: 100
    })
    @Length(10, 100)
    @IsEmail()
    email: string;

    @Column()
    @Length(8, 20)
    @IsPhoneNumber()
    phone: number;

    @Column({
        length: 20
    })
    @Length(8, 20)
    @IsPhoneNumber()
    access_token: string;

    @Column({
        length: 20
    })
    @Length(8, 20)
    @IsPhoneNumber()
    address: string;

    @OneToMany(() => Focus, focus => focus.user)
    focuss: Focus[]
}

export const userSchema = {
    id: { type: "number", required: true, example: 1 },
    name: { type: "string", required: true, example: "Javier" },
    email: { type: "string", required: false, example: "avileslopez.javier@gmail.com" },
    phone: { type: "number", required: true, example: "17899999999" },
    access_token: { type: "string", required: true, example: "access_token" },
    address: { type: "string", required: false, example: "浙江杭州" }
};
