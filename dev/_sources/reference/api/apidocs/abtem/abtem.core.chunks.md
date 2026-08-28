# {py:mod}`abtem.core.chunks`

```{py:module} abtem.core.chunks
```

```{autodoc2-docstring} abtem.core.chunks
:parser: rst
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`assert_chunks_match_shape <abtem.core.chunks.assert_chunks_match_shape>`
  - ```{autodoc2-docstring} abtem.core.chunks.assert_chunks_match_shape
    :parser: rst
    :summary:
    ```
* - {py:obj}`check_chunks_match_shape_length <abtem.core.chunks.check_chunks_match_shape_length>`
  - ```{autodoc2-docstring} abtem.core.chunks.check_chunks_match_shape_length
    :parser: rst
    :summary:
    ```
* - {py:obj}`chunk_ranges <abtem.core.chunks.chunk_ranges>`
  - ```{autodoc2-docstring} abtem.core.chunks.chunk_ranges
    :parser: rst
    :summary:
    ```
* - {py:obj}`equal_sized_chunks <abtem.core.chunks.equal_sized_chunks>`
  - ```{autodoc2-docstring} abtem.core.chunks.equal_sized_chunks
    :parser: rst
    :summary:
    ```
* - {py:obj}`fill_in_chunk_sizes <abtem.core.chunks.fill_in_chunk_sizes>`
  - ```{autodoc2-docstring} abtem.core.chunks.fill_in_chunk_sizes
    :parser: rst
    :summary:
    ```
* - {py:obj}`generate_chunks <abtem.core.chunks.generate_chunks>`
  - ```{autodoc2-docstring} abtem.core.chunks.generate_chunks
    :parser: rst
    :summary:
    ```
* - {py:obj}`is_tuple_of_ints <abtem.core.chunks.is_tuple_of_ints>`
  - ```{autodoc2-docstring} abtem.core.chunks.is_tuple_of_ints
    :parser: rst
    :summary:
    ```
* - {py:obj}`is_tuple_of_ints_or_tuple_of_ints <abtem.core.chunks.is_tuple_of_ints_or_tuple_of_ints>`
  - ```{autodoc2-docstring} abtem.core.chunks.is_tuple_of_ints_or_tuple_of_ints
    :parser: rst
    :summary:
    ```
* - {py:obj}`is_tuple_of_ints_or_tuple_of_tuple_of_ints <abtem.core.chunks.is_tuple_of_ints_or_tuple_of_tuple_of_ints>`
  - ```{autodoc2-docstring} abtem.core.chunks.is_tuple_of_ints_or_tuple_of_tuple_of_ints
    :parser: rst
    :summary:
    ```
* - {py:obj}`is_tuple_of_tuple_of_ints <abtem.core.chunks.is_tuple_of_tuple_of_ints>`
  - ```{autodoc2-docstring} abtem.core.chunks.is_tuple_of_tuple_of_ints
    :parser: rst
    :summary:
    ```
* - {py:obj}`is_validated_chunks <abtem.core.chunks.is_validated_chunks>`
  - ```{autodoc2-docstring} abtem.core.chunks.is_validated_chunks
    :parser: rst
    :summary:
    ```
* - {py:obj}`iterate_chunk_ranges <abtem.core.chunks.iterate_chunk_ranges>`
  - ```{autodoc2-docstring} abtem.core.chunks.iterate_chunk_ranges
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_chunks <abtem.core.chunks.validate_chunks>`
  - ```{autodoc2-docstring} abtem.core.chunks.validate_chunks
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Chunks <abtem.core.chunks.Chunks>`
  - ```{autodoc2-docstring} abtem.core.chunks.Chunks
    :parser: rst
    :summary:
    ```
* - {py:obj}`ChunksTuple <abtem.core.chunks.ChunksTuple>`
  - ```{autodoc2-docstring} abtem.core.chunks.ChunksTuple
    :parser: rst
    :summary:
    ```
* - {py:obj}`ValidatedChunks <abtem.core.chunks.ValidatedChunks>`
  - ```{autodoc2-docstring} abtem.core.chunks.ValidatedChunks
    :parser: rst
    :summary:
    ```
````

### API

````{py:data} Chunks
:canonical: abtem.core.chunks.Chunks
:value: >
   None

```{autodoc2-docstring} abtem.core.chunks.Chunks
:parser: rst
```

````

````{py:data} ChunksTuple
:canonical: abtem.core.chunks.ChunksTuple
:value: >
   None

```{autodoc2-docstring} abtem.core.chunks.ChunksTuple
:parser: rst
```

````

````{py:data} ValidatedChunks
:canonical: abtem.core.chunks.ValidatedChunks
:value: >
   None

```{autodoc2-docstring} abtem.core.chunks.ValidatedChunks
:parser: rst
```

````

````{py:function} assert_chunks_match_shape(shape: tuple[int, ...], chunks: abtem.core.chunks.ValidatedChunks) -> None
:canonical: abtem.core.chunks.assert_chunks_match_shape

```{autodoc2-docstring} abtem.core.chunks.assert_chunks_match_shape
:parser: rst
```
````

````{py:function} check_chunks_match_shape_length(shape: tuple[int, ...], chunks: abtem.core.chunks.Chunks) -> None
:canonical: abtem.core.chunks.check_chunks_match_shape_length

```{autodoc2-docstring} abtem.core.chunks.check_chunks_match_shape_length
:parser: rst
```
````

````{py:function} chunk_ranges(chunks: abtem.core.chunks.ValidatedChunks) -> tuple[tuple[tuple[int, int], ...], ...]
:canonical: abtem.core.chunks.chunk_ranges

```{autodoc2-docstring} abtem.core.chunks.chunk_ranges
:parser: rst
```
````

````{py:function} equal_sized_chunks(num_items: int, num_chunks: typing.Optional[int] = None, chunk_size: typing.Optional[int] = None) -> tuple[int, ...]
:canonical: abtem.core.chunks.equal_sized_chunks

```{autodoc2-docstring} abtem.core.chunks.equal_sized_chunks
:parser: rst
```
````

````{py:function} fill_in_chunk_sizes(shape: tuple[int, ...], chunks: tuple[int | tuple[int, ...], ...]) -> abtem.core.chunks.ValidatedChunks
:canonical: abtem.core.chunks.fill_in_chunk_sizes

```{autodoc2-docstring} abtem.core.chunks.fill_in_chunk_sizes
:parser: rst
```
````

````{py:function} generate_chunks(num_items: int, num_chunks: typing.Optional[int] = None, chunks: typing.Optional[int] = None, start: int = 0) -> typing.Generator[tuple[int, int], None, None]
:canonical: abtem.core.chunks.generate_chunks

```{autodoc2-docstring} abtem.core.chunks.generate_chunks
:parser: rst
```
````

````{py:function} is_tuple_of_ints(x: abtem.core.chunks.Chunks) -> typing.TypeGuard[tuple[int, ...]]
:canonical: abtem.core.chunks.is_tuple_of_ints

```{autodoc2-docstring} abtem.core.chunks.is_tuple_of_ints
:parser: rst
```
````

````{py:function} is_tuple_of_ints_or_tuple_of_ints(x: abtem.core.chunks.Chunks) -> typing.TypeGuard[tuple[tuple[int, ...], ...]]
:canonical: abtem.core.chunks.is_tuple_of_ints_or_tuple_of_ints

```{autodoc2-docstring} abtem.core.chunks.is_tuple_of_ints_or_tuple_of_ints
:parser: rst
```
````

````{py:function} is_tuple_of_ints_or_tuple_of_tuple_of_ints(x: abtem.core.chunks.Chunks) -> typing.TypeGuard[tuple[int | tuple[int, ...], ...]]
:canonical: abtem.core.chunks.is_tuple_of_ints_or_tuple_of_tuple_of_ints

```{autodoc2-docstring} abtem.core.chunks.is_tuple_of_ints_or_tuple_of_tuple_of_ints
:parser: rst
```
````

````{py:function} is_tuple_of_tuple_of_ints(x: abtem.core.chunks.Chunks) -> typing.TypeGuard[tuple[tuple[int, ...], ...]]
:canonical: abtem.core.chunks.is_tuple_of_tuple_of_ints

```{autodoc2-docstring} abtem.core.chunks.is_tuple_of_tuple_of_ints
:parser: rst
```
````

````{py:function} is_validated_chunks(x: abtem.core.chunks.Chunks) -> typing.TypeGuard[abtem.core.chunks.ValidatedChunks]
:canonical: abtem.core.chunks.is_validated_chunks

```{autodoc2-docstring} abtem.core.chunks.is_validated_chunks
:parser: rst
```
````

````{py:function} iterate_chunk_ranges(chunks: abtem.core.chunks.ValidatedChunks)
:canonical: abtem.core.chunks.iterate_chunk_ranges

```{autodoc2-docstring} abtem.core.chunks.iterate_chunk_ranges
:parser: rst
```
````

````{py:function} validate_chunks(shape: tuple[int, ...], chunks: abtem.core.chunks.Chunks, max_elements: int | str = 'auto', dtype: typing.Optional[numpy.dtype] = None, device: str = 'cpu') -> abtem.core.chunks.ValidatedChunks
:canonical: abtem.core.chunks.validate_chunks

```{autodoc2-docstring} abtem.core.chunks.validate_chunks
:parser: rst
```
````
