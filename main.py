from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
async def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    ##params = {"latitude": 27.7172, "longitude": 85.3240, "current": "temperature_2m"}
    response = httpx.get(url,params={"latitude": 27.7172, "longitude": 85.3240, "current": "temperature_2m"})
    return response.json()
