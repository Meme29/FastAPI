from fastapi import FastAPI
from routes import multiplier, salary
from fastapi.responses import HTMLResponse


app = FastAPI()

app.include_router(multiplier.router, prefix="/double", tags=["Multiplier"])
app.include_router(salary.router, prefix="/compute", tags=["Salary"])

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("./pages/index.html") as f:
        return f.read()