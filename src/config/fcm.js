import admin from "firebase-admin";
import serviceAccount from "../../servicekey.json" with { type: "json" };

export const adminFCM = admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
});