# {py:mod}`abtem.parametrizations`

```{py:module} abtem.parametrizations
```

```{autodoc2-docstring} abtem.parametrizations
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

* - {py:obj}`Parametrization <abtem.parametrizations.Parametrization>`
  - ```{autodoc2-docstring} abtem.parametrizations.Parametrization
    :summary:
    ```
* - {py:obj}`KirklandParametrization <abtem.parametrizations.KirklandParametrization>`
  - ```{autodoc2-docstring} abtem.parametrizations.KirklandParametrization
    :summary:
    ```
* - {py:obj}`LobatoParametrization <abtem.parametrizations.LobatoParametrization>`
  - ```{autodoc2-docstring} abtem.parametrizations.LobatoParametrization
    :summary:
    ```
* - {py:obj}`PengParametrization <abtem.parametrizations.PengParametrization>`
  - ```{autodoc2-docstring} abtem.parametrizations.PengParametrization
    :summary:
    ```
* - {py:obj}`EwaldParametrization <abtem.parametrizations.EwaldParametrization>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`validate_sigmas <abtem.parametrizations.validate_sigmas>`
  - ```{autodoc2-docstring} abtem.parametrizations.validate_sigmas
    :summary:
    ```
* - {py:obj}`validate_parametrization <abtem.parametrizations.validate_parametrization>`
  - ```{autodoc2-docstring} abtem.parametrizations.validate_parametrization
    :summary:
    ```
* - {py:obj}`validate_parameters <abtem.parametrizations.validate_parameters>`
  - ```{autodoc2-docstring} abtem.parametrizations.validate_parameters
    :summary:
    ```
````

### API

````{py:function} validate_sigmas(sigmas: float | dict) -> dict
:canonical: abtem.parametrizations.validate_sigmas

```{autodoc2-docstring} abtem.parametrizations.validate_sigmas
```
````

`````{py:class} Parametrization(parameters: dict[str, numpy.ndarray] | str, sigmas: dict[str, float] = None)
:canonical: abtem.parametrizations.Parametrization

Bases: {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.parametrizations.Parametrization
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.parametrizations.Parametrization.__init__
```

````{py:method} to_json(file: str)
:canonical: abtem.parametrizations.Parametrization.to_json

```{autodoc2-docstring} abtem.parametrizations.Parametrization.to_json
```

````

````{py:method} from_json(file: str)
:canonical: abtem.parametrizations.Parametrization.from_json

```{autodoc2-docstring} abtem.parametrizations.Parametrization.from_json
```

````

````{py:property} sigmas
:canonical: abtem.parametrizations.Parametrization.sigmas

```{autodoc2-docstring} abtem.parametrizations.Parametrization.sigmas
```

````

````{py:property} parameters
:canonical: abtem.parametrizations.Parametrization.parameters
:type: dict[str, numpy.ndarray]

```{autodoc2-docstring} abtem.parametrizations.Parametrization.parameters
```

````

````{py:method} scaled_parameters(symbol: str, name: str) -> numpy.ndarray
:canonical: abtem.parametrizations.Parametrization.scaled_parameters
:abstractmethod:

```{autodoc2-docstring} abtem.parametrizations.Parametrization.scaled_parameters
```

````

````{py:method} potential(symbol: str, charge: float = 0.0) -> callable
:canonical: abtem.parametrizations.Parametrization.potential

```{autodoc2-docstring} abtem.parametrizations.Parametrization.potential
```

````

````{py:method} scattering_factor(symbol: str, charge: float = 0.0) -> typing.Callable
:canonical: abtem.parametrizations.Parametrization.scattering_factor

```{autodoc2-docstring} abtem.parametrizations.Parametrization.scattering_factor
```

````

````{py:method} projected_potential(symbol: str, charge: float = 0.0) -> typing.Callable
:canonical: abtem.parametrizations.Parametrization.projected_potential

```{autodoc2-docstring} abtem.parametrizations.Parametrization.projected_potential
```

````

````{py:method} projected_scattering_factor(symbol: str, charge: float = 0.0) -> callable
:canonical: abtem.parametrizations.Parametrization.projected_scattering_factor

```{autodoc2-docstring} abtem.parametrizations.Parametrization.projected_scattering_factor
```

````

````{py:method} charge(symbol: str, charge: float = 0.0) -> callable
:canonical: abtem.parametrizations.Parametrization.charge

```{autodoc2-docstring} abtem.parametrizations.Parametrization.charge
```

````

````{py:method} x_ray_scattering_factor(symbol: str, charge: float = 0.0) -> callable
:canonical: abtem.parametrizations.Parametrization.x_ray_scattering_factor

