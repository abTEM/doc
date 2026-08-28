# {py:mod}`abtem.array`

```{py:module} abtem.array
```

```{autodoc2-docstring} abtem.array
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ArrayObject <abtem.array.ArrayObject>`
  - ```{autodoc2-docstring} abtem.array.ArrayObject
    :parser: rst
    :summary:
    ```
* - {py:obj}`ComputableList <abtem.array.ComputableList>`
  - ```{autodoc2-docstring} abtem.array.ComputableList
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`concatenate <abtem.array.concatenate>`
  - ```{autodoc2-docstring} abtem.array.concatenate
    :parser: rst
    :summary:
    ```
* - {py:obj}`from_zarr <abtem.array.from_zarr>`
  - ```{autodoc2-docstring} abtem.array.from_zarr
    :parser: rst
    :summary:
    ```
* - {py:obj}`moveaxis <abtem.array.moveaxis>`
  - ```{autodoc2-docstring} abtem.array.moveaxis
    :parser: rst
    :summary:
    ```
* - {py:obj}`multi_output_blockwise <abtem.array.multi_output_blockwise>`
  - ```{autodoc2-docstring} abtem.array.multi_output_blockwise
    :parser: rst
    :summary:
    ```
* - {py:obj}`stack <abtem.array.stack>`
  - ```{autodoc2-docstring} abtem.array.stack
    :parser: rst
    :summary:
    ```
* - {py:obj}`swapaxes <abtem.array.swapaxes>`
  - ```{autodoc2-docstring} abtem.array.swapaxes
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_axis_metadata <abtem.array.validate_axis_metadata>`
  - ```{autodoc2-docstring} abtem.array.validate_axis_metadata
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_lazy <abtem.array.validate_lazy>`
  - ```{autodoc2-docstring} abtem.array.validate_lazy
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ArrayItemType <abtem.array.ArrayItemType>`
  - ```{autodoc2-docstring} abtem.array.ArrayItemType
    :parser: rst
    :summary:
    ```
* - {py:obj}`ArrayObjectType <abtem.array.ArrayObjectType>`
  - ```{autodoc2-docstring} abtem.array.ArrayObjectType
    :parser: rst
    :summary:
    ```
* - {py:obj}`ArrayObjectTypeAlt <abtem.array.ArrayObjectTypeAlt>`
  - ```{autodoc2-docstring} abtem.array.ArrayObjectTypeAlt
    :parser: rst
    :summary:
    ```
* - {py:obj}`em <abtem.array.em>`
  - ```{autodoc2-docstring} abtem.array.em
    :parser: rst
    :summary:
    ```
* - {py:obj}`hs <abtem.array.hs>`
  - ```{autodoc2-docstring} abtem.array.hs
    :parser: rst
    :summary:
    ```
* - {py:obj}`tifffile <abtem.array.tifffile>`
  - ```{autodoc2-docstring} abtem.array.tifffile
    :parser: rst
    :summary:
    ```
* - {py:obj}`xr <abtem.array.xr>`
  - ```{autodoc2-docstring} abtem.array.xr
    :parser: rst
    :summary:
    ```
````

### API

````{py:data} ArrayItemType
:canonical: abtem.array.ArrayItemType
:value: >
   None

```{autodoc2-docstring} abtem.array.ArrayItemType
:parser: rst
```

````

`````{py:class} ArrayObject(...)
:canonical: abtem.array.ArrayObject

