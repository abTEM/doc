# {py:mod}`abtem.core.energy`

```{py:module} abtem.core.energy
```

```{autodoc2-docstring} abtem.core.energy
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Accelerator <abtem.core.energy.Accelerator>`
  - ```{autodoc2-docstring} abtem.core.energy.Accelerator
    :summary:
    ```
* - {py:obj}`HasAcceleratorMixin <abtem.core.energy.HasAcceleratorMixin>`
  - ```{autodoc2-docstring} abtem.core.energy.HasAcceleratorMixin
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`energy2mass <abtem.core.energy.energy2mass>`
  - ```{autodoc2-docstring} abtem.core.energy.energy2mass
    :summary:
    ```
* - {py:obj}`energy2sigma <abtem.core.energy.energy2sigma>`
  - ```{autodoc2-docstring} abtem.core.energy.energy2sigma
    :summary:
    ```
* - {py:obj}`energy2wavelength <abtem.core.energy.energy2wavelength>`
  - ```{autodoc2-docstring} abtem.core.energy.energy2wavelength
    :summary:
    ```
* - {py:obj}`reciprocal_space_sampling_to_angular_sampling <abtem.core.energy.reciprocal_space_sampling_to_angular_sampling>`
  - ```{autodoc2-docstring} abtem.core.energy.reciprocal_space_sampling_to_angular_sampling
    :summary:
    ```
* - {py:obj}`relativistic_mass_correction <abtem.core.energy.relativistic_mass_correction>`
  - ```{autodoc2-docstring} abtem.core.energy.relativistic_mass_correction
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`T <abtem.core.energy.T>`
  - ```{autodoc2-docstring} abtem.core.energy.T
    :summary:
    ```
````

### API

`````{py:class} Accelerator(energy: typing.Optional[float] = None, lock_energy: bool = False)
:canonical: abtem.core.energy.Accelerator

Bases: {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.core.energy.Accelerator
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.core.energy.Accelerator.__init__
```

````{py:method} check_is_defined()
:canonical: abtem.core.energy.Accelerator.check_is_defined

```{autodoc2-docstring} abtem.core.energy.Accelerator.check_is_defined
```

````

````{py:method} check_match(other: abtem.core.energy.Accelerator | abtem.core.energy.HasAcceleratorMixin)
:canonical: abtem.core.energy.Accelerator.check_match

```{autodoc2-docstring} abtem.core.energy.Accelerator.check_match
```

````

````{py:property} energy
:canonical: abtem.core.energy.Accelerator.energy
:type: float | None

```{autodoc2-docstring} abtem.core.energy.Accelerator.energy
```

````

````{py:method} match(other: abtem.core.energy.Accelerator | abtem.core.energy.HasAcceleratorMixin, check_match: bool = False)
:canonical: abtem.core.energy.Accelerator.match

```{autodoc2-docstring} abtem.core.energy.Accelerator.match
```

````

````{py:property} sigma
:canonical: abtem.core.energy.Accelerator.sigma
:type: float

```{autodoc2-docstring} abtem.core.energy.Accelerator.sigma
```

````

````{py:property} wavelength
:canonical: abtem.core.energy.Accelerator.wavelength
:type: float

```{autodoc2-docstring} abtem.core.energy.Accelerator.wavelength
```

````

`````

````{py:exception} EnergyUndefinedError()
:canonical: abtem.core.energy.EnergyUndefinedError

Bases: {py:obj}`Exception`

```{autodoc2-docstring} abtem.core.energy.EnergyUndefinedError
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.core.energy.EnergyUndefinedError.__init__
```

````

`````{py:class} HasAcceleratorMixin
:canonical: abtem.core.energy.HasAcceleratorMixin

```{autodoc2-docstring} abtem.core.energy.HasAcceleratorMixin
```

````{py:property} accelerator
:canonical: abtem.core.energy.HasAcceleratorMixin.accelerator
:type: abtem.core.energy.Accelerator

```{autodoc2-docstring} abtem.core.energy.HasAcceleratorMixin.accelerator
```

````

````{py:property} energy
:canonical: abtem.core.energy.HasAcceleratorMixin.energy
:type: float | None

```{autodoc2-docstring} abtem.core.energy.HasAcceleratorMixin.energy
```

````

````{py:property} wavelength
:canonical: abtem.core.energy.HasAcceleratorMixin.wavelength
:type: float

```{autodoc2-docstring} abtem.core.energy.HasAcceleratorMixin.wavelength
```

````

`````

````{py:data} T
:canonical: abtem.core.energy.T
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.core.energy.T
```

````

````{py:function} energy2mass(energy: float) -> float
:canonical: abtem.core.energy.energy2mass

```{autodoc2-docstring} abtem.core.energy.energy2mass
```
````

````{py:function} energy2sigma(energy: float) -> float
:canonical: abtem.core.energy.energy2sigma

```{autodoc2-docstring} abtem.core.energy.energy2sigma
```
````

````{py:function} energy2wavelength(energy: float) -> float
:canonical: abtem.core.energy.energy2wavelength

```{autodoc2-docstring} abtem.core.energy.energy2wavelength
```
````

````{py:function} reciprocal_space_sampling_to_angular_sampling(reciprocal_space_sampling: abtem.core.energy.T, energy: float) -> abtem.core.energy.T
:canonical: abtem.core.energy.reciprocal_space_sampling_to_angular_sampling

```{autodoc2-docstring} abtem.core.energy.reciprocal_space_sampling_to_angular_sampling
```
````

````{py:function} relativistic_mass_correction(energy: float) -> float
:canonical: abtem.core.energy.relativistic_mass_correction

```{autodoc2-docstring} abtem.core.energy.relativistic_mass_correction
```
````
