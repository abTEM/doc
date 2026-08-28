# {py:mod}`abtem.visualize.artists`

```{py:module} abtem.visualize.artists
```

```{autodoc2-docstring} abtem.visualize.artists
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AreaIndicator <abtem.visualize.artists.AreaIndicator>`
  - ```{autodoc2-docstring} abtem.visualize.artists.AreaIndicator
    :parser: rst
    :summary:
    ```
* - {py:obj}`Artist <abtem.visualize.artists.Artist>`
  - ```{autodoc2-docstring} abtem.visualize.artists.Artist
    :parser: rst
    :summary:
    ```
* - {py:obj}`Artist1D <abtem.visualize.artists.Artist1D>`
  - ```{autodoc2-docstring} abtem.visualize.artists.Artist1D
    :parser: rst
    :summary:
    ```
* - {py:obj}`Artist2D <abtem.visualize.artists.Artist2D>`
  - ```{autodoc2-docstring} abtem.visualize.artists.Artist2D
    :parser: rst
    :summary:
    ```
* - {py:obj}`CircleAnnotations <abtem.visualize.artists.CircleAnnotations>`
  - ```{autodoc2-docstring} abtem.visualize.artists.CircleAnnotations
    :parser: rst
    :summary:
    ```
* - {py:obj}`DomainColoringArtist <abtem.visualize.artists.DomainColoringArtist>`
  - ```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist
    :parser: rst
    :summary:
    ```
* - {py:obj}`ImageArtist <abtem.visualize.artists.ImageArtist>`
  - ```{autodoc2-docstring} abtem.visualize.artists.ImageArtist
    :parser: rst
    :summary:
    ```
* - {py:obj}`LinesArtist <abtem.visualize.artists.LinesArtist>`
  - ```{autodoc2-docstring} abtem.visualize.artists.LinesArtist
    :parser: rst
    :summary:
    ```
* - {py:obj}`OverlayImshowArtist <abtem.visualize.artists.OverlayImshowArtist>`
  - ```{autodoc2-docstring} abtem.visualize.artists.OverlayImshowArtist
    :parser: rst
    :summary:
    ```
* - {py:obj}`ScaleBar <abtem.visualize.artists.ScaleBar>`
  - ```{autodoc2-docstring} abtem.visualize.artists.ScaleBar
    :parser: rst
    :summary:
    ```
* - {py:obj}`ScaledCircleCollection <abtem.visualize.artists.ScaledCircleCollection>`
  - ```{autodoc2-docstring} abtem.visualize.artists.ScaledCircleCollection
    :parser: rst
    :summary:
    ```
* - {py:obj}`ScatterArtist <abtem.visualize.artists.ScatterArtist>`
  - ```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`default_cbar_scalar_formatter <abtem.visualize.artists.default_cbar_scalar_formatter>`
  - ```{autodoc2-docstring} abtem.visualize.artists.default_cbar_scalar_formatter
    :parser: rst
    :summary:
    ```
* - {py:obj}`get_extent <abtem.visualize.artists.get_extent>`
  - ```{autodoc2-docstring} abtem.visualize.artists.get_extent
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_cmap <abtem.visualize.artists.validate_cmap>`
  - ```{autodoc2-docstring} abtem.visualize.artists.validate_cmap
    :parser: rst
    :summary:
    ```
````

### API

````{py:class} AreaIndicator(ax, xy, width, height, alpha: float = 0.33, facecolor: str = 'r', edgecolor: str = 'r', **kwargs)
:canonical: abtem.visualize.artists.AreaIndicator

```{autodoc2-docstring} abtem.visualize.artists.AreaIndicator
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.artists.AreaIndicator.__init__
:parser: rst
```

````

`````{py:class} Artist(ax, measurement)
:canonical: abtem.visualize.artists.Artist

```{autodoc2-docstring} abtem.visualize.artists.Artist
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.artists.Artist.__init__
:parser: rst
```

````{py:method} get_power()
:canonical: abtem.visualize.artists.Artist.get_power
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist.get_power
:parser: rst
```

````

````{py:method} get_xlim()
:canonical: abtem.visualize.artists.Artist.get_xlim
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist.get_xlim
:parser: rst
```

````

````{py:method} get_ylim()
:canonical: abtem.visualize.artists.Artist.get_ylim
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist.get_ylim
:parser: rst
```

````

````{py:method} remove()
:canonical: abtem.visualize.artists.Artist.remove
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist.remove
:parser: rst
```

