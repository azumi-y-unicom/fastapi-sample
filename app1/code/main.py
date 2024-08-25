from fastapi import FastAPI
import routers.items

app = FastAPI(
    title="Sample App1",
    description="サンプルAPI App1",
    version="1.0.0"
)

app.include_router(routers.items.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
