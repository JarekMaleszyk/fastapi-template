from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import json

from schemas import InputData
from models import InputRecord
from database import get_db  # zakładam że masz get_db z sessionmakerem

app = FastAPI()

@app.post("/submit")
def submit_input(data: InputData, db: Session = Depends(get_db)):
    record = InputRecord()

    for item in data.inputs:
        field_name = item.name.upper()

        if item.type == "string" or item.type == "decimal":
            setattr(record, field_name, str(item.value))

        elif item.type == "datagrid":
            metadata = None
            data_rows = None

            for part in item.value:
                if part.metadata:
                    metadata = json.dumps([m.__root__ for m in part.metadata])
                if part.data:
                    data_rows = json.dumps(part.data)

            setattr(record, f"{field_name}_METADATA", metadata)
            setattr(record, f"{field_name}_DATA", data_rows)

    db.add(record)
    db.commit()
    return {"status": "success", "record_id": record.id}