from pydantic import BaseModel

class GraphData(BaseModel):
    data: dict
    plot_type: str