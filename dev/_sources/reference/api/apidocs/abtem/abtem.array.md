# {py:mod}`abtem.array`

```{py:module} abtem.array
```

```{autodoc2-docstring} abtem.array
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ComputableList <abtem.array.ComputableList>`
  - ```{autodoc2-docstring} abtem.array.ComputableList
    :summary:
    ```
* - {py:obj}`ArrayObject <abtem.array.ArrayObject>`
  - ```{autodoc2-docstring} abtem.array.ArrayObject
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`multi_output_blockwise <abtem.array.multi_output_blockwise>`
  - ```{autodoc2-docstring} abtem.array.multi_output_blockwise
    :summary:
    ```
* - {py:obj}`validate_lazy <abtem.array.validate_lazy>`
  - ```{autodoc2-docstring} abtem.array.validate_lazy
    :summary:
    ```
* - {py:obj}`from_zarr <abtem.array.from_zarr>`
  - ```{autodoc2-docstring} abtem.array.from_zarr
    :summary:
    ```
* - {py:obj}`validate_axis_metadata <abtem.array.validate_axis_metadata>`
  - ```{autodoc2-docstring} abtem.array.validate_axis_metadata
    :summary:
    ```
* - {py:obj}`stack <abtem.array.stack>`
  - ```{autodoc2-docstring} abtem.array.stack
    :summary:
    ```
* - {py:obj}`concatenate <abtem.array.concatenate>`
  - ```{autodoc2-docstring} abtem.array.concatenate
    :summary:
    ```
* - {py:obj}`swapaxes <abtem.array.swapaxes>`
  - ```{autodoc2-docstring} abtem.array.swapaxes
    :summary:
    ```
* - {py:obj}`moveaxis <abtem.array.moveaxis>`
  - ```{autodoc2-docstring} abtem.array.moveaxis
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`tifffile <abtem.array.tifffile>`
  - ```{autodoc2-docstring} abtem.array.tifffile
    :summary:
    ```
* - {py:obj}`hs <abtem.array.hs>`
  - ```{autodoc2-docstring} abtem.array.hs
    :summary:
    ```
* - {py:obj}`xr <abtem.array.xr>`
  - ```{autodoc2-docstring} abtem.array.xr
    :summary:
    ```
* - {py:obj}`em <abtem.array.em>`
  - ```{autodoc2-docstring} abtem.array.em
    :summary:
    ```
* - {py:obj}`ArrayObjectType <abtem.array.ArrayObjectType>`
  - ```{autodoc2-docstring} abtem.array.ArrayObjectType
    :summary:
    ```
* - {py:obj}`ArrayObjectTypeAlt <abtem.array.ArrayObjectTypeAlt>`
  - ```{autodoc2-docstring} abtem.array.ArrayObjectTypeAlt
    :summary:
    ```
* - {py:obj}`ArrayItemType <abtem.array.ArrayItemType>`
  - ```{autodoc2-docstring} abtem.array.ArrayItemType
    :summary:
    ```
````

### API

````{py:data} tifffile
:canonical: abtem.array.tifffile
:type: typing.Optional[types.ModuleType]
:value: >
   None

```{autodoc2-docstring} abtem.array.tifffile
```

````

````{py:data} hs
:canonical: abtem.array.hs
:type: typing.Optional[types.ModuleType]
:value: >
   None

```{autodoc2-docstring} abtem.array.hs
```

````

````{py:data} xr
:canonical: abtem.array.xr
:type: typing.Optional[types.ModuleType]
:value: >
   None

```{autodoc2-docstring} abtem.array.xr
```

````

````{py:data} em
:canonical: abtem.array.em
:type: typing.Optional[types.ModuleType]
:value: >
   None

```{autodoc2-docstring} abtem.array.em
```

````

````{py:data} ArrayObjectType
:canonical: abtem.array.ArrayObjectType
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.array.ArrayObjectType
```

````

````{py:data} ArrayObjectTypeAlt
:canonical: abtem.array.ArrayObjectTypeAlt
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.array.ArrayObjectTypeAlt
```

````

````{py:data} ArrayItemType
:canonical: abtem.array.ArrayItemType
:value: >
   None

```{autodoc2-docstring} abtem.array.ArrayItemType
```

````

