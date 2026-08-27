# {py:mod}`abtem.detectors`

```{py:module} abtem.detectors
```

```{autodoc2-docstring} abtem.detectors
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AnnularDetector <abtem.detectors.AnnularDetector>`
  - ```{autodoc2-docstring} abtem.detectors.AnnularDetector
    :summary:
    ```
* - {py:obj}`BaseDetector <abtem.detectors.BaseDetector>`
  - ```{autodoc2-docstring} abtem.detectors.BaseDetector
    :summary:
    ```
* - {py:obj}`FlexibleAnnularDetector <abtem.detectors.FlexibleAnnularDetector>`
  - ```{autodoc2-docstring} abtem.detectors.FlexibleAnnularDetector
    :summary:
    ```
* - {py:obj}`PixelatedDetector <abtem.detectors.PixelatedDetector>`
  - ```{autodoc2-docstring} abtem.detectors.PixelatedDetector
    :summary:
    ```
* - {py:obj}`SegmentedDetector <abtem.detectors.SegmentedDetector>`
  - ```{autodoc2-docstring} abtem.detectors.SegmentedDetector
    :summary:
    ```
* - {py:obj}`WavesDetector <abtem.detectors.WavesDetector>`
  - ```{autodoc2-docstring} abtem.detectors.WavesDetector
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`validate_detectors <abtem.detectors.validate_detectors>`
  - ```{autodoc2-docstring} abtem.detectors.validate_detectors
    :summary:
    ```
````

### API

`````{py:class} AnnularDetector(inner: float = 0.0, outer: typing.Optional[float] = None, offset: tuple[float, float] = (0.0, 0.0), to_cpu: bool = True, url: typing.Optional[str] = None)
:canonical: abtem.detectors.AnnularDetector

Bases: {py:obj}`abtem.detectors._AbstractRadialDetector`

```{autodoc2-docstring} abtem.detectors.AnnularDetector
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.AnnularDetector.__init__
```

````{py:method} angular_limits(waves: abtem.waves.BaseWaves) -> tuple[float, float]
:canonical: abtem.detectors.AnnularDetector.angular_limits

````

````{py:property} azimuthal_sampling
:canonical: abtem.detectors.AnnularDetector.azimuthal_sampling
:type: float

````

````{py:method} detect(waves: abtem.transform.WavesType) -> abtem.measurements.Images | abtem.measurements.RealSpaceLineProfiles | abtem.measurements.MeasurementsEnsemble
:canonical: abtem.detectors.AnnularDetector.detect

```{autodoc2-docstring} abtem.detectors.AnnularDetector.detect
```

````

````{py:method} get_detector_region(waves: abtem.waves.BaseWaves, fftshift: bool = True)
:canonical: abtem.detectors.AnnularDetector.get_detector_region

```{autodoc2-docstring} abtem.detectors.AnnularDetector.get_detector_region
```

````

````{py:property} inner
:canonical: abtem.detectors.AnnularDetector.inner
:type: float

```{autodoc2-docstring} abtem.detectors.AnnularDetector.inner
```

````

````{py:property} nbins_azimuthal
:canonical: abtem.detectors.AnnularDetector.nbins_azimuthal

````

````{py:property} nbins_radial
:canonical: abtem.detectors.AnnularDetector.nbins_radial

````

````{py:property} offset
:canonical: abtem.detectors.AnnularDetector.offset
:type: tuple[float, float]

```{autodoc2-docstring} abtem.detectors.AnnularDetector.offset
```

````

````{py:property} outer
:canonical: abtem.detectors.AnnularDetector.outer
:type: float | None

```{autodoc2-docstring} abtem.detectors.AnnularDetector.outer
```

````

````{py:property} radial_sampling
:canonical: abtem.detectors.AnnularDetector.radial_sampling
:type: float

````

`````

`````{py:class} BaseDetector(to_cpu: bool = True, url: typing.Optional[str] = None)
:canonical: abtem.detectors.BaseDetector

Bases: {py:obj}`abtem.transform.ArrayObjectTransform`\[{py:obj}`abtem.waves.Waves`\, {py:obj}`abtem.measurements.BaseMeasurements | abtem.waves.Waves`\]

```{autodoc2-docstring} abtem.detectors.BaseDetector
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.BaseDetector.__init__
```

````{py:method} angular_limits(waves: abtem.waves.Waves) -> tuple[float, float]
:canonical: abtem.detectors.BaseDetector.angular_limits
:abstractmethod:

```{autodoc2-docstring} abtem.detectors.BaseDetector.angular_limits
```

````

````{py:method} apply(waves: abtem.waves.Waves, max_batch: int | str = 'auto') -> abtem.measurements.BaseMeasurements | abtem.waves.Waves
:canonical: abtem.detectors.BaseDetector.apply

```{autodoc2-docstring} abtem.detectors.BaseDetector.apply
```

````

````{py:method} detect(waves: abtem.waves.Waves) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves
:canonical: abtem.detectors.BaseDetector.detect

```{autodoc2-docstring} abtem.detectors.BaseDetector.detect
```

````

````{py:property} to_cpu
:canonical: abtem.detectors.BaseDetector.to_cpu
:type: bool

```{autodoc2-docstring} abtem.detectors.BaseDetector.to_cpu
```

````

````{py:property} url
:canonical: abtem.detectors.BaseDetector.url
:type: typing.Optional[str]

```{autodoc2-docstring} abtem.detectors.BaseDetector.url
```

````

