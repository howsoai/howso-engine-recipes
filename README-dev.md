#  Howso Engine&trade; Recipes - Dev

This project uses pip-tools (pip-compile and pip-sync) to build dependencies.

## How to update your virtual environment for this project

### TL;DR;
Run: `bin/build.sh gen_requirements && bin/build.sh sync_requirements`
to update your current virtual environment to using the latest requirements for Python 3.9.

### Step-by-step
From a fresh Python environment:

> pip install -U pip pip-tools

Next, run:

> bin/build.sh gen_requirements [VERSION]

Where `[VERSION]` is  a `MAJOR.MINOR` version number of Python you wish to use.
E.g. "3.8" or "3.9". If you omit this parameter, gen_requirements will default
to building Python 3.9 dependencies for this project.

    NOTE: This may take a short while, because it may need to compute hashes for each requirement.

Once complete, you should have `requirements-VERSION.txt` and
`requirements-dev-VERSION.txt` updated to latest on your system.

Now run:

> pip-sync requirements-VERSION.txt requirements-dev-VERSION.txt

(Again, the `VERSION` can be omitted and this will default to `3.9`)

This will synchronize your current environment to use the latest requirements.

The advantage of using `pip-sync` is that it will only make the changes
required to bring your ENV up-to-date.

## License

[License](LICENSE.txt)

## Contributing

[Contributing](CONTRIBUTING.md)