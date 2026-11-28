
import express from 'express'
import { loginController , createUserController  } from '../controllers/auth.controllers.js';
import { authMiddleWare } from '../middlewares/auth.middlewares.ts';
export const authRouter = express.Router();

authRouter.use(authMiddleWare)
authRouter.post('/login', loginController)
authRouter.post('/register', createUserController)
// authRouter.post('/update-fcm',updateFCMController)
// authRouter.post('/send-msg',sendFcmController)

