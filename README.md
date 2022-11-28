# data archiver

This is an sandbox example pattern for archiving data from REST services.

The intent is to explore Python with flask, swagger ui, file IO, app config, logging and Click CLI library.

The test with compatible services, also pull the 
`morbrian/sample-flask-services` repository and run the sample service.

Running the flask development server

```
flask run -p 5001

# swagger available at http://127.0.0.1:5001
#
# port can be changed per your environment, 
# 5001 helps deconflict with the sample data dev server on default 5000
```

Building the Docker image

```
docker build -t darchman .
```

Running the Docker container in development

```
docker run --network="host" -p 8080:8080 darchman

# swagger available at http://127.0.0.1:8080/
```

Running the Docker container with custom configuration

```
docker run -v /full/path/data-archive-manager/darchman-local.yaml:/app/darchman.yaml -p 8080:8080 darchman
```

Using the Mediator CLI

```
# take a snapshot of all cats data
python cli/mediator_cli.py snapshot cats

# get a histor of all cat data snapshots
python cli/mediator_cli.py history cats
```

Using the Adapter CLI

```
# show the command help
python cli/adapter_cli.py

# example export all dogs
python cli/adapter_cli.py export dogs

# example export all dogs on alternate URL
python cli/adapter_cli.py export dogs --url http://localhost:8080

# example put a new cat
python cli/adapter_cli.py put cats piggy '{ "id": "piggy", "name": "Piggy", "color": "pink" }'

# example get a cat
python cli/adapter_cli.py get cats chloe

# example delete a dog
python cli/adapter_cli.py delete dog piper
```
