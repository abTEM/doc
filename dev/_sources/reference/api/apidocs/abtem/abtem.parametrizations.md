# {py:mod}`abtem.parametrizations`

```{py:module} abtem.parametrizations
```

```{autodoc2-docstring} abtem.parametrizations
:parser: rst
:allowtitles:
```

## Subpackages

```{toctree}
:titlesonly:
:maxdepth: 3

abtem.parametrizations.functions
```

## Package Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EwaldParametrization <abtem.parametrizations.EwaldParametrization>`
  -
* - {py:obj}`KirklandParametrization <abtem.parametrizations.KirklandParametrization>`
  - ```{autodoc2-docstring} abtem.parametrizations.KirklandParametrization
    :parser: rst
    :summary:
    ```
* - {py:obj}`LobatoParametrization <abtem.parametrizations.LobatoParametrization>`
  - ```{autodoc2-docstring} abtem.parametrizations.LobatoParametrization
    :parser: rst
    :summary:
    ```
* - {py:obj}`Parametrization <abtem.parametrizations.Parametrization>`
  - ```{autodoc2-docstring} abtem.parametrizations.Parametrization
    :parser: rst
    :summary:
    ```
* - {py:obj}`PengParametrization <abtem.parametrizations.PengParametrization>`
  - ```{autodoc2-docstring} abtem.parametrizations.PengParametrization
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`validate_parameters <abtem.parametrizations.validate_parameters>`
  - ```{autodoc2-docstring} abtem.parametrizations.validate_parameters
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_parametrization <abtem.parametrizations.validate_parametrization>`
  - ```{autodoc2-docstring} abtem.parametrizations.validate_parametrization
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_sigmas <abtem.parametrizations.validate_sigmas>`
  - ```{autodoc2-docstring} abtem.parametrizations.validate_sigmas
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} EwaldParametrization(...)
:canonical: abtem.parametrizations.EwaldParametrization

Bases: {py:obj}`abtem.parametrizations.Parametrization`

````{py:method} scaled_parameters(...) -> numpy.ndarray
:canonical: abtem.parametrizations.EwaldParametrization.scaled_parameters

````

````{py:property} width
:canonical: abtem.parametrizations.EwaldParametrization.width

```{autodoc2-docstring} abtem.parametrizations.EwaldParametrization.width
:parser: rst
```

````

`````

`````{py:class} KirklandParametrization(...)
:canonical: abtem.parametrizations.KirklandParametrization

Bases: {py:obj}`abtem.parametrizations.Parametrization`

```{autodoc2-docstring} abtem.parametrizations.KirklandParametrization
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.parametrizations.KirklandParametrization.__init__
:parser: rst
```

````{py:method} fit(...)
:canonical: abtem.parametrizations.KirklandParametrization.fit

```{autodoc2-docstring} abtem.parametrizations.KirklandParametrization.fit
:parser: rst
```

````

````{py:method} scaled_parameters(...) -> numpy.ndarray
:canonical: abtem.parametrizations.KirklandParametrization.scaled_parameters

````

`````

`````{py:class} LobatoParametrization(...)
:canonical: abtem.parametrizations.LobatoParametrization

Bases: {py:obj}`abtem.parametrizations.Parametrization`

```{autodoc2-docstring} abtem.parametrizations.LobatoParametrization
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.parametrizations.LobatoParametrization.__init__
:parser: rst
```

````{py:method} fit(...)
:canonical: abtem.parametrizations.LobatoParametrization.fit

```{autodoc2-docstring} abtem.parametrizations.LobatoParametrization.fit
:parser: rst
```

````

````{py:method} scaled_parameters(...) -> numpy.ndarray
:canonical: abtem.parametrizations.LobatoParametrization.scaled_parameters

````

`````

`````{py:class} Parametrization(...)
:canonical: abtem.parametrizations.Parametrization