````

````{py:method} set_data(data)
:canonical: abtem.visualize.artists.Artist.set_data
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist.set_data
:parser: rst
```

````

````{py:method} set_logscale()
:canonical: abtem.visualize.artists.Artist.set_logscale

```{autodoc2-docstring} abtem.visualize.artists.Artist.set_logscale
:parser: rst
```

````

````{py:method} set_power(power=1.0)
:canonical: abtem.visualize.artists.Artist.set_power
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist.set_power
:parser: rst
```

````

````{py:method} set_value_limits(value_limits)
:canonical: abtem.visualize.artists.Artist.set_value_limits
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist.set_value_limits
:parser: rst
```

````

````{py:method} set_xlabel(label)
:canonical: abtem.visualize.artists.Artist.set_xlabel

```{autodoc2-docstring} abtem.visualize.artists.Artist.set_xlabel
:parser: rst
```

````

````{py:method} set_xlim(xlim)
:canonical: abtem.visualize.artists.Artist.set_xlim

```{autodoc2-docstring} abtem.visualize.artists.Artist.set_xlim
:parser: rst
```

````

````{py:method} set_ylabel(label)
:canonical: abtem.visualize.artists.Artist.set_ylabel

```{autodoc2-docstring} abtem.visualize.artists.Artist.set_ylabel
:parser: rst
```

````

````{py:method} set_ylim(ylim)
:canonical: abtem.visualize.artists.Artist.set_ylim

```{autodoc2-docstring} abtem.visualize.artists.Artist.set_ylim
:parser: rst
```

````

`````

````{py:class} Artist1D(ax, measurement)
:canonical: abtem.visualize.artists.Artist1D

Bases: {py:obj}`abtem.visualize.artists.Artist`

```{autodoc2-docstring} abtem.visualize.artists.Artist1D
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.artists.Artist1D.__init__
:parser: rst
```

````

`````{py:class} Artist2D(ax, measurement)
:canonical: abtem.visualize.artists.Artist2D

Bases: {py:obj}`abtem.visualize.artists.Artist`

```{autodoc2-docstring} abtem.visualize.artists.Artist2D
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.artists.Artist2D.__init__
:parser: rst
```

````{py:method} add_area_indicator(area_indicator, panel='first', **kwargs)
:canonical: abtem.visualize.artists.Artist2D.add_area_indicator
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist2D.add_area_indicator
:parser: rst
```

````

````{py:method} get_value_limits()
:canonical: abtem.visualize.artists.Artist2D.get_value_limits
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist2D.get_value_limits
:parser: rst
```

````

````{py:method} get_xlim()
:canonical: abtem.visualize.artists.Artist2D.get_xlim
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist2D.get_xlim
:parser: rst
```

````

````{py:method} get_ylim()
:canonical: abtem.visualize.artists.Artist2D.get_ylim
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist2D.get_ylim
:parser: rst
```

````

````{py:property} num_cbars
:canonical: abtem.visualize.artists.Artist2D.num_cbars
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist2D.num_cbars
:parser: rst
```

````

````{py:method} set_cbars(cmap)
:canonical: abtem.visualize.artists.Artist2D.set_cbars
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist2D.set_cbars
:parser: rst
```

````

````{py:method} set_cmap(cmap)
:canonical: abtem.visualize.artists.Artist2D.set_cmap
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist2D.set_cmap
:parser: rst
```

````

````{py:method} set_data(data)
:canonical: abtem.visualize.artists.Artist2D.set_data
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist2D.set_data
:parser: rst
```

````

````{py:method} set_logscale()
:canonical: abtem.visualize.artists.Artist2D.set_logscale

```{autodoc2-docstring} abtem.visualize.artists.Artist2D.set_logscale
:parser: rst
```

````

````{py:method} set_power(power: float = 1.0)
:canonical: abtem.visualize.artists.Artist2D.set_power
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist2D.set_power
:parser: rst
```

````

````{py:method} set_scale_bars(**kwargs)
:canonical: abtem.visualize.artists.Artist2D.set_scale_bars

```{autodoc2-docstring} abtem.visualize.artists.Artist2D.set_scale_bars
:parser: rst
```

````

````{py:method} set_value_limits(value_limits)
:canonical: abtem.visualize.artists.Artist2D.set_value_limits
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.Artist2D.set_value_limits
:parser: rst
```

````

`````

