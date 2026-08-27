# {py:mod}`abtem.core.axes`

```{py:module} abtem.core.axes
```

```{autodoc2-docstring} abtem.core.axes
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AxesMetadataList <abtem.core.axes.AxesMetadataList>`
  -
* - {py:obj}`AxisAlignedTiltAxis <abtem.core.axes.AxisAlignedTiltAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.AxisAlignedTiltAxis
    :summary:
    ```
* - {py:obj}`AxisMetadata <abtem.core.axes.AxisMetadata>`
  - ```{autodoc2-docstring} abtem.core.axes.AxisMetadata
    :summary:
    ```
* - {py:obj}`FrozenPhononsAxis <abtem.core.axes.FrozenPhononsAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.FrozenPhononsAxis
    :summary:
    ```
* - {py:obj}`LinearAxis <abtem.core.axes.LinearAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.LinearAxis
    :summary:
    ```
* - {py:obj}`NonLinearAxis <abtem.core.axes.NonLinearAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.NonLinearAxis
    :summary:
    ```
* - {py:obj}`OrdinalAxis <abtem.core.axes.OrdinalAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.OrdinalAxis
    :summary:
    ```
* - {py:obj}`ParameterAxis <abtem.core.axes.ParameterAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.ParameterAxis
    :summary:
    ```
* - {py:obj}`PositionsAxis <abtem.core.axes.PositionsAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.PositionsAxis
    :summary:
    ```
* - {py:obj}`PrismPlaneWavesAxis <abtem.core.axes.PrismPlaneWavesAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.PrismPlaneWavesAxis
    :summary:
    ```
* - {py:obj}`RealSpaceAxis <abtem.core.axes.RealSpaceAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.RealSpaceAxis
    :summary:
    ```
* - {py:obj}`ReciprocalSpaceAxis <abtem.core.axes.ReciprocalSpaceAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.ReciprocalSpaceAxis
    :summary:
    ```
* - {py:obj}`SampleAxis <abtem.core.axes.SampleAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.SampleAxis
    :summary:
    ```
* - {py:obj}`ScaleAxis <abtem.core.axes.ScaleAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.ScaleAxis
    :summary:
    ```
* - {py:obj}`ScanAxis <abtem.core.axes.ScanAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.ScanAxis
    :summary:
    ```
* - {py:obj}`ThicknessAxis <abtem.core.axes.ThicknessAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.ThicknessAxis
    :summary:
    ```
* - {py:obj}`TiltAxis <abtem.core.axes.TiltAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.TiltAxis
    :summary:
    ```
* - {py:obj}`UnknownAxis <abtem.core.axes.UnknownAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.UnknownAxis
    :summary:
    ```
* - {py:obj}`WaveVectorAxis <abtem.core.axes.WaveVectorAxis>`
  - ```{autodoc2-docstring} abtem.core.axes.WaveVectorAxis
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`axis_from_dict <abtem.core.axes.axis_from_dict>`
  - ```{autodoc2-docstring} abtem.core.axes.axis_from_dict
    :summary:
    ```
* - {py:obj}`axis_to_dict <abtem.core.axes.axis_to_dict>`
  - ```{autodoc2-docstring} abtem.core.axes.axis_to_dict
    :summary:
    ```
* - {py:obj}`format_axes_metadata <abtem.core.axes.format_axes_metadata>`
  - ```{autodoc2-docstring} abtem.core.axes.format_axes_metadata
    :summary:
    ```
* - {py:obj}`format_label <abtem.core.axes.format_label>`
  - ```{autodoc2-docstring} abtem.core.axes.format_label
    :summary:
    ```
* - {py:obj}`format_title <abtem.core.axes.format_title>`
  - ```{autodoc2-docstring} abtem.core.axes.format_title
    :summary:
    ```
* - {py:obj}`format_value <abtem.core.axes.format_value>`
  - ```{autodoc2-docstring} abtem.core.axes.format_value
    :summary:
    ```
* - {py:obj}`latex_float <abtem.core.axes.latex_float>`
  - ```{autodoc2-docstring} abtem.core.axes.latex_float
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`categories <abtem.core.axes.categories>`
  - ```{autodoc2-docstring} abtem.core.axes.categories
    :summary:
    ```
* - {py:obj}`complex_labels <abtem.core.axes.complex_labels>`
  - ```{autodoc2-docstring} abtem.core.axes.complex_labels
    :summary:
    ```
````

### API

```{py:class} AxesMetadataList(lst, shape)
:canonical: abtem.core.axes.AxesMetadataList

Bases: {py:obj}`list`

```

