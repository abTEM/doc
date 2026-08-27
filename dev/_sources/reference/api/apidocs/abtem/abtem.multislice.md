# {py:mod}`abtem.multislice`

```{py:module} abtem.multislice
```

```{autodoc2-docstring} abtem.multislice
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FresnelPropagator <abtem.multislice.FresnelPropagator>`
  - ```{autodoc2-docstring} abtem.multislice.FresnelPropagator
    :summary:
    ```
* - {py:obj}`FourierMultislice <abtem.multislice.FourierMultislice>`
  - ```{autodoc2-docstring} abtem.multislice.FourierMultislice
    :summary:
    ```
* - {py:obj}`RealSpaceMultislice <abtem.multislice.RealSpaceMultislice>`
  - ```{autodoc2-docstring} abtem.multislice.RealSpaceMultislice
    :summary:
    ```
* - {py:obj}`MultisliceTransform <abtem.multislice.MultisliceTransform>`
  - ```{autodoc2-docstring} abtem.multislice.MultisliceTransform
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`allocate_measurement <abtem.multislice.allocate_measurement>`
  - ```{autodoc2-docstring} abtem.multislice.allocate_measurement
    :summary:
    ```
* - {py:obj}`allocate_multislice_measurements <abtem.multislice.allocate_multislice_measurements>`
  - ```{autodoc2-docstring} abtem.multislice.allocate_multislice_measurements
    :summary:
    ```
* - {py:obj}`conventional_multislice_step <abtem.multislice.conventional_multislice_step>`
  - ```{autodoc2-docstring} abtem.multislice.conventional_multislice_step
    :summary:
    ```
* - {py:obj}`lookahead <abtem.multislice.lookahead>`
  - ```{autodoc2-docstring} abtem.multislice.lookahead
    :summary:
    ```
* - {py:obj}`multislice_and_detect <abtem.multislice.multislice_and_detect>`
  - ```{autodoc2-docstring} abtem.multislice.multislice_and_detect
    :summary:
    ```
* - {py:obj}`transition_potential_multislice_and_detect <abtem.multislice.transition_potential_multislice_and_detect>`
  - ```{autodoc2-docstring} abtem.multislice.transition_potential_multislice_and_detect
    :summary:
    ```
* - {py:obj}`is_waves_base_measurements_or_list <abtem.multislice.is_waves_base_measurements_or_list>`
  - ```{autodoc2-docstring} abtem.multislice.is_waves_base_measurements_or_list
    :summary:
    ```
````

### API

`````{py:class} FresnelPropagator()
:canonical: abtem.multislice.FresnelPropagator

```{autodoc2-docstring} abtem.multislice.FresnelPropagator
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.multislice.FresnelPropagator.__init__
```

````{py:method} get_array(waves: abtem.waves.Waves, thickness: float, order: int = 1) -> numpy.ndarray
:canonical: abtem.multislice.FresnelPropagator.get_array

```{autodoc2-docstring} abtem.multislice.FresnelPropagator.get_array
```

````

````{py:method} propagate(waves: abtem.waves.Waves, thickness: float, in_place: bool = False, order: int = 1) -> abtem.waves.Waves
:canonical: abtem.multislice.FresnelPropagator.propagate

```{autodoc2-docstring} abtem.multislice.FresnelPropagator.propagate
```

````

`````

````{py:function} allocate_measurement(waves: abtem.waves.Waves, detector: abtem.detectors.BaseDetector, extra_ensemble_axes_shape: tuple[int, ...], extra_ensemble_axes_metadata: list[abtem.core.axes.AxisMetadata]) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves
:canonical: abtem.multislice.allocate_measurement

```{autodoc2-docstring} abtem.multislice.allocate_measurement
```
````

````{py:function} allocate_multislice_measurements(waves: abtem.waves.Waves, detectors: list[abtem.detectors.BaseDetector], extra_ensemble_axes_shape: tuple[int, ...], extra_ensemble_axes_metadata: list[abtem.core.axes.AxisMetadata]) -> list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
:canonical: abtem.multislice.allocate_multislice_measurements

```{autodoc2-docstring} abtem.multislice.allocate_multislice_measurements
```
````

````{py:function} conventional_multislice_step(waves: abtem.waves.Waves, potential_slice: abtem.potentials.iam.PotentialArray | abtem.potentials.iam.TransmissionFunction, propagator: abtem.multislice.FresnelPropagator, antialias_aperture: abtem.antialias.AntialiasAperture, conjugate: bool = False, transpose: bool = False, order: int = 1) -> abtem.waves.Waves
:canonical: abtem.multislice.conventional_multislice_step

```{autodoc2-docstring} abtem.multislice.conventional_multislice_step
```
````

````{py:function} lookahead(iterable)
:canonical: abtem.multislice.lookahead

```{autodoc2-docstring} abtem.multislice.lookahead
```
````

`````{py:class} FourierMultislice
:canonical: abtem.multislice.FourierMultislice

```{autodoc2-docstring} abtem.multislice.FourierMultislice
```

````{py:attribute} order
:canonical: abtem.multislice.FourierMultislice.order
:type: typing.Literal[1, 2]
:value: >
   1

```{autodoc2-docstring} abtem.multislice.FourierMultislice.order
```

````

````{py:attribute} expansion_scope
:canonical: abtem.multislice.FourierMultislice.expansion_scope
:type: typing.Literal[propagator]
:value: >
   'propagator'

```{autodoc2-docstring} abtem.multislice.FourierMultislice.expansion_scope
```

