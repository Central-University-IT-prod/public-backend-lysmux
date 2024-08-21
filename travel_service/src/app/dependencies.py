from typing import Annotated, AsyncGenerator

from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from workflow import WorkflowData


def get_workflow_data(request: Request) -> WorkflowData:
    return request.state.workflow_data


WorkflowDataDep = Annotated[WorkflowData, Depends(get_workflow_data)]


async def get_db_session(
        workflow_data: WorkflowDataDep
) -> AsyncGenerator[AsyncSession, None]:
    session_maker = workflow_data.session_maker

    async with session_maker() as session:
        async with session.begin():
            yield session


DBSessionDep = Annotated[AsyncSession, Depends(get_db_session)]
