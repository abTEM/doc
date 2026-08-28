# {py:mod}`abtem.visualize.visualizations`

```{py:module} abtem.visualize.visualizations
```

```{autodoc2-docstring} abtem.visualize.visualizations
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Visualization <abtem.visualize.visualizations.Visualization>`
  - ```{autodoc2-docstring} abtem.visualize.visualizations.Visualization
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`convert_complex <abtem.visualize.visualizations.convert_complex>`
  - ```{autodoc2-docstring} abtem.visualize.visualizations.convert_complex
    :parser: rst
    :summary:
    ```
* - {py:obj}`discrete_cmap <abtem.visualize.visualizations.discrete_cmap>`
  - ```{autodoc2-docstring} abtem.visualize.visualizations.discrete_cmap
    :parser: rst
    :summary:
    ```
* - {py:obj}`show_atoms <abtem.visualize.visualizations.show_atoms>`
  - ```{autodoc2-docstring} abtem.visualize.visualizations.show_atoms
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} Visualization(...)
:canonical: abtem.visualize.visualizations.Visualization

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.__init__
:parser: rst
```

````{py:method} adjust_coordinate_limits_to_artists(...)
:canonical: abtem.visualize.visualizations.Visualization.adjust_coordinate_limits_to_artists

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.adjust_coordinate_limits_to_artists
:parser: rst
```

````

````{py:property} artists
:canonical: abtem.visualize.visualizations.Visualization.artists

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.artists
:parser: rst
```

````

````{py:property} autoscale
:canonical: abtem.visualize.visualizations.Visualization.autoscale

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.autoscale
:parser: rst
```

````

````{py:property} axes
:canonical: abtem.visualize.visualizations.Visualization.axes

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.axes
:parser: rst
```

````

````{py:method} axis(...)
:canonical: abtem.visualize.visualizations.Visualization.axis

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.axis
:parser: rst
```

````

````{py:method} axis_off()
:canonical: abtem.visualize.visualizations.Visualization.axis_off

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.axis_off
:parser: rst
```

````

````{py:method} get_figure()
:canonical: abtem.visualize.visualizations.Visualization.get_figure

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.get_figure
:parser: rst
```

````

````{py:property} indexing_axes
:canonical: abtem.visualize.visualizations.Visualization.indexing_axes

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.indexing_axes
:parser: rst
```

````

````{py:method} interact(...)
:canonical: abtem.visualize.visualizations.Visualization.interact

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.interact
:parser: rst
```

````

````{py:property} measurement
:canonical: abtem.visualize.visualizations.Visualization.measurement
:type: abtem.measurements.BaseMeasurements

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.measurement
:parser: rst
```

````

````{py:method} remove_artists()
:canonical: abtem.visualize.visualizations.Visualization.remove_artists

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.remove_artists
:parser: rst
```

````

````{py:method} set_artists(...)
:canonical: abtem.visualize.visualizations.Visualization.set_artists

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_artists
:parser: rst
```

````

````{py:method} set_cbars(...)
:canonical: abtem.visualize.visualizations.Visualization.set_cbars

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_cbars
:parser: rst
```

````

````{py:method} set_cmap(...)
:canonical: abtem.visualize.visualizations.Visualization.set_cmap

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_cmap
:parser: rst
```

````

````{py:method} set_column_titles(...)
:canonical: abtem.visualize.visualizations.Visualization.set_column_titles

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_column_titles
:parser: rst
```

````

````{py:method} set_common_value_limits(...)
:canonical: abtem.visualize.visualizations.Visualization.set_common_value_limits

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_common_value_limits
:parser: rst
```

````

````{py:method} set_complex_conversion(...)
:canonical: abtem.visualize.visualizations.Visualization.set_complex_conversion
:abstractmethod:

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_complex_conversion
:parser: rst
```

````

````{py:method} set_legend(...)
:canonical: abtem.visualize.visualizations.Visualization.set_legend

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_legend
:parser: rst
```

````

````{py:method} set_logscale(...)
:canonical: abtem.visualize.visualizations.Visualization.set_logscale

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_logscale
:parser: rst
```

````

````{py:method} set_power(...)
:canonical: abtem.visualize.visualizations.Visualization.set_power

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_power
:parser: rst
```

````

````{py:method} set_row_titles(...)
:canonical: abtem.visualize.visualizations.Visualization.set_row_titles

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_row_titles
:parser: rst
```

````

````{py:method} set_scale_bars(...)
:canonical: abtem.visualize.visualizations.Visualization.set_scale_bars

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_scale_bars
:parser: rst
```

````

````{py:method} set_value_limits(...)
:canonical: abtem.visualize.visualizations.Visualization.set_value_limits

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_value_limits
:parser: rst
```

````

````{py:method} set_xlabel(...)
:canonical: abtem.visualize.visualizations.Visualization.set_xlabel

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_xlabel
:parser: rst
```

````

````{py:method} set_xlim(...)
:canonical: abtem.visualize.visualizations.Visualization.set_xlim

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_xlim
:parser: rst
```

````

````{py:method} set_ylabel(...)
:canonical: abtem.visualize.visualizations.Visualization.set_ylabel

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_ylabel
:parser: rst
```

````

````{py:method} set_ylim(...)
:canonical: abtem.visualize.visualizations.Visualization.set_ylim

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.set_ylim
:parser: rst
```

````

````{py:method} update_data_indices(...)
:canonical: abtem.visualize.visualizations.Visualization.update_data_indices

```{autodoc2-docstring} abtem.visualize.visualizations.Visualization.update_data_indices
:parser: rst
```

````

`````

````{py:function} convert_complex(...) -> abtem.measurements.BaseMeasurements
:canonical: abtem.visualize.visualizations.convert_complex

```{autodoc2-docstring} abtem.visualize.visualizations.convert_complex
:parser: rst
```
````

````{py:function} discrete_cmap(...)
:canonical: abtem.visualize.visualizations.discrete_cmap

```{autodoc2-docstring} abtem.visualize.visualizations.discrete_cmap
:parser: rst
```
````

````{py:function} show_atoms(...)
:canonical: abtem.visualize.visualizations.show_atoms

```{autodoc2-docstring} abtem.visualize.visualizations.show_atoms
:parser: rst
```
````
