# {py:mod}`abtem.multislice`

```{py:module} abtem.multislice
```

```{autodoc2-docstring} abtem.multislice
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FourierMultislice <abtem.multislice.FourierMultislice>`
  - ```{autodoc2-docstring} abtem.multislice.FourierMultislice
    :parser: rst
    :summary:
    ```
* - {py:obj}`FresnelPropagator <abtem.multislice.FresnelPropagator>`
  - ```{autodoc2-docstring} abtem.multislice.FresnelPropagator
    :parser: rst
    :summary:
    ```
* - {py:obj}`MultisliceTransform <abtem.multislice.MultisliceTransform>`
  - ```{autodoc2-docstring} abtem.multislice.MultisliceTransform
    :parser: rst
    :summary:
    ```
* - {py:obj}`RealSpaceMultislice <abtem.multislice.RealSpaceMultislice>`
  - ```{autodoc2-docstring} abtem.multislice.RealSpaceMultislice
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`allocate_measurement <abtem.multislice.allocate_measurement>`
  - ```{autodoc2-docstring} abtem.multislice.allocate_measurement
    :parser: rst
    :summary:
    ```
* - {py:obj}`allocate_multislice_measurements <abtem.multislice.allocate_multislice_measurements>`
  - ```{autodoc2-docstring} abtem.multislice.allocate_multislice_measurements
    :parser: rst
    :summary:
    ```
* - {py:obj}`conventional_multislice_step <abtem.multislice.conventional_multislice_step>`
  - ```{autodoc2-docstring} abtem.multislice.conventional_multislice_step
    :parser: rst
    :summary:
    ```
* - {py:obj}`is_waves_base_measurements_or_list <abtem.multislice.is_waves_base_measurements_or_list>`
  - ```{autodoc2-docstring} abtem.multislice.is_waves_base_measurements_or_list
    :parser: rst
    :summary:
    ```
* - {py:obj}`lookahead <abtem.multislice.lookahead>`
  - ```{autodoc2-docstring} abtem.multislice.lookahead
    :parser: rst
    :summary:
    ```
* - {py:obj}`multislice_and_detect <abtem.multislice.multislice_and_detect>`
  - ```{autodoc2-docstring} abtem.multislice.multislice_and_detect
    :parser: rst
    :summary:
    ```
* - {py:obj}`transition_potential_multislice_and_detect <abtem.multislice.transition_potential_multislice_and_detect>`
  - ```{autodoc2-docstring} abtem.multislice.transition_potential_multislice_and_detect
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} FourierMultislice
:canonical: abtem.multislice.FourierMultislice

```{autodoc2-docstring} abtem.multislice.FourierMultislice
:parser: rst
```

````{py:attribute} conjugate
:canonical: abtem.multislice.FourierMultislice.conjugate
:type: bool
:value: >
   False

```{autodoc2-docstring} abtem.multislice.FourierMultislice.conjugate
:parser: rst
```

````

````{py:attribute} expansion_scope
:canonical: abtem.multislice.FourierMultislice.expansion_scope
:type: typing.Literal[propagator]
:value: >
   'propagator'

```{autodoc2-docstring} abtem.multislice.FourierMultislice.expansion_scope
:parser: rst
```

````

````{py:attribute} order
:canonical: abtem.multislice.FourierMultislice.order
:type: typing.Literal[1, 2, exact]
:value: >
   'exact'

```{autodoc2-docstring} abtem.multislice.FourierMultislice.order
:parser: rst
```

````

````{py:attribute} transpose
:canonical: abtem.multislice.FourierMultislice.transpose
:type: bool
:value: >
   False

```{autodoc2-docstring} abtem.multislice.FourierMultislice.transpose
:parser: rst
```

````

`````

`````{py:class} FresnelPropagator()
:canonical: abtem.multislice.FresnelPropagator

```{autodoc2-docstring} abtem.multislice.FresnelPropagator
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.multislice.FresnelPropagator.__init__
:parser: rst
```

````{py:method} get_array(...) -> numpy.ndarray
:canonical: abtem.multislice.FresnelPropagator.get_array

```{autodoc2-docstring} abtem.multislice.FresnelPropagator.get_array
:parser: rst
```

````

````{py:method} propagate(...) -> abtem.waves.Waves
:canonical: abtem.multislice.FresnelPropagator.propagate

```{autodoc2-docstring} abtem.multislice.FresnelPropagator.propagate
:parser: rst
```

````

`````

`````{py:class} MultisliceTransform(...)
:canonical: abtem.multislice.MultisliceTransform

