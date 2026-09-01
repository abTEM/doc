# {py:mod}`abtem.core.energy`

```{py:module} abtem.core.energy
```

```{autodoc2-docstring} abtem.core.energy
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Accelerator <abtem.core.energy.Accelerator>`
  - ```{autodoc2-docstring} abtem.core.energy.Accelerator
    :parser: rst
    :summary:
    ```
* - {py:obj}`HasAcceleratorMixin <abtem.core.energy.HasAcceleratorMixin>`
  - ```{autodoc2-docstring} abtem.core.energy.HasAcceleratorMixin
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`energy2mass <abtem.core.energy.energy2mass>`
  - ```{autodoc2-docstring} abtem.core.energy.energy2mass
    :parser: rst
    :summary:
    ```
* - {py:obj}`energy2sigma <abtem.core.energy.energy2sigma>`
  - ```{autodoc2-docstring} abtem.core.energy.energy2sigma
    :parser: rst
    :summary:
    ```
* - {py:obj}`energy2wavelength <abtem.core.energy.energy2wavelength>`
  - ```{autodoc2-docstring} abtem.core.energy.energy2wavelength
    :parser: rst
    :summary:
    ```
* - {py:obj}`reciprocal_space_sampling_to_angular_sampling <abtem.core.energy.reciprocal_space_sampling_to_angular_sampling>`
  - ```{autodoc2-docstring} abtem.core.energy.reciprocal_space_sampling_to_angular_sampling
    :parser: rst
    :summary:
    ```
* - {py:obj}`relativistic_mass_correction <abtem.core.energy.relativistic_mass_correction>`
  - ```{autodoc2-docstring} abtem.core.energy.relativistic_mass_correction
    :parser: rst
    :summary:
    ```
* - {py:obj}`resolve_energy <abtem.core.energy.resolve_energy>`
  - ```{autodoc2-docstring} abtem.core.energy.resolve_energy
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`T <abtem.core.energy.T>`
  - ```{autodoc2-docstring} abtem.core.energy.T
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} Accelerator(...)
:canonical: abtem.core.energy.Accelerator

Bases: {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.core.energy.Accelerator
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.core.energy.Accelerator.__init__
:parser: rst
```

````{py:method} check_is_defined()
:canonical: abtem.core.energy.Accelerator.check_is_defined

```{autodoc2-docstring} abtem.core.energy.Accelerator.check_is_defined
:parser: rst
```

````

````{py:method} check_match(...)
:canonical: abtem.core.energy.Accelerator.check_match

```{autodoc2-docstring} abtem.core.energy.Accelerator.check_match
:parser: rst
```

````

````{py:property} energy
:canonical: abtem.core.energy.Accelerator.energy
:type: float | None

```{autodoc2-docstring} abtem.core.energy.Accelerator.energy
:parser: rst
```

````

````{py:method} match(...)
:canonical: abtem.core.energy.Accelerator.match

```{autodoc2-docstring} abtem.core.energy.Accelerator.match
:parser: rst
```

````

````{py:property} sigma
:canonical: abtem.core.energy.Accelerator.sigma
:type: float

```{autodoc2-docstring} abtem.core.energy.Accelerator.sigma
:parser: rst
```

````

````{py:property} wavelength
:canonical: abtem.core.energy.Accelerator.wavelength
:type: float

```{autodoc2-docstring} abtem.core.energy.Accelerator.wavelength
:parser: rst
```

````

`````

````{py:exception} EnergyUndefinedError()
:canonical: abtem.core.energy.EnergyUndefinedError

Bases: {py:obj}`Exception`

```{autodoc2-docstring} abtem.core.energy.EnergyUndefinedError
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.core.energy.EnergyUndefinedError.__init__
:parser: rst
```

````

`````{py:class} HasAcceleratorMixin
:canonical: abtem.core.energy.HasAcceleratorMixin

```{autodoc2-docstring} abtem.core.energy.HasAcceleratorMixin
:parser: rst
```

````{py:property} accelerator
:canonical: abtem.core.energy.HasAcceleratorMixin.accelerator
:type: abtem.core.energy.Accelerator

```{autodoc2-docstring} abtem.core.energy.HasAcceleratorMixin.accelerator
:parser: rst
```

````

````{py:property} energy
:canonical: abtem.core.energy.HasAcceleratorMixin.energy
:type: float | None

```{autodoc2-docstring} abtem.core.energy.HasAcceleratorMixin.energy
:parser: rst
```

````

````{py:property} wavelength
:canonical: abtem.core.energy.HasAcceleratorMixin.wavelength
:type: float

```{autodoc2-docstring} abtem.core.energy.HasAcceleratorMixin.wavelength
:parser: rst
```

````

`````

````{py:data} T
:canonical: abtem.core.energy.T
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.core.energy.T
:parser: rst
```

````

````{py:function} energy2mass(...) -> float
:canonical: abtem.core.energy.energy2mass

```{autodoc2-docstring} abtem.core.energy.energy2mass
:parser: rst
```
````

````{py:function} energy2sigma(...) -> float
:canonical: abtem.core.energy.energy2sigma

```{autodoc2-docstring} abtem.core.energy.energy2sigma
:parser: rst
```
````

````{py:function} energy2wavelength(...) -> float
:canonical: abtem.core.energy.energy2wavelength

```{autodoc2-docstring} abtem.core.energy.energy2wavelength
:parser: rst
```
````

````{py:function} reciprocal_space_sampling_to_angular_sampling(...) -> abtem.core.energy.T
:canonical: abtem.core.energy.reciprocal_space_sampling_to_angular_sampling

```{autodoc2-docstring} abtem.core.energy.reciprocal_space_sampling_to_angular_sampling
:parser: rst
```
````

````{py:function} relativistic_mass_correction(...) -> float
:canonical: abtem.core.energy.relativistic_mass_correction

```{autodoc2-docstring} abtem.core.energy.relativistic_mass_correction
:parser: rst
```
````

````{py:function} resolve_energy(...) -> typing.Optional[float]
:canonical: abtem.core.energy.resolve_energy

```{autodoc2-docstring} abtem.core.energy.resolve_energy
:parser: rst
```
````
