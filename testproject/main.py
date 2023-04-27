"""Application main file."""
from fastapi import FastAPI

from neomodel import (
    StructuredNode,
    StringProperty,
    IntegerProperty,
    RelationshipTo,
    OneOrMore,
)
from neomodel.contrib.spatial_properties import PointProperty

from neomodel import config

neo4j_dsn = "bolt://neo4j:Abcd-1234@localhost:7687/citation-neomodel"
config.DATABASE_URL = neo4j_dsn


class Venue(StructuredNode):
    name = StringProperty(index=True)


class Author(StructuredNode):
    name = StringProperty(index=True)
    address = PointProperty(crs="wgs-84")

    co_author = RelationshipTo("Author", "CO_AUTHOR")


class Article(StructuredNode):
    abstract = StringProperty()
    index = StringProperty(unique_index=True)
    n_citation = IntegerProperty()
    title = StringProperty(index=True)
    year = IntegerProperty(index=True)

    author = RelationshipTo(Author, "AUTHOR", cardinality=OneOrMore)
    cited = RelationshipTo("Article", "CITED")
    venue = RelationshipTo(Venue, "VENUE", cardinality=OneOrMore)


# Create app
app = FastAPI()


@app.get("/")
async def root():
    articles = Article.nodes.all()
    return {"# of articles": len(articles)}

    # france = Country.nodes.get_or_none(code="FR")
    # if france is None:
    #     france = Country(code="FR").save()
