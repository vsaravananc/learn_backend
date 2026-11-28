import { authValidator, createUser } from "../validators/auth.validators.js"
import { prisma } from "../config/db.js"
import hash from 'bcrypt'
// import { adminFCM } from "../config/fcm.js"

export const loginController = async (req , res) => {
    try {
        const result = await authValidator.validateAsync(req.body)
        res.json(req.body)
    } catch (error) {
        console.log(error)
        if (error.isJoi === true) {
            res.status(422).send({
                "validation": error.message || "validation failed"
            })
        }
    }
}

export const createUserController = async (req, res) => {
    try {
        const result = await createUser.validateAsync(req.body)
        const { name, age, email, password, phone_number, confirm_password } = result;
        if (password != confirm_password) {
            return res.status(422).json({
                'password': 'not same'
            });
        }
        const hash_password = hash.hash(password,10);
        const user = await prisma.user.create({
            data: { name, age, email, hash_password , phone_number }
        })
        
        return res.status(201).json({
            message: "User created successfully",
            data: user,
        });
    } catch (error) {
        console.log(error)
        if (error.isJoi === true) {
            res.status(422).send({
                "validation": error.message || "validation failed"
            })
        }
    }
}

// export const updateFCMController = async (req, res) => {
//     try {
//         const { id, fcmToken } = req.body;
//         const user = await prisma.user.update({
//             where: {
//                 id: Number(id),
//             },
//             data: {
//                 fcm_token: fcmToken,
//             }
//         });

//         return res.status(200).json({
//             message: "FCM token updated successfully",
//             data: user,
//         });

//     } catch (error) {
//         console.log(error);
//         return res.status(500).json({
//             message: "Internal server error",
//         });
//     }
// };

// export const sendFcmController = async (req, res) => {
//     try {
//         const { fcm, title, msg } = req.body;
//         const response = await adminFCM.messaging().send({
//             notification: {
//                 title: title,
//                 body: msg,
//             },
//             token: fcm,
//         });

//         return res.status(200).json({
//             message: "Notification sent successfully",
//             data: response,
//         });

//     } catch (error) {
//         console.log(error);
//         return res.status(500).json({
//             message: "Failed to send notification",
//         });
//     }
// };