`````{py:class} AxisAlignedTiltAxis
:canonical: abtem.core.axes.AxisAlignedTiltAxis

Bases: {py:obj}`abtem.core.axes.NonLinearAxis`

```{autodoc2-docstring} abtem.core.axes.AxisAlignedTiltAxis
```

````{py:attribute} direction
:canonical: abtem.core.axes.AxisAlignedTiltAxis.direction
:type: str
:value: >
   'x'

```{autodoc2-docstring} abtem.core.axes.AxisAlignedTiltAxis.direction
```

````

````{py:method} item_metadata(item, metadata=None)
:canonical: abtem.core.axes.AxisAlignedTiltAxis.item_metadata

````

````{py:property} tilt
:canonical: abtem.core.axes.AxisAlignedTiltAxis.tilt

```{autodoc2-docstring} abtem.core.axes.AxisAlignedTiltAxis.tilt
```

````

````{py:attribute} units
:canonical: abtem.core.axes.AxisAlignedTiltAxis.units
:type: str
:value: >
   'mrad'

```{autodoc2-docstring} abtem.core.axes.AxisAlignedTiltAxis.units
```

````

`````

`````{py:class} AxisMetadata
:canonical: abtem.core.axes.AxisMetadata

```{autodoc2-docstring} abtem.core.axes.AxisMetadata
```

````{py:method} concatenate(other: abtem.core.axes.AxisMetadata) -> abtem.core.axes.AxisMetadata
:canonical: abtem.core.axes.AxisMetadata.concatenate

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.concatenate
```

````

````{py:method} coordinates(n: int) -> tuple
:canonical: abtem.core.axes.AxisMetadata.coordinates

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.coordinates
```

````

````{py:method} copy() -> abtem.core.axes.AxisMetadata
:canonical: abtem.core.axes.AxisMetadata.copy

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.copy
```

````

````{py:method} format_coordinates(n: typing.Optional[int] = None)
:canonical: abtem.core.axes.AxisMetadata.format_coordinates

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.format_coordinates
```

````

````{py:method} format_label(units: typing.Optional[str] = None) -> str
:canonical: abtem.core.axes.AxisMetadata.format_label

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.format_label
```

````

````{py:method} format_title(*args: typing.Any, **kwargs: typing.Any) -> str
:canonical: abtem.core.axes.AxisMetadata.format_title

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.format_title
```

````

````{py:method} format_type() -> str
:canonical: abtem.core.axes.AxisMetadata.format_type

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.format_type
```

````

````{py:method} from_dict(d) -> abtem.core.axes.AxisMetadata
:canonical: abtem.core.axes.AxisMetadata.from_dict
:staticmethod:

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.from_dict
```

````

````{py:method} item_metadata(item, metadata=None) -> dict
:canonical: abtem.core.axes.AxisMetadata.item_metadata

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.item_metadata
```

````

````{py:attribute} label
:canonical: abtem.core.axes.AxisMetadata.label
:type: str
:value: <Multiline-String>

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.label
```

````

````{py:method} limits(n=None) -> tuple
:canonical: abtem.core.axes.AxisMetadata.limits

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.limits
```

````

````{py:attribute} tex_label
:canonical: abtem.core.axes.AxisMetadata.tex_label
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.tex_label
```

````

````{py:attribute} tex_units
:canonical: abtem.core.axes.AxisMetadata.tex_units
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.tex_units
```

````

````{py:method} to_dict() -> dict
:canonical: abtem.core.axes.AxisMetadata.to_dict

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.to_dict
```

````

````{py:method} to_ordinal_axis(n)
:canonical: abtem.core.axes.AxisMetadata.to_ordinal_axis

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.to_ordinal_axis
```

````

````{py:attribute} units
:canonical: abtem.core.axes.AxisMetadata.units
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} abtem.core.axes.AxisMetadata.units
```

````

`````

`````{py:class} FrozenPhononsAxis
:canonical: abtem.core.axes.FrozenPhononsAxis

Bases: {py:obj}`abtem.core.axes.AxisMetadata`

```{autodoc2-docstring} abtem.core.axes.FrozenPhononsAxis
```

````{py:attribute} label
:canonical: abtem.core.axes.FrozenPhononsAxis.label
:type: str
:value: >
   'Frozen phonons'

```{autodoc2-docstring} abtem.core.axes.FrozenPhononsAxis.label
```

````

`````

