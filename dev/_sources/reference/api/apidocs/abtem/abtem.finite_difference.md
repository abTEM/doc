# {py:mod}`abtem.finite_difference`

```{py:module} abtem.finite_difference
```

```{autodoc2-docstring} abtem.finite_difference
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LaplaceOperator <abtem.finite_difference.LaplaceOperator>`
  - ```{autodoc2-docstring} abtem.finite_difference.LaplaceOperator
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`conventional_operator <abtem.finite_difference.conventional_operator>`
  - ```{autodoc2-docstring} abtem.finite_difference.conventional_operator
    :parser: rst
    :summary:
    ```
* - {py:obj}`finite_difference_coefficients <abtem.finite_difference.finite_difference_coefficients>`
  - ```{autodoc2-docstring} abtem.finite_difference.finite_difference_coefficients
    :parser: rst
    :summary:
    ```
* - {py:obj}`full_series <abtem.finite_difference.full_series>`
  - ```{autodoc2-docstring} abtem.finite_difference.full_series
    :parser: rst
    :summary:
    ```
* - {py:obj}`multislice_step <abtem.finite_difference.multislice_step>`
  - ```{autodoc2-docstring} abtem.finite_difference.multislice_step
    :parser: rst
    :summary:
    ```
* - {py:obj}`propagator_taylor_series <abtem.finite_difference.propagator_taylor_series>`
  - ```{autodoc2-docstring} abtem.finite_difference.propagator_taylor_series
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`fd_coefficients <abtem.finite_difference.fd_coefficients>`
  - ```{autodoc2-docstring} abtem.finite_difference.fd_coefficients
    :parser: rst
    :summary:
    ```
````

### API

```{py:exception} DivergedError(...)
:canonical: abtem.finite_difference.DivergedError

Bases: {py:obj}`Exception`

```

`````{py:class} LaplaceOperator(...)
:canonical: abtem.finite_difference.LaplaceOperator

```{autodoc2-docstring} abtem.finite_difference.LaplaceOperator
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.finite_difference.LaplaceOperator.__init__
:parser: rst
```

````{py:method} apply(...)
:canonical: abtem.finite_difference.LaplaceOperator.apply

```{autodoc2-docstring} abtem.finite_difference.LaplaceOperator.apply
:parser: rst
```

````

````{py:method} get_stencil(...) -> typing.Callable
:canonical: abtem.finite_difference.LaplaceOperator.get_stencil

```{autodoc2-docstring} abtem.finite_difference.LaplaceOperator.get_stencil
:parser: rst
```

````

`````

```{py:exception} NotConvergedError(...)
:canonical: abtem.finite_difference.NotConvergedError

Bases: {py:obj}`Exception`

```

````{py:function} conventional_operator(...)
:canonical: abtem.finite_difference.conventional_operator

```{autodoc2-docstring} abtem.finite_difference.conventional_operator
:parser: rst
```
````

````{py:data} fd_coefficients
:canonical: abtem.finite_difference.fd_coefficients
:value: >
   None

```{autodoc2-docstring} abtem.finite_difference.fd_coefficients
:parser: rst
```

````

````{py:function} finite_difference_coefficients(...)
:canonical: abtem.finite_difference.finite_difference_coefficients

```{autodoc2-docstring} abtem.finite_difference.finite_difference_coefficients
:parser: rst
```
````

````{py:function} full_series(...)
:canonical: abtem.finite_difference.full_series

```{autodoc2-docstring} abtem.finite_difference.full_series
:parser: rst
```
````

````{py:function} multislice_step(...) -> abtem.waves.Waves | typing.Sequence[abtem.waves.Waves]
:canonical: abtem.finite_difference.multislice_step

```{autodoc2-docstring} abtem.finite_difference.multislice_step
:parser: rst
```
````

````{py:function} propagator_taylor_series(...)
:canonical: abtem.finite_difference.propagator_taylor_series

```{autodoc2-docstring} abtem.finite_difference.propagator_taylor_series
:parser: rst
```
````
