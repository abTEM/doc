# autodoc2 experiment

## Probe, default (rST) docstring parsing

```{autodoc2-object} abtem.waves.Probe
render_plugin = "myst"
no_index = true
docstring_parser_regexes = [
    [".*", "rst"],
]
```

## Probe, napoleon-bridge docstring parsing

```{autodoc2-object} abtem.waves.Probe
render_plugin = "myst"
no_index = true
docstring_parser_regexes = [
    [".*", "napoleon_parser"],
]
```
