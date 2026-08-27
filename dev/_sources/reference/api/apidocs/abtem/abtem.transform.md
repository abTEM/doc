# {py:mod}`abtem.transform`

```{py:module} abtem.transform
```

```{autodoc2-docstring} abtem.transform
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ArrayObjectTransform <abtem.transform.ArrayObjectTransform>`
  - ```{autodoc2-docstring} abtem.transform.ArrayObjectTransform
    :summary:
    ```
* - {py:obj}`EmptyTransform <abtem.transform.EmptyTransform>`
  - ```{autodoc2-docstring} abtem.transform.EmptyTransform
    :summary:
    ```
* - {py:obj}`EnsembleTransform <abtem.transform.EnsembleTransform>`
  -
* - {py:obj}`WavesTransform <abtem.transform.WavesTransform>`
  -
* - {py:obj}`WavesToMeasurementTransform <abtem.transform.WavesToMeasurementTransform>`
  -
* - {py:obj}`WavesToWavesTransform <abtem.transform.WavesToWavesTransform>`
  -
* - {py:obj}`TransformFromFunc <abtem.transform.TransformFromFunc>`
  - ```{autodoc2-docstring} abtem.transform.TransformFromFunc
    :summary:
    ```
* - {py:obj}`ReciprocalSpaceMultiplication <abtem.transform.ReciprocalSpaceMultiplication>`
  - ```{autodoc2-docstring} abtem.transform.ReciprocalSpaceMultiplication
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`join_tuples <abtem.transform.join_tuples>`
  - ```{autodoc2-docstring} abtem.transform.join_tuples
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`WavesType <abtem.transform.WavesType>`
  - ```{autodoc2-docstring} abtem.transform.WavesType
    :summary:
    ```
````

### API

````{py:data} WavesType
:canonical: abtem.transform.WavesType
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.transform.WavesType
```

````

`````{py:class} ArrayObjectTransform
:canonical: abtem.transform.ArrayObjectTransform