Bases: {py:obj}`abtem.core.ensemble.Ensemble`, {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.array.ArrayObject
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.array.ArrayObject.__init__
:parser: rst
```

````{py:method} apply_func(...) -> typing.Self
:canonical: abtem.array.ArrayObject.apply_func

```{autodoc2-docstring} abtem.array.ArrayObject.apply_func
:parser: rst
```

````

````{py:method} apply_transform(...) -> abtem.array.ArrayObject | list[abtem.array.ArrayObject]
:canonical: abtem.array.ArrayObject.apply_transform

```{autodoc2-docstring} abtem.array.ArrayObject.apply_transform
:parser: rst
```

````

````{py:property} array
:canonical: abtem.array.ArrayObject.array
:type: numpy.ndarray | dask.array.core.Array

```{autodoc2-docstring} abtem.array.ArrayObject.array
:parser: rst
```

````

````{py:property} axes_metadata
:canonical: abtem.array.ArrayObject.axes_metadata
:type: abtem.core.axes.AxesMetadataList

```{autodoc2-docstring} abtem.array.ArrayObject.axes_metadata
:parser: rst
```

````

````{py:property} base_axes_metadata
:canonical: abtem.array.ArrayObject.base_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} base_dims
:canonical: abtem.array.ArrayObject.base_dims
:type: int

```{autodoc2-docstring} abtem.array.ArrayObject.base_dims
:parser: rst
```

````

````{py:property} base_shape
:canonical: abtem.array.ArrayObject.base_shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.array.ArrayObject.base_shape
:parser: rst
```

````

````{py:method} compute(...) -> typing.Self | tuple[typing.Self, tuple]
:canonical: abtem.array.ArrayObject.compute

```{autodoc2-docstring} abtem.array.ArrayObject.compute
:parser: rst
```

````

````{py:method} copy_to_device(...) -> typing.Self
:canonical: abtem.array.ArrayObject.copy_to_device

```{autodoc2-docstring} abtem.array.ArrayObject.copy_to_device
:parser: rst
```

````

````{py:property} device
:canonical: abtem.array.ArrayObject.device
:type: str

```{autodoc2-docstring} abtem.array.ArrayObject.device
:parser: rst
```

````

````{py:property} dtype
:canonical: abtem.array.ArrayObject.dtype
:type: numpy.dtype

```{autodoc2-docstring} abtem.array.ArrayObject.dtype
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.array.ArrayObject.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.array.ArrayObject.ensemble_axes_metadata
:parser: rst
```

````

````{py:property} ensemble_dims
:canonical: abtem.array.ArrayObject.ensemble_dims
:type: int

```{autodoc2-docstring} abtem.array.ArrayObject.ensemble_dims
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.array.ArrayObject.ensemble_shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.array.ArrayObject.ensemble_shape
:parser: rst
```

````

````{py:method} ensure_lazy(...) -> typing.Self
:canonical: abtem.array.ArrayObject.ensure_lazy

```{autodoc2-docstring} abtem.array.ArrayObject.ensure_lazy
:parser: rst
```

````

````{py:method} expand_dims(...) -> typing.Self
:canonical: abtem.array.ArrayObject.expand_dims

```{autodoc2-docstring} abtem.array.ArrayObject.expand_dims
:parser: rst
```

````

````{py:method} from_array_and_metadata(...) -> typing.Self
:canonical: abtem.array.ArrayObject.from_array_and_metadata
:abstractmethod:
:classmethod:

```{autodoc2-docstring} abtem.array.ArrayObject.from_array_and_metadata
:parser: rst
```

````

````{py:method} from_zarr(...) -> typing.Self
:canonical: abtem.array.ArrayObject.from_zarr
:classmethod:

```{autodoc2-docstring} abtem.array.ArrayObject.from_zarr
:parser: rst
```

````

````{py:method} get_from_metadata(...)
:canonical: abtem.array.ArrayObject.get_from_metadata

```{autodoc2-docstring} abtem.array.ArrayObject.get_from_metadata
:parser: rst
```

````

````{py:method} get_items(...) -> dict
:canonical: abtem.array.ArrayObject.get_items

```{autodoc2-docstring} abtem.array.ArrayObject.get_items
:parser: rst
```

````

````{py:property} is_complex
:canonical: abtem.array.ArrayObject.is_complex
:type: bool

```{autodoc2-docstring} abtem.array.ArrayObject.is_complex
:parser: rst
```

````

````{py:property} is_lazy
:canonical: abtem.array.ArrayObject.is_lazy
:type: bool

```{autodoc2-docstring} abtem.array.ArrayObject.is_lazy
:parser: rst
```

````

````{py:method} lazy(...) -> typing.Self
:canonical: abtem.array.ArrayObject.lazy

```{autodoc2-docstring} abtem.array.ArrayObject.lazy
:parser: rst
```

````

````{py:method} max(...) -> abtem.array.ArrayObject
:canonical: abtem.array.ArrayObject.max

```{autodoc2-docstring} abtem.array.ArrayObject.max
:parser: rst
```

````

````{py:method} mean(...) -> typing.Self
:canonical: abtem.array.ArrayObject.mean

```{autodoc2-docstring} abtem.array.ArrayObject.mean
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.array.ArrayObject.metadata
:type: dict

```{autodoc2-docstring} abtem.array.ArrayObject.metadata
:parser: rst
```

````

````{py:method} min(...) -> abtem.array.ArrayObject
:canonical: abtem.array.ArrayObject.min

```{autodoc2-docstring} abtem.array.ArrayObject.min
:parser: rst
```

````

````{py:method} no_base_chunks()
:canonical: abtem.array.ArrayObject.no_base_chunks

```{autodoc2-docstring} abtem.array.ArrayObject.no_base_chunks
:parser: rst
```

````

````{py:method} rechunk(...) -> abtem.array.ArrayObject
:canonical: abtem.array.ArrayObject.rechunk

```{autodoc2-docstring} abtem.array.ArrayObject.rechunk
:parser: rst
```

````

````{py:method} set_ensemble_axes_metadata(...) -> typing.Self
:canonical: abtem.array.ArrayObject.set_ensemble_axes_metadata

```{autodoc2-docstring} abtem.array.ArrayObject.set_ensemble_axes_metadata
:parser: rst
```

````

````{py:property} shape
:canonical: abtem.array.ArrayObject.shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.array.ArrayObject.shape
:parser: rst
```

````

````{py:method} squeeze(...) -> typing.Self
:canonical: abtem.array.ArrayObject.squeeze

```{autodoc2-docstring} abtem.array.ArrayObject.squeeze
:parser: rst
```

````

````{py:method} std(...) -> abtem.array.ArrayObject
:canonical: abtem.array.ArrayObject.std

```{autodoc2-docstring} abtem.array.ArrayObject.std
:parser: rst
```

````

````{py:method} sum(...) -> abtem.array.ArrayObject
:canonical: abtem.array.ArrayObject.sum

```{autodoc2-docstring} abtem.array.ArrayObject.sum
:parser: rst
```

````

````{py:method} to_cpu() -> typing.Self
:canonical: abtem.array.ArrayObject.to_cpu

```{autodoc2-docstring} abtem.array.ArrayObject.to_cpu
:parser: rst
```

````

````{py:method} to_data_array()
:canonical: abtem.array.ArrayObject.to_data_array

```{autodoc2-docstring} abtem.array.ArrayObject.to_data_array
:parser: rst
```

````

````{py:method} to_gpu(...) -> typing.Self
:canonical: abtem.array.ArrayObject.to_gpu

```{autodoc2-docstring} abtem.array.ArrayObject.to_gpu
:parser: rst
```

````

````{py:method} to_hyperspy(...)
:canonical: abtem.array.ArrayObject.to_hyperspy

```{autodoc2-docstring} abtem.array.ArrayObject.to_hyperspy
:parser: rst
```

````

````{py:method} to_quantem()
:canonical: abtem.array.ArrayObject.to_quantem

```{autodoc2-docstring} abtem.array.ArrayObject.to_quantem
:parser: rst
```

````

````{py:method} to_tiff(...)
:canonical: abtem.array.ArrayObject.to_tiff

```{autodoc2-docstring} abtem.array.ArrayObject.to_tiff
:parser: rst
```

````

````{py:method} to_zarr(...)
:canonical: abtem.array.ArrayObject.to_zarr

```{autodoc2-docstring} abtem.array.ArrayObject.to_zarr
:parser: rst
```

````

`````

````{py:data} ArrayObjectType
:canonical: abtem.array.ArrayObjectType
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.array.ArrayObjectType
:parser: rst
```

````

````{py:data} ArrayObjectTypeAlt
:canonical: abtem.array.ArrayObjectTypeAlt
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.array.ArrayObjectTypeAlt
:parser: rst
```

````

`````{py:class} ComputableList()
:canonical: abtem.array.ComputableList

Bases: {py:obj}`list`

```{autodoc2-docstring} abtem.array.ComputableList
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.array.ComputableList.__init__
:parser: rst
```

````{py:method} compute(...) -> list[abtem.array.ArrayObject] | tuple[list[abtem.array.ArrayObject], tuple]
:canonical: abtem.array.ComputableList.compute

```{autodoc2-docstring} abtem.array.ComputableList.compute
:parser: rst
```

````

````{py:method} to_zarr(...)
:canonical: abtem.array.ComputableList.to_zarr

```{autodoc2-docstring} abtem.array.ComputableList.to_zarr
:parser: rst
```

````

`````

````{py:function} concatenate(...) -> abtem.array.ArrayObject
:canonical: abtem.array.concatenate

```{autodoc2-docstring} abtem.array.concatenate
:parser: rst
```
````

````{py:data} em
:canonical: abtem.array.em
:type: typing.Optional[types.ModuleType]
:value: >
   None

```{autodoc2-docstring} abtem.array.em
:parser: rst
```

````

````{py:function} from_zarr(...)
:canonical: abtem.array.from_zarr

```{autodoc2-docstring} abtem.array.from_zarr
:parser: rst
```
````

````{py:data} hs
:canonical: abtem.array.hs
:type: typing.Optional[types.ModuleType]
:value: >
   None

```{autodoc2-docstring} abtem.array.hs
:parser: rst
```

````

````{py:function} moveaxis(...) -> abtem.array.ArrayObject
:canonical: abtem.array.moveaxis

```{autodoc2-docstring} abtem.array.moveaxis
:parser: rst
```
````

````{py:function} multi_output_blockwise(...) -> tuple[dask.array.core.Array, ...]
:canonical: abtem.array.multi_output_blockwise

```{autodoc2-docstring} abtem.array.multi_output_blockwise
:parser: rst
```
````

````{py:function} stack(...) -> abtem.array.ArrayObjectType
:canonical: abtem.array.stack

```{autodoc2-docstring} abtem.array.stack
:parser: rst
```
````

````{py:function} swapaxes(...)
:canonical: abtem.array.swapaxes

```{autodoc2-docstring} abtem.array.swapaxes
:parser: rst
```
````

````{py:data} tifffile
:canonical: abtem.array.tifffile
:type: typing.Optional[types.ModuleType]
:value: >
   None

```{autodoc2-docstring} abtem.array.tifffile
:parser: rst
```

````

````{py:function} validate_axis_metadata(...) -> abtem.core.axes.AxisMetadata
:canonical: abtem.array.validate_axis_metadata

```{autodoc2-docstring} abtem.array.validate_axis_metadata
:parser: rst
```
````

````{py:function} validate_lazy(...) -> bool
:canonical: abtem.array.validate_lazy

```{autodoc2-docstring} abtem.array.validate_lazy
:parser: rst
```
````

````{py:data} xr
:canonical: abtem.array.xr
:type: typing.Optional[types.ModuleType]
:value: >
   None

```{autodoc2-docstring} abtem.array.xr
:parser: rst
```

````
