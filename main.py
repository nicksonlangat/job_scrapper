from typing import Union

from fastapi import FastAPI

from scrape_python_jobs import scrape_data

app = FastAPI()


@app.get("/")
def get_python_jobs():

    return {"data": scrape_data()}
