# {py:mod}`abtem.reconstruct`

```{py:module} abtem.reconstruct
```

```{autodoc2-docstring} abtem.reconstruct
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AbstractPtychographicOperator <abtem.reconstruct.AbstractPtychographicOperator>`
  - ```{autodoc2-docstring} abtem.reconstruct.AbstractPtychographicOperator
    :parser: rst
    :summary:
    ```
* - {py:obj}`MixedStatePtychographicOperator <abtem.reconstruct.MixedStatePtychographicOperator>`
  - ```{autodoc2-docstring} abtem.reconstruct.MixedStatePtychographicOperator
    :parser: rst
    :summary:
    ```
* - {py:obj}`MultislicePtychographicOperator <abtem.reconstruct.MultislicePtychographicOperator>`
  - ```{autodoc2-docstring} abtem.reconstruct.MultislicePtychographicOperator
    :parser: rst
    :summary:
    ```
* - {py:obj}`ProgressBar <abtem.reconstruct.ProgressBar>`
  - ```{autodoc2-docstring} abtem.reconstruct.ProgressBar
    :parser: rst
    :summary:
    ```
* - {py:obj}`RegularizedPtychographicOperator <abtem.reconstruct.RegularizedPtychographicOperator>`
  - ```{autodoc2-docstring} abtem.reconstruct.RegularizedPtychographicOperator
    :parser: rst
    :summary:
    ```
* - {py:obj}`SimultaneousPtychographicOperator <abtem.reconstruct.SimultaneousPtychographicOperator>`
  - ```{autodoc2-docstring} abtem.reconstruct.SimultaneousPtychographicOperator
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`experimental_symbols <abtem.reconstruct.experimental_symbols>`
  - ```{autodoc2-docstring} abtem.reconstruct.experimental_symbols
    :parser: rst
    :summary:
    ```
* - {py:obj}`reconstruction_symbols <abtem.reconstruct.reconstruction_symbols>`
  - ```{autodoc2-docstring} abtem.reconstruct.reconstruction_symbols
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} AbstractPtychographicOperator
:canonical: abtem.reconstruct.AbstractPtychographicOperator

```{autodoc2-docstring} abtem.reconstruct.AbstractPtychographicOperator
:parser: rst
```

````{py:property} angular_sampling
:canonical: abtem.reconstruct.AbstractPtychographicOperator.angular_sampling

```{autodoc2-docstring} abtem.reconstruct.AbstractPtychographicOperator.angular_sampling
:parser: rst
```

````

````{py:method} preprocess()
:canonical: abtem.reconstruct.AbstractPtychographicOperator.preprocess
:abstractmethod:

```{autodoc2-docstring} abtem.reconstruct.AbstractPtychographicOperator.preprocess
:parser: rst
```

````

````{py:method} reconstruct(max_iterations, return_iterations, fix_com, random_seed, verbose, functions_queue, parameters, **kwargs)
:canonical: abtem.reconstruct.AbstractPtychographicOperator.reconstruct
:abstractmethod:

```{autodoc2-docstring} abtem.reconstruct.AbstractPtychographicOperator.reconstruct
:parser: rst
```

````

````{py:property} sampling
:canonical: abtem.reconstruct.AbstractPtychographicOperator.sampling

```{autodoc2-docstring} abtem.reconstruct.AbstractPtychographicOperator.sampling
:parser: rst
```

````

`````

`````{py:class} MixedStatePtychographicOperator(diffraction_patterns: typing.Union[numpy.ndarray, abtem.measurements.DiffractionPatterns], energy: float, num_probes: int, region_of_interest_shape: typing.Sequence[int] = None, objects: numpy.ndarray = None, probes: typing.Union[numpy.ndarray, abtem.waves.Probe] = None, positions: numpy.ndarray = None, semiangle_cutoff: float = None, preprocess: bool = False, device: str = 'cpu', parameters: typing.Mapping[str, float] = None, **kwargs)
:canonical: abtem.reconstruct.MixedStatePtychographicOperator

Bases: {py:obj}`abtem.reconstruct.AbstractPtychographicOperator`

