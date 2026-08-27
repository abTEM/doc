# {py:mod}`abtem.visualize.visualizations`

```{py:module} abtem.visualize.visualizations
```

```{autodoc2-docstring} abtem.visualize.visualizations
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Visualization <abtem.visualize.visualizations.Visualization>`
  - ```{autodoc2-docstring} abtem.visualize.visualizations.Visualization
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`discrete_cmap <abtem.visualize.visualizations.discrete_cmap>`
  - ```{autodoc2-docstring} abtem.visualize.visualizations.discrete_cmap
    :summary:
    ```
* - {py:obj}`convert_complex <abtem.visualize.visualizations.convert_complex>`
  - ```{autodoc2-docstring} abtem.visualize.visualizations.convert_complex
    :summary:
    ```
* - {py:obj}`show_atoms <abtem.visualize.visualizations.show_atoms>`
  - ```{autodoc2-docstring} abtem.visualize.visualizations.show_atoms
    :summary:
    ```
````

### API

````{py:function} discrete_cmap(num_colors, base_cmap)
:canonical: abtem.visualize.visualizations.discrete_cmap

```{autodoc2-docstring} abtem.visualize.visualizations.discrete_cmap
```
````

````{py:function} convert_complex(measurement: abtem.measurements.BaseMeasurements, method: str) -> abtem.measurements.BaseMeasurements
:canonical: abtem.visualize.visualizations.convert_complex

```{autodoc2-docstring} abtem.visualize.visualizations.convert_complex
```
````

`````{py:class} Visualization(measurement, ax: matplotlib.axes.Axes = None, artist_type=None, figsize: tuple[int, int] = None, aspect: bool = False, common_scale: bool = False, value_limits: tuple[float, float] = (None, None), overlay: bool | tuple[int, ...] = False, explode: bool | tuple[int, ...] = False, share_x: bool = False, share_y: bool = False, cbar: bool = False, interactive: bool = True, title: str = None, xlim: tuple[float, float] = None, ylim: tuple[float, float] = None, convert_complex: str = 'none', **kwargs)
:canonical: abtem.visualize.visualizations.Visualization

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.__init__
```

````{py:method} interact(gui_type, display)
:canonical: abtem.visualize.visualizations.Visualization.interact

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.interact
```

````

````{py:property} autoscale
:canonical: abtem.visualize.visualizations.Visualization.autoscale

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.autoscale
```

````

````{py:property} indexing_axes
:canonical: abtem.visualize.visualizations.Visualization.indexing_axes

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.indexing_axes
```

````

````{py:property} measurement
:canonical: abtem.visualize.visualizations.Visualization.measurement
:type: abtem.measurements.BaseMeasurements

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.measurement
```

````

````{py:property} artists
:canonical: abtem.visualize.visualizations.Visualization.artists

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.artists
```

````

````{py:property} axes
:canonical: abtem.visualize.visualizations.Visualization.axes

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.axes
```

````

````{py:method} get_figure()
:canonical: abtem.visualize.visualizations.Visualization.get_figure

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.get_figure
```

````

````{py:method} adjust_coordinate_limits_to_artists(xlim=None, ylim=None)
:canonical: abtem.visualize.visualizations.Visualization.adjust_coordinate_limits_to_artists

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.adjust_coordinate_limits_to_artists
```

````

````{py:method} set_xlabel(label: str = None)
:canonical: abtem.visualize.visualizations.Visualization.set_xlabel

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_xlabel
```

````

````{py:method} set_ylabel(label: str = None)
:canonical: abtem.visualize.visualizations.Visualization.set_ylabel

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_ylabel
```

````

````{py:method} set_xlim(xlim: tuple[float, float] | list[float] = None)
:canonical: abtem.visualize.visualizations.Visualization.set_xlim

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_xlim
```

````

````{py:method} set_ylim(ylim: tuple[float, float] | list[float] = None)
:canonical: abtem.visualize.visualizations.Visualization.set_ylim

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_ylim
```

````

````{py:method} set_value_limits(value_limits: tuple[float, float] | list[float] = (None, None))
:canonical: abtem.visualize.visualizations.Visualization.set_value_limits

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_value_limits
```

````

````{py:method} set_power(power: float = 1.0)
:canonical: abtem.visualize.visualizations.Visualization.set_power

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_power
```

````

````{py:method} set_logscale(logscale: bool = False)
:canonical: abtem.visualize.visualizations.Visualization.set_logscale

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_logscale
```

````

````{py:method} set_common_value_limits(value_limits=(None, None))
:canonical: abtem.visualize.visualizations.Visualization.set_common_value_limits

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_common_value_limits
```

````

````{py:method} set_column_titles(titles: str | list[str], pad: float = 10.0, fontsize: float = 12, **kwargs)
:canonical: abtem.visualize.visualizations.Visualization.set_column_titles

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_column_titles
```

````

````{py:method} set_row_titles(titles: str | list[str], shift: float = 0.0, fontsize: float = 12, **kwargs)
:canonical: abtem.visualize.visualizations.Visualization.set_row_titles

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_row_titles
```

````

````{py:method} axis(mode: str = 'all', ticks: bool = False, spines: bool = True)
:canonical: abtem.visualize.visualizations.Visualization.axis

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.axis
```

````

````{py:method} axis_off()
:canonical: abtem.visualize.visualizations.Visualization.axis_off

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.axis_off
```

````

````{py:method} remove_artists()
:canonical: abtem.visualize.visualizations.Visualization.remove_artists

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.remove_artists
```

````

````{py:method} update_data_indices(indices)
:canonical: abtem.visualize.visualizations.Visualization.update_data_indices

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.update_data_indices
```

````

````{py:method} set_artists(name, locs: str | tuple[int, ...] = 'all', **kwargs)
:canonical: abtem.visualize.visualizations.Visualization.set_artists

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_artists
```

````

````{py:method} set_legend(**kwargs)
:canonical: abtem.visualize.visualizations.Visualization.set_legend

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_legend
```

````

````{py:method} set_cbars(**kwargs)
:canonical: abtem.visualize.visualizations.Visualization.set_cbars

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_cbars
```

````

````{py:method} set_complex_conversion(complex_conversion: str)
:canonical: abtem.visualize.visualizations.Visualization.set_complex_conversion
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_complex_conversion
```

````

````{py:method} set_cmap(cmap)
:canonical: abtem.visualize.visualizations.Visualization.set_cmap

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_cmap
```

````

````{py:method} set_scale_bars(locs: str = 'lower right', **kwargs)
:canonical: abtem.visualize.visualizations.Visualization.set_scale_bars

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_scale_bars
```

````

`````

````{py:function} show_atoms(atoms: ase.Atoms, plane: tuple[float, float] | str = 'xy', ax: matplotlib.axes.Axes = None, scale: float = 0.75, title: str = None, numbering: bool = False, show_periodic: bool = False, figsize: tuple[float, float] = None, legend: bool = False, merge: float = 0.01, tight_limits: bool = False, show_cell: bool = None, **kwargs)
:canonical: abtem.visualize.visualizations.show_atoms

```{autodoc2-docstring} abtem.visualize.visualizations.show_atoms
```
````
