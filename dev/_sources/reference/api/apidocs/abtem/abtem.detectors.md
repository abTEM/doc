# {py:mod}`abtem.detectors`

```{py:module} abtem.detectors
```

```{autodoc2-docstring} abtem.detectors
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AnnularDetector <abtem.detectors.AnnularDetector>`
  - ```{autodoc2-docstring} abtem.detectors.AnnularDetector
    :parser: rst
    :summary:
    ```
* - {py:obj}`BaseDetector <abtem.detectors.BaseDetector>`
  - ```{autodoc2-docstring} abtem.detectors.BaseDetector
    :parser: rst
    :summary:
    ```
* - {py:obj}`FlexibleAnnularDetector <abtem.detectors.FlexibleAnnularDetector>`
  - ```{autodoc2-docstring} abtem.detectors.FlexibleAnnularDetector
    :parser: rst
    :summary:
    ```
* - {py:obj}`PixelatedDetector <abtem.detectors.PixelatedDetector>`
  - ```{autodoc2-docstring} abtem.detectors.PixelatedDetector
    :parser: rst
    :summary:
    ```
* - {py:obj}`SegmentedDetector <abtem.detectors.SegmentedDetector>`
  - ```{autodoc2-docstring} abtem.detectors.SegmentedDetector
    :parser: rst
    :summary:
    ```
* - {py:obj}`SpectralAnnularDetector <abtem.detectors.SpectralAnnularDetector>`
  - ```{autodoc2-docstring} abtem.detectors.SpectralAnnularDetector
    :parser: rst
    :summary:
    ```
* - {py:obj}`SpectralSlitDetector <abtem.detectors.SpectralSlitDetector>`
  - ```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector
    :parser: rst
    :summary:
    ```
* - {py:obj}`WavesDetector <abtem.detectors.WavesDetector>`
  - ```{autodoc2-docstring} abtem.detectors.WavesDetector
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`validate_detectors <abtem.detectors.validate_detectors>`
  - ```{autodoc2-docstring} abtem.detectors.validate_detectors
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} AnnularDetector(...)
:canonical: abtem.detectors.AnnularDetector

Bases: {py:obj}`abtem.detectors._AbstractRadialDetector`

```{autodoc2-docstring} abtem.detectors.AnnularDetector
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.AnnularDetector.__init__
:parser: rst
```

````{py:method} angular_limits(...) -> tuple[float, float]
:canonical: abtem.detectors.AnnularDetector.angular_limits

```{autodoc2-docstring} abtem.detectors.AnnularDetector.angular_limits
:parser: rst
```

````

````{py:property} azimuthal_sampling
:canonical: abtem.detectors.AnnularDetector.azimuthal_sampling
:type: float

````

````{py:method} detect(...) -> abtem.measurements.Images | abtem.measurements.RealSpaceLineProfiles | abtem.measurements.MeasurementsEnsemble
:canonical: abtem.detectors.AnnularDetector.detect

```{autodoc2-docstring} abtem.detectors.AnnularDetector.detect
:parser: rst
```

````

````{py:method} get_detector_region(...)
:canonical: abtem.detectors.AnnularDetector.get_detector_region

```{autodoc2-docstring} abtem.detectors.AnnularDetector.get_detector_region
:parser: rst
```

````

````{py:property} inner
:canonical: abtem.detectors.AnnularDetector.inner
:type: float

```{autodoc2-docstring} abtem.detectors.AnnularDetector.inner
:parser: rst
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
:parser: rst
```

````

````{py:property} outer
:canonical: abtem.detectors.AnnularDetector.outer
:type: float | None

```{autodoc2-docstring} abtem.detectors.AnnularDetector.outer
:parser: rst
```

````

````{py:property} radial_sampling
:canonical: abtem.detectors.AnnularDetector.radial_sampling
:type: float

````

`````

`````{py:class} BaseDetector(...)
:canonical: abtem.detectors.BaseDetector

Bases: {py:obj}`abtem.transform.ArrayObjectTransform`\[{py:obj}`abtem.waves.Waves`\, {py:obj}`abtem.measurements.BaseMeasurements | abtem.waves.Waves`\]

```{autodoc2-docstring} abtem.detectors.BaseDetector
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.BaseDetector.__init__
:parser: rst
```

````{py:method} apply(...) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves
:canonical: abtem.detectors.BaseDetector.apply

```{autodoc2-docstring} abtem.detectors.BaseDetector.apply
:parser: rst
```

