# {py:mod}`abtem.core.backend`

```{py:module} abtem.core.backend
```

```{autodoc2-docstring} abtem.core.backend
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`asnumpy <abtem.core.backend.asnumpy>`
  - ```{autodoc2-docstring} abtem.core.backend.asnumpy
    :summary:
    ```
* - {py:obj}`check_cupy_is_installed <abtem.core.backend.check_cupy_is_installed>`
  - ```{autodoc2-docstring} abtem.core.backend.check_cupy_is_installed
    :summary:
    ```
* - {py:obj}`copy_to_device <abtem.core.backend.copy_to_device>`
  - ```{autodoc2-docstring} abtem.core.backend.copy_to_device
    :summary:
    ```
* - {py:obj}`device_name_from_array_module <abtem.core.backend.device_name_from_array_module>`
  - ```{autodoc2-docstring} abtem.core.backend.device_name_from_array_module
    :summary:
    ```
* - {py:obj}`get_array_module <abtem.core.backend.get_array_module>`
  - ```{autodoc2-docstring} abtem.core.backend.get_array_module
    :summary:
    ```
* - {py:obj}`get_ndimage_module <abtem.core.backend.get_ndimage_module>`
  - ```{autodoc2-docstring} abtem.core.backend.get_ndimage_module
    :summary:
    ```
* - {py:obj}`get_scipy_module <abtem.core.backend.get_scipy_module>`
  - ```{autodoc2-docstring} abtem.core.backend.get_scipy_module
    :summary:
    ```
* - {py:obj}`validate_device <abtem.core.backend.validate_device>`
  - ```{autodoc2-docstring} abtem.core.backend.validate_device
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ArrayModule <abtem.core.backend.ArrayModule>`
  - ```{autodoc2-docstring} abtem.core.backend.ArrayModule
    :summary:
    ```
````

### API

````{py:data} ArrayModule
:canonical: abtem.core.backend.ArrayModule
:value: >
   None

```{autodoc2-docstring} abtem.core.backend.ArrayModule
```

````

````{py:function} asnumpy(array: numpy.ndarray | dask.array.Array)
:canonical: abtem.core.backend.asnumpy

```{autodoc2-docstring} abtem.core.backend.asnumpy
```
````

````{py:function} check_cupy_is_installed()
:canonical: abtem.core.backend.check_cupy_is_installed

```{autodoc2-docstring} abtem.core.backend.check_cupy_is_installed
```
````

````{py:function} copy_to_device(array: numpy.ndarray | dask.array.core.Array, device: types.ModuleType | numpy.ndarray | dask.array.core.Array | str | None = None)
:canonical: abtem.core.backend.copy_to_device

```{autodoc2-docstring} abtem.core.backend.copy_to_device
```
````

````{py:function} device_name_from_array_module(xp: abtem.core.backend.ArrayModule) -> str
:canonical: abtem.core.backend.device_name_from_array_module

```{autodoc2-docstring} abtem.core.backend.device_name_from_array_module
```
````

````{py:function} get_array_module(x: types.ModuleType | numpy.ndarray | dask.array.core.Array | str | None = None) -> types.ModuleType
:canonical: abtem.core.backend.get_array_module

```{autodoc2-docstring} abtem.core.backend.get_array_module
```
````

````{py:function} get_ndimage_module(x: types.ModuleType | numpy.ndarray | dask.array.core.Array | str | None = None) -> types.ModuleType
:canonical: abtem.core.backend.get_ndimage_module

```{autodoc2-docstring} abtem.core.backend.get_ndimage_module
```
````

````{py:function} get_scipy_module(x: types.ModuleType | numpy.ndarray | dask.array.core.Array | str | None = None)
:canonical: abtem.core.backend.get_scipy_module

```{autodoc2-docstring} abtem.core.backend.get_scipy_module
```
````

````{py:function} validate_device(device: str | None = None) -> str
:canonical: abtem.core.backend.validate_device

```{autodoc2-docstring} abtem.core.backend.validate_device
```
````
