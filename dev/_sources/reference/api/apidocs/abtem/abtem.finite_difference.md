# {py:mod}`abtem.finite_difference`

```{py:module} abtem.finite_difference
```

```{autodoc2-docstring} abtem.finite_difference
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LaplaceOperator <abtem.finite_difference.LaplaceOperator>`
  - ```{autodoc2-docstring} abtem.finite_difference.LaplaceOperator
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`finite_difference_coefficients <abtem.finite_difference.finite_difference_coefficients>`
  - ```{autodoc2-docstring} abtem.finite_difference.finite_difference_coefficients
    :summary:
    ```
* - {py:obj}`conventional_operator <abtem.finite_difference.conventional_operator>`
  - ```{autodoc2-docstring} abtem.finite_difference.conventional_operator
    :summary:
    ```
* - {py:obj}`propagator_taylor_series <abtem.finite_difference.propagator_taylor_series>`
  - ```{autodoc2-docstring} abtem.finite_difference.propagator_taylor_series
    :summary:
    ```
* - {py:obj}`full_series <abtem.finite_difference.full_series>`
  - ```{autodoc2-docstring} abtem.finite_difference.full_series
    :summary:
    ```
* - {py:obj}`multislice_step <abtem.finite_difference.multislice_step>`
  - ```{autodoc2-docstring} abtem.finite_difference.multislice_step
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`fd_coefficients <abtem.finite_difference.fd_coefficients>`
  - ```{autodoc2-docstring} abtem.finite_difference.fd_coefficients
    :summary:
    ```
````

### API

````{py:data} fd_coefficients
:canonical: abtem.finite_difference.fd_coefficients
:value: >
   None

```{autodoc2-docstring} abtem.finite_difference.fd_coefficients
```

````

````{py:function} finite_difference_coefficients(derivative: int, accuracy: int = 2)
:canonical: abtem.finite_difference.finite_difference_coefficients

```{autodoc2-docstring} abtem.finite_difference.finite_difference_coefficients
```
````

`````{py:class} LaplaceOperator(accuracy)
:canonical: abtem.finite_difference.LaplaceOperator

```{autodoc2-docstring} abtem.finite_difference.LaplaceOperator
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.finite_difference.LaplaceOperator.__init__
```

````{py:method} get_stencil(waves: abtem.waves.Waves, device: str = 'cpu') -> typing.Callable
:canonical: abtem.finite_difference.LaplaceOperator.get_stencil

```{autodoc2-docstring} abtem.finite_difference.LaplaceOperator.get_stencil
```

````

````{py:method} apply(waves)
:canonical: abtem.finite_difference.LaplaceOperator.apply

```{autodoc2-docstring} abtem.finite_difference.LaplaceOperator.apply
```

````

`````

```{py:exception} DivergedError(message='the multislice exponential series diverged')
:canonical: abtem.finite_difference.DivergedError

Bases: {py:obj}`Exception`

```

```{py:exception} NotConvergedError(message='the series did not converge')
:canonical: abtem.finite_difference.NotConvergedError

Bases: {py:obj}`Exception`

```

````{py:function} conventional_operator(waves: numpy.ndarray | dask.array.core.Array, laplace: typing.Callable, transmission_function: numpy.ndarray, wavelength: float)
:canonical: abtem.finite_difference.conventional_operator

```{autodoc2-docstring} abtem.finite_difference.conventional_operator
```
````

````{py:function} propagator_taylor_series(waves: numpy.ndarray | dask.array.core.Array, order: int, laplace: typing.Callable, transmission_function: numpy.ndarray, wavelength: float, thickness: float)
:canonical: abtem.finite_difference.propagator_taylor_series

```{autodoc2-docstring} abtem.finite_difference.propagator_taylor_series
```
````

````{py:function} full_series(waves: numpy.ndarray | dask.array.core.Array, laplace: typing.Callable, transmission_function: numpy.ndarray, order: int, wavelength: float, thickness: float, override_prefactor: list[float] = [])
:canonical: abtem.finite_difference.full_series

```{autodoc2-docstring} abtem.finite_difference.full_series
```
````

````{py:function} multislice_step(waves: abtem.waves.Waves, potential_slice: abtem.potentials.iam.PotentialArray, next_slice: abtem.potentials.iam.PotentialArray | None, laplace: abtem.finite_difference.LaplaceOperator, tolerance: float = 1e-16, max_terms: int = 300, order: int = 1, fully_corrected: bool = False) -> abtem.waves.Waves | typing.Sequence[abtem.waves.Waves]
:canonical: abtem.finite_difference.multislice_step

```{autodoc2-docstring} abtem.finite_difference.multislice_step
```
````