Bases: {py:obj}`abtem.transform.WavesTransform`\[{py:obj}`abtem.measurements.BaseMeasurements`\]

```{autodoc2-docstring} abtem.multislice.MultisliceTransform
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.multislice.MultisliceTransform.__init__
:parser: rst
```

````{py:method} apply(...) -> abtem.waves.Waves | abtem.measurements.BaseMeasurements | list[abtem.waves.Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.multislice.MultisliceTransform.apply

```{autodoc2-docstring} abtem.multislice.MultisliceTransform.apply
:parser: rst
```

````

````{py:property} detectors
:canonical: abtem.multislice.MultisliceTransform.detectors
:type: list[abtem.detectors.BaseDetector]

```{autodoc2-docstring} abtem.multislice.MultisliceTransform.detectors
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.multislice.MultisliceTransform.ensemble_axes_metadata

````

````{py:property} ensemble_shape
:canonical: abtem.multislice.MultisliceTransform.ensemble_shape

````

````{py:property} multislice_func
:canonical: abtem.multislice.MultisliceTransform.multislice_func
:type: typing.Callable

```{autodoc2-docstring} abtem.multislice.MultisliceTransform.multislice_func
:parser: rst
```

````

````{py:property} potential
:canonical: abtem.multislice.MultisliceTransform.potential
:type: abtem.potentials.iam.BasePotential

```{autodoc2-docstring} abtem.multislice.MultisliceTransform.potential
:parser: rst
```

````

`````

`````{py:class} RealSpaceMultislice
:canonical: abtem.multislice.RealSpaceMultislice

```{autodoc2-docstring} abtem.multislice.RealSpaceMultislice
:parser: rst
```

````{py:attribute} derivative_accuracy
:canonical: abtem.multislice.RealSpaceMultislice.derivative_accuracy
:type: int
:value: >
   6

```{autodoc2-docstring} abtem.multislice.RealSpaceMultislice.derivative_accuracy
:parser: rst
```

````

````{py:attribute} expansion_scope
:canonical: abtem.multislice.RealSpaceMultislice.expansion_scope
:type: typing.Literal[propagator, full]
:value: >
   'propagator'

```{autodoc2-docstring} abtem.multislice.RealSpaceMultislice.expansion_scope
:parser: rst
```

````

````{py:attribute} max_terms
:canonical: abtem.multislice.RealSpaceMultislice.max_terms
:type: int
:value: >
   80

```{autodoc2-docstring} abtem.multislice.RealSpaceMultislice.max_terms
:parser: rst
```

````

````{py:attribute} order
:canonical: abtem.multislice.RealSpaceMultislice.order
:type: int
:value: >
   1

```{autodoc2-docstring} abtem.multislice.RealSpaceMultislice.order
:parser: rst
```

````

`````

````{py:function} allocate_measurement(...) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves
:canonical: abtem.multislice.allocate_measurement

```{autodoc2-docstring} abtem.multislice.allocate_measurement
:parser: rst
```
````

````{py:function} allocate_multislice_measurements(...) -> list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
:canonical: abtem.multislice.allocate_multislice_measurements

```{autodoc2-docstring} abtem.multislice.allocate_multislice_measurements
:parser: rst
```
````

````{py:function} conventional_multislice_step(...) -> abtem.waves.Waves
:canonical: abtem.multislice.conventional_multislice_step

```{autodoc2-docstring} abtem.multislice.conventional_multislice_step
:parser: rst
```
````

````{py:function} is_waves_base_measurements_or_list(...) -> typing.TypeGuard[Waves | BaseMeasurements | list[Waves | BaseMeasurements]]
:canonical: abtem.multislice.is_waves_base_measurements_or_list

```{autodoc2-docstring} abtem.multislice.is_waves_base_measurements_or_list
:parser: rst
```
````

````{py:function} lookahead(...)
:canonical: abtem.multislice.lookahead

```{autodoc2-docstring} abtem.multislice.lookahead
:parser: rst
```
````

````{py:function} multislice_and_detect(...) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves | list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
:canonical: abtem.multislice.multislice_and_detect

```{autodoc2-docstring} abtem.multislice.multislice_and_detect
:parser: rst
```
````

````{py:function} transition_potential_multislice_and_detect(...) -> list[abtem.measurements.BaseMeasurements | abtem.waves.Waves] | abtem.measurements.BaseMeasurements | abtem.waves.Waves
:canonical: abtem.multislice.transition_potential_multislice_and_detect

```{autodoc2-docstring} abtem.multislice.transition_potential_multislice_and_detect
:parser: rst
```
````