````{py:function} multi_output_blockwise(func: typing.Callable, array: dask.array.core.Array, chunks: tuple[tuple[int, ...], ...], array_axes: tuple[dask.array.core.Array, ...], new_axes: tuple[dask.array.core.Array, ...], out_metas: tuple, drop_axes: tuple[tuple[int, ...], ...], new_shapes: tuple[tuple[int, ...], ...], **kwargs) -> tuple[dask.array.core.Array, ...]
:canonical: abtem.array.multi_output_blockwise

```{autodoc2-docstring} abtem.array.multi_output_blockwise
```
````

`````{py:class} ComputableList()
:canonical: abtem.array.ComputableList

Bases: {py:obj}`list`

```{autodoc2-docstring} abtem.array.ComputableList
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.array.ComputableList.__init__
```

````{py:method} to_zarr(url: str, compute: bool = True, overwrite: bool = False, progress_bar: typing.Optional[bool] = None, compression_level: int | None = 4, **kwargs: typing.Any)
:canonical: abtem.array.ComputableList.to_zarr

```{autodoc2-docstring} abtem.array.ComputableList.to_zarr
```

````

````{py:method} compute(**kwargs) -> list[abtem.array.ArrayObject] | tuple[list[abtem.array.ArrayObject], tuple]
:canonical: abtem.array.ComputableList.compute

```{autodoc2-docstring} abtem.array.ComputableList.compute
```

````

`````

````{py:function} validate_lazy(lazy: typing.Optional[bool]) -> bool
:canonical: abtem.array.validate_lazy

```{autodoc2-docstring} abtem.array.validate_lazy
```
````

`````{py:class} ArrayObject(array: numpy.ndarray | dask.array.core.Array, ensemble_axes_metadata: list[abtem.core.axes.AxisMetadata] | None = None, metadata: dict | None = None, **kwargs)
:canonical: abtem.array.ArrayObject

Bases: {py:obj}`abtem.core.ensemble.Ensemble`, {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.array.ArrayObject
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.array.ArrayObject.__init__
```

````{py:property} base_dims
:canonical: abtem.array.ArrayObject.base_dims
:type: int

```{autodoc2-docstring} abtem.array.ArrayObject.base_dims
```

````

````{py:property} ensemble_dims
:canonical: abtem.array.ArrayObject.ensemble_dims
:type: int

```{autodoc2-docstring} abtem.array.ArrayObject.ensemble_dims
```

````

````{py:property} base_axes_metadata
:canonical: abtem.array.ArrayObject.base_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} shape
:canonical: abtem.array.ArrayObject.shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.array.ArrayObject.shape
```

````

````{py:property} base_shape
:canonical: abtem.array.ArrayObject.base_shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.array.ArrayObject.base_shape
```

````

