# {py:mod}`abtem.potentials.gpaw`

```{py:module} abtem.potentials.gpaw
```

```{autodoc2-docstring} abtem.potentials.gpaw
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GPAWParametrization <abtem.potentials.gpaw.GPAWParametrization>`
  - ```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization
    :summary:
    ```
* - {py:obj}`GPAWPotential <abtem.potentials.gpaw.GPAWPotential>`
  - ```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_core_correction_interpolators <abtem.potentials.gpaw.get_core_correction_interpolators>`
  - ```{autodoc2-docstring} abtem.potentials.gpaw.get_core_correction_interpolators
    :summary:
    ```
* - {py:obj}`integrate_slice <abtem.potentials.gpaw.integrate_slice>`
  - ```{autodoc2-docstring} abtem.potentials.gpaw.integrate_slice
    :summary:
    ```
````

### API

`````{py:class} GPAWParametrization(nodes=None, integration_step=0.002)
:canonical: abtem.potentials.gpaw.GPAWParametrization

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization.__init__
```

````{py:method} charge(symbol: str, charge: float = 0.0)
:canonical: abtem.potentials.gpaw.GPAWParametrization.charge

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization.charge
```

````

````{py:method} potential(symbol: str, charge: float = 0.0)
:canonical: abtem.potentials.gpaw.GPAWParametrization.potential

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization.potential
```

````

````{py:method} scattering_factor(symbol, charge: float = 0.0)
:canonical: abtem.potentials.gpaw.GPAWParametrization.scattering_factor

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization.scattering_factor
```

````

````{py:method} x_ray_scattering_factor(symbol: str, charge: float = 0.0)
:canonical: abtem.potentials.gpaw.GPAWParametrization.x_ray_scattering_factor

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization.x_ray_scattering_factor
```

````

`````

`````{py:class} GPAWPotential(calculators: typing.Union[gpaw.GPAW, typing.List[gpaw.GPAW], typing.List[str], str], gpts: typing.Union[int, typing.Tuple[int, int]] = None, sampling: typing.Union[float, typing.Tuple[float, float]] = None, slice_thickness: float = 1.0, exit_planes: int = None, plane: str = 'xy', origin: typing.Tuple[float, float, float] = (0.0, 0.0, 0.0), box: typing.Tuple[float, float, float] = None, periodic: bool = True, frozen_phonons: abtem.inelastic.phonons.BaseFrozenPhonons = None, repetitions: typing.Tuple[int, int, int] = (1, 1, 1), gridrefinement: int = 4, device: str = None)
:canonical: abtem.potentials.gpaw.GPAWPotential

Bases: {py:obj}`abtem.potentials.iam._PotentialBuilder`

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential.__init__
```

````{py:property} calculators
:canonical: abtem.potentials.gpaw.GPAWPotential.calculators

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential.calculators
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.potentials.gpaw.GPAWPotential.ensemble_axes_metadata
:type: typing.List[abtem.core.axes.AxisMetadata]

````

````{py:property} ensemble_shape
:canonical: abtem.potentials.gpaw.GPAWPotential.ensemble_shape

````

````{py:property} frozen_phonons
:canonical: abtem.potentials.gpaw.GPAWPotential.frozen_phonons

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential.frozen_phonons
```

````

````{py:method} generate_slices(first_slice: int = 0, last_slice: int = None)
:canonical: abtem.potentials.gpaw.GPAWPotential.generate_slices

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential.generate_slices
```

````

````{py:property} gridrefinement
:canonical: abtem.potentials.gpaw.GPAWPotential.gridrefinement

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential.gridrefinement
```

````

````{py:property} num_configurations
:canonical: abtem.potentials.gpaw.GPAWPotential.num_configurations

````

````{py:property} num_frozen_phonons
:canonical: abtem.potentials.gpaw.GPAWPotential.num_frozen_phonons

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential.num_frozen_phonons
```

````

````{py:property} repetitions
:canonical: abtem.potentials.gpaw.GPAWPotential.repetitions

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential.repetitions
```

````

`````

````{py:function} get_core_correction_interpolators(setups, D_asp, Q_aL, rcgauss)
:canonical: abtem.potentials.gpaw.get_core_correction_interpolators

```{autodoc2-docstring} abtem.potentials.gpaw.get_core_correction_interpolators
```
````

````{py:function} integrate_slice(array, gpts, a, b, thickness)
:canonical: abtem.potentials.gpaw.integrate_slice

```{autodoc2-docstring} abtem.potentials.gpaw.integrate_slice
```
````