`````

`````{py:class} FlexibleAnnularDetector(step_size: float = 1.0, inner: float = 0.0, outer: typing.Optional[float] = None, to_cpu: bool = True, url: typing.Optional[str] = None)
:canonical: abtem.detectors.FlexibleAnnularDetector

Bases: {py:obj}`abtem.detectors._AbstractRadialDetector`

```{autodoc2-docstring} abtem.detectors.FlexibleAnnularDetector
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.FlexibleAnnularDetector.__init__
```

````{py:property} azimuthal_sampling
:canonical: abtem.detectors.FlexibleAnnularDetector.azimuthal_sampling
:type: float

````

````{py:method} detect(waves: abtem.waves.Waves) -> abtem.measurements.PolarMeasurements
:canonical: abtem.detectors.FlexibleAnnularDetector.detect

````

````{py:property} nbins_azimuthal
:canonical: abtem.detectors.FlexibleAnnularDetector.nbins_azimuthal

````

````{py:property} nbins_radial
:canonical: abtem.detectors.FlexibleAnnularDetector.nbins_radial

````

````{py:property} radial_sampling
:canonical: abtem.detectors.FlexibleAnnularDetector.radial_sampling
:type: float

````

````{py:property} step_size
:canonical: abtem.detectors.FlexibleAnnularDetector.step_size
:type: float

```{autodoc2-docstring} abtem.detectors.FlexibleAnnularDetector.step_size
```

````

`````

`````{py:class} PixelatedDetector(max_angle: str | float = 'valid', resample: str | tuple[float, float] | bool = False, reciprocal_space: bool = True, to_cpu: bool = True, url: typing.Optional[str] = None)
:canonical: abtem.detectors.PixelatedDetector

Bases: {py:obj}`abtem.detectors.BaseDetector`

```{autodoc2-docstring} abtem.detectors.PixelatedDetector
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.PixelatedDetector.__init__
```

````{py:method} angular_limits(waves: abtem.waves.Waves) -> tuple[float, float]
:canonical: abtem.detectors.PixelatedDetector.angular_limits

````

````{py:method} detect(waves: abtem.transform.WavesType) -> abtem.measurements.DiffractionPatterns | abtem.measurements.Images
:canonical: abtem.detectors.PixelatedDetector.detect

```{autodoc2-docstring} abtem.detectors.PixelatedDetector.detect
```

````

````{py:property} max_angle
:canonical: abtem.detectors.PixelatedDetector.max_angle
:type: str | float

```{autodoc2-docstring} abtem.detectors.PixelatedDetector.max_angle
```

````

````{py:property} reciprocal_space
:canonical: abtem.detectors.PixelatedDetector.reciprocal_space
:type: bool

```{autodoc2-docstring} abtem.detectors.PixelatedDetector.reciprocal_space
```

````

````{py:property} resample
:canonical: abtem.detectors.PixelatedDetector.resample
:type: str | bool | tuple[float, float]

```{autodoc2-docstring} abtem.detectors.PixelatedDetector.resample
```

````

`````

`````{py:class} SegmentedDetector(nbins_radial: int, nbins_azimuthal: int, inner: float, outer: float, rotation: float = 0.0, offset: tuple[float, float] = (0.0, 0.0), to_cpu: bool = False, url: typing.Optional[str] = None)
:canonical: abtem.detectors.SegmentedDetector

Bases: {py:obj}`abtem.detectors._AbstractRadialDetector`

```{autodoc2-docstring} abtem.detectors.SegmentedDetector
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.SegmentedDetector.__init__
```

````{py:property} azimuthal_sampling
:canonical: abtem.detectors.SegmentedDetector.azimuthal_sampling

````

````{py:property} nbins_azimuthal
:canonical: abtem.detectors.SegmentedDetector.nbins_azimuthal
:type: int

```{autodoc2-docstring} abtem.detectors.SegmentedDetector.nbins_azimuthal
```

````

````{py:property} nbins_radial
:canonical: abtem.detectors.SegmentedDetector.nbins_radial
:type: int

```{autodoc2-docstring} abtem.detectors.SegmentedDetector.nbins_radial
```

````

````{py:property} radial_sampling
:canonical: abtem.detectors.SegmentedDetector.radial_sampling

````

````{py:property} rotation
:canonical: abtem.detectors.SegmentedDetector.rotation

````

`````

`````{py:class} WavesDetector(gpts: typing.Optional[tuple[int, int]] = None, to_cpu: bool = False, url: typing.Optional[str] = None)
:canonical: abtem.detectors.WavesDetector

Bases: {py:obj}`abtem.detectors.BaseDetector`

```{autodoc2-docstring} abtem.detectors.WavesDetector
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.WavesDetector.__init__
```

````{py:method} angular_limits(waves: abtem.waves.BaseWaves) -> tuple[float, float]
:canonical: abtem.detectors.WavesDetector.angular_limits

````

````{py:method} detect(waves: abtem.transform.WavesType) -> abtem.waves.Waves
:canonical: abtem.detectors.WavesDetector.detect

```{autodoc2-docstring} abtem.detectors.WavesDetector.detect
```

````

`````

````{py:function} validate_detectors(detectors: typing.Optional[BaseDetector | list[BaseDetector]] = None, waves: typing.Optional[abtem.waves.BaseWaves] = None) -> list[BaseDetector]
:canonical: abtem.detectors.validate_detectors

```{autodoc2-docstring} abtem.detectors.validate_detectors
```
````
