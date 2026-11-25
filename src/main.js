import express from 'express'
import { authRouter } from './routes/auth.routes.js';
const app = express();

app.get('/', (req, res) => {
    res.send({"happy":"see you"})
})

app.use('/auth',authRouter)

app.listen(3000,()=>{
    console.log("http://localhost:3000")
})