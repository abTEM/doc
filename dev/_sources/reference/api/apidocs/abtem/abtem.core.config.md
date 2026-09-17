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
* - {py:obj}`collect <abtem.core.config.collect>`
  - ```{autodoc2-docstring} abtem.core.config.collect
    :parser: rst
    :summary:
    ```
* - {py:obj}`collect_env <abtem.core.config.collect_env>`
  - ```{autodoc2-docstring} abtem.core.config.collect_env
    :parser: rst
    :summary:
    ```
* - {py:obj}`collect_legacy_env <abtem.core.config.collect_legacy_env>`
  - ```{autodoc2-docstring} abtem.core.config.collect_legacy_env
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

* - {py:obj}`ENV_PREFIX <abtem.core.config.ENV_PREFIX>`
  - ```{autodoc2-docstring} abtem.core.config.ENV_PREFIX
    :parser: rst
    :summary:
    ```
* - {py:obj}`LEGACY_ENV_PREFIX <abtem.core.config.LEGACY_ENV_PREFIX>`
  - ```{autodoc2-docstring} abtem.core.config.LEGACY_ENV_PREFIX
    :parser: rst
    :summary:
    ```
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
* - {py:obj}`paths <abtem.core.config.paths>`
  - ```{autodoc2-docstring} abtem.core.config.paths
    :parser: rst
    :summary:
    ```
````

### API

````{py:data} ENV_PREFIX
:canonical: abtem.core.config.ENV_PREFIX
:value: >
   'ABTEM_'

```{autodoc2-docstring} abtem.core.config.ENV_PREFIX
:parser: rst
```

````

````{py:data} LEGACY_ENV_PREFIX
:canonical: abtem.core.config.LEGACY_ENV_PREFIX
:value: >
   'DASK_'

```{autodoc2-docstring} abtem.core.config.LEGACY_ENV_PREFIX
:parser: rst
```

````

````{py:function} check_deprecations(...) -> str
:canonical: abtem.core.config.check_deprecations

```{autodoc2-docstring} abtem.core.config.check_deprecations
:parser: rst
```
````

````{py:function} collect(...) -> dict
:canonical: abtem.core.config.collect

```{autodoc2-docstring} abtem.core.config.collect
:parser: rst
```
````

````{py:function} collect_env(...) -> dict
:canonical: abtem.core.config.collect_env

```{autodoc2-docstring} abtem.core.config.collect_env
:parser: rst
```
````

````{py:function} collect_legacy_env(...) -> dict
:canonical: abtem.core.config.collect_legacy_env

```{autodoc2-docstring} abtem.core.config.collect_legacy_env
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

````{py:function} get(...) -> typing.Any
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

````{py:data} paths
:canonical: abtem.core.config.paths
:value: >
   '_get_paths(...)'

```{autodoc2-docstring} abtem.core.config.paths
:parser: rst
```

````

````{py:function} refresh(...) -> None
:canonical: abtem.core.config.refresh

```{autodoc2-docstring} abtem.core.config.refresh
:parser: rst
```
````

`````{py:class} set(...)
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

````{py:function} update_defaults(...) -> None
:canonical: abtem.core.config.update_defaults

```{autodoc2-docstring} abtem.core.config.update_defaults
:parser: rst
```
````
