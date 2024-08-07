# Installation

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