```{autodoc2-docstring} abtem.parametrizations.Parametrization.x_ray_scattering_factor
```

````

````{py:method} finite_projected_potential(symbol: str, charge: float = 0.0) -> callable
:canonical: abtem.parametrizations.Parametrization.finite_projected_potential

```{autodoc2-docstring} abtem.parametrizations.Parametrization.finite_projected_potential
```

````

````{py:method} finite_projected_scattering_factor(symbol: str, charge: float = 0.0) -> callable
:canonical: abtem.parametrizations.Parametrization.finite_projected_scattering_factor

```{autodoc2-docstring} abtem.parametrizations.Parametrization.finite_projected_scattering_factor
```

````

````{py:method} get_function(name: str, symbol: str, charge: float = 0.0) -> callable
:canonical: abtem.parametrizations.Parametrization.get_function

```{autodoc2-docstring} abtem.parametrizations.Parametrization.get_function
```

````

````{py:method} line_profiles(symbol: str | typing.Sequence[str], cutoff: float, sampling: float = 0.001, name: str = 'potential') -> abtem.measurements.RealSpaceLineProfiles | abtem.measurements.ReciprocalSpaceLineProfiles
:canonical: abtem.parametrizations.Parametrization.line_profiles

```{autodoc2-docstring} abtem.parametrizations.Parametrization.line_profiles
```

````

`````

`````{py:class} KirklandParametrization(parameters: str | dict = 'kirkland.json', sigmas: dict[str, float] = None)
:canonical: abtem.parametrizations.KirklandParametrization

Bases: {py:obj}`abtem.parametrizations.Parametrization`

```{autodoc2-docstring} abtem.parametrizations.KirklandParametrization
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.parametrizations.KirklandParametrization.__init__
```

````{py:method} fit(Z, k, f, guess=None)
:canonical: abtem.parametrizations.KirklandParametrization.fit

```{autodoc2-docstring} abtem.parametrizations.KirklandParametrization.fit
```

````

````{py:method} scaled_parameters(symbol: str, name: str) -> numpy.ndarray
:canonical: abtem.parametrizations.KirklandParametrization.scaled_parameters

````

`````

`````{py:class} LobatoParametrization(parameters: str | dict = 'lobato.json', sigmas: dict[str, float] = None)
:canonical: abtem.parametrizations.LobatoParametrization

Bases: {py:obj}`abtem.parametrizations.Parametrization`

```{autodoc2-docstring} abtem.parametrizations.LobatoParametrization
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.parametrizations.LobatoParametrization.__init__
```

````{py:method} fit(Z, k, f, guess=None)
:canonical: abtem.parametrizations.LobatoParametrization.fit

```{autodoc2-docstring} abtem.parametrizations.LobatoParametrization.fit
```

````

````{py:method} scaled_parameters(symbol: str, name: str) -> numpy.ndarray
:canonical: abtem.parametrizations.LobatoParametrization.scaled_parameters

````

`````

`````{py:class} PengParametrization(parameters: str | dict = 'peng_high.json', sigmas: dict[str, float] = None)
:canonical: abtem.parametrizations.PengParametrization

Bases: {py:obj}`abtem.parametrizations.Parametrization`

```{autodoc2-docstring} abtem.parametrizations.PengParametrization
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.parametrizations.PengParametrization.__init__
```

````{py:method} scaled_parameters(symbol: str, name: str) -> numpy.ndarray
:canonical: abtem.parametrizations.PengParametrization.scaled_parameters

````

`````

`````{py:class} EwaldParametrization(width: float = 1.0)
:canonical: abtem.parametrizations.EwaldParametrization

Bases: {py:obj}`abtem.parametrizations.Parametrization`

````{py:property} width
:canonical: abtem.parametrizations.EwaldParametrization.width

```{autodoc2-docstring} abtem.parametrizations.EwaldParametrization.width
```

````

````{py:method} scaled_parameters(symbol: str, name: str) -> numpy.ndarray
:canonical: abtem.parametrizations.EwaldParametrization.scaled_parameters

````

`````

````{py:function} validate_parametrization(parametrization: str | abtem.parametrizations.Parametrization) -> abtem.parametrizations.Parametrization
:canonical: abtem.parametrizations.validate_parametrization

```{autodoc2-docstring} abtem.parametrizations.validate_parametrization
```
````

````{py:function} validate_parameters(parameters: str | dict) -> dict
:canonical: abtem.parametrizations.validate_parameters

```{autodoc2-docstring} abtem.parametrizations.validate_parameters
```
````
