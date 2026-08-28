# {py:mod}`abtem.transform`

```{py:module} abtem.transform
```

```{autodoc2-docstring} abtem.transform
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ArrayObjectTransform <abtem.transform.ArrayObjectTransform>`
  - ```{autodoc2-docstring} abtem.transform.ArrayObjectTransform
    :parser: rst
    :summary:
    ```
* - {py:obj}`EmptyTransform <abtem.transform.EmptyTransform>`
  - ```{autodoc2-docstring} abtem.transform.EmptyTransform
    :parser: rst
    :summary:
    ```
* - {py:obj}`EnsembleTransform <abtem.transform.EnsembleTransform>`
  -
* - {py:obj}`ReciprocalSpaceMultiplication <abtem.transform.ReciprocalSpaceMultiplication>`
  - ```{autodoc2-docstring} abtem.transform.ReciprocalSpaceMultiplication
    :parser: rst
    :summary:
    ```
* - {py:obj}`TransformFromFunc <abtem.transform.TransformFromFunc>`
  - ```{autodoc2-docstring} abtem.transform.TransformFromFunc
    :parser: rst
    :summary:
    ```
* - {py:obj}`WavesToMeasurementTransform <abtem.transform.WavesToMeasurementTransform>`
  -
* - {py:obj}`WavesToWavesTransform <abtem.transform.WavesToWavesTransform>`
  -
* - {py:obj}`WavesTransform <abtem.transform.WavesTransform>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`join_tuples <abtem.transform.join_tuples>`
  - ```{autodoc2-docstring} abtem.transform.join_tuples
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`WavesType <abtem.transform.WavesType>`
  - ```{autodoc2-docstring} abtem.transform.WavesType
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} ArrayObjectTransform
:canonical: abtem.transform.ArrayObjectTransform

Bases: {py:obj}`typing.Generic`\[{py:obj}`abtem.array.ArrayObjectType`\, {py:obj}`abtem.array.ArrayObjectTypeAlt`\], {py:obj}`abtem.core.ensemble.Ensemble`, {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.transform.ArrayObjectTransform
:parser: rst
```

````{py:method} apply(...) -> abtem.array.ArrayObjectType | abtem.array.ArrayObjectTypeAlt | list[abtem.array.ArrayObjectType | abtem.array.ArrayObjectTypeAlt]
:canonical: abtem.transform.ArrayObjectTransform.apply
:abstractmethod:

```{autodoc2-docstring} abtem.transform.ArrayObjectTransform.apply
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.transform.ArrayObjectTransform.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.transform.ArrayObjectTransform.ensemble_axes_metadata
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.transform.ArrayObjectTransform.ensemble_shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.transform.ArrayObjectTransform.ensemble_shape
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.transform.ArrayObjectTransform.metadata
:type: dict

```{autodoc2-docstring} abtem.transform.ArrayObjectTransform.metadata
:parser: rst
```

````

`````

`````{py:class} EmptyTransform
:canonical: abtem.transform.EmptyTransform

Bases: {py:obj}`abtem.core.ensemble.EmptyEnsemble`, {py:obj}`abtem.transform.ArrayObjectTransform`\[{py:obj}`abtem.array.ArrayObject`\, {py:obj}`abtem.array.ArrayObject`\]

```{autodoc2-docstring} abtem.transform.EmptyTransform
:parser: rst
```

````{py:method} apply(...) -> abtem.array.ArrayObject
:canonical: abtem.transform.EmptyTransform.apply

```{autodoc2-docstring} abtem.transform.EmptyTransform.apply
:parser: rst
```

````

`````

```{py:class} EnsembleTransform(...)
:canonical: abtem.transform.EnsembleTransform

Bases: {py:obj}`abtem.distributions.EnsembleFromDistributions`, {py:obj}`abtem.transform.ArrayObjectTransform`\[{py:obj}`abtem.array.ArrayObjectType`\, {py:obj}`abtem.array.ArrayObjectTypeAlt`\]

```

