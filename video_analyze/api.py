from fastapi import Body, FastAPI, status, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
import uvicorn
from typing import Optional
from pydantic import BaseModel

from schema import ai_camera_config_schema
from utils.check_config import CheckConfig

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConfigSchema(BaseModel):
    usecase_name: str
    usecase_type: str
    camera_setup: dict
    duration: dict
    zac_human: Optional[dict]
    zac_vehicle: Optional[dict]

@app.get("/usecases",  status_code = status.HTTP_200_OK)
async def get_all_usecase(response: Response):
    bockup_message = {"all_configs": [
    {
        "usecase_name": "camera1_zac_vehicle",
        "usecase_type": "zac_vehicle",
        "camera_name": "camera1"
    },
    {
        "usecase_name": "camera1_zac_human",
        "usecase_type": "zac_human",
        "camera_name": "camera1"
    }
    ]}

    return bockup_message

@app.get("/usecases/{usecase_name}",  status_code = status.HTTP_200_OK)
async def get_usecase(response: Response):
    bockup_message = ai_camera_config_schema
    return bockup_message

# addUsecase
@app.post("/usecases/",  status_code = status.HTTP_201_CREATED)
async def add_usecase(response: Response,
    config:ConfigSchema=Body(
        ...,
        example=ai_camera_config_schema)):
    config = config.dict()

    check_config = CheckConfig(config)
    config_accept, config_infor = check_config.check()
    if config_accept is False:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {"config_infor": config_infor}


    bockup_message = {"usecase_name": "camera1_zac_vehicle"}
    return bockup_message

# update usecase
@app.post("/usecases/{usecase_name}",  status_code = status.HTTP_201_CREATED)
async def update_usecase(response: Response,
    config:ConfigSchema=Body(
        ...,
        example=ai_camera_config_schema
)):
    config = config.dict()

    bockup_message = {"usecase_name": "camera1_zac_vehicle"}
    return bockup_message

# delete usecase 
@app.delete("/usecases/{usecase_name}", status_code = status.HTTP_204_NO_CONTENT)
async def remove_usecase(response: Response):
    # m_config = json.dumps(config)

    bockup_message = {"usecase_name": "camera1_zac_vehicle"}
    return bockup_message

# delete all usecases
@app.delete("/usecases/", status_code = status.HTTP_204_NO_CONTENT)
async def remove_all_usecases(response: Response):
    return {}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=5000, reload=True) 