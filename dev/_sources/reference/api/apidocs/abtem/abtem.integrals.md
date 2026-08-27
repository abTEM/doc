# {py:mod}`abtem.integrals`

```{py:module} abtem.integrals
```

```{autodoc2-docstring} abtem.integrals
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FieldIntegrator <abtem.integrals.FieldIntegrator>`
  - ```{autodoc2-docstring} abtem.integrals.FieldIntegrator
    :summary:
    ```
* - {py:obj}`GaussianProjectionIntegrals <abtem.integrals.GaussianProjectionIntegrals>`
  - ```{autodoc2-docstring} abtem.integrals.GaussianProjectionIntegrals
    :summary:
    ```
* - {py:obj}`ProjectionIntegralTable <abtem.integrals.ProjectionIntegralTable>`
  - ```{autodoc2-docstring} abtem.integrals.ProjectionIntegralTable
    :summary:
    ```
* - {py:obj}`QuadratureProjectionIntegrals <abtem.integrals.QuadratureProjectionIntegrals>`
  - ```{autodoc2-docstring} abtem.integrals.QuadratureProjectionIntegrals
    :summary:
    ```
* - {py:obj}`ScatteringFactorProjectionIntegrals <abtem.integrals.ScatteringFactorProjectionIntegrals>`
  - ```{autodoc2-docstring} abtem.integrals.ScatteringFactorProjectionIntegrals
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`correction_projected_scattering_factors <abtem.integrals.correction_projected_scattering_factors>`
  - ```{autodoc2-docstring} abtem.integrals.correction_projected_scattering_factors
    :summary:
    ```
* - {py:obj}`cutoff_taper <abtem.integrals.cutoff_taper>`
  - ```{autodoc2-docstring} abtem.integrals.cutoff_taper
    :summary:
    ```
* - {py:obj}`gaussian_projected_scattering_factors <abtem.integrals.gaussian_projected_scattering_factors>`
  - ```{autodoc2-docstring} abtem.integrals.gaussian_projected_scattering_factors
    :summary:
    ```
* - {py:obj}`gaussian_projection_weights <abtem.integrals.gaussian_projection_weights>`
  - ```{autodoc2-docstring} abtem.integrals.gaussian_projection_weights
    :summary:
    ```
* - {py:obj}`interpolate_radial_functions <abtem.integrals.interpolate_radial_functions>`
  - ```{autodoc2-docstring} abtem.integrals.interpolate_radial_functions
    :summary:
    ```
* - {py:obj}`optimize_cutoff <abtem.integrals.optimize_cutoff>`
  - ```{autodoc2-docstring} abtem.integrals.optimize_cutoff
    :summary:
    ```
* - {py:obj}`sinc <abtem.integrals.sinc>`
  - ```{autodoc2-docstring} abtem.integrals.sinc
    :summary:
    ```
* - {py:obj}`superpose_deltas <abtem.integrals.superpose_deltas>`
  - ```{autodoc2-docstring} abtem.integrals.superpose_deltas
    :summary:
    ```
````

### API

`````{py:class} FieldIntegrator(periodic: bool, finite: bool, retain_data: bool = False)
:canonical: abtem.integrals.FieldIntegrator

