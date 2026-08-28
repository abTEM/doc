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

````{py:method} reconstruct(...)
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

`````{py:class} MixedStatePtychographicOperator(...)
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

````{py:method} reconstruct(...)
:canonical: abtem.reconstruct.MixedStatePtychographicOperator.reconstruct

```{autodoc2-docstring} abtem.reconstruct.MixedStatePtychographicOperator.reconstruct
:parser: rst
```

````

`````

`````{py:class} MultislicePtychographicOperator(...)
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

````{py:method} reconstruct(...)
:canonical: abtem.reconstruct.MultislicePtychographicOperator.reconstruct

```{autodoc2-docstring} abtem.reconstruct.MultislicePtychographicOperator.reconstruct
:parser: rst
```

````

`````

`````{py:class} ProgressBar(...)
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

````{py:method} update(...)
:canonical: abtem.reconstruct.ProgressBar.update

```{autodoc2-docstring} abtem.reconstruct.ProgressBar.update
:parser: rst
```

````

`````

`````{py:class} RegularizedPtychographicOperator(...)
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

````{py:method} reconstruct(...)
:canonical: abtem.reconstruct.RegularizedPtychographicOperator.reconstruct

```{autodoc2-docstring} abtem.reconstruct.RegularizedPtychographicOperator.reconstruct
:parser: rst
```

````

`````

`````{py:class} SimultaneousPtychographicOperator(...)
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

````{py:method} reconstruct(...)
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