`````{py:class} CircleAnnotations(circle_collection, annotations, fontsize: int = 8, placement: str = 'top', threshold: float = 0.0001, **kwargs)
:canonical: abtem.visualize.artists.CircleAnnotations

```{autodoc2-docstring} abtem.visualize.artists.CircleAnnotations
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.artists.CircleAnnotations.__init__
:parser: rst
```

````{py:method} set_placement(placement)
:canonical: abtem.visualize.artists.CircleAnnotations.set_placement

```{autodoc2-docstring} abtem.visualize.artists.CircleAnnotations.set_placement
:parser: rst
```

````

````{py:method} set_threshold(threshold)
:canonical: abtem.visualize.artists.CircleAnnotations.set_threshold

```{autodoc2-docstring} abtem.visualize.artists.CircleAnnotations.set_threshold
:parser: rst
```

````

````{py:method} set_visible(visible)
:canonical: abtem.visualize.artists.CircleAnnotations.set_visible

```{autodoc2-docstring} abtem.visualize.artists.CircleAnnotations.set_visible
:parser: rst
```

````

````{py:property} threshold
:canonical: abtem.visualize.artists.CircleAnnotations.threshold

```{autodoc2-docstring} abtem.visualize.artists.CircleAnnotations.threshold
:parser: rst
```

````

`````

`````{py:class} DomainColoringArtist(ax: matplotlib.axes.Axes, measurement, caxes: list[matplotlib.axes.Axes] = None, cmap: str | matplotlib.colors.Colormap | None = None, vmin: float = None, vmax: float = None, power: float = 1.0, logscale: bool = False, units: str = None, **kwargs)
:canonical: abtem.visualize.artists.DomainColoringArtist

Bases: {py:obj}`abtem.visualize.artists.Artist2D`

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.__init__
:parser: rst
```

````{py:property} amplitude_axes_image
:canonical: abtem.visualize.artists.DomainColoringArtist.amplitude_axes_image

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.amplitude_axes_image
:parser: rst
```

````

````{py:property} amplitude_norm
:canonical: abtem.visualize.artists.DomainColoringArtist.amplitude_norm

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.amplitude_norm
:parser: rst
```

````

````{py:method} get_power()
:canonical: abtem.visualize.artists.DomainColoringArtist.get_power

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.get_power
:parser: rst
```

````

````{py:method} get_value_limits()
:canonical: abtem.visualize.artists.DomainColoringArtist.get_value_limits

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.get_value_limits
:parser: rst
```

````

````{py:method} get_xlim()
:canonical: abtem.visualize.artists.DomainColoringArtist.get_xlim

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.get_xlim
:parser: rst
```

````

````{py:method} get_ylim()
:canonical: abtem.visualize.artists.DomainColoringArtist.get_ylim

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.get_ylim
:parser: rst
```

````

````{py:attribute} num_cbars
:canonical: abtem.visualize.artists.DomainColoringArtist.num_cbars
:value: >
   2

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.num_cbars
:parser: rst
```

````

````{py:property} phase_axes_image
:canonical: abtem.visualize.artists.DomainColoringArtist.phase_axes_image

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.phase_axes_image
:parser: rst
```

````

````{py:method} remove()
:canonical: abtem.visualize.artists.DomainColoringArtist.remove

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.remove
:parser: rst
```

````

````{py:method} set_cbars(caxes, label: str = None, **kwargs)
:canonical: abtem.visualize.artists.DomainColoringArtist.set_cbars

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.set_cbars
:parser: rst
```

````

````{py:method} set_cmap(cmap)
:canonical: abtem.visualize.artists.DomainColoringArtist.set_cmap

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.set_cmap
:parser: rst
```

````

````{py:method} set_data(data)
:canonical: abtem.visualize.artists.DomainColoringArtist.set_data

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.set_data
:parser: rst
```

````

````{py:method} set_extent(extent)
:canonical: abtem.visualize.artists.DomainColoringArtist.set_extent

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.set_extent
:parser: rst
```

````

````{py:method} set_power(power: float = 1.0)
:canonical: abtem.visualize.artists.DomainColoringArtist.set_power

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.set_power
:parser: rst
```

````

````{py:method} set_value_limits(value_limits: tuple[float, float] = (None, None))
:canonical: abtem.visualize.artists.DomainColoringArtist.set_value_limits

```{autodoc2-docstring} abtem.visualize.artists.DomainColoringArtist.set_value_limits
:parser: rst
```

````

