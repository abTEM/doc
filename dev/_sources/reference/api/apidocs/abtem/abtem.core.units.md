# {py:mod}`abtem.core.units`

```{py:module} abtem.core.units
```

```{autodoc2-docstring} abtem.core.units
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`format_units <abtem.core.units.format_units>`
  - ```{autodoc2-docstring} abtem.core.units.format_units
    :summary:
    ```
* - {py:obj}`get_conversion_factor <abtem.core.units.get_conversion_factor>`
  - ```{autodoc2-docstring} abtem.core.units.get_conversion_factor
    :summary:
    ```
* - {py:obj}`validate_units <abtem.core.units.validate_units>`
  - ```{autodoc2-docstring} abtem.core.units.validate_units
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`units_type <abtem.core.units.units_type>`
  - ```{autodoc2-docstring} abtem.core.units.units_type
    :summary:
    ```
````

### API

````{py:function} format_units(units: typing.Optional[str], use_tex: typing.Optional[bool] = None) -> str
:canonical: abtem.core.units.format_units

```{autodoc2-docstring} abtem.core.units.format_units
```
````

````{py:function} get_conversion_factor(units: typing.Optional[str] = None, old_units: typing.Optional[str] = None, energy: typing.Optional[float] = None) -> float
:canonical: abtem.core.units.get_conversion_factor

```{autodoc2-docstring} abtem.core.units.get_conversion_factor
```
````

````{py:data} units_type
:canonical: abtem.core.units.units_type
:value: >
   None

```{autodoc2-docstring} abtem.core.units.units_type
```

````

````{py:function} validate_units(units: typing.Optional[str] = None, old_units: typing.Optional[str] = None) -> typing.Optional[str]
:canonical: abtem.core.units.validate_units

```{autodoc2-docstring} abtem.core.units.validate_units
```
````
