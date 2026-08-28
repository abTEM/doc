# {py:mod}`abtem.core.ensemble`

```{py:module} abtem.core.ensemble
```

```{autodoc2-docstring} abtem.core.ensemble
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EmptyEnsemble <abtem.core.ensemble.EmptyEnsemble>`
  - ```{autodoc2-docstring} abtem.core.ensemble.EmptyEnsemble
    :parser: rst
    :summary:
    ```
* - {py:obj}`Ensemble <abtem.core.ensemble.Ensemble>`
  - ```{autodoc2-docstring} abtem.core.ensemble.Ensemble
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`concatenate_array_blocks <abtem.core.ensemble.concatenate_array_blocks>`
  - ```{autodoc2-docstring} abtem.core.ensemble.concatenate_array_blocks
    :parser: rst
    :summary:
    ```
* - {py:obj}`unpack_blockwise_args <abtem.core.ensemble.unpack_blockwise_args>`
  - ```{autodoc2-docstring} abtem.core.ensemble.unpack_blockwise_args
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} EmptyEnsemble
:canonical: abtem.core.ensemble.EmptyEnsemble

Bases: {py:obj}`abtem.core.ensemble.Ensemble`

```{autodoc2-docstring} abtem.core.ensemble.EmptyEnsemble
:parser: rst
```

````{py:property} ensemble_axes_metadata
:canonical: abtem.core.ensemble.EmptyEnsemble.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} ensemble_shape
:canonical: abtem.core.ensemble.EmptyEnsemble.ensemble_shape
:type: tuple[int, ...]

````

`````

`````{py:class} Ensemble
:canonical: abtem.core.ensemble.Ensemble

```{autodoc2-docstring} abtem.core.ensemble.Ensemble
:parser: rst
```

````{py:property} axes_metadata
:canonical: abtem.core.ensemble.Ensemble.axes_metadata
:type: abtem.core.axes.AxesMetadataList

```{autodoc2-docstring} abtem.core.ensemble.Ensemble.axes_metadata
:parser: rst
```

````

````{py:property} base_axes_metadata
:canonical: abtem.core.ensemble.Ensemble.base_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.core.ensemble.Ensemble.base_axes_metadata
:parser: rst
```

````

````{py:property} base_shape
:canonical: abtem.core.ensemble.Ensemble.base_shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.core.ensemble.Ensemble.base_shape
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.core.ensemble.Ensemble.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.core.ensemble.Ensemble.ensemble_axes_metadata
:parser: rst
```

````

````{py:method} ensemble_blocks(chunks: typing.Optional[abtem.core.chunks.Chunks] = None) -> dask.array.core.Array
:canonical: abtem.core.ensemble.Ensemble.ensemble_blocks

```{autodoc2-docstring} abtem.core.ensemble.Ensemble.ensemble_blocks
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.core.ensemble.Ensemble.ensemble_shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.core.ensemble.Ensemble.ensemble_shape
:parser: rst
```

````

````{py:method} generate_blocks(chunks: abtem.core.chunks.Chunks = 1) -> typing.Generator[tuple[tuple[int, ...], tuple[slice, ...], numpy.ndarray], None, None]
:canonical: abtem.core.ensemble.Ensemble.generate_blocks

```{autodoc2-docstring} abtem.core.ensemble.Ensemble.generate_blocks
:parser: rst
```

````

````{py:property} shape
:canonical: abtem.core.ensemble.Ensemble.shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.core.ensemble.Ensemble.shape
:parser: rst
```

````

`````

````{py:function} concatenate_array_blocks(blocks: numpy.ndarray) -> numpy.ndarray
:canonical: abtem.core.ensemble.concatenate_array_blocks

```{autodoc2-docstring} abtem.core.ensemble.concatenate_array_blocks
:parser: rst
```
````

````{py:function} unpack_blockwise_args(args) -> tuple
:canonical: abtem.core.ensemble.unpack_blockwise_args

```{autodoc2-docstring} abtem.core.ensemble.unpack_blockwise_args
:parser: rst
```
````
