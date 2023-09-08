# Howso Engine&trade; Recipes

This repository contains a collection of common use-cases primarily in Jupyter
Notebook form. This is to help demonstrate not only the capabilities of
[Howso Engine](https://github.com/howsoai/howso-engine) but to also illustrate important concepts and show how these
tools can be used.


## Installation

This repository is not a package to be installed in the usual sense, but rather
placed onto the local filesystem where the various notebooks can be
interactively run, modified and explored.

    cd your_local_workspace
    unzip howso-recipes-engine-[VERSION].zip
    cd howso-recipes-engine-[VERSION]


### Virtual Python Environment

Howso strongly recommends isolating from other Python projects with a
virtual enviroment. How this is done depends on your work-flow.

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

Among other things, this will install Jupyter notebook support. To get started,
run in your terminal:

    jupyter lab

This should open a new window/tab in your browser, but if not, follow the
instructions emitted to your terminal by the Jupyter notebook server and either
CTRL-click one of the URLs, or simply copy and paste the URL into your browser.

From here, you should have available to you all of the Howso recipes for
Engine as Jupyter notebooks. If you're un-familiar with using JupyterLab or
Notebooks, please visit: [jupyter.org](https://jupyter.org/) and
[Jupyter's documentation](https://docs.jupyter.org/en/latest/) to learn more.

Happy exploring!

## License

[License](LICENSE.txt)

## Contributing

[Contributing](CONTRIBUTING.md)