from fastapi import APIRouter, status, Depends, Body, Path
from app.auth.oauth2 import get_current_user
from app.query.project import put_project, add_project, get_project
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.connection import get_session
from app.schemas.auth import SuccessfulResponse
from app.schemas.project import ProjectRequestPut, ProjectRequest, ProjectResponse
from typing import List

project_router = APIRouter(tags=["Project"])


@project_router.post(
    "/project/new",
    response_model=SuccessfulResponse,
    status_code=status.HTTP_201_CREATED,
)
async def add_project_new(
    project: ProjectRequest = Body(...),
    session: AsyncSession = Depends(get_session),
    current_user: str = Depends(get_current_user),
):
    # await check_admin(current_user, session)
    await add_project(project, session, current_user)
    return SuccessfulResponse()


@project_router.get(
    "/project/new",
    status_code=status.HTTP_200_OK,
    response_model=ProjectResponse,
)
async def get_project_new(
    session: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
) -> ProjectResponse:
    # await check_admin(current_user, session)
    return await get_project(current_user, session)


@project_router.put(
    "/project/new",
    response_model=SuccessfulResponse,
    status_code=status.HTTP_201_CREATED,
)
async def put_project_route(
    new_proj: ProjectRequestPut = Body(..., description="New name"),
    session: AsyncSession = Depends(get_session),
    current_user: str = Depends(get_current_user),
):
    # await check_admin(current_user, session)
    await put_project(
        new_proj,
        session,
        current_user
    )
    return SuccessfulResponse()
