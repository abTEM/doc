# {py:mod}`abtem.visualize.axes_grid`

```{py:module} abtem.visualize.axes_grid
```

```{autodoc2-docstring} abtem.visualize.axes_grid
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AxesCollection <abtem.visualize.axes_grid.AxesCollection>`
  - ```{autodoc2-docstring} abtem.visualize.axes_grid.AxesCollection
    :summary:
    ```
* - {py:obj}`AxesGrid <abtem.visualize.axes_grid.AxesGrid>`
  - ```{autodoc2-docstring} abtem.visualize.axes_grid.AxesGrid
    :summary:
    ```
````

### API

`````{py:class} AxesCollection(axes, caxes, cbar_mode='single')
:canonical: abtem.visualize.axes_grid.AxesCollection

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesCollection
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesCollection.__init__
```

````{py:property} axes
:canonical: abtem.visualize.axes_grid.AxesCollection.axes

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesCollection.axes
```

````

````{py:property} fig
:canonical: abtem.visualize.axes_grid.AxesCollection.fig

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesCollection.fig
```

````

````{py:property} ncols
:canonical: abtem.visualize.axes_grid.AxesCollection.ncols
:type: int

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesCollection.ncols
```

````

````{py:property} nrows
:canonical: abtem.visualize.axes_grid.AxesCollection.nrows
:type: int

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesCollection.nrows
```

````

````{py:property} shape
:canonical: abtem.visualize.axes_grid.AxesCollection.shape
:type: tuple[int, int]

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesCollection.shape
```

````

`````

`````{py:class} AxesGrid(fig, ncols: int, nrows: int, ncbars: int = 0, cbar_mode: str = 'single', cbar_loc: str = 'right', aspect: bool = True, anchor: str = 'NW', sharex: bool = True, sharey: bool = True, rect: tuple = (0.1, 0.1, 0.9, 0.9), origin: str = 'lower')
:canonical: abtem.visualize.axes_grid.AxesGrid

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesGrid
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesGrid.__init__
```

````{py:method} axis_location_to_indices(axis_location)
:canonical: abtem.visualize.axes_grid.AxesGrid.axis_location_to_indices

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesGrid.axis_location_to_indices
```

````

````{py:method} set_sizes(**kwargs)
:canonical: abtem.visualize.axes_grid.AxesGrid.set_sizes

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesGrid.set_sizes
```

````

````{py:method} set_cbar_layout(**kwargs)
:canonical: abtem.visualize.axes_grid.AxesGrid.set_cbar_layout

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesGrid.set_cbar_layout
```

````

````{py:method} adjust_figure_to_bbox()
:canonical: abtem.visualize.axes_grid.AxesGrid.adjust_figure_to_bbox

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesGrid.adjust_figure_to_bbox
```

````

````{py:property} axes
:canonical: abtem.visualize.axes_grid.AxesGrid.axes

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesGrid.axes
```

````

````{py:property} fig
:canonical: abtem.visualize.axes_grid.AxesGrid.fig

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesGrid.fig
```

````

````{py:property} ncols
:canonical: abtem.visualize.axes_grid.AxesGrid.ncols
:type: int

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesGrid.ncols
```

````

````{py:property} nrows
:canonical: abtem.visualize.axes_grid.AxesGrid.nrows
:type: int

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesGrid.nrows
```

````

````{py:property} shape
:canonical: abtem.visualize.axes_grid.AxesGrid.shape
:type: tuple[int, int]

```{autodoc2-docstring} abtem.visualize.axes_grid.AxesGrid.shape
```

````

`````
