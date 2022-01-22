# MDST Movie Recommendations

The official landing page of MDST Movie Recommendations project run during the Winter 2022 semester.

## Setup

Getting all setup to contribute to this project is as simple as a few commands.

### Virtual Environment

The first step is to initialize the virtual environment with all the required packages. Luckily, this isn't too hard.

First create a Python 3.8 virtual environment, below is the creation code for Linux/MacOS.

```bash
python3.8 -m venv venv
```

After activating the virtual environment, install the required dependencies using

```bash
pip install -r requirements.txt
```

If you also want to install dependencies of the development environment like code formatters and Jupyter notebook, run

```bash
pip install -r requirements-dev.txt
```

### Obtaining the Data

Getting the MovieLens dataset this project utilizes is not too difficult as well. With your virtual environment activated, run

```bash
python setup.py
```

That's all! You'll find the extracted dataset in the `data` folder. If you'd like more control over where you want to download and extract the dataset, you can run more fine-grained commands like

```bash
python setup.py --download custom_filepath --extract custom_filepath custom_extraction_dir
```

All setup options can be viewed using

```bash
python setup.py --help
```