`````{py:class} ReciprocalSpaceMultiplication(...)
:canonical: abtem.transform.ReciprocalSpaceMultiplication

Bases: {py:obj}`abtem.transform.WavesToWavesTransform`

```{autodoc2-docstring} abtem.transform.ReciprocalSpaceMultiplication
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transform.ReciprocalSpaceMultiplication.__init__
:parser: rst
```

````{py:property} in_place
:canonical: abtem.transform.ReciprocalSpaceMultiplication.in_place
:type: bool

```{autodoc2-docstring} abtem.transform.ReciprocalSpaceMultiplication.in_place
:parser: rst
```

````

`````

`````{py:class} TransformFromFunc(...)
:canonical: abtem.transform.TransformFromFunc

Bases: {py:obj}`abtem.transform.ArrayObjectTransform`\[{py:obj}`abtem.array.ArrayObject`\, {py:obj}`abtem.array.ArrayObject`\]

```{autodoc2-docstring} abtem.transform.TransformFromFunc
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transform.TransformFromFunc.__init__
:parser: rst
```

````{py:method} apply(...) -> abtem.array.ArrayObjectType
:canonical: abtem.transform.TransformFromFunc.apply

```{autodoc2-docstring} abtem.transform.TransformFromFunc.apply
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.transform.TransformFromFunc.ensemble_shape
:type: tuple[int, ...]

````

````{py:property} func
:canonical: abtem.transform.TransformFromFunc.func

```{autodoc2-docstring} abtem.transform.TransformFromFunc.func
:parser: rst
```

````

````{py:property} func_kwargs
:canonical: abtem.transform.TransformFromFunc.func_kwargs

```{autodoc2-docstring} abtem.transform.TransformFromFunc.func_kwargs
:parser: rst
```

````

`````

`````{py:class} WavesToMeasurementTransform(...)
:canonical: abtem.transform.WavesToMeasurementTransform

Bases: {py:obj}`abtem.transform.WavesTransform`\[{py:obj}`abtem.measurements.BaseMeasurements`\]

````{py:method} apply(...) -> abtem.waves.Waves | abtem.measurements.BaseMeasurements | list[abtem.waves.Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.transform.WavesToMeasurementTransform.apply

```{autodoc2-docstring} abtem.transform.WavesToMeasurementTransform.apply
:parser: rst
```

````

`````

`````{py:class} WavesToWavesTransform(...)
:canonical: abtem.transform.WavesToWavesTransform

Bases: {py:obj}`abtem.transform.WavesTransform`

````{py:method} apply(...) -> abtem.waves.Waves
:canonical: abtem.transform.WavesToWavesTransform.apply

```{autodoc2-docstring} abtem.transform.WavesToWavesTransform.apply
:parser: rst
```

````

`````

`````{py:class} WavesTransform(...)
:canonical: abtem.transform.WavesTransform

Bases: {py:obj}`abtem.transform.EnsembleTransform`\[{py:obj}`abtem.waves.Waves`\, {py:obj}`abtem.array.ArrayObjectType`\]

````{py:method} apply(...) -> abtem.waves.Waves | abtem.array.ArrayObjectType | list[abtem.waves.Waves | abtem.array.ArrayObjectType]
:canonical: abtem.transform.WavesTransform.apply
:abstractmethod:

```{autodoc2-docstring} abtem.transform.WavesTransform.apply
:parser: rst
```

````

````{py:property} distributions
:canonical: abtem.transform.WavesTransform.distributions
:type: tuple[str, ...]

```{autodoc2-docstring} abtem.transform.WavesTransform.distributions
:parser: rst
```

````

`````

````{py:data} WavesType
:canonical: abtem.transform.WavesType
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.transform.WavesType
:parser: rst
```

````

````{py:function} join_tuples(...) -> tuple[typing.Any, ...]
:canonical: abtem.transform.join_tuples

```{autodoc2-docstring} abtem.transform.join_tuples
:parser: rst
```
````
