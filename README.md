# Summarisr

Simple REST API application using FastAPI to summarise documents

## Tools used

- [FastAPI](https://fastapi.tiangolo.com/)
- [pytest](https://docs.pytest.org/)
- [Docker](https://www.docker.com/)

## Functionality

The application has two endpoints.

The first endpoint accepts a POST request with an English document and returns an ID (`document_id`).
An example request for the service would be:
 
```
POST / HTTP/1.1
Accept: application/json
Content-Type: application/x-www-form-urlencoded
 
text=This%20is%20a%20long%20text
```
 
The second endpoint accepts a GET request with a document ID and returns a summary of the specified document.
The response of this endpoint should look like the below:
 
```
HTTP/1.1 200 OK
Content-Type: application/json
   
{
    "document_id": "exampaple_id",
    "summary": "This is the summary"
}
``` 

## Design decisions

The following design decisions have been made when implementing this application.

1. Storage  

    To simplify the implementation, the application currently stores uploaded documents only in memory (Python dictionary).

    This implementation has several issues:

    - The data will be lost when the application server stops.
    - The dictionary does not automatically generate unique IDs, so the document ID is manually assigned from a random [UUID](https://docs.python.org/3/library/uuid.html).
    - The max data volume will depend on the available memory in the server environment. No test has been done to check this limitation.

    The storage layer can be replaced with a permanent storage system (such as PostgreSQL, other databases or file-based storage like Amazon S3) to solve these issues. It can be easily done because the storage layer is currently implemented as a FastAPI dependency.


2. Summarisation
   
    The application uses a library called [Sumy](https://github.com/miso-belica/sumy) to summarise texts. Verifying its quality is out of this project's scope, but it seems very popular based on the number of stars on Github.

    The application currently uses English as the text language, and the summary length is set to 3 (i.e. three sentences or less).

    For example, the application returns the following summary for the plot of the film "The Matrix" (taken from [Wikipedia](https://en.wikipedia.org/wiki/The_Matrix#Plot)).

    > "Computer programmer Thomas Anderson, known by his hacking alias \"Neo\", is puzzled by repeated online encounters with the phrase \"the Matrix\". Morpheus offers Neo a choice between two pills: red to reveal the truth about the Matrix, and blue to forget everything and return to his former life. As Neo recuperates from a lifetime of physical inactivity in the pod in the aftermath of being redpilled, Morpheus explains the situation: In the early 21st century, a war broke out between humanity and intelligent machines."

    The summarisation occurs when a document is uploaded, which might not be ideal for large documents. The process can be pushed to a storage layer, where documents can be summarised asynchronously.

    It is easy to replace the library with something else if necessary because it is implemented as a FastAPI dependency.

3. Tests

    The application contains unit tests and integration tests. The integration tests automatically run the Docker container to start the FastAPI server.

    Unit and integration tests run via Github Actions when changes are pushed to the Github repository.


## How to run the application

You can start the application by running the docker image.

```
$ cd summarisr
$ docker-compose up -d
```

After the application starts, the API documentation will become accessible at [http://localhost:8001/docs](http://localhost:8001/docs).