````

````{py:method} detect(...) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves
:canonical: abtem.detectors.BaseDetector.detect

```{autodoc2-docstring} abtem.detectors.BaseDetector.detect
:parser: rst
```

````

````{py:property} to_cpu
:canonical: abtem.detectors.BaseDetector.to_cpu
:type: bool

```{autodoc2-docstring} abtem.detectors.BaseDetector.to_cpu
:parser: rst
```

````

````{py:property} url
:canonical: abtem.detectors.BaseDetector.url
:type: typing.Optional[str]

```{autodoc2-docstring} abtem.detectors.BaseDetector.url
:parser: rst
```

````

`````

`````{py:class} FlexibleAnnularDetector(...)
:canonical: abtem.detectors.FlexibleAnnularDetector

Bases: {py:obj}`abtem.detectors._AbstractRadialDetector`

```{autodoc2-docstring} abtem.detectors.FlexibleAnnularDetector
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.FlexibleAnnularDetector.__init__
:parser: rst
```

````{py:property} azimuthal_sampling
:canonical: abtem.detectors.FlexibleAnnularDetector.azimuthal_sampling
:type: float

````

````{py:method} detect(...) -> abtem.measurements.PolarMeasurements
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
:parser: rst
```

````

`````

`````{py:class} PixelatedDetector(...)
:canonical: abtem.detectors.PixelatedDetector

Bases: {py:obj}`abtem.detectors.BaseDetector`

```{autodoc2-docstring} abtem.detectors.PixelatedDetector
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.PixelatedDetector.__init__
:parser: rst
```

````{py:method} angular_limits(...) -> tuple[float, float]
:canonical: abtem.detectors.PixelatedDetector.angular_limits

```{autodoc2-docstring} abtem.detectors.PixelatedDetector.angular_limits
:parser: rst
```

````

````{py:method} detect(...) -> abtem.measurements.DiffractionPatterns | abtem.measurements.Images
:canonical: abtem.detectors.PixelatedDetector.detect

```{autodoc2-docstring} abtem.detectors.PixelatedDetector.detect
:parser: rst
```

````

````{py:property} max_angle
:canonical: abtem.detectors.PixelatedDetector.max_angle
:type: str | float

```{autodoc2-docstring} abtem.detectors.PixelatedDetector.max_angle
:parser: rst
```

````

````{py:property} reciprocal_space
:canonical: abtem.detectors.PixelatedDetector.reciprocal_space
:type: bool

```{autodoc2-docstring} abtem.detectors.PixelatedDetector.reciprocal_space
:parser: rst
```

````

````{py:property} resample
:canonical: abtem.detectors.PixelatedDetector.resample
:type: str | bool | tuple[float, float]

```{autodoc2-docstring} abtem.detectors.PixelatedDetector.resample
:parser: rst
```

````

`````

`````{py:class} SegmentedDetector(...)
:canonical: abtem.detectors.SegmentedDetector

Bases: {py:obj}`abtem.detectors._AbstractRadialDetector`

```{autodoc2-docstring} abtem.detectors.SegmentedDetector
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.SegmentedDetector.__init__
:parser: rst
```

````{py:property} azimuthal_sampling
:canonical: abtem.detectors.SegmentedDetector.azimuthal_sampling

````

````{py:property} nbins_azimuthal
:canonical: abtem.detectors.SegmentedDetector.nbins_azimuthal
:type: int

```{autodoc2-docstring} abtem.detectors.SegmentedDetector.nbins_azimuthal
:parser: rst
```

````

````{py:property} nbins_radial
:canonical: abtem.detectors.SegmentedDetector.nbins_radial
:type: int

```{autodoc2-docstring} abtem.detectors.SegmentedDetector.nbins_radial
:parser: rst
```

````

````{py:property} radial_sampling
:canonical: abtem.detectors.SegmentedDetector.radial_sampling

````

````{py:property} rotation
:canonical: abtem.detectors.SegmentedDetector.rotation

````

`````