`````{py:class} LinearAxis
:canonical: abtem.core.axes.LinearAxis

Bases: {py:obj}`abtem.core.axes.AxisMetadata`

```{autodoc2-docstring} abtem.core.axes.LinearAxis
```

````{py:method} convert_units(units: str, **kwargs)
:canonical: abtem.core.axes.LinearAxis.convert_units

```{autodoc2-docstring} abtem.core.axes.LinearAxis.convert_units
```

````

````{py:method} coordinates(n: int) -> tuple[float, ...]
:canonical: abtem.core.axes.LinearAxis.coordinates

```{autodoc2-docstring} abtem.core.axes.LinearAxis.coordinates
```

````

````{py:method} format_coordinates(n: typing.Optional[int] = None) -> str
:canonical: abtem.core.axes.LinearAxis.format_coordinates

```{autodoc2-docstring} abtem.core.axes.LinearAxis.format_coordinates
```

````

````{py:attribute} offset
:canonical: abtem.core.axes.LinearAxis.offset
:type: float
:value: >
   0.0

```{autodoc2-docstring} abtem.core.axes.LinearAxis.offset
```

````

````{py:attribute} sampling
:canonical: abtem.core.axes.LinearAxis.sampling
:type: float
:value: >
   1.0

```{autodoc2-docstring} abtem.core.axes.LinearAxis.sampling
```

````

````{py:method} to_ordinal_axis(n)
:canonical: abtem.core.axes.LinearAxis.to_ordinal_axis

```{autodoc2-docstring} abtem.core.axes.LinearAxis.to_ordinal_axis
```

````

````{py:attribute} units
:canonical: abtem.core.axes.LinearAxis.units
:type: str
:value: <Multiline-String>

```{autodoc2-docstring} abtem.core.axes.LinearAxis.units
```

````

`````

`````{py:class} NonLinearAxis
:canonical: abtem.core.axes.NonLinearAxis

Bases: {py:obj}`abtem.core.axes.OrdinalAxis`

```{autodoc2-docstring} abtem.core.axes.NonLinearAxis
```

````{py:method} format_coordinates(n: typing.Optional[int] = None)
:canonical: abtem.core.axes.NonLinearAxis.format_coordinates

```{autodoc2-docstring} abtem.core.axes.NonLinearAxis.format_coordinates
```

````

````{py:method} format_title(formatting: typing.Optional[str] = None, include_label: bool = True, **kwargs) -> str
:canonical: abtem.core.axes.NonLinearAxis.format_title

````

````{py:attribute} units
:canonical: abtem.core.axes.NonLinearAxis.units
:type: str
:value: >
   'unknown'

```{autodoc2-docstring} abtem.core.axes.NonLinearAxis.units
```

````

`````

`````{py:class} OrdinalAxis
:canonical: abtem.core.axes.OrdinalAxis

Bases: {py:obj}`abtem.core.axes.AxisMetadata`

```{autodoc2-docstring} abtem.core.axes.OrdinalAxis
```

````{py:method} concatenate(other: abtem.core.axes.AxisMetadata) -> abtem.core.axes.OrdinalAxis
:canonical: abtem.core.axes.OrdinalAxis.concatenate

````

````{py:method} coordinates(n: int) -> tuple
:canonical: abtem.core.axes.OrdinalAxis.coordinates

```{autodoc2-docstring} abtem.core.axes.OrdinalAxis.coordinates
```

````

````{py:method} format_all_titles() -> list[str]
:canonical: abtem.core.axes.OrdinalAxis.format_all_titles

```{autodoc2-docstring} abtem.core.axes.OrdinalAxis.format_all_titles
```

````

````{py:method} format_title(formatting: typing.Optional[str] = None, include_label: bool = True, **kwargs) -> str
:canonical: abtem.core.axes.OrdinalAxis.format_title

````

````{py:method} item_metadata(item, metadata=None)
:canonical: abtem.core.axes.OrdinalAxis.item_metadata

````

````{py:method} to_ordinal_axis(n) -> abtem.core.axes.OrdinalAxis
:canonical: abtem.core.axes.OrdinalAxis.to_ordinal_axis

```{autodoc2-docstring} abtem.core.axes.OrdinalAxis.to_ordinal_axis
```

````

````{py:attribute} values
:canonical: abtem.core.axes.OrdinalAxis.values
:type: tuple
:value: >
   ()

```{autodoc2-docstring} abtem.core.axes.OrdinalAxis.values
```

````

`````

`````{py:class} ParameterAxis
:canonical: abtem.core.axes.ParameterAxis

Bases: {py:obj}`abtem.core.axes.NonLinearAxis`

```{autodoc2-docstring} abtem.core.axes.ParameterAxis
```

````{py:attribute} label
:canonical: abtem.core.axes.ParameterAxis.label
:type: str
:value: <Multiline-String>

```{autodoc2-docstring} abtem.core.axes.ParameterAxis.label
```

````

`````