Bases: {py:obj}`typing.Generic`\[{py:obj}`abtem.array.ArrayObjectType`\, {py:obj}`abtem.array.ArrayObjectTypeAlt`\], {py:obj}`abtem.core.ensemble.Ensemble`, {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.transform.ArrayObjectTransform
```

````{py:property} metadata
:canonical: abtem.transform.ArrayObjectTransform.metadata
:type: dict

```{autodoc2-docstring} abtem.transform.ArrayObjectTransform.metadata
```

````

````{py:property} ensemble_shape
:canonical: abtem.transform.ArrayObjectTransform.ensemble_shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.transform.ArrayObjectTransform.ensemble_shape
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.transform.ArrayObjectTransform.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.transform.ArrayObjectTransform.ensemble_axes_metadata
```

````

````{py:method} apply(array_object: abtem.array.ArrayObjectType, max_batch: int | str = 'auto') -> abtem.array.ArrayObjectType | abtem.array.ArrayObjectTypeAlt | list[abtem.array.ArrayObjectType | abtem.array.ArrayObjectTypeAlt]
:canonical: abtem.transform.ArrayObjectTransform.apply
:abstractmethod:

```{autodoc2-docstring} abtem.transform.ArrayObjectTransform.apply
```

````

`````

`````{py:class} EmptyTransform
:canonical: abtem.transform.EmptyTransform

Bases: {py:obj}`abtem.core.ensemble.EmptyEnsemble`, {py:obj}`abtem.transform.ArrayObjectTransform`\[{py:obj}`abtem.array.ArrayObject`\, {py:obj}`abtem.array.ArrayObject`\]

```{autodoc2-docstring} abtem.transform.EmptyTransform
```

````{py:method} apply(array_object: abtem.array.ArrayObject, max_batch: int | str = 'auto') -> abtem.array.ArrayObject
:canonical: abtem.transform.EmptyTransform.apply

```{autodoc2-docstring} abtem.transform.EmptyTransform.apply
```

````

`````

```{py:class} EnsembleTransform(distributions: tuple[str, ...] = ())
:canonical: abtem.transform.EnsembleTransform

Bases: {py:obj}`abtem.distributions.EnsembleFromDistributions`, {py:obj}`abtem.transform.ArrayObjectTransform`\[{py:obj}`abtem.array.ArrayObjectType`\, {py:obj}`abtem.array.ArrayObjectTypeAlt`\]

```

`````{py:class} WavesTransform(distributions: tuple[str, ...] = ())
:canonical: abtem.transform.WavesTransform

Bases: {py:obj}`abtem.transform.EnsembleTransform`\[{py:obj}`abtem.waves.Waves`\, {py:obj}`abtem.array.ArrayObjectType`\]

````{py:property} distributions
:canonical: abtem.transform.WavesTransform.distributions
:type: tuple[str, ...]

```{autodoc2-docstring} abtem.transform.WavesTransform.distributions
```

````

````{py:method} apply(waves: abtem.waves.Waves, max_batch: int | str = 'auto') -> abtem.waves.Waves | abtem.array.ArrayObjectType | list[abtem.waves.Waves | abtem.array.ArrayObjectType]
:canonical: abtem.transform.WavesTransform.apply
:abstractmethod:

```{autodoc2-docstring} abtem.transform.WavesTransform.apply
```

````

`````

`````{py:class} WavesToMeasurementTransform(distributions: tuple[str, ...] = ())
:canonical: abtem.transform.WavesToMeasurementTransform

Bases: {py:obj}`abtem.transform.WavesTransform`\[{py:obj}`abtem.measurements.BaseMeasurements`\]

````{py:method} apply(waves: abtem.waves.Waves, max_batch: int | str = 'auto') -> abtem.waves.Waves | abtem.measurements.BaseMeasurements | list[abtem.waves.Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.transform.WavesToMeasurementTransform.apply

```{autodoc2-docstring} abtem.transform.WavesToMeasurementTransform.apply
```

````

`````

`````{py:class} WavesToWavesTransform(distributions: tuple[str, ...] = ())
:canonical: abtem.transform.WavesToWavesTransform

Bases: {py:obj}`abtem.transform.WavesTransform`

````{py:method} apply(waves: abtem.waves.Waves, max_batch: int | str = 'auto') -> abtem.waves.Waves
:canonical: abtem.transform.WavesToWavesTransform.apply

```{autodoc2-docstring} abtem.transform.WavesToWavesTransform.apply
```

````

`````

`````{py:class} TransformFromFunc(func, func_kwargs)
:canonical: abtem.transform.TransformFromFunc

Bases: {py:obj}`abtem.transform.ArrayObjectTransform`\[{py:obj}`abtem.array.ArrayObject`\, {py:obj}`abtem.array.ArrayObject`\]

```{autodoc2-docstring} abtem.transform.TransformFromFunc
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transform.TransformFromFunc.__init__
```

````{py:property} ensemble_shape
:canonical: abtem.transform.TransformFromFunc.ensemble_shape
:type: tuple[int, ...]

````

````{py:property} func
:canonical: abtem.transform.TransformFromFunc.func

```{autodoc2-docstring} abtem.transform.TransformFromFunc.func
```

````

````{py:property} func_kwargs
:canonical: abtem.transform.TransformFromFunc.func_kwargs

```{autodoc2-docstring} abtem.transform.TransformFromFunc.func_kwargs
```

````

````{py:method} apply(array_object: abtem.array.ArrayObjectType, max_batch: int | str = 'auto') -> abtem.array.ArrayObjectType
:canonical: abtem.transform.TransformFromFunc.apply

```{autodoc2-docstring} abtem.transform.TransformFromFunc.apply
```

````

`````

````{py:function} join_tuples(tuples: tuple[tuple[typing.Any, ...], ...]) -> tuple[typing.Any, ...]
:canonical: abtem.transform.join_tuples

```{autodoc2-docstring} abtem.transform.join_tuples
```
````

`````{py:class} ReciprocalSpaceMultiplication(in_place: bool = False, distributions: tuple[str, ...] = ())
:canonical: abtem.transform.ReciprocalSpaceMultiplication

Bases: {py:obj}`abtem.transform.WavesToWavesTransform`

```{autodoc2-docstring} abtem.transform.ReciprocalSpaceMultiplication
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transform.ReciprocalSpaceMultiplication.__init__
```

````{py:property} in_place
:canonical: abtem.transform.ReciprocalSpaceMultiplication.in_place
:type: bool

```{autodoc2-docstring} abtem.transform.ReciprocalSpaceMultiplication.in_place
```

````

`````