`````

`````{py:class} ImageArtist(ax: matplotlib.axes.Axes, measurement: abtem.measurements.Images | abtem.measurements.DiffractionPatterns | abtem.measurements.MeasurementsEnsemble, caxes: list[matplotlib.axes.Axes] = None, cmap: str | matplotlib.colors.Colormap | None = None, vmin: float = None, vmax: float = None, power: float = 1.0, logscale: bool = False, origin: typing.Literal[upper, lower] | None = 'lower', units: str = None, **kwargs)
:canonical: abtem.visualize.artists.ImageArtist

Bases: {py:obj}`abtem.visualize.artists.Artist2D`

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.__init__
:parser: rst
```

````{py:property} axes_image
:canonical: abtem.visualize.artists.ImageArtist.axes_image

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.axes_image
:parser: rst
```

````

````{py:method} get_power()
:canonical: abtem.visualize.artists.ImageArtist.get_power

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.get_power
:parser: rst
```

````

````{py:method} get_value_limits()
:canonical: abtem.visualize.artists.ImageArtist.get_value_limits

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.get_value_limits
:parser: rst
```

````

````{py:method} get_xlim()
:canonical: abtem.visualize.artists.ImageArtist.get_xlim

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.get_xlim
:parser: rst
```

````

````{py:method} get_ylim()
:canonical: abtem.visualize.artists.ImageArtist.get_ylim

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.get_ylim
:parser: rst
```

````

````{py:property} norm
:canonical: abtem.visualize.artists.ImageArtist.norm

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.norm
:parser: rst
```

````

````{py:attribute} num_cbars
:canonical: abtem.visualize.artists.ImageArtist.num_cbars
:value: >
   1

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.num_cbars
:parser: rst
```

````

````{py:method} remove()
:canonical: abtem.visualize.artists.ImageArtist.remove

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.remove
:parser: rst
```

````

````{py:method} set_cbars(caxes, **kwargs)
:canonical: abtem.visualize.artists.ImageArtist.set_cbars

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.set_cbars
:parser: rst
```

````

````{py:method} set_cmap(cmap)
:canonical: abtem.visualize.artists.ImageArtist.set_cmap

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.set_cmap
:parser: rst
```

````

````{py:method} set_data(data)
:canonical: abtem.visualize.artists.ImageArtist.set_data

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.set_data
:parser: rst
```

````

````{py:method} set_extent(extent)
:canonical: abtem.visualize.artists.ImageArtist.set_extent

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.set_extent
:parser: rst
```

````

````{py:method} set_logscale(logscale: bool = False)
:canonical: abtem.visualize.artists.ImageArtist.set_logscale

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.set_logscale
:parser: rst
```

````

````{py:method} set_power(power: float = 1.0)
:canonical: abtem.visualize.artists.ImageArtist.set_power

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.set_power
:parser: rst
```

````

````{py:method} set_value_limits(value_limits: tuple[float, float] = None)
:canonical: abtem.visualize.artists.ImageArtist.set_value_limits

```{autodoc2-docstring} abtem.visualize.artists.ImageArtist.set_value_limits
:parser: rst
```

````

`````

`````{py:class} LinesArtist(ax: matplotlib.axes.Axes, measurement, caxes: list[matplotlib.axes.Axes] = None, label=None, units: str = None, legend: bool = False, **kwargs)
:canonical: abtem.visualize.artists.LinesArtist

Bases: {py:obj}`abtem.visualize.artists.Artist1D`

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist.__init__
:parser: rst
```

````{py:method} get_logscale()
:canonical: abtem.visualize.artists.LinesArtist.get_logscale

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist.get_logscale
:parser: rst
```

````

````{py:method} get_power()
:canonical: abtem.visualize.artists.LinesArtist.get_power

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist.get_power
:parser: rst
```

````

````{py:method} get_value_limits()
:canonical: abtem.visualize.artists.LinesArtist.get_value_limits

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist.get_value_limits
:parser: rst
```

````

````{py:method} get_xlim()
:canonical: abtem.visualize.artists.LinesArtist.get_xlim

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist.get_xlim
:parser: rst
```

````

````{py:method} get_ylim()
:canonical: abtem.visualize.artists.LinesArtist.get_ylim

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist.get_ylim
:parser: rst
```

````

````{py:attribute} num_cbars
:canonical: abtem.visualize.artists.LinesArtist.num_cbars
:value: >
   0

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist.num_cbars
:parser: rst
```

````

