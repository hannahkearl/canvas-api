from pydantic import BaseModel



class Course(BaseModel):
    name: str
    id: int

class Discussion(BaseModel):
    title: str
    id: int

class DiscussionEntry(BaseModel):
    body: str
