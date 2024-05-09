# Howso Engine&trade; Recipes

This repository contains a collection of common use-cases primarily in Jupyter
Notebook form. They help demonstrate not only the capabilities of
[Howso Engine](https://github.com/howsoai/howso-engine) but also 
important concepts and usage instructions.

## Contents

The recipes are divided into 5 sections along with an introduction recipe.

### Sections
- 1-Insights: Explores the different types of insights that can be accessed using Howso
- 2-Workflows: Example workflows and use cases using a combination of different Howso insights and capabilities
- 3-Integration: Details how to connect and use Howso with a variety of outside platforms
- 4-Examples: Includes industry examples as well as extra examples of previously covered concepts
- 5-Technical_Validation: Demonstrations of certain Howso technical capabilities

## Set up

There are two main methods for setting up to run the recipes:
- Use a prebuilt VS Code dev container (requires VS Code and Docker)
  - Quicker startup method to try out Howso Engine or if dev containers are already part of your work environment
  - VS Code and Docker are required, but a Python environment isn't 
  - Run notebooks in VS Code only
- Install Howso Engine locally
  - Typical setup for those familiar with Python development
  - Howso Engine and dependencies are installed into your local Python environment
  - Run notebooks using whatever application you prefer (e.g. Jupyter servers, IDEs)

## Run in a Dev Container
Running in a dev container is a quick method to get set up to run the recipes,
assuming that you'd like to use Docker and VS Code. This method uses 
[container images](https://github.com/howsoai/howso-devcontainers/pkgs/container/howso)
built as part of the [Howso Development Containers](https://github.com/howsoai/howso-devcontainers).
You can use the dev containers
either by cloning this repo first and reopening VS Code, or using the "one click"
method that does both steps for you.

### Reopen in a Dev Container
There are a few quick steps needed to use the reopen method:
1. Clone this repository and cd into `howso-engine-recipes`
1. Start VS Code from the cloned repo directory using `code .`
1. Use the blue "><" button in the lower left corner of VS Code to open the dev container menu.
1. Select "Reopen in Container" and pick which dev container version you'd like to to use for the current session
1. Once it's restarted, you should be able to run recipes/notebooks and Python from that VS Code session using Howso Engine

### One Click Clone and Run in a Dev Container
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/howsoai/howso-engine-recipes)

If you already have VS Code and Docker installed, you can click the badge above
or [here](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/howsoai/howso-engine-recipes) 
to get started without cloning first and reopening VS Code. Clicking these links
will cause VS Code to automatically install the Dev Containers extension if
needed, clone the recipes into a container volume, and spin up a dev container
for use.

Note that this method clones the recipes into a Docker volume, which essentially
means that the setup is cached. If you'd like to use this method again later with
a newer version of the recipes and engine, you'll need to clear the cached volume.
Do that by using `docker volume list` to find the
`howso-engine-recipes-<hash>` volume, then use 
`docker volume rm howso-engine-recipes-<hash>` to remove the volume so VS Code
 will re-clone the repo and ensure that you're using both the latest recipes and
 latest Howso Dev Container (including the most recent release of Howso
 Engine).

## Local Installation

This repository is not a package to be installed in the usual sense. It's a
collection of Jupyter notebooks that can be be cloned into your local filesystem
and interactively run, modified and explored. To do that, the Python package
dependencies, including Howso Engine, must be installed. Start by cloning this
repo and opening a terminal in the resulting directory.

### Virtual Python Environment

Howso strongly recommends isolating from other Python projects with a
virtual environment. How this is done depends on your work-flow.

For example, if you use `venv`:

    python3 -m venv env
    source env/bin/activate

Or, if you use Anaconda, you might do (assuming Python 3.10):

    conda create --name howso-recipes-engine python=3.10
    conda activate howso-recipes-engine


### Installing Dependencies

Once a virtual environment is created with the desired version of Python,
activate the venv and install requirements with:

    pip install -r requirements.in

If successful, Howso Engine and all dependencies needed to run the recipes are
installed. It should be possible to run any of the recipes using your preferred
method of running Jupyter notebooks (e.g. Jupyter server, VS Code, etc.)

Happy exploring!

## License

[License](LICENSE.txt)

## Contributing

[Contributing](CONTRIBUTING.md)