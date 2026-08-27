# {py:mod}`abtem.distributions`

```{py:module} abtem.distributions
```

```{autodoc2-docstring} abtem.distributions
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseDistribution <abtem.distributions.BaseDistribution>`
  - ```{autodoc2-docstring} abtem.distributions.BaseDistribution
    :summary:
    ```
* - {py:obj}`DistributionFromValues <abtem.distributions.DistributionFromValues>`
  - ```{autodoc2-docstring} abtem.distributions.DistributionFromValues
    :summary:
    ```
* - {py:obj}`EnsembleFromDistributions <abtem.distributions.EnsembleFromDistributions>`
  - ```{autodoc2-docstring} abtem.distributions.EnsembleFromDistributions
    :summary:
    ```
* - {py:obj}`MultidimensionalDistribution <abtem.distributions.MultidimensionalDistribution>`
  - ```{autodoc2-docstring} abtem.distributions.MultidimensionalDistribution
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`from_values <abtem.distributions.from_values>`
  - ```{autodoc2-docstring} abtem.distributions.from_values
    :summary:
    ```
* - {py:obj}`gaussian <abtem.distributions.gaussian>`
  - ```{autodoc2-docstring} abtem.distributions.gaussian
    :summary:
    ```
* - {py:obj}`tuple_range_except <abtem.distributions.tuple_range_except>`
  - ```{autodoc2-docstring} abtem.distributions.tuple_range_except
    :summary:
    ```
* - {py:obj}`uniform <abtem.distributions.uniform>`
  - ```{autodoc2-docstring} abtem.distributions.uniform
    :summary:
    ```
* - {py:obj}`validate_distribution <abtem.distributions.validate_distribution>`
  - ```{autodoc2-docstring} abtem.distributions.validate_distribution
    :summary:
    ```
````

### API

`````{py:class} BaseDistribution
:canonical: abtem.distributions.BaseDistribution

