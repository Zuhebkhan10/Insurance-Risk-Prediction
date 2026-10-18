from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Optional
import pickle
import pandas as pd

# Import the ML model
with open("model.pkl",'rb')as f:
    model=pickel.load(f)

app=FastAPI()

# Pydantic model to validate incoming data