`````{py:class} PositionsAxis
:canonical: abtem.core.axes.PositionsAxis

Bases: {py:obj}`abtem.core.axes.OrdinalAxis`

```{autodoc2-docstring} abtem.core.axes.PositionsAxis
```

````{py:method} format_title(formatting: typing.Optional[str] = None, include_label: bool = True, **kwargs) -> str
:canonical: abtem.core.axes.PositionsAxis.format_title

````

````{py:attribute} label
:canonical: abtem.core.axes.PositionsAxis.label
:type: str
:value: >
   'x, y'

```{autodoc2-docstring} abtem.core.axes.PositionsAxis.label
```

````

````{py:attribute} units
:canonical: abtem.core.axes.PositionsAxis.units
:type: str
:value: >
   'Å'

```{autodoc2-docstring} abtem.core.axes.PositionsAxis.units
```

````

`````

````{py:class} PrismPlaneWavesAxis
:canonical: abtem.core.axes.PrismPlaneWavesAxis

Bases: {py:obj}`abtem.core.axes.AxisMetadata`

```{autodoc2-docstring} abtem.core.axes.PrismPlaneWavesAxis
```

````

`````{py:class} RealSpaceAxis
:canonical: abtem.core.axes.RealSpaceAxis

Bases: {py:obj}`abtem.core.axes.LinearAxis`

```{autodoc2-docstring} abtem.core.axes.RealSpaceAxis
```

````{py:attribute} endpoint
:canonical: abtem.core.axes.RealSpaceAxis.endpoint
:type: bool
:value: >
   True

```{autodoc2-docstring} abtem.core.axes.RealSpaceAxis.endpoint
```

````

````{py:attribute} sampling
:canonical: abtem.core.axes.RealSpaceAxis.sampling
:type: float
:value: >
   1.0

```{autodoc2-docstring} abtem.core.axes.RealSpaceAxis.sampling
```

````

````{py:attribute} units
:canonical: abtem.core.axes.RealSpaceAxis.units
:type: str
:value: >
   'pixels'

```{autodoc2-docstring} abtem.core.axes.RealSpaceAxis.units
```

````

`````

`````{py:class} ReciprocalSpaceAxis
:canonical: abtem.core.axes.ReciprocalSpaceAxis

Bases: {py:obj}`abtem.core.axes.LinearAxis`

```{autodoc2-docstring} abtem.core.axes.ReciprocalSpaceAxis
```

````{py:attribute} fftshift
:canonical: abtem.core.axes.ReciprocalSpaceAxis.fftshift
:type: bool
:value: >
   True

```{autodoc2-docstring} abtem.core.axes.ReciprocalSpaceAxis.fftshift
```

````

````{py:attribute} sampling
:canonical: abtem.core.axes.ReciprocalSpaceAxis.sampling
:type: float
:value: >
   1.0

```{autodoc2-docstring} abtem.core.axes.ReciprocalSpaceAxis.sampling
```

````

````{py:attribute} units
:canonical: abtem.core.axes.ReciprocalSpaceAxis.units
:type: str
:value: >
   'pixels'

```{autodoc2-docstring} abtem.core.axes.ReciprocalSpaceAxis.units
```

````

`````

````{py:class} SampleAxis
:canonical: abtem.core.axes.SampleAxis

Bases: {py:obj}`abtem.core.axes.AxisMetadata`

```{autodoc2-docstring} abtem.core.axes.SampleAxis
```

````

`````{py:class} ScaleAxis
:canonical: abtem.core.axes.ScaleAxis

```{autodoc2-docstring} abtem.core.axes.ScaleAxis
```

````{py:method} format_label()
:canonical: abtem.core.axes.ScaleAxis.format_label

```{autodoc2-docstring} abtem.core.axes.ScaleAxis.format_label
```

````

````{py:attribute} label
:canonical: abtem.core.axes.ScaleAxis.label
:type: str
:value: <Multiline-String>

```{autodoc2-docstring} abtem.core.axes.ScaleAxis.label
```

````

````{py:attribute} tex_label
:canonical: abtem.core.axes.ScaleAxis.tex_label
:type: str | None
:value: >
   None

```{autodoc2-docstring} abtem.core.axes.ScaleAxis.tex_label
```

````

````{py:attribute} units
:canonical: abtem.core.axes.ScaleAxis.units
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} abtem.core.axes.ScaleAxis.units
```

````

