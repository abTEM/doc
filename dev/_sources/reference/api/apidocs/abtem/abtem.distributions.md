# {py:mod}`abtem.distributions`

```{py:module} abtem.distributions
```

```{autodoc2-docstring} abtem.distributions
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseDistribution <abtem.distributions.BaseDistribution>`
  - ```{autodoc2-docstring} abtem.distributions.BaseDistribution
    :parser: rst
    :summary:
    ```
* - {py:obj}`DistributionFromValues <abtem.distributions.DistributionFromValues>`
  - ```{autodoc2-docstring} abtem.distributions.DistributionFromValues
    :parser: rst
    :summary:
    ```
* - {py:obj}`EnsembleFromDistributions <abtem.distributions.EnsembleFromDistributions>`
  - ```{autodoc2-docstring} abtem.distributions.EnsembleFromDistributions
    :parser: rst
    :summary:
    ```
* - {py:obj}`MultidimensionalDistribution <abtem.distributions.MultidimensionalDistribution>`
  - ```{autodoc2-docstring} abtem.distributions.MultidimensionalDistribution
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`from_values <abtem.distributions.from_values>`
  - ```{autodoc2-docstring} abtem.distributions.from_values
    :parser: rst
    :summary:
    ```
* - {py:obj}`gaussian <abtem.distributions.gaussian>`
  - ```{autodoc2-docstring} abtem.distributions.gaussian
    :parser: rst
    :summary:
    ```
* - {py:obj}`lorentzian <abtem.distributions.lorentzian>`
  - ```{autodoc2-docstring} abtem.distributions.lorentzian
    :parser: rst
    :summary:
    ```
* - {py:obj}`pseudo_voigtian <abtem.distributions.pseudo_voigtian>`
  - ```{autodoc2-docstring} abtem.distributions.pseudo_voigtian
    :parser: rst
    :summary:
    ```
* - {py:obj}`tuple_range_except <abtem.distributions.tuple_range_except>`
  - ```{autodoc2-docstring} abtem.distributions.tuple_range_except
    :parser: rst
    :summary:
    ```
* - {py:obj}`uniform <abtem.distributions.uniform>`
  - ```{autodoc2-docstring} abtem.distributions.uniform
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_distribution <abtem.distributions.validate_distribution>`
  - ```{autodoc2-docstring} abtem.distributions.validate_distribution
    :parser: rst
    :summary:
    ```
* - {py:obj}`voigtian <abtem.distributions.voigtian>`
  - ```{autodoc2-docstring} abtem.distributions.voigtian
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} BaseDistribution
:canonical: abtem.distributions.BaseDistribution

