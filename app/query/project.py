from sqlalchemy import and_, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import coalesce
from app.db.models import Project
from app.schemas.project import ProjectResponse, ProjectRequest, ProjectRequestPut
from app.schemas.exception import BadRequest


async def put_project(
    project: ProjectRequestPut,
    session: AsyncSession,
    nickname: str
):
    update_project_query = (
        update(Project)
        .values(
            brief_information=coalesce(project.brief_information, Project.brief_information),
            descrip_problem=coalesce(project.descrip_problem, Project.descrip_problem),
            primary_goal=coalesce(project.primary_goal, Project.primary_goal),
            major_groups=coalesce(project.major_groups, Project.major_groups),
            implementation_experience=coalesce(project.implementation_experience, Project.implementation_experience),
            project_potential=coalesce(project.project_potential, Project.project_potential)
        )
        .where(
            and_(
                Project.author == nickname,
                Project.status == False
            )
        )
    )
    await session.execute(update_project_query)
    await session.commit()


async def get_project(nickname: str, session: AsyncSession):
    project_query = select(Project).where(and_(Project.author == nickname, Project.status == False))
    project: Project = await session.scalar(project_query)
    if not project:
        raise BadRequest(error="Проекта не  существует")
    return ProjectResponse(brief_information=project.brief_information,
                           descrip_problem=project.descrip_problem,
                           primary_goal=project.primary_goal,
                           major_groups=project.major_groups,
                           implementation_experience=project.implementation_experience,
                           project_potential=project.project_potential)


async def add_project(project: ProjectRequest, session: AsyncSession, nickename: str):
    project_query = select(Project).where(and_(Project.author == nickename, Project.status == False))
    project_check: Project = await session.scalar(project_query)
    if project_check:
        raise BadRequest(error="Проект уже существует")

    new_project = Project(
        author=nickename,
        brief_information=project.brief_information,
        descrip_problem=project.descrip_problem,
        primary_goal=project.primary_goal,
        major_groups=project.major_groups,
        implementation_experience=project.implementation_experience,
        project_potential=project.project_potential,
        status=False
    )
    session.add(new_project)
    await session.commit()
