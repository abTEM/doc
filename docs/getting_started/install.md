(getting_started:install)=
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

To distribute a calculation across **several GPUs** on a node, also install
[`dask-cuda`](https://docs.rapids.ai/api/dask-cuda/stable/install/) (NVIDIA GPUs,
Linux only), matched to your CUDA/RAPIDS version. See
{ref}`Multiple GPUs <walkthrough:parallelization:multigpu>` in the walkthrough.

```{note}
`dask-cuda` pins `dask` and `distributed` to the versions of its own RAPIDS
release, which may not be the versions *ab*TEM was installed with. If pip
insists on downgrading `dask` (or refuses to resolve the environment at all),
install `dask-cuda` without its dependencies and keep the versions you already
have:

    pip install --no-deps dask-cuda

Both packages track `dask` closely, so it is worth checking that a simple
multi-GPU computation runs after installing this way.
```

### Metal on Apple silicon (experimental)

*ab*TEM can run on the GPU of an Apple silicon Mac through their
[Metal API](https://developer.apple.com/metal/), using [PyTorch](https://pytorch.org/) the way it uses CuPy
for CUDA. Metal support is experimental. Operations without a Metal implementation raise an error naming the
operation rather than quietly moving your data back to the CPU, so an unsupported path is visible rather than
merely slow.

Install *ab*TEM with the `mps` extra, which pulls in PyTorch:

```{code-block}
pip install "abtem[mps]"
```

The extra is restricted to macOS on Apple silicon, since Metal exists nowhere else.

To enable the backend, set `enable_mps` **before** *ab*TEM is imported — either through the environment:

```{code-block}
ABTEM_ENABLE_MPS=true python your_script.py
```

or in `~/.config/abtem/abtem.yaml`:

```{code-block}
enable_mps: true
```

```{note}
`abtem.config.set(enable_mps=True)` does **not** work: the setting decides whether PyTorch is imported before
FFTW, and by the time the call runs that has already been settled. PyTorch and FFTW each bundle their own copy
of `libomp`, and a process that loaded FFTW's first crashes inside ordinary PyTorch operations.
```

You can verify that Metal support is available using the code below:

```python
import torch
assert torch.backends.mps.is_available()

import abtem
wave = abtem.PlaneWave(energy=100e3, gpts=128, sampling=0.05)
assert wave.build(lazy=False).copy_to_device("mps").array.device.type == "mps"
```

Then pass `device="mps"` where you would otherwise pass `"gpu"`:

```python
potential = abtem.Potential(atoms, gpts=512, device="mps")
probe = abtem.Probe(energy=200e3, semiangle_cutoff=20, device="mps")
```

Two things are worth knowing before you benchmark:

- **Metal is single precision.** `precision` must be `float32`; pairing `device="mps"` with `float64` is
  refused outright rather than silently narrowed. Use the `cpu` or `gpu` device if you need double precision.
- **Grid size matters more than on other backends.** Metal's FFT degrades sharply on sizes whose prime
  factors exceed 7. A grid of 272 (which is 16 times 17) can be no faster than the CPU, where 256 or 512
  runs several times faster. Choose `gpts` accordingly, or set `grid.round-to-fast-fft`.

### Development installation

See [our guide to contributing](contributing:clone_and_install) for instructions on a development installation of 
*ab*TEM.