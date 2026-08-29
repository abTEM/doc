# {py:mod}`abtem.core.fft`

```{py:module} abtem.core.fft
```

```{autodoc2-docstring} abtem.core.fft
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CachedFFTWConvolution <abtem.core.fft.CachedFFTWConvolution>`
  - ```{autodoc2-docstring} abtem.core.fft.CachedFFTWConvolution
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`fft2 <abtem.core.fft.fft2>`
  - ```{autodoc2-docstring} abtem.core.fft.fft2
    :parser: rst
    :summary:
    ```
* - {py:obj}`fft2_convolve <abtem.core.fft.fft2_convolve>`
  - ```{autodoc2-docstring} abtem.core.fft.fft2_convolve
    :parser: rst
    :summary:
    ```
* - {py:obj}`fft_crop <abtem.core.fft.fft_crop>`
  - ```{autodoc2-docstring} abtem.core.fft.fft_crop
    :parser: rst
    :summary:
    ```
* - {py:obj}`fft_interpolate <abtem.core.fft.fft_interpolate>`
  - ```{autodoc2-docstring} abtem.core.fft.fft_interpolate
    :parser: rst
    :summary:
    ```
* - {py:obj}`fft_interpolation_masks <abtem.core.fft.fft_interpolation_masks>`
  - ```{autodoc2-docstring} abtem.core.fft.fft_interpolation_masks
    :parser: rst
    :summary:
    ```
* - {py:obj}`fft_shift <abtem.core.fft.fft_shift>`
  - ```{autodoc2-docstring} abtem.core.fft.fft_shift
    :parser: rst
    :summary:
    ```
* - {py:obj}`fft_shift_kernel <abtem.core.fft.fft_shift_kernel>`
  - ```{autodoc2-docstring} abtem.core.fft.fft_shift_kernel
    :parser: rst
    :summary:
    ```
* - {py:obj}`fftn <abtem.core.fft.fftn>`
  - ```{autodoc2-docstring} abtem.core.fft.fftn
    :parser: rst
    :summary:
    ```
* - {py:obj}`get_fftw_object <abtem.core.fft.get_fftw_object>`
  - ```{autodoc2-docstring} abtem.core.fft.get_fftw_object
    :parser: rst
    :summary:
    ```
* - {py:obj}`ifft2 <abtem.core.fft.ifft2>`
  - ```{autodoc2-docstring} abtem.core.fft.ifft2
    :parser: rst
    :summary:
    ```
* - {py:obj}`ifftn <abtem.core.fft.ifftn>`
  - ```{autodoc2-docstring} abtem.core.fft.ifftn
    :parser: rst
    :summary:
    ```
* - {py:obj}`is_fast_fft_size <abtem.core.fft.is_fast_fft_size>`
  - ```{autodoc2-docstring} abtem.core.fft.is_fast_fft_size
    :parser: rst
    :summary:
    ```
* - {py:obj}`next_fast_fft_size <abtem.core.fft.next_fast_fft_size>`
  - ```{autodoc2-docstring} abtem.core.fft.next_fast_fft_size
    :parser: rst
    :summary:
    ```
* - {py:obj}`warn_if_slow_gpu_fft <abtem.core.fft.warn_if_slow_gpu_fft>`
  - ```{autodoc2-docstring} abtem.core.fft.warn_if_slow_gpu_fft
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`U <abtem.core.fft.U>`
  - ```{autodoc2-docstring} abtem.core.fft.U
    :parser: rst
    :summary:
    ```
````

### API

````{py:class} CachedFFTWConvolution()
:canonical: abtem.core.fft.CachedFFTWConvolution

```{autodoc2-docstring} abtem.core.fft.CachedFFTWConvolution
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.core.fft.CachedFFTWConvolution.__init__
:parser: rst
```

````

````{py:data} U
:canonical: abtem.core.fft.U
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.core.fft.U
:parser: rst
```

````

````{py:function} fft2(...) -> abtem.core.fft.U
:canonical: abtem.core.fft.fft2

```{autodoc2-docstring} abtem.core.fft.fft2
:parser: rst
```
````

````{py:function} fft2_convolve(...) -> abtem.core.fft.U
:canonical: abtem.core.fft.fft2_convolve

```{autodoc2-docstring} abtem.core.fft.fft2_convolve
:parser: rst
```
````

````{py:function} fft_crop(...)
:canonical: abtem.core.fft.fft_crop

```{autodoc2-docstring} abtem.core.fft.fft_crop
:parser: rst
```
````

````{py:function} fft_interpolate(...)
:canonical: abtem.core.fft.fft_interpolate

```{autodoc2-docstring} abtem.core.fft.fft_interpolate
:parser: rst
```
````

````{py:function} fft_interpolation_masks(...) -> tuple[numpy.ndarray, numpy.ndarray]
:canonical: abtem.core.fft.fft_interpolation_masks

```{autodoc2-docstring} abtem.core.fft.fft_interpolation_masks
:parser: rst
```
````

````{py:function} fft_shift(...) -> numpy.ndarray
:canonical: abtem.core.fft.fft_shift

```{autodoc2-docstring} abtem.core.fft.fft_shift
:parser: rst
```
````

````{py:function} fft_shift_kernel(...) -> numpy.ndarray
:canonical: abtem.core.fft.fft_shift_kernel

```{autodoc2-docstring} abtem.core.fft.fft_shift_kernel
:parser: rst
```
````

````{py:function} fftn(...) -> abtem.core.fft.U
:canonical: abtem.core.fft.fftn

```{autodoc2-docstring} abtem.core.fft.fftn
:parser: rst
```
````

````{py:function} get_fftw_object(...)
:canonical: abtem.core.fft.get_fftw_object

```{autodoc2-docstring} abtem.core.fft.get_fftw_object
:parser: rst
```
````

````{py:function} ifft2(...) -> abtem.core.fft.U
:canonical: abtem.core.fft.ifft2

```{autodoc2-docstring} abtem.core.fft.ifft2
:parser: rst
```
````

````{py:function} ifftn(...) -> abtem.core.fft.U
:canonical: abtem.core.fft.ifftn

```{autodoc2-docstring} abtem.core.fft.ifftn
:parser: rst
```
````

````{py:function} is_fast_fft_size(...) -> bool
:canonical: abtem.core.fft.is_fast_fft_size

```{autodoc2-docstring} abtem.core.fft.is_fast_fft_size
:parser: rst
```
````

````{py:function} next_fast_fft_size(...) -> int
:canonical: abtem.core.fft.next_fast_fft_size

```{autodoc2-docstring} abtem.core.fft.next_fast_fft_size
:parser: rst
```
````

````{py:function} warn_if_slow_gpu_fft(...)
:canonical: abtem.core.fft.warn_if_slow_gpu_fft

```{autodoc2-docstring} abtem.core.fft.warn_if_slow_gpu_fft
:parser: rst
```
````