`````{py:class} SpectralAnnularDetector(...)
:canonical: abtem.detectors.SpectralAnnularDetector

Bases: {py:obj}`abtem.detectors.AnnularDetector`

```{autodoc2-docstring} abtem.detectors.SpectralAnnularDetector
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.SpectralAnnularDetector.__init__
:parser: rst
```

````{py:property} q_max
:canonical: abtem.detectors.SpectralAnnularDetector.q_max
:type: typing.Optional[float]

```{autodoc2-docstring} abtem.detectors.SpectralAnnularDetector.q_max
:parser: rst
```

````

````{py:property} q_min
:canonical: abtem.detectors.SpectralAnnularDetector.q_min
:type: float

```{autodoc2-docstring} abtem.detectors.SpectralAnnularDetector.q_min
:parser: rst
```

````

````{py:property} q_sampling
:canonical: abtem.detectors.SpectralAnnularDetector.q_sampling
:type: typing.Optional[float]

```{autodoc2-docstring} abtem.detectors.SpectralAnnularDetector.q_sampling
:parser: rst
```

````

````{py:method} show(...)
:canonical: abtem.detectors.SpectralAnnularDetector.show

```{autodoc2-docstring} abtem.detectors.SpectralAnnularDetector.show
:parser: rst
```

````

````{py:property} sweep_angle
:canonical: abtem.detectors.SpectralAnnularDetector.sweep_angle
:type: float

```{autodoc2-docstring} abtem.detectors.SpectralAnnularDetector.sweep_angle
:parser: rst
```

````

`````

`````{py:class} SpectralSlitDetector(...)
:canonical: abtem.detectors.SpectralSlitDetector

Bases: {py:obj}`abtem.detectors.BaseDetector`

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector.__init__
:parser: rst
```

````{py:property} angle
:canonical: abtem.detectors.SpectralSlitDetector.angle
:type: float

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector.angle
:parser: rst
```

````

````{py:method} angular_limits(...) -> tuple[float, float]
:canonical: abtem.detectors.SpectralSlitDetector.angular_limits

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector.angular_limits
:parser: rst
```

````

````{py:property} corners
:canonical: abtem.detectors.SpectralSlitDetector.corners
:type: tuple[float, float, float, float]

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector.corners
:parser: rst
```

````

````{py:method} detect(...) -> abtem.measurements.Images | abtem.measurements.RealSpaceLineProfiles | abtem.measurements.MeasurementsEnsemble
:canonical: abtem.detectors.SpectralSlitDetector.detect

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector.detect
:parser: rst
```

````

````{py:property} extent
:canonical: abtem.detectors.SpectralSlitDetector.extent
:type: float

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector.extent
:parser: rst
```

````

````{py:method} get_detector_region(...)
:canonical: abtem.detectors.SpectralSlitDetector.get_detector_region

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector.get_detector_region
:parser: rst
```

````

````{py:property} offset
:canonical: abtem.detectors.SpectralSlitDetector.offset
:type: tuple[float, float]

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector.offset
:parser: rst
```

````

````{py:property} q_max
:canonical: abtem.detectors.SpectralSlitDetector.q_max
:type: float

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector.q_max
:parser: rst
```

````

````{py:property} q_min
:canonical: abtem.detectors.SpectralSlitDetector.q_min
:type: float

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector.q_min
:parser: rst
```

````

````{py:property} q_sampling
:canonical: abtem.detectors.SpectralSlitDetector.q_sampling
:type: typing.Optional[float]

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector.q_sampling
:parser: rst
```

````

````{py:method} show(...)
:canonical: abtem.detectors.SpectralSlitDetector.show

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector.show
:parser: rst
```

````

````{py:property} width
:canonical: abtem.detectors.SpectralSlitDetector.width
:type: float

```{autodoc2-docstring} abtem.detectors.SpectralSlitDetector.width
:parser: rst
```

````

`````

`````{py:class} WavesDetector(...)
:canonical: abtem.detectors.WavesDetector

Bases: {py:obj}`abtem.detectors.BaseDetector`

```{autodoc2-docstring} abtem.detectors.WavesDetector
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.detectors.WavesDetector.__init__
:parser: rst
```

````{py:method} angular_limits(...) -> tuple[float, float]
:canonical: abtem.detectors.WavesDetector.angular_limits

```{autodoc2-docstring} abtem.detectors.WavesDetector.angular_limits
:parser: rst
```

````

````{py:method} detect(...) -> abtem.waves.Waves
:canonical: abtem.detectors.WavesDetector.detect

```{autodoc2-docstring} abtem.detectors.WavesDetector.detect
:parser: rst
```

````

`````

````{py:function} validate_detectors(...) -> list[BaseDetector]
:canonical: abtem.detectors.validate_detectors

```{autodoc2-docstring} abtem.detectors.validate_detectors
:parser: rst
```
````