```{autodoc2-docstring} abtem.reconstruct.MixedStatePtychographicOperator
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.reconstruct.MixedStatePtychographicOperator.__init__
:parser: rst
```

````{py:method} preprocess()
:canonical: abtem.reconstruct.MixedStatePtychographicOperator.preprocess

```{autodoc2-docstring} abtem.reconstruct.MixedStatePtychographicOperator.preprocess
:parser: rst
```

````

````{py:method} reconstruct(max_iterations: int = 5, return_iterations: bool = False, probe_orthogonalization_frequency: int = None, warmup_update_steps: int = 0, fix_com: bool = True, random_seed=None, verbose: bool = False, parameters: typing.Mapping[str, float] = None, functions_queue: typing.Iterable = None, **kwargs)
:canonical: abtem.reconstruct.MixedStatePtychographicOperator.reconstruct

```{autodoc2-docstring} abtem.reconstruct.MixedStatePtychographicOperator.reconstruct
:parser: rst
```

````

`````

`````{py:class} MultislicePtychographicOperator(diffraction_patterns: typing.Union[numpy.ndarray, abtem.measurements.DiffractionPatterns], energy: float, num_slices: int, slice_thicknesses: typing.Union[float, typing.Sequence[float]], region_of_interest_shape: typing.Sequence[int] = None, objects: numpy.ndarray = None, probes: typing.Union[numpy.ndarray, abtem.waves.Probe] = None, positions: numpy.ndarray = None, semiangle_cutoff: float = None, preprocess: bool = False, device: str = 'cpu', parameters: typing.Mapping[str, float] = None, **kwargs)
:canonical: abtem.reconstruct.MultislicePtychographicOperator

Bases: {py:obj}`abtem.reconstruct.AbstractPtychographicOperator`

```{autodoc2-docstring} abtem.reconstruct.MultislicePtychographicOperator
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.reconstruct.MultislicePtychographicOperator.__init__
:parser: rst
```

````{py:method} preprocess()
:canonical: abtem.reconstruct.MultislicePtychographicOperator.preprocess

```{autodoc2-docstring} abtem.reconstruct.MultislicePtychographicOperator.preprocess
:parser: rst
```

````

````{py:method} reconstruct(max_iterations: int = 5, return_iterations: bool = False, fix_com: bool = True, random_seed=None, verbose: bool = False, parameters: typing.Mapping[str, float] = None, measurement_output_view: str = 'padded', functions_queue: typing.Iterable = None, **kwargs)
:canonical: abtem.reconstruct.MultislicePtychographicOperator.reconstruct

```{autodoc2-docstring} abtem.reconstruct.MultislicePtychographicOperator.reconstruct
:parser: rst
```

````

`````

`````{py:class} ProgressBar(**kwargs)
:canonical: abtem.reconstruct.ProgressBar

```{autodoc2-docstring} abtem.reconstruct.ProgressBar
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.reconstruct.ProgressBar.__init__
:parser: rst
```

````{py:method} close()
:canonical: abtem.reconstruct.ProgressBar.close

```{autodoc2-docstring} abtem.reconstruct.ProgressBar.close
:parser: rst
```

````

````{py:property} disable
:canonical: abtem.reconstruct.ProgressBar.disable

```{autodoc2-docstring} abtem.reconstruct.ProgressBar.disable
:parser: rst
```

````

````{py:method} refresh()
:canonical: abtem.reconstruct.ProgressBar.refresh

```{autodoc2-docstring} abtem.reconstruct.ProgressBar.refresh
:parser: rst
```

````

````{py:method} reset()
:canonical: abtem.reconstruct.ProgressBar.reset

```{autodoc2-docstring} abtem.reconstruct.ProgressBar.reset
:parser: rst
```

````

````{py:property} tqdm
:canonical: abtem.reconstruct.ProgressBar.tqdm

```{autodoc2-docstring} abtem.reconstruct.ProgressBar.tqdm
:parser: rst
```

````

````{py:method} update(n)
:canonical: abtem.reconstruct.ProgressBar.update

