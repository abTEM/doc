# {py:mod}`abtem.potentials.gpaw`

```{py:module} abtem.potentials.gpaw
```

```{autodoc2-docstring} abtem.potentials.gpaw
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GPAWParametrization <abtem.potentials.gpaw.GPAWParametrization>`
  - ```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization
    :parser: rst
    :summary:
    ```
* - {py:obj}`GPAWPotential <abtem.potentials.gpaw.GPAWPotential>`
  - ```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_core_correction_interpolators <abtem.potentials.gpaw.get_core_correction_interpolators>`
  - ```{autodoc2-docstring} abtem.potentials.gpaw.get_core_correction_interpolators
    :parser: rst
    :summary:
    ```
* - {py:obj}`integrate_slice <abtem.potentials.gpaw.integrate_slice>`
  - ```{autodoc2-docstring} abtem.potentials.gpaw.integrate_slice
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} GPAWParametrization(...)
:canonical: abtem.potentials.gpaw.GPAWParametrization

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization.__init__
:parser: rst
```

````{py:method} charge(...)
:canonical: abtem.potentials.gpaw.GPAWParametrization.charge

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization.charge
:parser: rst
```

````

````{py:method} potential(...)
:canonical: abtem.potentials.gpaw.GPAWParametrization.potential

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization.potential
:parser: rst
```

````

````{py:method} scattering_factor(...)
:canonical: abtem.potentials.gpaw.GPAWParametrization.scattering_factor

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization.scattering_factor
:parser: rst
```

````

````{py:method} x_ray_scattering_factor(...)
:canonical: abtem.potentials.gpaw.GPAWParametrization.x_ray_scattering_factor

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWParametrization.x_ray_scattering_factor
:parser: rst
```

````

`````

`````{py:class} GPAWPotential(...)
:canonical: abtem.potentials.gpaw.GPAWPotential

Bases: {py:obj}`abtem.potentials.iam._PotentialBuilder`

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential.__init__
:parser: rst
```

````{py:property} calculators
:canonical: abtem.potentials.gpaw.GPAWPotential.calculators

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential.calculators
:parser: rst
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
:parser: rst
```

````

````{py:method} generate_slices(...)
:canonical: abtem.potentials.gpaw.GPAWPotential.generate_slices

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential.generate_slices
:parser: rst
```

````

````{py:property} gridrefinement
:canonical: abtem.potentials.gpaw.GPAWPotential.gridrefinement

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential.gridrefinement
:parser: rst
```

````

````{py:property} num_configurations
:canonical: abtem.potentials.gpaw.GPAWPotential.num_configurations

````

````{py:property} num_frozen_phonons
:canonical: abtem.potentials.gpaw.GPAWPotential.num_frozen_phonons

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential.num_frozen_phonons
:parser: rst
```

````

````{py:property} repetitions
:canonical: abtem.potentials.gpaw.GPAWPotential.repetitions

```{autodoc2-docstring} abtem.potentials.gpaw.GPAWPotential.repetitions
:parser: rst
```

````

`````

````{py:function} get_core_correction_interpolators(...)
:canonical: abtem.potentials.gpaw.get_core_correction_interpolators

```{autodoc2-docstring} abtem.potentials.gpaw.get_core_correction_interpolators
:parser: rst
```
````

````{py:function} integrate_slice(...)
:canonical: abtem.potentials.gpaw.integrate_slice

```{autodoc2-docstring} abtem.potentials.gpaw.integrate_slice
:parser: rst
```
````
