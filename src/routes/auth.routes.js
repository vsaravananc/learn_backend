
import express from 'express'
import { loginController , createUserController } from '../controllers/auth.controllers.js';
import { authMiddleWare } from '../middlewares/auth.middlewares.js';
export const authRouter = express.Router();

authRouter.use(authMiddleWare)
authRouter.post('/login', loginController)
authRouter.post('/register', createUserController)

