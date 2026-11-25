
import express from 'express'
import { loginController } from '../controllers/auth.controllers.js';
import { authMiddleWare } from '../middlewares/auth.middlewares.js';
export const authRouter = express.Router();

authRouter.use(authMiddleWare)
authRouter.get('/login', loginController)

