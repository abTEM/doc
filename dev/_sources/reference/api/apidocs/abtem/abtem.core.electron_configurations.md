# {py:mod}`abtem.core.electron_configurations`

```{py:module} abtem.core.electron_configurations
```

```{autodoc2-docstring} abtem.core.electron_configurations
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`config_str_to_config_tuples <abtem.core.electron_configurations.config_str_to_config_tuples>`
  - ```{autodoc2-docstring} abtem.core.electron_configurations.config_str_to_config_tuples
    :summary:
    ```
* - {py:obj}`config_tuples_to_config_str <abtem.core.electron_configurations.config_tuples_to_config_str>`
  - ```{autodoc2-docstring} abtem.core.electron_configurations.config_tuples_to_config_str
    :summary:
    ```
* - {py:obj}`remove_electron_from_config_str <abtem.core.electron_configurations.remove_electron_from_config_str>`
  - ```{autodoc2-docstring} abtem.core.electron_configurations.remove_electron_from_config_str
    :summary:
    ```
* - {py:obj}`aufbau <abtem.core.electron_configurations.aufbau>`
  - ```{autodoc2-docstring} abtem.core.electron_configurations.aufbau
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`electron_configurations <abtem.core.electron_configurations.electron_configurations>`
  - ```{autodoc2-docstring} abtem.core.electron_configurations.electron_configurations
    :summary:
    ```
* - {py:obj}`azimuthal_number <abtem.core.electron_configurations.azimuthal_number>`
  - ```{autodoc2-docstring} abtem.core.electron_configurations.azimuthal_number
    :summary:
    ```
* - {py:obj}`azimuthal_letter <abtem.core.electron_configurations.azimuthal_letter>`
  - ```{autodoc2-docstring} abtem.core.electron_configurations.azimuthal_letter
    :summary:
    ```
````

### API

````{py:data} electron_configurations
:canonical: abtem.core.electron_configurations.electron_configurations
:value: >
   None

```{autodoc2-docstring} abtem.core.electron_configurations.electron_configurations
```

````

````{py:data} azimuthal_number
:canonical: abtem.core.electron_configurations.azimuthal_number
:value: >
   None

```{autodoc2-docstring} abtem.core.electron_configurations.azimuthal_number
```

````

````{py:data} azimuthal_letter
:canonical: abtem.core.electron_configurations.azimuthal_letter
:value: >
   None

```{autodoc2-docstring} abtem.core.electron_configurations.azimuthal_letter
```

````

````{py:function} config_str_to_config_tuples(config_str: str) -> list[tuple]
:canonical: abtem.core.electron_configurations.config_str_to_config_tuples

```{autodoc2-docstring} abtem.core.electron_configurations.config_str_to_config_tuples
```
````

````{py:function} config_tuples_to_config_str(config_tuples: list[tuple]) -> str
:canonical: abtem.core.electron_configurations.config_tuples_to_config_str

```{autodoc2-docstring} abtem.core.electron_configurations.config_tuples_to_config_str
```
````

````{py:function} remove_electron_from_config_str(config_str: str, n: int, ell: int) -> str
:canonical: abtem.core.electron_configurations.remove_electron_from_config_str

```{autodoc2-docstring} abtem.core.electron_configurations.remove_electron_from_config_str
```
````

````{py:function} aufbau(n_max: int = 7) -> list[tuple[int, int, int]]
:canonical: abtem.core.electron_configurations.aufbau

```{autodoc2-docstring} abtem.core.electron_configurations.aufbau
```
````
