import { authValidator, createUser } from "../validators/auth.validators.js"
import { prisma } from "../config/db.js"

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
        const user = await prisma.user.create({
            data: result
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

export const updateFCMController = async (req, res) => {
    try {
        const { id, fcmToken } = req.body;
        const user = await prisma.user.update({
            where: {
                id: Number(id),
            },
            data: {
                fcm_token: fcmToken,
            }
        });

        return res.status(200).json({
            message: "FCM token updated successfully",
            data: user,
        });

    } catch (error) {
        console.log(error);
        return res.status(500).json({
            message: "Internal server error",
        });
    }
};