Bases: {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.distributions.BaseDistribution
```

````{py:property} dimensions
:canonical: abtem.distributions.BaseDistribution.dimensions
:abstractmethod:
:type: int

```{autodoc2-docstring} abtem.distributions.BaseDistribution.dimensions
```

````

````{py:method} divide(chunks: int | tuple[int, ...] = 1, lazy: bool = True) -> numpy.ndarray | dask.array.Array
:canonical: abtem.distributions.BaseDistribution.divide
:abstractmethod:

```{autodoc2-docstring} abtem.distributions.BaseDistribution.divide
```

````

````{py:property} ensemble_mean
:canonical: abtem.distributions.BaseDistribution.ensemble_mean
:abstractmethod:
:type: bool

```{autodoc2-docstring} abtem.distributions.BaseDistribution.ensemble_mean
```

````

````{py:property} shape
:canonical: abtem.distributions.BaseDistribution.shape
:abstractmethod:
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.distributions.BaseDistribution.shape
```

````

````{py:property} values
:canonical: abtem.distributions.BaseDistribution.values
:abstractmethod:
:type: numpy.ndarray

```{autodoc2-docstring} abtem.distributions.BaseDistribution.values
```

````

````{py:property} weights
:canonical: abtem.distributions.BaseDistribution.weights
:abstractmethod:
:type: numpy.ndarray

```{autodoc2-docstring} abtem.distributions.BaseDistribution.weights
```

````

`````

`````{py:class} DistributionFromValues(values: numpy.ndarray, weights: numpy.ndarray | None = None, ensemble_mean: bool = False)
:canonical: abtem.distributions.DistributionFromValues

Bases: {py:obj}`abtem.distributions.BaseDistribution`

```{autodoc2-docstring} abtem.distributions.DistributionFromValues
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.distributions.DistributionFromValues.__init__
```

````{py:method} combine(other: abtem.distributions.DistributionFromValues) -> abtem.distributions.MultidimensionalDistribution
:canonical: abtem.distributions.DistributionFromValues.combine

```{autodoc2-docstring} abtem.distributions.DistributionFromValues.combine
```

````

````{py:property} dimensions
:canonical: abtem.distributions.DistributionFromValues.dimensions
:type: int

````

````{py:method} divide(chunks: int | tuple[int, ...] = 1, lazy: bool = True) -> numpy.ndarray | dask.array.Array
:canonical: abtem.distributions.DistributionFromValues.divide

````

````{py:property} ensemble_mean
:canonical: abtem.distributions.DistributionFromValues.ensemble_mean
:type: bool

````

````{py:property} shape
:canonical: abtem.distributions.DistributionFromValues.shape
:type: tuple[int]

````

````{py:property} values
:canonical: abtem.distributions.DistributionFromValues.values
:type: numpy.ndarray

````

````{py:property} weights
:canonical: abtem.distributions.DistributionFromValues.weights
:type: numpy.ndarray

````

`````

`````{py:class} EnsembleFromDistributions(distributions: tuple[str, ...] = (), **kwargs)
:canonical: abtem.distributions.EnsembleFromDistributions

Bases: {py:obj}`abtem.core.ensemble.Ensemble`, {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.distributions.EnsembleFromDistributions
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.distributions.EnsembleFromDistributions.__init__
```

````{py:property} ensemble_shape
:canonical: abtem.distributions.EnsembleFromDistributions.ensemble_shape
:type: tuple[int, ...]

````

`````

`````{py:class} MultidimensionalDistribution(distributions: typing.Sequence[abtem.distributions.BaseDistribution])
:canonical: abtem.distributions.MultidimensionalDistribution

Bases: {py:obj}`abtem.distributions.BaseDistribution`

```{autodoc2-docstring} abtem.distributions.MultidimensionalDistribution
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.distributions.MultidimensionalDistribution.__init__
```

````{py:property} dimensions
:canonical: abtem.distributions.MultidimensionalDistribution.dimensions
:type: int

````

````{py:property} distributions
:canonical: abtem.distributions.MultidimensionalDistribution.distributions

```{autodoc2-docstring} abtem.distributions.MultidimensionalDistribution.distributions
```

````

````{py:method} divide(chunks: int | tuple[int, ...] = 1, lazy: bool = True) -> numpy.ndarray | dask.array.Array
:canonical: abtem.distributions.MultidimensionalDistribution.divide

````

````{py:property} ensemble_mean
:canonical: abtem.distributions.MultidimensionalDistribution.ensemble_mean
:type: bool

````

````{py:property} shape
:canonical: abtem.distributions.MultidimensionalDistribution.shape
:type: tuple[int, ...]

````

````{py:property} values
:canonical: abtem.distributions.MultidimensionalDistribution.values
:type: numpy.ndarray

````

````{py:property} weights
:canonical: abtem.distributions.MultidimensionalDistribution.weights
:type: numpy.ndarray

````

`````

````{py:function} from_values(values: typing.Sequence[typing.SupportsFloat] | numpy.ndarray, weights: numpy.ndarray | None = None, ensemble_mean: bool = False) -> abtem.distributions.DistributionFromValues
:canonical: abtem.distributions.from_values

```{autodoc2-docstring} abtem.distributions.from_values
```
````

````{py:function} gaussian(standard_deviation: float | tuple[float, ...], num_samples: int | tuple[int, ...], dimension: int = 1, center: float | tuple[float, ...] = 0.0, ensemble_mean: bool | tuple[bool, ...] = True, sampling_limit: float | tuple[float, ...] = 3.0, normalize: str = 'intensity') -> abtem.distributions.MultidimensionalDistribution
:canonical: abtem.distributions.gaussian

```{autodoc2-docstring} abtem.distributions.gaussian
```
````

````{py:function} tuple_range_except(n, i)
:canonical: abtem.distributions.tuple_range_except

```{autodoc2-docstring} abtem.distributions.tuple_range_except
```
````

````{py:function} uniform(low: float, high: float, num_samples: int, endpoint: bool = True, ensemble_mean: bool = False) -> abtem.distributions.DistributionFromValues
:canonical: abtem.distributions.uniform

```{autodoc2-docstring} abtem.distributions.uniform
```
````

````{py:function} validate_distribution(distribution: abtem.distributions.BaseDistribution | tuple | list | numpy.ndarray | typing.SupportsFloat) -> abtem.distributions.BaseDistribution | float | int
:canonical: abtem.distributions.validate_distribution

```{autodoc2-docstring} abtem.distributions.validate_distribution
```
````
