
import express from 'express';

export const authMiddleWare = (
    req : express.Request, 
    res : express.Response,
    next : express.NextFunction
)=>{
    const brear : string | null = req.headers.authorization
    if (!brear){
       return res.status(401).json({'check':'mother'})
    }
    console.log(brear.trim().substring(6))
    next()
}