Bases: {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.parametrizations.Parametrization
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.parametrizations.Parametrization.__init__
:parser: rst
```

````{py:method} charge(...) -> callable
:canonical: abtem.parametrizations.Parametrization.charge

```{autodoc2-docstring} abtem.parametrizations.Parametrization.charge
:parser: rst
```

````

````{py:method} finite_projected_potential(...) -> callable
:canonical: abtem.parametrizations.Parametrization.finite_projected_potential

```{autodoc2-docstring} abtem.parametrizations.Parametrization.finite_projected_potential
:parser: rst
```

````

````{py:method} finite_projected_scattering_factor(...) -> callable
:canonical: abtem.parametrizations.Parametrization.finite_projected_scattering_factor

```{autodoc2-docstring} abtem.parametrizations.Parametrization.finite_projected_scattering_factor
:parser: rst
```

````

````{py:method} from_json(...)
:canonical: abtem.parametrizations.Parametrization.from_json

```{autodoc2-docstring} abtem.parametrizations.Parametrization.from_json
:parser: rst
```

````

````{py:method} get_function(...) -> callable
:canonical: abtem.parametrizations.Parametrization.get_function

```{autodoc2-docstring} abtem.parametrizations.Parametrization.get_function
:parser: rst
```

````

````{py:method} line_profiles(...) -> abtem.measurements.RealSpaceLineProfiles | abtem.measurements.ReciprocalSpaceLineProfiles
:canonical: abtem.parametrizations.Parametrization.line_profiles

```{autodoc2-docstring} abtem.parametrizations.Parametrization.line_profiles
:parser: rst
```

````

````{py:property} parameters
:canonical: abtem.parametrizations.Parametrization.parameters
:type: dict[str, numpy.ndarray]

```{autodoc2-docstring} abtem.parametrizations.Parametrization.parameters
:parser: rst
```

````

````{py:method} potential(...) -> callable
:canonical: abtem.parametrizations.Parametrization.potential

```{autodoc2-docstring} abtem.parametrizations.Parametrization.potential
:parser: rst
```

````

````{py:method} projected_potential(...) -> typing.Callable
:canonical: abtem.parametrizations.Parametrization.projected_potential

```{autodoc2-docstring} abtem.parametrizations.Parametrization.projected_potential
:parser: rst
```

````

````{py:method} projected_scattering_factor(...) -> callable
:canonical: abtem.parametrizations.Parametrization.projected_scattering_factor

```{autodoc2-docstring} abtem.parametrizations.Parametrization.projected_scattering_factor
:parser: rst
```

````

````{py:method} scaled_parameters(...) -> numpy.ndarray
:canonical: abtem.parametrizations.Parametrization.scaled_parameters
:abstractmethod:

```{autodoc2-docstring} abtem.parametrizations.Parametrization.scaled_parameters
:parser: rst
```

````

````{py:method} scattering_factor(...) -> typing.Callable
:canonical: abtem.parametrizations.Parametrization.scattering_factor

```{autodoc2-docstring} abtem.parametrizations.Parametrization.scattering_factor
:parser: rst
```

````

````{py:property} sigmas
:canonical: abtem.parametrizations.Parametrization.sigmas

```{autodoc2-docstring} abtem.parametrizations.Parametrization.sigmas
:parser: rst
```

````

````{py:method} to_json(...)
:canonical: abtem.parametrizations.Parametrization.to_json

```{autodoc2-docstring} abtem.parametrizations.Parametrization.to_json
:parser: rst
```

````

````{py:method} x_ray_scattering_factor(...) -> callable
:canonical: abtem.parametrizations.Parametrization.x_ray_scattering_factor

```{autodoc2-docstring} abtem.parametrizations.Parametrization.x_ray_scattering_factor
:parser: rst
```

````

`````

`````{py:class} PengParametrization(...)
:canonical: abtem.parametrizations.PengParametrization

Bases: {py:obj}`abtem.parametrizations.Parametrization`

```{autodoc2-docstring} abtem.parametrizations.PengParametrization
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.parametrizations.PengParametrization.__init__
:parser: rst
```

````{py:method} scaled_parameters(...) -> numpy.ndarray
:canonical: abtem.parametrizations.PengParametrization.scaled_parameters

````

`````

````{py:function} validate_parameters(...) -> dict
:canonical: abtem.parametrizations.validate_parameters

```{autodoc2-docstring} abtem.parametrizations.validate_parameters
:parser: rst
```
````

````{py:function} validate_parametrization(...) -> abtem.parametrizations.Parametrization
:canonical: abtem.parametrizations.validate_parametrization

```{autodoc2-docstring} abtem.parametrizations.validate_parametrization
:parser: rst
```
````

````{py:function} validate_sigmas(...) -> dict
:canonical: abtem.parametrizations.validate_sigmas

```{autodoc2-docstring} abtem.parametrizations.validate_sigmas
:parser: rst
```
````
