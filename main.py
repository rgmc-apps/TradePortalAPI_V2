import uvicorn
from config import DEV_MODE

if __name__ == "__main__":
    if DEV_MODE:
        uvicorn.run("app.main:app", reload=True, host='0.0.0.0', port=8000)
    else:
        uvicorn.run("app.main:app", reload=True)