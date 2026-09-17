# Open Research Europe *ab*TEM methods article (2021)

Code for reproducing the use cases shown in our Open Research Europe *ab*TEM methods
article ([doi:10.12688/openreseurope.13015.1](https://doi.org/10.12688/openreseurope.13015.1)).

> [!WARNING]
> Written against the *ab*TEM 1.0.0beta API of 2021; these notebooks do not run with
> current *ab*TEM. See the [articles README](../README.md).

- `hBN_DFT_IAM.ipynb` — HRTEM/STEM of hBN comparing a GPAW *ab initio* potential with the
  independent atom model. Requires the optional GPAW installation.
- `MoS2_ptycho.ipynb` — 4D-STEM of MoS<sub>2</sub> with a ptychographic phase reconstruction.
- `cbed_md_phonons.ipynb` — CBED and electron diffraction of thick Si(100), comparing
  molecular-dynamics phonons with the Einstein model. Reads an `md_phonons.traj`
  trajectory that was never included in the repository.
- `large_stem_simulations.ipynb` — PRISM benchmark of large STEM simulations on CPU and
  GPU, against published Prismatic 1.2.1 timings.
