import uvicorn
from config import DEV_MODE, PORT

if __name__ == "__main__":
    # uvicorn.run("app.main:app", reload=True)
    if DEV_MODE:
        uvicorn.run("app.main:app", reload=True)
    else:
        uvicorn.run("app.main:app", reload=True, host='127.0.0.1', port=PORT)