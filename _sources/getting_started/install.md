# Installation

````{important}
The instructions on this page installs the stable version of *abTEM*. To install the upcoming version described in these pages, you have to install the code from source. 
```{code-block}
pip install git+https://github.com/abtem/abtem
```
````

There are two ways to install the *ab*TEM package, using conda or pip:

`````{tab-set}

````{tab-item} conda
Install *ab*TEM using conda:
```{code-block}
conda install -c conda-forge abtem
```
(Instructions on how to install miniconda can be found [here](https://docs.conda.io/en/latest/miniconda.html).)
````
````{tab-item} pip
Install *ab*TEM using pip:
```{code-block}
pip install abtem
```

Alternatively, if you have git and want to use unreleased features, you can install directly from github:
```{code-block}
pip install git+https://github.com/abTEM/abTEM
```
````
`````

## Optional dependencies

### GPAW (not available on Windows)

Some features of *ab*TEM, such as calculating potentials from DFT, require a working installation
of [GPAW](https://wiki.fysik.dtu.dk/gpaw/index.html). See [here](https://wiki.fysik.dtu.dk/gpaw/install.html) for
detailed installation instructions.

`````{tab-set}
````{tab-item} conda
Install GPAW using conda:
```{code-block}
conda install -c conda-forge gpaw
```
````
````{tab-item} pip

Install GPAW using pip:
```{code-block}
pip install gpaw
```
Install the PAW datasets into the folder `<dir>` using this command:
```{code-block}
gpaw install-data <dir>
```
````
`````

### GPU (only Nvidia) 

GPU calculations with *ab*TEM require a working installation of [CuPy](https://cupy.dev/) and compatible hardware.
See [here](https://docs.cupy.dev/en/stable/install.html) for detailed installation instructions.

`````{tab-set}

````{tab-item} conda
Install CuPy using conda:
```{code-block}
conda install -c conda-forge cupy
```
````
````{tab-item} pip
First, install the [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit).

Install CuPy using pip:
```{code-block}
pip install cupy-cuda*
```
where * should be substituted for the CUDA Toolkit version.
````
`````

### Development

See [our guide to contributing](contributing:clone_and_install) for instructions on a development installation of 
*ab*TEM.