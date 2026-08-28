# {py:mod}`abtem.noise`

```{py:module} abtem.noise
```

```{autodoc2-docstring} abtem.noise
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`NoiseTransform <abtem.noise.NoiseTransform>`
  -
* - {py:obj}`ScanNoiseTransform <abtem.noise.ScanNoiseTransform>`
  -
````

### API

`````{py:class} NoiseTransform(dose: float | numpy.ndarray | abtem.distributions.BaseDistribution, samples: typing.Optional[int] = None, seeds: typing.Optional[int | tuple[int, ...]] = None)
:canonical: abtem.noise.NoiseTransform

Bases: {py:obj}`abtem.transform.EnsembleTransform`

````{py:method} apply(array_object: abtem.array.ArrayObject, max_batch: int | str = 'auto') -> abtem.array.ArrayObject
:canonical: abtem.noise.NoiseTransform.apply

```{autodoc2-docstring} abtem.noise.NoiseTransform.apply
:parser: rst
```

````

````{py:property} dose
:canonical: abtem.noise.NoiseTransform.dose
:type: float | numpy.ndarray | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.noise.NoiseTransform.dose
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.noise.NoiseTransform.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} metadata
:canonical: abtem.noise.NoiseTransform.metadata
:type: dict

````

````{py:property} samples
:canonical: abtem.noise.NoiseTransform.samples
:type: int

```{autodoc2-docstring} abtem.noise.NoiseTransform.samples
:parser: rst
```

````

````{py:property} seeds
:canonical: abtem.noise.NoiseTransform.seeds
:type: typing.Optional[abtem.distributions.BaseDistribution | int]

```{autodoc2-docstring} abtem.noise.NoiseTransform.seeds
:parser: rst
```

````

`````

`````{py:class} ScanNoiseTransform(rms_power: float | numpy.ndarray | abtem.distributions.BaseDistribution, dwell_time: float, flyback_time: float, samples: typing.Optional[int] = None, max_frequency: float = 500, num_components: int = 1000, seeds: typing.Optional[int | tuple[int, ...]] = None)
:canonical: abtem.noise.ScanNoiseTransform

Bases: {py:obj}`abtem.transform.EnsembleTransform`

````{py:property} dwell_time
:canonical: abtem.noise.ScanNoiseTransform.dwell_time
:type: float

```{autodoc2-docstring} abtem.noise.ScanNoiseTransform.dwell_time
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.noise.ScanNoiseTransform.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} flyback_time
:canonical: abtem.noise.ScanNoiseTransform.flyback_time
:type: float

```{autodoc2-docstring} abtem.noise.ScanNoiseTransform.flyback_time
:parser: rst
```

````

````{py:property} max_frequency
:canonical: abtem.noise.ScanNoiseTransform.max_frequency
:type: float

```{autodoc2-docstring} abtem.noise.ScanNoiseTransform.max_frequency
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.noise.ScanNoiseTransform.metadata
:type: dict

````

````{py:property} num_components
:canonical: abtem.noise.ScanNoiseTransform.num_components
:type: int

```{autodoc2-docstring} abtem.noise.ScanNoiseTransform.num_components
:parser: rst
```

````

````{py:property} rms_power
:canonical: abtem.noise.ScanNoiseTransform.rms_power
:type: float | numpy.ndarray | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.noise.ScanNoiseTransform.rms_power
:parser: rst
```

````

````{py:property} samples
:canonical: abtem.noise.ScanNoiseTransform.samples
:type: int

```{autodoc2-docstring} abtem.noise.ScanNoiseTransform.samples
:parser: rst
```

````

````{py:property} seeds
:canonical: abtem.noise.ScanNoiseTransform.seeds
:type: typing.Optional[abtem.distributions.BaseDistribution]

```{autodoc2-docstring} abtem.noise.ScanNoiseTransform.seeds
:parser: rst
```

````

`````
