# {py:mod}`abtem.core.config`

```{py:module} abtem.core.config
```

```{autodoc2-docstring} abtem.core.config
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`set <abtem.core.config.set>`
  - ```{autodoc2-docstring} abtem.core.config.set
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`check_deprecations <abtem.core.config.check_deprecations>`
  - ```{autodoc2-docstring} abtem.core.config.check_deprecations
    :parser: rst
    :summary:
    ```
* - {py:obj}`get <abtem.core.config.get>`
  - ```{autodoc2-docstring} abtem.core.config.get
    :parser: rst
    :summary:
    ```
* - {py:obj}`refresh <abtem.core.config.refresh>`
  - ```{autodoc2-docstring} abtem.core.config.refresh
    :parser: rst
    :summary:
    ```
* - {py:obj}`update_defaults <abtem.core.config.update_defaults>`
  - ```{autodoc2-docstring} abtem.core.config.update_defaults
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`config <abtem.core.config.config>`
  - ```{autodoc2-docstring} abtem.core.config.config
    :parser: rst
    :summary:
    ```
* - {py:obj}`config_lock <abtem.core.config.config_lock>`
  - ```{autodoc2-docstring} abtem.core.config.config_lock
    :parser: rst
    :summary:
    ```
* - {py:obj}`defaults <abtem.core.config.defaults>`
  - ```{autodoc2-docstring} abtem.core.config.defaults
    :parser: rst
    :summary:
    ```
* - {py:obj}`deprecations <abtem.core.config.deprecations>`
  - ```{autodoc2-docstring} abtem.core.config.deprecations
    :parser: rst
    :summary:
    ```
* - {py:obj}`no_default <abtem.core.config.no_default>`
  - ```{autodoc2-docstring} abtem.core.config.no_default
    :parser: rst
    :summary:
    ```
````

### API

````{py:function} check_deprecations(key: str, deprecations: dict = deprecations) -> str
:canonical: abtem.core.config.check_deprecations

```{autodoc2-docstring} abtem.core.config.check_deprecations
:parser: rst
```
````

````{py:data} config
:canonical: abtem.core.config.config
:type: dict
:value: >
   None

```{autodoc2-docstring} abtem.core.config.config
:parser: rst
```

````

````{py:data} config_lock
:canonical: abtem.core.config.config_lock
:value: >
   'Lock(...)'

```{autodoc2-docstring} abtem.core.config.config_lock
:parser: rst
```

````

````{py:data} defaults
:canonical: abtem.core.config.defaults
:type: list[collections.abc.Mapping]
:value: >
   []

```{autodoc2-docstring} abtem.core.config.defaults
:parser: rst
```

````

````{py:data} deprecations
:canonical: abtem.core.config.deprecations
:type: dict[str, str | None]
:value: >
   None

```{autodoc2-docstring} abtem.core.config.deprecations
:parser: rst
```

````

````{py:function} get(key: str, default: typing.Any = no_default, config: dict = config, override_with: typing.Any = None) -> typing.Any
:canonical: abtem.core.config.get

```{autodoc2-docstring} abtem.core.config.get
:parser: rst
```
````

````{py:data} no_default
:canonical: abtem.core.config.no_default
:value: >
   '__no_default__'

```{autodoc2-docstring} abtem.core.config.no_default
:parser: rst
```

````

````{py:function} refresh(config: dict = config, defaults: list[collections.abc.Mapping] = defaults, **kwargs) -> None
:canonical: abtem.core.config.refresh

```{autodoc2-docstring} abtem.core.config.refresh
:parser: rst
```
````

`````{py:class} set(arg: typing.Union[collections.abc.Mapping, None] = None, config: dict = config, lock: threading.Lock = config_lock, **kwargs)
:canonical: abtem.core.config.set

```{autodoc2-docstring} abtem.core.config.set
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.core.config.set.__init__
:parser: rst
```

````{py:attribute} config
:canonical: abtem.core.config.set.config
:type: dict
:value: >
   None

```{autodoc2-docstring} abtem.core.config.set.config
:parser: rst
```

````

`````

````{py:function} update_defaults(new: collections.abc.Mapping, config: dict = config, defaults: list[collections.abc.Mapping] = defaults) -> None
:canonical: abtem.core.config.update_defaults

```{autodoc2-docstring} abtem.core.config.update_defaults
:parser: rst
```
````