````{py:method} remove()
:canonical: abtem.visualize.artists.LinesArtist.remove

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist.remove
:parser: rst
```

````

````{py:method} set_data(data)
:canonical: abtem.visualize.artists.LinesArtist.set_data

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist.set_data
:parser: rst
```

````

````{py:method} set_legend(**kwargs)
:canonical: abtem.visualize.artists.LinesArtist.set_legend

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist.set_legend
:parser: rst
```

````

````{py:method} set_logscale()
:canonical: abtem.visualize.artists.LinesArtist.set_logscale

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist.set_logscale
:parser: rst
```

````

````{py:method} set_power(power: float = 1.0) -> None
:canonical: abtem.visualize.artists.LinesArtist.set_power
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist.set_power
:parser: rst
```

````

````{py:method} set_value_limits(value_limits: list[float] = None)
:canonical: abtem.visualize.artists.LinesArtist.set_value_limits

```{autodoc2-docstring} abtem.visualize.artists.LinesArtist.set_value_limits
:parser: rst
```

````

`````

````{py:class} OverlayImshowArtist(ax, data, cmap, vmin: float = None, vmax: float = None, power: float = 1.0, logscale: bool = False)
:canonical: abtem.visualize.artists.OverlayImshowArtist

Bases: {py:obj}`abtem.visualize.artists.Artist2D`

```{autodoc2-docstring} abtem.visualize.artists.OverlayImshowArtist
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.artists.OverlayImshowArtist.__init__
:parser: rst
```

````

````{py:class} ScaleBar(ax: matplotlib.axes.Axes, label: str = '', size: float = None, loc: str = 'lower right', borderpad: float = 0.5, size_vertical: float = None, sep: float = 6, pad: float = 0.3, label_top: bool = True, frameon: bool = False, **kwargs)
:canonical: abtem.visualize.artists.ScaleBar

```{autodoc2-docstring} abtem.visualize.artists.ScaleBar
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.artists.ScaleBar.__init__
:parser: rst
```

````

`````{py:class} ScaledCircleCollection(array: numpy.ndarray, offsets: numpy.ndarray, scale: float = 1.0, threshold: float = 1e-06, **kwargs)
:canonical: abtem.visualize.artists.ScaledCircleCollection

Bases: {py:obj}`matplotlib.collections.Collection`

```{autodoc2-docstring} abtem.visualize.artists.ScaledCircleCollection
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.artists.ScaledCircleCollection.__init__
:parser: rst
```

````{py:method} draw(renderer)
:canonical: abtem.visualize.artists.ScaledCircleCollection.draw

````

````{py:method} get_all_offsets()
:canonical: abtem.visualize.artists.ScaledCircleCollection.get_all_offsets

```{autodoc2-docstring} abtem.visualize.artists.ScaledCircleCollection.get_all_offsets
:parser: rst
```

````

````{py:method} get_radii()
:canonical: abtem.visualize.artists.ScaledCircleCollection.get_radii

```{autodoc2-docstring} abtem.visualize.artists.ScaledCircleCollection.get_radii
:parser: rst
```

````

````{py:method} get_scale()
:canonical: abtem.visualize.artists.ScaledCircleCollection.get_scale

```{autodoc2-docstring} abtem.visualize.artists.ScaledCircleCollection.get_scale
:parser: rst
```

````

````{py:method} set_array(array)
:canonical: abtem.visualize.artists.ScaledCircleCollection.set_array

````

````{py:method} set_data(array, offsets)
:canonical: abtem.visualize.artists.ScaledCircleCollection.set_data

```{autodoc2-docstring} abtem.visualize.artists.ScaledCircleCollection.set_data
:parser: rst
```

````

````{py:method} set_norm(norm)
:canonical: abtem.visualize.artists.ScaledCircleCollection.set_norm

````

````{py:method} set_scale(scale)
:canonical: abtem.visualize.artists.ScaledCircleCollection.set_scale

```{autodoc2-docstring} abtem.visualize.artists.ScaledCircleCollection.set_scale
:parser: rst
```

````

````{py:method} set_threshold(threshold)
:canonical: abtem.visualize.artists.ScaledCircleCollection.set_threshold

```{autodoc2-docstring} abtem.visualize.artists.ScaledCircleCollection.set_threshold
:parser: rst
```

````

````{py:property} threshold
:canonical: abtem.visualize.artists.ScaledCircleCollection.threshold

```{autodoc2-docstring} abtem.visualize.artists.ScaledCircleCollection.threshold
:parser: rst
```

````

`````

