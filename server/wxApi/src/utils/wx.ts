import crypto from "crypto";

export class WXBizDataCrypt {
    appId: string;
    sessionKey: string;
    constructor({ appId, sessionKey }: { appId: string , sessionKey: string}) {
        this.appId = appId;
        this.sessionKey = sessionKey;
    }

    /**
     * name
     */
    public decryptData(encryptedData: string | Buffer, iv: Buffer | crypto.BinaryLike):string | Buffer {
        // base64 decode
        const sessionKey = new Buffer(this.sessionKey, "base64");
        encryptedData = new Buffer(encryptedData as string, "base64");
        iv = new Buffer(iv as string, "base64");

        try {
            // 解密
            const decipher = crypto.createDecipheriv("aes-128-cbc", sessionKey, iv);
            // 设置自动 padding 为 true，删除填充补位
            decipher.setAutoPadding(true);
            // eslint-disable-next-line
            var decoded = decipher.update(encryptedData, "binary", "utf8", null) as any;
            decoded += decipher.final("utf8");
            decoded = JSON.parse(decoded);
        } catch (err) {
            throw new Error("Illegal Buffer");
        }

        if (decoded && decoded?.watermark  ) {
            if (decoded?.watermark?.appid !== this.appId)
                throw new Error("Illegal Buffer");
        }
        return decoded;
    }
}

//解密
// var pc = new WXBizDataCrypt(appid, sessionKey);//这里的sessionKey 是上面获取到的
// var decodeData = pc.decryptData(encryptedData, iv);//encryptedData 是从小程序获取到的
// console.log('解密后 data: ', decodeData);

