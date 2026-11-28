import joi from 'joi'

export const authValidator = joi.object({
    email : joi.string().email().required(),
    passwrod : joi.string().min(4).required()
}).required()

export const createUser = joi.object({
    name : joi.string().min(3).required(),
    age : joi.number().integer().min(18).required(),
    email : joi.string().email().required(),
    password : joi.string().min(4).required(),
    phone_number : joi.string().required(),
    confirm_password : joi.ref('password')
}).required()