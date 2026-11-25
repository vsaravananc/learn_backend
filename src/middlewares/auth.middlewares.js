
export const authMiddleWare = (req,res,next)=>{
    console.log(req.path)
    console.log(req.body)
    next()
}