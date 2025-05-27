from fastapi import FastAPI
import uvicorn

# Setup the flask application
app = FastAPI()

# Get the route
@app.get('/')
async def read_root():
    return {'message':'this is a fastapi test'}

if __name__ == "__main__":

# Run the Fast application
    uvicorn.run(app, host="127.0.0.1", port=8000)