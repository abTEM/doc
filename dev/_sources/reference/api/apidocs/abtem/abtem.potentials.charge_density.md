# {py:mod}`abtem.potentials.charge_density`

```{py:module} abtem.potentials.charge_density
```

```{autodoc2-docstring} abtem.potentials.charge_density
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ChargeDensityPotential <abtem.potentials.charge_density.ChargeDensityPotential>`
  - ```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`add_point_charges_fourier <abtem.potentials.charge_density.add_point_charges_fourier>`
  - ```{autodoc2-docstring} abtem.potentials.charge_density.add_point_charges_fourier
    :parser: rst
    :summary:
    ```
* - {py:obj}`curl_fourier <abtem.potentials.charge_density.curl_fourier>`
  - ```{autodoc2-docstring} abtem.potentials.charge_density.curl_fourier
    :parser: rst
    :summary:
    ```
* - {py:obj}`integrate_gradient_fourier <abtem.potentials.charge_density.integrate_gradient_fourier>`
  - ```{autodoc2-docstring} abtem.potentials.charge_density.integrate_gradient_fourier
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} ChargeDensityPotential(...)
:canonical: abtem.potentials.charge_density.ChargeDensityPotential

Bases: {py:obj}`abtem.potentials.iam._PotentialBuilder`

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential.__init__
:parser: rst
```

````{py:property} charge_density
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.charge_density

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential.charge_density
:parser: rst
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
:parser: rst
```

````

````{py:method} generate_slices(...)
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.generate_slices

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential.generate_slices
:parser: rst
```

````

````{py:property} is_lazy
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.is_lazy

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential.is_lazy
:parser: rst
```

````

````{py:property} num_configurations
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.num_configurations

````

````{py:property} num_frozen_phonons
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.num_frozen_phonons

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential.num_frozen_phonons
:parser: rst
```

````

````{py:property} repetitions
:canonical: abtem.potentials.charge_density.ChargeDensityPotential.repetitions

```{autodoc2-docstring} abtem.potentials.charge_density.ChargeDensityPotential.repetitions
:parser: rst
```

````

`````

````{py:function} add_point_charges_fourier(...) -> numpy.ndarray
:canonical: abtem.potentials.charge_density.add_point_charges_fourier

```{autodoc2-docstring} abtem.potentials.charge_density.add_point_charges_fourier
:parser: rst
```
````

````{py:function} curl_fourier(...) -> numpy.ndarray
:canonical: abtem.potentials.charge_density.curl_fourier

```{autodoc2-docstring} abtem.potentials.charge_density.curl_fourier
:parser: rst
```
````

````{py:function} integrate_gradient_fourier(...) -> numpy.ndarray
:canonical: abtem.potentials.charge_density.integrate_gradient_fourier

```{autodoc2-docstring} abtem.potentials.charge_density.integrate_gradient_fourier
:parser: rst
```
````
