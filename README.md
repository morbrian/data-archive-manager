# data archiver

This is an sandbox example pattern for archiving data from REST services.

The intent is to explore Python with flask, swagger ui, file IO, app config, logging and Click CLI library.

The test with compatible services, also pull the `morbrian/sample-flask-services` repository and run the sample service.

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