`````

````{py:class} ScanAxis
:canonical: abtem.core.axes.ScanAxis

Bases: {py:obj}`abtem.core.axes.RealSpaceAxis`

```{autodoc2-docstring} abtem.core.axes.ScanAxis
```

````

`````{py:class} ThicknessAxis
:canonical: abtem.core.axes.ThicknessAxis

Bases: {py:obj}`abtem.core.axes.NonLinearAxis`

```{autodoc2-docstring} abtem.core.axes.ThicknessAxis
```

````{py:attribute} label
:canonical: abtem.core.axes.ThicknessAxis.label
:type: str
:value: >
   'thickness'

```{autodoc2-docstring} abtem.core.axes.ThicknessAxis.label
```

````

````{py:attribute} units
:canonical: abtem.core.axes.ThicknessAxis.units
:type: str
:value: >
   'Å'

```{autodoc2-docstring} abtem.core.axes.ThicknessAxis.units
```

````

`````

`````{py:class} TiltAxis
:canonical: abtem.core.axes.TiltAxis

Bases: {py:obj}`abtem.core.axes.OrdinalAxis`

```{autodoc2-docstring} abtem.core.axes.TiltAxis
```

````{py:method} item_metadata(item, metadata=None)
:canonical: abtem.core.axes.TiltAxis.item_metadata

````

````{py:property} tilt
:canonical: abtem.core.axes.TiltAxis.tilt
:type: tuple

```{autodoc2-docstring} abtem.core.axes.TiltAxis.tilt
```

````

````{py:attribute} units
:canonical: abtem.core.axes.TiltAxis.units
:type: str
:value: >
   'mrad'

```{autodoc2-docstring} abtem.core.axes.TiltAxis.units
```

````

`````

`````{py:class} UnknownAxis
:canonical: abtem.core.axes.UnknownAxis

Bases: {py:obj}`abtem.core.axes.AxisMetadata`

```{autodoc2-docstring} abtem.core.axes.UnknownAxis
```

````{py:attribute} label
:canonical: abtem.core.axes.UnknownAxis.label
:type: str
:value: >
   'unknown'

```{autodoc2-docstring} abtem.core.axes.UnknownAxis.label
```

````

`````

`````{py:class} WaveVectorAxis
:canonical: abtem.core.axes.WaveVectorAxis

Bases: {py:obj}`abtem.core.axes.OrdinalAxis`

```{autodoc2-docstring} abtem.core.axes.WaveVectorAxis
```

````{py:attribute} units
:canonical: abtem.core.axes.WaveVectorAxis.units
:type: str
:value: >
   '1/Å'

```{autodoc2-docstring} abtem.core.axes.WaveVectorAxis.units
```

````

`````

````{py:function} axis_from_dict(d)
:canonical: abtem.core.axes.axis_from_dict

```{autodoc2-docstring} abtem.core.axes.axis_from_dict
```
````

````{py:function} axis_to_dict(axis: abtem.core.axes.AxisMetadata)
:canonical: abtem.core.axes.axis_to_dict

```{autodoc2-docstring} abtem.core.axes.axis_to_dict
```
````

````{py:data} categories
:canonical: abtem.core.axes.categories
:value: >
   None

```{autodoc2-docstring} abtem.core.axes.categories
```

````

````{py:data} complex_labels
:canonical: abtem.core.axes.complex_labels
:value: >
   None

```{autodoc2-docstring} abtem.core.axes.complex_labels
```

````

````{py:function} format_axes_metadata(axes_metadata, shape)
:canonical: abtem.core.axes.format_axes_metadata

```{autodoc2-docstring} abtem.core.axes.format_axes_metadata
```
````

````{py:function} format_label(axes: AxisMetadata, units: typing.Optional[str] = None) -> str
:canonical: abtem.core.axes.format_label

```{autodoc2-docstring} abtem.core.axes.format_label
```
````

````{py:function} format_title(axes: OrdinalAxis, formatting: typing.Optional[str] = None, units: typing.Optional[str] = None, include_label: bool = True) -> str
:canonical: abtem.core.axes.format_title

```{autodoc2-docstring} abtem.core.axes.format_title
```
````

````{py:function} format_value(value: numbers.Number | tuple, formatting: str, tolerance: float = 1e-14) -> str
:canonical: abtem.core.axes.format_value

```{autodoc2-docstring} abtem.core.axes.format_value
```
````

````{py:function} latex_float(number: float, formatting: str) -> str
:canonical: abtem.core.axes.latex_float

```{autodoc2-docstring} abtem.core.axes.latex_float
```
````
