FROM neo4j:latest

ENV NEO4J_AUTH=neo4j/password

COPY data/neo4j.dump /var/lib/neo4j/data/databases/neo4j.dump

RUN neo4j-admin database load --from-path=/var/lib/neo4j/data/databases neo4j --overwrite-destination=true && \
    rm /var/lib/neo4j/data/databases/neo4j.dump