````

````{py:attribute} conjugate
:canonical: abtem.multislice.FourierMultislice.conjugate
:type: bool
:value: >
   False

```{autodoc2-docstring} abtem.multislice.FourierMultislice.conjugate
```

````

````{py:attribute} transpose
:canonical: abtem.multislice.FourierMultislice.transpose
:type: bool
:value: >
   False

```{autodoc2-docstring} abtem.multislice.FourierMultislice.transpose
```

````

`````

`````{py:class} RealSpaceMultislice
:canonical: abtem.multislice.RealSpaceMultislice

```{autodoc2-docstring} abtem.multislice.RealSpaceMultislice
```

````{py:attribute} order
:canonical: abtem.multislice.RealSpaceMultislice.order
:type: int
:value: >
   1

```{autodoc2-docstring} abtem.multislice.RealSpaceMultislice.order
```

````

````{py:attribute} expansion_scope
:canonical: abtem.multislice.RealSpaceMultislice.expansion_scope
:type: typing.Literal[propagator, full]
:value: >
   'propagator'

```{autodoc2-docstring} abtem.multislice.RealSpaceMultislice.expansion_scope
```

````

````{py:attribute} derivative_accuracy
:canonical: abtem.multislice.RealSpaceMultislice.derivative_accuracy
:type: int
:value: >
   6

```{autodoc2-docstring} abtem.multislice.RealSpaceMultislice.derivative_accuracy
```

````

````{py:attribute} max_terms
:canonical: abtem.multislice.RealSpaceMultislice.max_terms
:type: int
:value: >
   80

```{autodoc2-docstring} abtem.multislice.RealSpaceMultislice.max_terms
```

````

`````

````{py:function} multislice_and_detect(waves: abtem.waves.Waves, potential: abtem.potentials.iam.BasePotential, detectors: typing.Optional[list[abtem.detectors.BaseDetector]] = None, algorithm: abtem.multislice.FourierMultislice | abtem.multislice.RealSpaceMultislice = FourierMultislice(), return_backscattered: bool = False, pbar: bool = False) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves | list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
:canonical: abtem.multislice.multislice_and_detect

```{autodoc2-docstring} abtem.multislice.multislice_and_detect
```
````

````{py:function} transition_potential_multislice_and_detect(waves: abtem.waves.Waves, potential: abtem.potentials.iam.BasePotential, transition_potential: abtem.inelastic.core_loss.TransitionPotential | abtem.inelastic.core_loss.TransitionPotentialArray, detectors: typing.Optional[list[abtem.detectors.BaseDetector]] = None, detectors_elastic: typing.Optional[list[abtem.detectors.BaseDetector]] = None, double_channel: bool = True, threshold: float = 1.0, sites: typing.Optional[abtem.slicing.SliceIndexedAtoms | ase.Atoms] = None, algorithm: abtem.multislice.FourierMultislice | abtem.multislice.RealSpaceMultislice = FourierMultislice(), scatter_max_batch: int | str = 1, pbar: bool = False) -> list[abtem.measurements.BaseMeasurements | abtem.waves.Waves] | abtem.measurements.BaseMeasurements | abtem.waves.Waves
:canonical: abtem.multislice.transition_potential_multislice_and_detect

```{autodoc2-docstring} abtem.multislice.transition_potential_multislice_and_detect
```
````

````{py:function} is_waves_base_measurements_or_list(value: typing.Any) -> typing.TypeGuard[Waves | BaseMeasurements | list[Waves | BaseMeasurements]]
:canonical: abtem.multislice.is_waves_base_measurements_or_list

```{autodoc2-docstring} abtem.multislice.is_waves_base_measurements_or_list
```
````

`````{py:class} MultisliceTransform(potential: abtem.potentials.iam.BasePotential, detectors: typing.Optional[abtem.detectors.BaseDetector | list[abtem.detectors.BaseDetector]] = None, multislice_func: typing.Optional[typing.Callable] = None, **multislice_func_kwargs)
:canonical: abtem.multislice.MultisliceTransform

Bases: {py:obj}`abtem.transform.WavesTransform`\[{py:obj}`abtem.measurements.BaseMeasurements`\]

```{autodoc2-docstring} abtem.multislice.MultisliceTransform
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.multislice.MultisliceTransform.__init__
```

````{py:property} multislice_func
:canonical: abtem.multislice.MultisliceTransform.multislice_func
:type: typing.Callable

```{autodoc2-docstring} abtem.multislice.MultisliceTransform.multislice_func
```

````

````{py:property} potential
:canonical: abtem.multislice.MultisliceTransform.potential
:type: abtem.potentials.iam.BasePotential

```{autodoc2-docstring} abtem.multislice.MultisliceTransform.potential
```

````

````{py:property} detectors
:canonical: abtem.multislice.MultisliceTransform.detectors
:type: list[abtem.detectors.BaseDetector]

```{autodoc2-docstring} abtem.multislice.MultisliceTransform.detectors
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.multislice.MultisliceTransform.ensemble_axes_metadata

````

````{py:property} ensemble_shape
:canonical: abtem.multislice.MultisliceTransform.ensemble_shape

````

````{py:method} apply(waves: abtem.waves.Waves, max_batch: int | str = 'auto') -> abtem.waves.Waves | abtem.measurements.BaseMeasurements | list[abtem.waves.Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.multislice.MultisliceTransform.apply

```{autodoc2-docstring} abtem.multislice.MultisliceTransform.apply
```

````

`````
