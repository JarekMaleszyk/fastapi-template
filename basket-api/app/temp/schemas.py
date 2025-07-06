from pydantic import BaseModel
from typing import Any, List, Union


class MetadataItem(BaseModel):
    __root__: dict[str, str]


class DataGridBlock(BaseModel):
    metadata: List[MetadataItem] | None = None
    data: List[List[Any]] | None = None


class InputItem(BaseModel):
    name: str
    type: str
    value: Union[str, int, List[DataGridBlock]]


class InputData(BaseModel):
    inputs: List[InputItem]