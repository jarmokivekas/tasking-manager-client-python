# HOTOSM Tasking Manager Client for Python


This python library is intended for workflow automation with the [HOTOSM Tasking Manager](tasks.hotosm.org).

## Installing for use


The package is not on PyPI, but is installable with pip using:

```
python3 -m pip install https://github.com/jarmokivekas/tasking-manager-client-python.git
```

Using the git url in a requirements.txt should also work.

## Configuring devel environment

```
git clone git@github.com:jarmokivekas/tasking-manager-client-python.git
cd tasking-manager-client-python
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip intall -U pip
python3 -m pip install .
