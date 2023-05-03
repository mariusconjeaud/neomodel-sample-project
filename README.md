# neomodelsampleproject

This is a sample project that uses the NeoModel library to interact with a Neo4j graph database.

## How to run
Before you proceed to running the project, you need to have a local Neo4j database running, with the expected data. For this, you can use the provided database dump and Dockerfile, or spin up your own local installation. Please proceed to the next section to understand how to use the Dockerfile.

**Note** : The dump targets Neo4j version 5.7.0 (latest as of May 2023).

Once you have a running database, you can run the following commands :

```bash
pipenv install
pipenv run dev
```

This project relies on [FastAPI](https://fastapi.tiangolo.com/) and will start an API listening on http://localhost:8000

## Local database
### Installation

You can use the provide Docker image that contains a sample database made for the sample project. You will need to first install Docker on your system. You can find instructions for installing Docker [here](https://docs.docker.com/get-docker).

### Building the Container

Once you have Docker installed, you can build the `neomodelsampleproject` container by running the following command in the root directory of this project:

```bash
docker build -t neomodelsampleproject .
```

This will create a new Docker image that you can use to launch the container.

### Running the Container

To run the container, use the following command:

```bash
docker run --name neomodelsampleproject -p7474:7474 -p7687:7687 -d neomodelsampleproject
```

Here's what each part of this command does:

- `--name`: Gives a name to the container.
- `-p 7474:7474`: Binds port 7474 on the host machine to port 7474 inside the container (7474 and 7687 are default ports for Neo4j ; 7474 for the web querying interface and 7687 for the driver Bolt protocol).
- `-d`: Runs the container in detached mode in the background.
- `neomodelsampleproject`: Uses the `neomodelsampleproject` Docker image that you built earlier.

You can then access the sample project by navigating to `http://localhost:7474` in your web browser. You should be able to see some data in the default `neo4j` database (Article, Author and Venue nodes)

### Stopping the Container

To stop the container, use the following command:

```
docker stop neomodelsampleproject
```

This will gracefully shut down the container and any services running inside it.

### Removing the Container Image

To remove the `neomodelsampleproject` image and all associated containers, use the following command:

```
docker rmi neomodelsampleproject
```

This will remove the image and any containers that were created from it.

### Conclusion

That's it! You should now be able to build and run this Docker container on your machine. If you encounter any issues or have questions, feel free to reach out to the project maintainers or seek help online.