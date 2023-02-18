from typing import Optional
from pydantic import BaseModel


class ProjectRequestPut(BaseModel):
    brief_information: Optional[str]
    descrip_problem: Optional[str]
    primary_goal: Optional[str]
    major_groups: Optional[str]
    implementation_experience: Optional[str]
    project_potential: Optional[str]


class ProjectRequest(BaseModel):
    brief_information: str
    descrip_problem: str
    primary_goal: str
    major_groups: str
    implementation_experience: str
    project_potential: str


class ProjectResponse(BaseModel):
    brief_information: str
    descrip_problem: str
    primary_goal: str
    major_groups: str
    implementation_experience: str
    project_potential: str