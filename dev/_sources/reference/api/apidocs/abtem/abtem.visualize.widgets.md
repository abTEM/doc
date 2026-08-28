# {py:mod}`abtem.visualize.widgets`

```{py:module} abtem.visualize.widgets
```

```{autodoc2-docstring} abtem.visualize.widgets
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseGUI <abtem.visualize.widgets.BaseGUI>`
  -
* - {py:obj}`ImageGUI <abtem.visualize.widgets.ImageGUI>`
  -
* - {py:obj}`LinesGUI <abtem.visualize.widgets.LinesGUI>`
  -
* - {py:obj}`ScatterGUI <abtem.visualize.widgets.ScatterGUI>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`make_toggle_hkl_button <abtem.visualize.widgets.make_toggle_hkl_button>`
  - ```{autodoc2-docstring} abtem.visualize.widgets.make_toggle_hkl_button
    :parser: rst
    :summary:
    ```
* - {py:obj}`slider_from_axes_metadata <abtem.visualize.widgets.slider_from_axes_metadata>`
  - ```{autodoc2-docstring} abtem.visualize.widgets.slider_from_axes_metadata
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ipywidgets_not_installed <abtem.visualize.widgets.ipywidgets_not_installed>`
  - ```{autodoc2-docstring} abtem.visualize.widgets.ipywidgets_not_installed
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} BaseGUI(...)
:canonical: abtem.visualize.widgets.BaseGUI

Bases: {py:obj}`ipywidgets.HBox`

````{py:method} attach_visualization(...)
:canonical: abtem.visualize.widgets.BaseGUI.attach_visualization

```{autodoc2-docstring} abtem.visualize.widgets.BaseGUI.attach_visualization
:parser: rst
```

````

````{py:property} autoscale_button
:canonical: abtem.visualize.widgets.BaseGUI.autoscale_button

```{autodoc2-docstring} abtem.visualize.widgets.BaseGUI.autoscale_button
:parser: rst
```

````

````{py:property} common_scale_button
:canonical: abtem.visualize.widgets.BaseGUI.common_scale_button

```{autodoc2-docstring} abtem.visualize.widgets.BaseGUI.common_scale_button
:parser: rst
```

````

````{py:property} powerscale_slider
:canonical: abtem.visualize.widgets.BaseGUI.powerscale_slider

```{autodoc2-docstring} abtem.visualize.widgets.BaseGUI.powerscale_slider
:parser: rst
```

````

````{py:property} scale_button
:canonical: abtem.visualize.widgets.BaseGUI.scale_button

```{autodoc2-docstring} abtem.visualize.widgets.BaseGUI.scale_button
:parser: rst
```

````

````{py:property} sliders
:canonical: abtem.visualize.widgets.BaseGUI.sliders

```{autodoc2-docstring} abtem.visualize.widgets.BaseGUI.sliders
:parser: rst
```

````

`````

`````{py:class} ImageGUI(...)
:canonical: abtem.visualize.widgets.ImageGUI

Bases: {py:obj}`abtem.visualize.widgets.BaseGUI`

````{py:method} attach_visualization(...)
:canonical: abtem.visualize.widgets.ImageGUI.attach_visualization

```{autodoc2-docstring} abtem.visualize.widgets.ImageGUI.attach_visualization
:parser: rst
```

````

````{py:property} cmap_dropdown
:canonical: abtem.visualize.widgets.ImageGUI.cmap_dropdown

```{autodoc2-docstring} abtem.visualize.widgets.ImageGUI.cmap_dropdown
:parser: rst
```

````

````{py:property} complex_dropdown
:canonical: abtem.visualize.widgets.ImageGUI.complex_dropdown

```{autodoc2-docstring} abtem.visualize.widgets.ImageGUI.complex_dropdown
:parser: rst
```

````

`````

`````{py:class} LinesGUI(...)
:canonical: abtem.visualize.widgets.LinesGUI

Bases: {py:obj}`abtem.visualize.widgets.BaseGUI`

````{py:method} attach_visualization(...)
:canonical: abtem.visualize.widgets.LinesGUI.attach_visualization

```{autodoc2-docstring} abtem.visualize.widgets.LinesGUI.attach_visualization
:parser: rst
```

````

````{py:property} complex_dropdown
:canonical: abtem.visualize.widgets.LinesGUI.complex_dropdown

```{autodoc2-docstring} abtem.visualize.widgets.LinesGUI.complex_dropdown
:parser: rst
```

````

`````

`````{py:class} ScatterGUI(...)
:canonical: abtem.visualize.widgets.ScatterGUI

Bases: {py:obj}`abtem.visualize.widgets.BaseGUI`

````{py:property} annotations_slider
:canonical: abtem.visualize.widgets.ScatterGUI.annotations_slider

```{autodoc2-docstring} abtem.visualize.widgets.ScatterGUI.annotations_slider
:parser: rst
```

````

````{py:method} attach_visualization(...)
:canonical: abtem.visualize.widgets.ScatterGUI.attach_visualization

```{autodoc2-docstring} abtem.visualize.widgets.ScatterGUI.attach_visualization
:parser: rst
```

````

````{py:property} cmap_dropdown
:canonical: abtem.visualize.widgets.ScatterGUI.cmap_dropdown

```{autodoc2-docstring} abtem.visualize.widgets.ScatterGUI.cmap_dropdown
:parser: rst
```

````

````{py:property} scale_slider
:canonical: abtem.visualize.widgets.ScatterGUI.scale_slider

```{autodoc2-docstring} abtem.visualize.widgets.ScatterGUI.scale_slider
:parser: rst
```

````

`````

````{py:data} ipywidgets_not_installed
:canonical: abtem.visualize.widgets.ipywidgets_not_installed
:value: >
   'RuntimeError(...)'

```{autodoc2-docstring} abtem.visualize.widgets.ipywidgets_not_installed
:parser: rst
```

````

````{py:function} make_toggle_hkl_button(...)
:canonical: abtem.visualize.widgets.make_toggle_hkl_button

```{autodoc2-docstring} abtem.visualize.widgets.make_toggle_hkl_button
:parser: rst
```
````

````{py:function} slider_from_axes_metadata(...)
:canonical: abtem.visualize.widgets.slider_from_axes_metadata

```{autodoc2-docstring} abtem.visualize.widgets.slider_from_axes_metadata
:parser: rst
```
````
