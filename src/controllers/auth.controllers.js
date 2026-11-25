import { authValidator } from "../validators/auth.validators.js"

export const loginController = async (req, res) => {
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