Bases: {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.distributions.BaseDistribution
:parser: rst
```

````{py:property} dimensions
:canonical: abtem.distributions.BaseDistribution.dimensions
:abstractmethod:
:type: int

```{autodoc2-docstring} abtem.distributions.BaseDistribution.dimensions
:parser: rst
```

````

````{py:method} divide(...) -> numpy.ndarray | dask.array.Array
:canonical: abtem.distributions.BaseDistribution.divide
:abstractmethod:

```{autodoc2-docstring} abtem.distributions.BaseDistribution.divide
:parser: rst
```

````

````{py:property} ensemble_mean
:canonical: abtem.distributions.BaseDistribution.ensemble_mean
:abstractmethod:
:type: bool

```{autodoc2-docstring} abtem.distributions.BaseDistribution.ensemble_mean
:parser: rst
```

````

````{py:property} shape
:canonical: abtem.distributions.BaseDistribution.shape
:abstractmethod:
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.distributions.BaseDistribution.shape
:parser: rst
```

````

````{py:property} values
:canonical: abtem.distributions.BaseDistribution.values
:abstractmethod:
:type: numpy.ndarray

```{autodoc2-docstring} abtem.distributions.BaseDistribution.values
:parser: rst
```

````

````{py:property} weights
:canonical: abtem.distributions.BaseDistribution.weights
:abstractmethod:
:type: numpy.ndarray

```{autodoc2-docstring} abtem.distributions.BaseDistribution.weights
:parser: rst
```

````

`````

`````{py:class} DistributionFromValues(...)
:canonical: abtem.distributions.DistributionFromValues

Bases: {py:obj}`abtem.distributions.BaseDistribution`

```{autodoc2-docstring} abtem.distributions.DistributionFromValues
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.distributions.DistributionFromValues.__init__
:parser: rst
```

````{py:method} combine(...) -> abtem.distributions.MultidimensionalDistribution
:canonical: abtem.distributions.DistributionFromValues.combine

```{autodoc2-docstring} abtem.distributions.DistributionFromValues.combine
:parser: rst
```

````

````{py:property} dimensions
:canonical: abtem.distributions.DistributionFromValues.dimensions
:type: int

````

````{py:method} divide(...) -> numpy.ndarray | dask.array.Array
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

`````{py:class} EnsembleFromDistributions(...)
:canonical: abtem.distributions.EnsembleFromDistributions

Bases: {py:obj}`abtem.core.ensemble.Ensemble`, {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.distributions.EnsembleFromDistributions
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.distributions.EnsembleFromDistributions.__init__
:parser: rst
```

````{py:property} ensemble_shape
:canonical: abtem.distributions.EnsembleFromDistributions.ensemble_shape
:type: tuple[int, ...]

````

`````

`````{py:class} MultidimensionalDistribution(...)
:canonical: abtem.distributions.MultidimensionalDistribution

Bases: {py:obj}`abtem.distributions.BaseDistribution`

```{autodoc2-docstring} abtem.distributions.MultidimensionalDistribution
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.distributions.MultidimensionalDistribution.__init__
:parser: rst
```

````{py:property} dimensions
:canonical: abtem.distributions.MultidimensionalDistribution.dimensions
:type: int

````

````{py:property} distributions
:canonical: abtem.distributions.MultidimensionalDistribution.distributions

```{autodoc2-docstring} abtem.distributions.MultidimensionalDistribution.distributions
:parser: rst
```

````

````{py:method} divide(...) -> numpy.ndarray | dask.array.Array
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

````{py:function} from_values(...) -> abtem.distributions.DistributionFromValues
:canonical: abtem.distributions.from_values

```{autodoc2-docstring} abtem.distributions.from_values
:parser: rst
```
````

````{py:function} gaussian(...) -> abtem.distributions.MultidimensionalDistribution
:canonical: abtem.distributions.gaussian

```{autodoc2-docstring} abtem.distributions.gaussian
:parser: rst
```
````

````{py:function} lorentzian(...) -> abtem.distributions.MultidimensionalDistribution
:canonical: abtem.distributions.lorentzian

```{autodoc2-docstring} abtem.distributions.lorentzian
:parser: rst
```
````

````{py:function} pseudo_voigtian(...) -> abtem.distributions.MultidimensionalDistribution
:canonical: abtem.distributions.pseudo_voigtian

```{autodoc2-docstring} abtem.distributions.pseudo_voigtian
:parser: rst
```
````

````{py:function} tuple_range_except(...)
:canonical: abtem.distributions.tuple_range_except

```{autodoc2-docstring} abtem.distributions.tuple_range_except
:parser: rst
```
````

````{py:function} uniform(...) -> abtem.distributions.DistributionFromValues
:canonical: abtem.distributions.uniform

```{autodoc2-docstring} abtem.distributions.uniform
:parser: rst
```
````

````{py:function} validate_distribution(...) -> abtem.distributions.BaseDistribution | float | int
:canonical: abtem.distributions.validate_distribution

```{autodoc2-docstring} abtem.distributions.validate_distribution
:parser: rst
```
````

````{py:function} voigtian(...) -> abtem.distributions.MultidimensionalDistribution
:canonical: abtem.distributions.voigtian

```{autodoc2-docstring} abtem.distributions.voigtian
:parser: rst
```
````
