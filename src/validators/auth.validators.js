import joi from 'joi'

export const authValidator = joi.object({
    email : joi.string().email().required(),
    passwrod : joi.string().min(4).required()
}).required()
