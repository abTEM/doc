# {py:mod}`abtem.potentials.charge_density`

```{py:module} abtem.potentials.charge_density
```

```{autodoc2-docstring} abtem.potentials.charge_density
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ChargeDensityPotential <abtem.potentials.charge_density.ChargeDensityPotential>`
  - ```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`add_point_charges_fourier <abtem.potentials.charge_density.add_point_charges_fourier>`
  - ```{autodoc2-docstring} abtem.potentials.charge_density.add_point_charges_fourier
    :summary:
    ```
* - {py:obj}`curl_fourier <abtem.potentials.charge_density.curl_fourier>`
  - ```{autodoc2-docstring} abtem.potentials.charge_density.curl_fourier
    :summary:
    ```
* - {py:obj}`integrate_gradient_fourier <abtem.potentials.charge_density.integrate_gradient_fourier>`
  - ```{autodoc2-docstring} abtem.potentials.charge_density.integrate_gradient_fourier
    :summary:
    ```
````

### API

`````{py:class} ChargeDensityPotential(atoms: typing.Union[ase.Atoms, abtem.inelastic.phonons.AtomsEnsemble], charge_density: numpy.ndarray = None, gpts: typing.Union[int, typing.Tuple[int, int]] = None, sampling: typing.Union[float, typing.Tuple[float, float]] = None, slice_thickness: typing.Union[float, typing.Tuple[float]] = 1.0, plane: str = 'xy', box: typing.Tuple[float, float, float] = None, origin: typing.Tuple[float, float, float] = (0.0, 0.0, 0.0), periodic: bool = True, exit_planes: int = None, repetitions: typing.Tuple[int, int, int] = (1, 1, 1), device: str = None)
:canonical: abtem.potentials.charge_density.ChargeDensityPotential

Bases: {py:obj}`abtem.potentials.iam._PotentialBuilder`

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential.__init__
```

````{py:property} charge_density
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.charge_density

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential.charge_density
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.ensemble_axes_metadata

````

````{py:property} ensemble_shape
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.ensemble_shape
:type: typing.Tuple[int, ...]

````

````{py:property} frozen_phonons
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.frozen_phonons

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential.frozen_phonons
```

````

````{py:method} generate_slices(first_slice: int = 0, last_slice: int = None)
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.generate_slices

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential.generate_slices
```

````

````{py:property} is_lazy
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.is_lazy

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential.is_lazy
```

````

````{py:property} num_configurations
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.num_configurations

````

````{py:property} num_frozen_phonons
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.num_frozen_phonons

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential.num_frozen_phonons
```

````

````{py:property} repetitions
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.repetitions

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential.repetitions
```

````

`````

````{py:function} add_point_charges_fourier(array: numpy.ndarray, atoms: ase.Atoms, broadening: float = 0.05) -> numpy.ndarray
:canonical: abtem.potentials.charge_density.add_point_charges_fourier

```{autodoc2-docstring} abtem.potentials.charge_density.add_point_charges_fourier
```
````

````{py:function} curl_fourier(vector_field: numpy.ndarray, cell: ase.cell.Cell) -> numpy.ndarray
:canonical: abtem.potentials.charge_density.curl_fourier

```{autodoc2-docstring} abtem.potentials.charge_density.curl_fourier
```
````

````{py:function} integrate_gradient_fourier(array: numpy.ndarray, cell: ase.cell.Cell, in_space: str = 'real', out_space: str = 'real') -> numpy.ndarray
:canonical: abtem.potentials.charge_density.integrate_gradient_fourier

```{autodoc2-docstring} abtem.potentials.charge_density.integrate_gradient_fourier
```
````