```{autodoc2-docstring} abtem.reconstruct.ProgressBar.update
:parser: rst
```

````

`````

`````{py:class} RegularizedPtychographicOperator(diffraction_patterns: typing.Union[numpy.ndarray, abtem.measurements.DiffractionPatterns], energy: float = None, region_of_interest_shape: typing.Sequence[int] = None, objects: numpy.ndarray = None, probes: typing.Union[numpy.ndarray, abtem.waves.Probe] = None, positions: numpy.ndarray = None, semiangle_cutoff: float = None, preprocess: bool = False, device: str = 'cpu', parameters: typing.Mapping[str, float] = None, **kwargs)
:canonical: abtem.reconstruct.RegularizedPtychographicOperator

Bases: {py:obj}`abtem.reconstruct.AbstractPtychographicOperator`

```{autodoc2-docstring} abtem.reconstruct.RegularizedPtychographicOperator
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.reconstruct.RegularizedPtychographicOperator.__init__
:parser: rst
```

````{py:method} preprocess()
:canonical: abtem.reconstruct.RegularizedPtychographicOperator.preprocess

```{autodoc2-docstring} abtem.reconstruct.RegularizedPtychographicOperator.preprocess
:parser: rst
```

````

````{py:method} reconstruct(max_iterations: int = 5, return_iterations: bool = False, fix_com: bool = True, random_seed=None, verbose: bool = False, functions_queue: typing.Iterable = None, parameters: typing.Mapping[str, float] = None, **kwargs)
:canonical: abtem.reconstruct.RegularizedPtychographicOperator.reconstruct

```{autodoc2-docstring} abtem.reconstruct.RegularizedPtychographicOperator.reconstruct
:parser: rst
```

````

`````

`````{py:class} SimultaneousPtychographicOperator(diffraction_patterns: typing.Union[typing.Sequence[numpy.ndarray], typing.Sequence[abtem.measurements.DiffractionPatterns]], energy: float, region_of_interest_shape: typing.Sequence[int] = None, objects: numpy.ndarray = None, probes: typing.Union[numpy.ndarray, abtem.waves.Probe] = None, positions: numpy.ndarray = None, semiangle_cutoff: float = None, preprocess: bool = False, device: str = 'cpu', parameters: typing.Mapping[str, float] = None, **kwargs)
:canonical: abtem.reconstruct.SimultaneousPtychographicOperator

Bases: {py:obj}`abtem.reconstruct.AbstractPtychographicOperator`

```{autodoc2-docstring} abtem.reconstruct.SimultaneousPtychographicOperator
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.reconstruct.SimultaneousPtychographicOperator.__init__
:parser: rst
```

````{py:method} preprocess()
:canonical: abtem.reconstruct.SimultaneousPtychographicOperator.preprocess

```{autodoc2-docstring} abtem.reconstruct.SimultaneousPtychographicOperator.preprocess
:parser: rst
```

````

````{py:method} reconstruct(max_iterations: int = 5, return_iterations: bool = False, warmup_update_steps: int = 0, common_probe: bool = False, fix_com: bool = True, random_seed=None, verbose: bool = False, functions_queue: typing.Iterable = None, parameters: typing.Mapping[str, float] = None, **kwargs)
:canonical: abtem.reconstruct.SimultaneousPtychographicOperator.reconstruct

```{autodoc2-docstring} abtem.reconstruct.SimultaneousPtychographicOperator.reconstruct
:parser: rst
```

````

`````

````{py:data} experimental_symbols
:canonical: abtem.reconstruct.experimental_symbols
:value: >
   ('rotation_angle', 'scan_step_sizes', 'angular_sampling', 'background_counts_cutoff', 'counts_scalin...

```{autodoc2-docstring} abtem.reconstruct.experimental_symbols
:parser: rst
```

````

````{py:data} reconstruction_symbols
:canonical: abtem.reconstruct.reconstruction_symbols
:value: >
   None

```{autodoc2-docstring} abtem.reconstruct.reconstruction_symbols
:parser: rst
```

````
