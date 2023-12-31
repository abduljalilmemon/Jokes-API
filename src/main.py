import uvicorn
from fastapi import FastAPI
from apis import api

app = FastAPI()
app.include_router(api)

if __name__ == '__main__':
    uvicorn.run(app, port=5000)
