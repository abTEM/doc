# {py:mod}`abtem.core.config`

```{py:module} abtem.core.config
```

```{autodoc2-docstring} abtem.core.config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`set <abtem.core.config.set>`
  - ```{autodoc2-docstring} abtem.core.config.set
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`refresh <abtem.core.config.refresh>`
  - ```{autodoc2-docstring} abtem.core.config.refresh
    :summary:
    ```
* - {py:obj}`get <abtem.core.config.get>`
  - ```{autodoc2-docstring} abtem.core.config.get
    :summary:
    ```
* - {py:obj}`update_defaults <abtem.core.config.update_defaults>`
  - ```{autodoc2-docstring} abtem.core.config.update_defaults
    :summary:
    ```
* - {py:obj}`check_deprecations <abtem.core.config.check_deprecations>`
  - ```{autodoc2-docstring} abtem.core.config.check_deprecations
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`no_default <abtem.core.config.no_default>`
  - ```{autodoc2-docstring} abtem.core.config.no_default
    :summary:
    ```
* - {py:obj}`config <abtem.core.config.config>`
  - ```{autodoc2-docstring} abtem.core.config.config
    :summary:
    ```
* - {py:obj}`config_lock <abtem.core.config.config_lock>`
  - ```{autodoc2-docstring} abtem.core.config.config_lock
    :summary:
    ```
* - {py:obj}`defaults <abtem.core.config.defaults>`
  - ```{autodoc2-docstring} abtem.core.config.defaults
    :summary:
    ```
* - {py:obj}`deprecations <abtem.core.config.deprecations>`
  - ```{autodoc2-docstring} abtem.core.config.deprecations
    :summary:
    ```
````

### API

````{py:data} no_default
:canonical: abtem.core.config.no_default
:value: >
   '__no_default__'

```{autodoc2-docstring} abtem.core.config.no_default
```

````

````{py:data} config
:canonical: abtem.core.config.config
:type: dict
:value: >
   None

```{autodoc2-docstring} abtem.core.config.config
```

````

````{py:data} config_lock
:canonical: abtem.core.config.config_lock
:value: >
   'Lock(...)'

```{autodoc2-docstring} abtem.core.config.config_lock
```

````

````{py:data} defaults
:canonical: abtem.core.config.defaults
:type: list[collections.abc.Mapping]
:value: >
   []

```{autodoc2-docstring} abtem.core.config.defaults
```

````

`````{py:class} set(arg: typing.Union[collections.abc.Mapping, None] = None, config: dict = config, lock: threading.Lock = config_lock, **kwargs)
:canonical: abtem.core.config.set

```{autodoc2-docstring} abtem.core.config.set
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.core.config.set.__init__
```

````{py:attribute} config
:canonical: abtem.core.config.set.config
:type: dict
:value: >
   None

```{autodoc2-docstring} abtem.core.config.set.config
```

````

`````

````{py:function} refresh(config: dict = config, defaults: list[collections.abc.Mapping] = defaults, **kwargs) -> None
:canonical: abtem.core.config.refresh

```{autodoc2-docstring} abtem.core.config.refresh
```
````

````{py:function} get(key: str, default: typing.Any = no_default, config: dict = config, override_with: typing.Any = None) -> typing.Any
:canonical: abtem.core.config.get

```{autodoc2-docstring} abtem.core.config.get
```
````

````{py:function} update_defaults(new: collections.abc.Mapping, config: dict = config, defaults: list[collections.abc.Mapping] = defaults) -> None
:canonical: abtem.core.config.update_defaults

```{autodoc2-docstring} abtem.core.config.update_defaults
```
````

````{py:data} deprecations
:canonical: abtem.core.config.deprecations
:type: dict[str, str | None]
:value: >
   None

```{autodoc2-docstring} abtem.core.config.deprecations
```

````

````{py:function} check_deprecations(key: str, deprecations: dict = deprecations) -> str
:canonical: abtem.core.config.check_deprecations

```{autodoc2-docstring} abtem.core.config.check_deprecations
```
````
