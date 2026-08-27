# Installation

There are many ways to install the *ab*TEM package, for example conda or pip:

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

Alternatively, if you have git and want to use unreleased features, you can install directly from GitHub:
```{code-block}
pip install git+https://github.com/abTEM/abTEM
```
````
`````

## Optional dependencies

A few optional Python packages are bundled as pip *extras*, so they can be installed together with *ab*TEM:

- `abtem[gpaw]` installs [hankel](https://hankel.readthedocs.io/) and [sympy](https://www.sympy.org/), the Python-side requirements of the DFT-based features — the form factors for core-loss EELS, and the potential parametrization fitted to an all-electron calculation. GPAW itself is *not* installed by this extra, see below.
- `abtem[extra]` installs [bokeh](https://bokeh.org/), [ipycytoscape](https://ipycytoscape.readthedocs.io/) and the [Dask labextension](https://github.com/dask/dask-labextension), used for the task-graph visualizations and the diagnostics dashboard shown in the [parallelization walkthrough](walkthrough:parallelization).
- `abtem[all]` installs both of the above.

```{code-block}
pip install abtem[all]
```

With conda, install the packages by name instead, for example:

```{code-block}
conda install -c conda-forge hankel sympy bokeh ipycytoscape
```

```{note}
Before version `1.1.0`, the `gpaw` extra was called `core-loss` and installed only `sympy`.
```

The GPU packages ([CuPy](https://cupy.dev/) and, for several GPUs, `dask-cuda`) are deliberately left out of the extras: their wheels are specific to a CUDA version and have to match the toolkit installed on your machine, so they are installed separately as described below.

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

The `hankel` and `sympy` packages that the DFT-based features need on top of GPAW itself come from the `abtem[gpaw]` extra above.

### GPU (only NVIDIA) 

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

### Metal on Apple silicon (experimental)

A subset of features in *ab*TEM can be accelerated on Apple silicon processors using their [Metal API](https://developer.apple.com/metal/). 
To enable this features requires a working installation of [PyTorch](https://pytorch.org/). Metal support is 
currently highly experimental, and not all features are supported. Features not currently supported, will fall 
back to the NumPy implementation.

```{code-block}
conda install pytorch torchvision torchaudio -c pytorch-nightly
conda install -c conda-forge abtem jupyterlab
pip install scipy --force-reinstall --no-deps
```
To enable this feature you need to configure `enable_mps`.
```python
import abtem
abtem.config.set(enable_mps=True)
```
You can verify that mps support is available using the code below:
```python
import torch
assert torch.backends.mps.is_available()

wave = abtem.PlaneWave(energy=100e3, gpts=128, sampling=0.05)
assert wave.build(lazy=False).copy_to_device("mps").array.device.type == "mps"
```

### Development installation

See [our guide to contributing](contributing:clone_and_install) for instructions on a development installation of 
*ab*TEM.