`````{py:class} ScatterArtist(ax: matplotlib.axes.Axes, measurement: abtem.measurements.IndexedDiffractionPatterns, caxes: list[matplotlib.axes.Axes] = None, cmap: str | matplotlib.colors.Colormap | None = None, value_limits: tuple[float, float] = None, power: float = 1.0, logscale: bool = False, units: str = None, scale: float = 0.5, annotations: bool = True, annotation_kwargs: dict = None, **kwargs)
:canonical: abtem.visualize.artists.ScatterArtist

Bases: {py:obj}`abtem.visualize.artists.Artist2D`

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.__init__
:parser: rst
```

````{py:property} annotations
:canonical: abtem.visualize.artists.ScatterArtist.annotations
:type: list[matplotlib.text.Annotation]

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.annotations
:parser: rst
```

````

````{py:property} circle_collection
:canonical: abtem.visualize.artists.ScatterArtist.circle_collection
:type: abtem.visualize.artists.ScaledCircleCollection

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.circle_collection
:parser: rst
```

````

````{py:method} get_offsets()
:canonical: abtem.visualize.artists.ScatterArtist.get_offsets

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.get_offsets
:parser: rst
```

````

````{py:method} get_power()
:canonical: abtem.visualize.artists.ScatterArtist.get_power

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.get_power
:parser: rst
```

````

````{py:method} get_scale()
:canonical: abtem.visualize.artists.ScatterArtist.get_scale

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.get_scale
:parser: rst
```

````

````{py:method} get_value_limits()
:canonical: abtem.visualize.artists.ScatterArtist.get_value_limits

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.get_value_limits
:parser: rst
```

````

````{py:method} get_xlim()
:canonical: abtem.visualize.artists.ScatterArtist.get_xlim

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.get_xlim
:parser: rst
```

````

````{py:method} get_ylim()
:canonical: abtem.visualize.artists.ScatterArtist.get_ylim

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.get_ylim
:parser: rst
```

````

````{py:attribute} num_cbars
:canonical: abtem.visualize.artists.ScatterArtist.num_cbars
:value: >
   1

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.num_cbars
:parser: rst
```

````

````{py:method} remove()
:canonical: abtem.visualize.artists.ScatterArtist.remove

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.remove
:parser: rst
```

````

````{py:method} set_annotation_kwargs(**kwargs)
:canonical: abtem.visualize.artists.ScatterArtist.set_annotation_kwargs

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.set_annotation_kwargs
:parser: rst
```

````

````{py:method} set_cbars(caxes=None, **kwargs)
:canonical: abtem.visualize.artists.ScatterArtist.set_cbars

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.set_cbars
:parser: rst
```

````

````{py:method} set_cmap(cmap: str)
:canonical: abtem.visualize.artists.ScatterArtist.set_cmap

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.set_cmap
:parser: rst
```

````

````{py:method} set_data(measurement: numpy.ndarray)
:canonical: abtem.visualize.artists.ScatterArtist.set_data

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.set_data
:parser: rst
```

````

````{py:method} set_logscale(logscale: bool = False)
:canonical: abtem.visualize.artists.ScatterArtist.set_logscale

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.set_logscale
:parser: rst
```

````

````{py:method} set_power(power: float = 1.0)
:canonical: abtem.visualize.artists.ScatterArtist.set_power

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.set_power
:parser: rst
```

````

````{py:method} set_scale(scale: float)
:canonical: abtem.visualize.artists.ScatterArtist.set_scale

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.set_scale
:parser: rst
```

````

````{py:method} set_value_limits(value_limits: tuple[float, float] = None)
:canonical: abtem.visualize.artists.ScatterArtist.set_value_limits

```{autodoc2-docstring} abtem.visualize.artists.ScatterArtist.set_value_limits
:parser: rst
```

````

`````

````{py:function} default_cbar_scalar_formatter()
:canonical: abtem.visualize.artists.default_cbar_scalar_formatter

```{autodoc2-docstring} abtem.visualize.artists.default_cbar_scalar_formatter
:parser: rst
```
````

````{py:function} get_extent(measurement, units=None)
:canonical: abtem.visualize.artists.get_extent

```{autodoc2-docstring} abtem.visualize.artists.get_extent
:parser: rst
```
````

````{py:function} validate_cmap(cmap, measurement, complex_conversion='none')
:canonical: abtem.visualize.artists.validate_cmap

```{autodoc2-docstring} abtem.visualize.artists.validate_cmap
:parser: rst
```
````