Bases: {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.integrals.FieldIntegrator
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.integrals.FieldIntegrator.__init__
```

````{py:method} cutoff(symbol: str) -> float
:canonical: abtem.integrals.FieldIntegrator.cutoff
:abstractmethod:

```{autodoc2-docstring} abtem.integrals.FieldIntegrator.cutoff
```

````

````{py:property} finite
:canonical: abtem.integrals.FieldIntegrator.finite
:type: bool

```{autodoc2-docstring} abtem.integrals.FieldIntegrator.finite
```

````

````{py:method} integrate_on_grid(positions: numpy.ndarray, a: numpy.ndarray, b: numpy.ndarray, gpts: tuple[int, int], sampling: tuple[float, float], device: str = 'cpu') -> numpy.ndarray
:canonical: abtem.integrals.FieldIntegrator.integrate_on_grid
:abstractmethod:

```{autodoc2-docstring} abtem.integrals.FieldIntegrator.integrate_on_grid
```

````

````{py:property} periodic
:canonical: abtem.integrals.FieldIntegrator.periodic
:type: bool

```{autodoc2-docstring} abtem.integrals.FieldIntegrator.periodic
```

````

`````

`````{py:class} GaussianProjectionIntegrals(parametrization: str | abtem.parametrizations.Parametrization = 'lobato', gaussian_parametrization: str | abtem.parametrizations.Parametrization = 'peng', cutoff_tolerance: float = 0.001)
:canonical: abtem.integrals.GaussianProjectionIntegrals

Bases: {py:obj}`abtem.integrals.FieldIntegrator`

```{autodoc2-docstring} abtem.integrals.GaussianProjectionIntegrals
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.integrals.GaussianProjectionIntegrals.__init__
```

````{py:property} correction_parametrization
:canonical: abtem.integrals.GaussianProjectionIntegrals.correction_parametrization

```{autodoc2-docstring} abtem.integrals.GaussianProjectionIntegrals.correction_parametrization
```

````

````{py:method} cutoff(symbol: str) -> float
:canonical: abtem.integrals.GaussianProjectionIntegrals.cutoff

````

````{py:property} cutoff_tolerance
:canonical: abtem.integrals.GaussianProjectionIntegrals.cutoff_tolerance

```{autodoc2-docstring} abtem.integrals.GaussianProjectionIntegrals.cutoff_tolerance
```

````

````{py:property} gaussian_parametrization
:canonical: abtem.integrals.GaussianProjectionIntegrals.gaussian_parametrization

```{autodoc2-docstring} abtem.integrals.GaussianProjectionIntegrals.gaussian_parametrization
```

````

````{py:method} get_corrections(symbol, gpts, sampling)
:canonical: abtem.integrals.GaussianProjectionIntegrals.get_corrections

```{autodoc2-docstring} abtem.integrals.GaussianProjectionIntegrals.get_corrections
```

````

````{py:method} get_gaussians(symbol, gpts, sampling)
:canonical: abtem.integrals.GaussianProjectionIntegrals.get_gaussians

```{autodoc2-docstring} abtem.integrals.GaussianProjectionIntegrals.get_gaussians
```

````

````{py:method} integrate_on_grid(atoms: ase.Atoms, a: numpy.ndarray, b: numpy.ndarray, gpts: tuple[int, int], sampling: tuple[float, float], device: str = 'cpu', fourier_space: bool = False) -> numpy.ndarray
:canonical: abtem.integrals.GaussianProjectionIntegrals.integrate_on_grid

````

`````

`````{py:class} ProjectionIntegralTable(radial_gpts: numpy.ndarray, limits: numpy.ndarray, values: numpy.ndarray)
:canonical: abtem.integrals.ProjectionIntegralTable

```{autodoc2-docstring} abtem.integrals.ProjectionIntegralTable
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.integrals.ProjectionIntegralTable.__init__
```

````{py:method} integrate(a: float | numpy.ndarray, b: float | numpy.ndarray) -> numpy.ndarray
:canonical: abtem.integrals.ProjectionIntegralTable.integrate

```{autodoc2-docstring} abtem.integrals.ProjectionIntegralTable.integrate
```

````

````{py:property} limits
:canonical: abtem.integrals.ProjectionIntegralTable.limits
:type: numpy.ndarray

```{autodoc2-docstring} abtem.integrals.ProjectionIntegralTable.limits
```

````

````{py:property} radial_gpts
:canonical: abtem.integrals.ProjectionIntegralTable.radial_gpts
:type: numpy.ndarray

```{autodoc2-docstring} abtem.integrals.ProjectionIntegralTable.radial_gpts
```

````

````{py:property} values
:canonical: abtem.integrals.ProjectionIntegralTable.values
:type: numpy.ndarray

```{autodoc2-docstring} abtem.integrals.ProjectionIntegralTable.values
```

````

`````

`````{py:class} QuadratureProjectionIntegrals(parametrization: str | abtem.parametrizations.Parametrization = 'lobato', cutoff_tolerance: float = 0.0001, inner_cutoff_factor: float = 2.0, taper: float = 0.85, integration_step: float = 0.02, quad_order: int = 8)
:canonical: abtem.integrals.QuadratureProjectionIntegrals

Bases: {py:obj}`abtem.integrals.FieldIntegrator`

```{autodoc2-docstring} abtem.integrals.QuadratureProjectionIntegrals
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.integrals.QuadratureProjectionIntegrals.__init__
```

````{py:method} cutoff(symbol: str) -> float
:canonical: abtem.integrals.QuadratureProjectionIntegrals.cutoff

````

````{py:property} cutoff_tolerance
:canonical: abtem.integrals.QuadratureProjectionIntegrals.cutoff_tolerance
:type: float

```{autodoc2-docstring} abtem.integrals.QuadratureProjectionIntegrals.cutoff_tolerance
```

````

````{py:method} get_integral_table(symbol, sampling)
:canonical: abtem.integrals.QuadratureProjectionIntegrals.get_integral_table

```{autodoc2-docstring} abtem.integrals.QuadratureProjectionIntegrals.get_integral_table
```

````

````{py:method} integrate_on_grid(atoms: ase.Atoms, a: float, b: float, gpts: tuple[int, int], sampling: tuple[float, float], device: str = 'cpu') -> numpy.ndarray
:canonical: abtem.integrals.QuadratureProjectionIntegrals.integrate_on_grid

````

````{py:property} integration_step
:canonical: abtem.integrals.QuadratureProjectionIntegrals.integration_step
:type: float

```{autodoc2-docstring} abtem.integrals.QuadratureProjectionIntegrals.integration_step
```

````

````{py:property} parametrization
:canonical: abtem.integrals.QuadratureProjectionIntegrals.parametrization

```{autodoc2-docstring} abtem.integrals.QuadratureProjectionIntegrals.parametrization
```

````

````{py:property} quad_order
:canonical: abtem.integrals.QuadratureProjectionIntegrals.quad_order

```{autodoc2-docstring} abtem.integrals.QuadratureProjectionIntegrals.quad_order
```

````

````{py:property} tables
:canonical: abtem.integrals.QuadratureProjectionIntegrals.tables

```{autodoc2-docstring} abtem.integrals.QuadratureProjectionIntegrals.tables
```

````

`````

`````{py:class} ScatteringFactorProjectionIntegrals(parametrization: str | abtem.parametrizations.Parametrization = 'lobato')
:canonical: abtem.integrals.ScatteringFactorProjectionIntegrals

Bases: {py:obj}`abtem.integrals.FieldIntegrator`

```{autodoc2-docstring} abtem.integrals.ScatteringFactorProjectionIntegrals
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.integrals.ScatteringFactorProjectionIntegrals.__init__
```

````{py:method} cutoff(symbol: str) -> float
:canonical: abtem.integrals.ScatteringFactorProjectionIntegrals.cutoff

````

````{py:method} get_scattering_factor(symbol, gpts, sampling, device)
:canonical: abtem.integrals.ScatteringFactorProjectionIntegrals.get_scattering_factor

```{autodoc2-docstring} abtem.integrals.ScatteringFactorProjectionIntegrals.get_scattering_factor
```

````

````{py:method} integrate_on_grid(atoms: ase.Atoms, a: numpy.ndarray, b: numpy.ndarray, gpts: tuple[int, int], sampling: tuple[float, float], device: str = 'cpu')
:canonical: abtem.integrals.ScatteringFactorProjectionIntegrals.integrate_on_grid

````

````{py:property} parametrization
:canonical: abtem.integrals.ScatteringFactorProjectionIntegrals.parametrization
:type: abtem.parametrizations.Parametrization

```{autodoc2-docstring} abtem.integrals.ScatteringFactorProjectionIntegrals.parametrization
```

````

````{py:property} scattering_factors
:canonical: abtem.integrals.ScatteringFactorProjectionIntegrals.scattering_factors
:type: dict[str, numpy.ndarray]

```{autodoc2-docstring} abtem.integrals.ScatteringFactorProjectionIntegrals.scattering_factors
```

````

`````

````{py:function} correction_projected_scattering_factors(symbol, gpts, sampling, short_range='lobato', long_range='peng')
:canonical: abtem.integrals.correction_projected_scattering_factors

```{autodoc2-docstring} abtem.integrals.correction_projected_scattering_factors
```
````

````{py:function} cutoff_taper(radial_gpts, cutoff, taper)
:canonical: abtem.integrals.cutoff_taper

```{autodoc2-docstring} abtem.integrals.cutoff_taper
```
````

````{py:function} gaussian_projected_scattering_factors(symbol, gpts, sampling, parametrization='peng')
:canonical: abtem.integrals.gaussian_projected_scattering_factors

```{autodoc2-docstring} abtem.integrals.gaussian_projected_scattering_factors
```
````

````{py:function} gaussian_projection_weights(symbol, a, b, parametrization='peng')
:canonical: abtem.integrals.gaussian_projection_weights

```{autodoc2-docstring} abtem.integrals.gaussian_projection_weights
```
````

````{py:function} interpolate_radial_functions(array: numpy.ndarray, positions: numpy.ndarray, disk_indices: numpy.ndarray, disk_counts: numpy.ndarray, sampling: tuple[float, float], radial_gpts: numpy.ndarray, radial_functions: numpy.ndarray, radial_derivative: numpy.ndarray)
:canonical: abtem.integrals.interpolate_radial_functions

```{autodoc2-docstring} abtem.integrals.interpolate_radial_functions
```
````

````{py:function} optimize_cutoff(func: typing.Callable, tolerance: float, a: float, b: float) -> float
:canonical: abtem.integrals.optimize_cutoff

```{autodoc2-docstring} abtem.integrals.optimize_cutoff
```
````

````{py:function} sinc(gpts: tuple[int, int], sampling: tuple[float, float], device: str = 'cpu') -> numpy.ndarray
:canonical: abtem.integrals.sinc

```{autodoc2-docstring} abtem.integrals.sinc
```
````

````{py:function} superpose_deltas(positions: numpy.ndarray, array: numpy.ndarray, weights: typing.Optional[numpy.ndarray] = None, round_positions: bool = False) -> numpy.ndarray
:canonical: abtem.integrals.superpose_deltas

```{autodoc2-docstring} abtem.integrals.superpose_deltas
```
````
