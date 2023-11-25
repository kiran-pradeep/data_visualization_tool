from pydantic import BaseModel

class GraphData(BaseModel):
    labels: list
    title: str
    data: dict
    plot_type: str
    