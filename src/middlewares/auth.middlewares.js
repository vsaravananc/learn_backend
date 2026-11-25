
export const authMiddleWare = (req,res,next)=>{
    console.log(req.path)
    next()
}