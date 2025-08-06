from strawberry.fastapi import GraphQLRouter
from fastapi import Depends
from sqlmodel import Session

from .schema import schema
from ...core.config.database import get_session

def get_context(session: Session = Depends(get_session)):
    return {"session": session}

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
    graphiql=True  # Enable GraphiQL playground
) 