# data archiver

This is an sandbox example pattern for archiving data from REST services.

The intent is to explore Python with flask, swagger ui, file IO, app config, logging and Click CLI library.

The test with compatible services, also pull the 
`morbrian/sample-flask-services` repository and run the sample service.

Some First Time Initialization Stuff

```
# only need to create env the first time after clone
conda env create -f environment.yml python=3.10.8

# need a few supporting apps
sudo apt install python3-flask
sudo apt install python3-pip

#TODO: not sure why this was needed since it's in the environment.yml
pip install flask-restx
```

Activate Environment

```
# need to do this eachy time you want to use this in a new terminal
conda activate data-archive-manager
```

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

# swagger available at http://127.0.0.1:8080/data-archive-manager
```

Running the Docker container with custom configuration

```
docker run -v /full/path/data-archive-manager/darchman-local.yaml:/app/darchman.yaml -p 8080:8080 darchman
```

Configuration `PYTHONPATH` so the CLI tools can find the rest of the library.

```
# running this from your project folder will be enough for development
export PYTHONPATH=`pwd`
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
python cli/adapter_cli.py export dogs --url http://localhost:8080/data-archive-manager

# example put a new cat
python cli/adapter_cli.py put cats piggy '{ "id": "piggy", "name": "Piggy", "color": "pink" }'

# example get a cat
python cli/adapter_cli.py get cats chloe

# example delete a dog
python cli/adapter_cli.py delete dog piper
```

# Versioned Build

```
export MY_TAG=0.0.1
docker compose build

# run the image to verify it
# wil be at http://localhost:5001/data-archive-manager
docker compose up

# and if you have a place to push it
docker compose push
```