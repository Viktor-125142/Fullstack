"""
Написать программу, которая сортирует список строк по длине,
сначала по возрастанию, а затем по убыванию.
"""
from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI(
    title="Сортировка списка по длине строк"
)


class SortRequest(BaseModel):
    strings: list[str] = Field(["a", "asd", "aswedf", "qwer"], example=["string1", "string2", "string3"])
    ascending: bool = Field(default=True, example=True)


@app.post("/sort_up")
def sort_strings(request: SortRequest, ascending: bool = True) -> list[str]:
    """
          Сортирует список строк сначала по возрастанию длины, а затем по убыванию. \n
          True - по возрастанию \n
          False - по убыванию
          """
    return sorted(request.strings, key=len, reverse=not ascending)


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)

