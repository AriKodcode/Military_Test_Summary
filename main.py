from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post("/assignWithCsv")
async def losd_soldiers(file: UploadFile = File(...)):
    raw = await file.read()
    text = raw.decode("utf-8")
    lines = text.split("\n")
    soldiers = []
    for raw in lines[1:]:
        raw = raw.split(",")
        soldiers.append({
            "id": int(raw[0]),
            "first name": raw[1],
            "last name": raw[2],
            "genser": raw[3],
            "city": raw[4],
            "distance from base": int(raw[5].strip("\r"))
        })
    return soldiers