````{py:property} ensemble_shape
:canonical: abtem.array.ArrayObject.ensemble_shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.array.ArrayObject.ensemble_shape
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.array.ArrayObject.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.array.ArrayObject.ensemble_axes_metadata
```

````

````{py:property} axes_metadata
:canonical: abtem.array.ArrayObject.axes_metadata
:type: abtem.core.axes.AxesMetadataList

```{autodoc2-docstring} abtem.array.ArrayObject.axes_metadata
```

````

````{py:method} apply_func(func: typing.Callable, **kwargs) -> typing.Self
:canonical: abtem.array.ArrayObject.apply_func

```{autodoc2-docstring} abtem.array.ArrayObject.apply_func
```

````

````{py:method} get_from_metadata(name: str, broadcastable: bool = False)
:canonical: abtem.array.ArrayObject.get_from_metadata

```{autodoc2-docstring} abtem.array.ArrayObject.get_from_metadata
```

````

````{py:method} from_array_and_metadata(array: numpy.ndarray | dask.array.core.Array, axes_metadata: list[abtem.core.axes.AxisMetadata], metadata: dict) -> typing.Self
:canonical: abtem.array.ArrayObject.from_array_and_metadata
:abstractmethod:
:classmethod:

```{autodoc2-docstring} abtem.array.ArrayObject.from_array_and_metadata
```

````

````{py:method} rechunk(chunks: abtem.core.chunks.Chunks, **kwargs) -> abtem.array.ArrayObject
:canonical: abtem.array.ArrayObject.rechunk

```{autodoc2-docstring} abtem.array.ArrayObject.rechunk
```

````

````{py:property} metadata
:canonical: abtem.array.ArrayObject.metadata
:type: dict

```{autodoc2-docstring} abtem.array.ArrayObject.metadata
```

````

````{py:property} array
:canonical: abtem.array.ArrayObject.array
:type: numpy.ndarray | dask.array.core.Array

```{autodoc2-docstring} abtem.array.ArrayObject.array
```

````

````{py:property} dtype
:canonical: abtem.array.ArrayObject.dtype
:type: numpy.dtype

```{autodoc2-docstring} abtem.array.ArrayObject.dtype
```

````

````{py:property} device
:canonical: abtem.array.ArrayObject.device
:type: str

```{autodoc2-docstring} abtem.array.ArrayObject.device
```

````

````{py:property} is_lazy
:canonical: abtem.array.ArrayObject.is_lazy
:type: bool

```{autodoc2-docstring} abtem.array.ArrayObject.is_lazy
```

````

````{py:property} is_complex
:canonical: abtem.array.ArrayObject.is_complex
:type: bool

```{autodoc2-docstring} abtem.array.ArrayObject.is_complex
```

````

````{py:method} mean(axis: typing.Optional[int | tuple[int, ...]] = None, keepdims: bool = False, split_every: int = 2) -> typing.Self
:canonical: abtem.array.ArrayObject.mean

```{autodoc2-docstring} abtem.array.ArrayObject.mean
```

````

````{py:method} sum(axis: typing.Optional[int | tuple[int, ...]] = None, keepdims: bool = False, split_every: int = 2) -> abtem.array.ArrayObject
:canonical: abtem.array.ArrayObject.sum

```{autodoc2-docstring} abtem.array.ArrayObject.sum
```

````

````{py:method} std(axis: typing.Optional[int | tuple[int, ...]] = None, keepdims: bool = False, split_every: int = 2) -> abtem.array.ArrayObject
:canonical: abtem.array.ArrayObject.std

```{autodoc2-docstring} abtem.array.ArrayObject.std
```

````

````{py:method} min(axis: typing.Optional[int | tuple[int, ...]] = None, keepdims: bool = False, split_every: int = 2) -> abtem.array.ArrayObject
:canonical: abtem.array.ArrayObject.min

```{autodoc2-docstring} abtem.array.ArrayObject.min
```

````

````{py:method} max(axis: typing.Optional[int | tuple[int, ...]] = None, keepdims: bool = False, split_every: int = 2) -> abtem.array.ArrayObject
:canonical: abtem.array.ArrayObject.max

```{autodoc2-docstring} abtem.array.ArrayObject.max
```

````

````{py:method} get_items(items: abtem.array.ArrayItemType | tuple[abtem.array.ArrayItemType, ...], keepdims: bool = False) -> dict
:canonical: abtem.array.ArrayObject.get_items

```{autodoc2-docstring} abtem.array.ArrayObject.get_items
```

````

````{py:method} expand_dims(axis: typing.Optional[int | tuple[int, ...]] = None, axis_metadata: typing.Optional[list[abtem.core.axes.AxisMetadata]] = None) -> typing.Self
:canonical: abtem.array.ArrayObject.expand_dims

```{autodoc2-docstring} abtem.array.ArrayObject.expand_dims
```

````

````{py:method} squeeze(axis: typing.Optional[tuple[int, ...]] = None) -> typing.Self
:canonical: abtem.array.ArrayObject.squeeze

```{autodoc2-docstring} abtem.array.ArrayObject.squeeze
```

````

````{py:method} ensure_lazy(chunks: abtem.core.chunks.Chunks = 'auto') -> typing.Self
:canonical: abtem.array.ArrayObject.ensure_lazy

```{autodoc2-docstring} abtem.array.ArrayObject.ensure_lazy
```

````

````{py:method} lazy(chunks: str = 'auto') -> typing.Self
:canonical: abtem.array.ArrayObject.lazy

```{autodoc2-docstring} abtem.array.ArrayObject.lazy
```

````

````{py:method} compute(progress_bar: bool | None = None, profiler: bool = False, resource_profiler: bool = False, **kwargs) -> typing.Self | tuple[typing.Self, tuple]
:canonical: abtem.array.ArrayObject.compute

```{autodoc2-docstring} abtem.array.ArrayObject.compute
```

````

````{py:method} copy_to_device(device: str) -> typing.Self
:canonical: abtem.array.ArrayObject.copy_to_device

```{autodoc2-docstring} abtem.array.ArrayObject.copy_to_device
```

````

````{py:method} to_cpu() -> typing.Self
:canonical: abtem.array.ArrayObject.to_cpu

```{autodoc2-docstring} abtem.array.ArrayObject.to_cpu
```

````

````{py:method} to_gpu(device: str = 'gpu') -> typing.Self
:canonical: abtem.array.ArrayObject.to_gpu

```{autodoc2-docstring} abtem.array.ArrayObject.to_gpu
```

````

````{py:method} to_zarr(url: str, compute: bool = True, overwrite: bool = False, **kwargs)
:canonical: abtem.array.ArrayObject.to_zarr

```{autodoc2-docstring} abtem.array.ArrayObject.to_zarr
```

````

````{py:method} to_tiff(filename: str, **kwargs)
:canonical: abtem.array.ArrayObject.to_tiff

```{autodoc2-docstring} abtem.array.ArrayObject.to_tiff
```

````

````{py:method} from_zarr(url: str, chunks: abtem.core.chunks.Chunks = 'auto') -> typing.Self
:canonical: abtem.array.ArrayObject.from_zarr
:classmethod:

```{autodoc2-docstring} abtem.array.ArrayObject.from_zarr
```

````

````{py:method} no_base_chunks()
:canonical: abtem.array.ArrayObject.no_base_chunks

```{autodoc2-docstring} abtem.array.ArrayObject.no_base_chunks
```

````

````{py:method} apply_transform(transform: abtem.transform.ArrayObjectTransform, max_batch: int | str = 'auto') -> abtem.array.ArrayObject | list[abtem.array.ArrayObject]
:canonical: abtem.array.ArrayObject.apply_transform

```{autodoc2-docstring} abtem.array.ArrayObject.apply_transform
```

````

````{py:method} set_ensemble_axes_metadata(axes_metadata: abtem.core.axes.AxisMetadata, axis: int) -> typing.Self
:canonical: abtem.array.ArrayObject.set_ensemble_axes_metadata

```{autodoc2-docstring} abtem.array.ArrayObject.set_ensemble_axes_metadata
```

````

````{py:method} to_hyperspy(transpose: bool = True)
:canonical: abtem.array.ArrayObject.to_hyperspy

```{autodoc2-docstring} abtem.array.ArrayObject.to_hyperspy
```

````

````{py:method} to_data_array()
:canonical: abtem.array.ArrayObject.to_data_array

```{autodoc2-docstring} abtem.array.ArrayObject.to_data_array
```

````

````{py:method} to_quantem()
:canonical: abtem.array.ArrayObject.to_quantem

```{autodoc2-docstring} abtem.array.ArrayObject.to_quantem
```

````

`````

