from fastapi import FastAPI
import uvicorn


from ishop.routers.product_router import product_router
from ishop.routers.user_router import user_router
from ishop.routers.sales_router import sales_router

from ishop.setup.populate_data import CREATE_DM, setup_db

if CREATE_DM == False:
    setup_db()
app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)
app.include_router(sales_router)
if __name__ == '__main__':
    uvicorn.run('server:app', port=8000)
