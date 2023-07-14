from fastapi import FastAPI
import uvicorn


from ishop.routers.product_router import product_router
from ishop.routers.user_router import user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)

if __name__ == '__main__':
    uvicorn.run('server:app', port=8000, reload=True)