````{py:function} from_zarr(url: str, chunks: typing.Optional[abtem.core.chunks.Chunks] = None)
:canonical: abtem.array.from_zarr

```{autodoc2-docstring} abtem.array.from_zarr
```
````

````{py:function} validate_axis_metadata(axis_metadata: typing.Optional[abtem.core.axes.AxisMetadata | typing.Sequence[str] | dict]) -> abtem.core.axes.AxisMetadata
:canonical: abtem.array.validate_axis_metadata

```{autodoc2-docstring} abtem.array.validate_axis_metadata
```
````

````{py:function} stack(arrays: typing.Sequence[abtem.array.ArrayObjectType], axis_metadata: typing.Optional[abtem.core.axes.AxisMetadata | typing.Sequence[str] | dict] = None, axis: int = 0) -> abtem.array.ArrayObjectType
:canonical: abtem.array.stack

```{autodoc2-docstring} abtem.array.stack
```
````

````{py:function} concatenate(arrays: typing.Sequence[abtem.array.ArrayObject], axis: int = 0) -> abtem.array.ArrayObject
:canonical: abtem.array.concatenate

```{autodoc2-docstring} abtem.array.concatenate
```
````

````{py:function} swapaxes(array_object, axis1, axis2)
:canonical: abtem.array.swapaxes

```{autodoc2-docstring} abtem.array.swapaxes
```
````

````{py:function} moveaxis(array_object: abtem.array.ArrayObject, source: tuple[int, ...], destination: tuple[int, ...]) -> abtem.array.ArrayObject
:canonical: abtem.array.moveaxis

```{autodoc2-docstring} abtem.array.moveaxis
```
````
