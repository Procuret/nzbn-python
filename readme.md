# New Zealand Business Number Python Library

A Python library for interacting with New Zealand Business Number (NZBN)
services provided by the New Zealand Ministry of Business, Innovation, and
Employment (MBIE).

## Installation

```
$ pip install nzbn
```

## Nomenclature

The MBIE NZBN API has two main "Entity" types, where "Entity" is used to refer
to a legal person recorded in the New Zealand Business Register (NZBR). The
firs is included in vector results from search queries, and is called
`SearchEntity`. The second is returned in response to requests for a specific
NBZN, and is called `FullEntity`.

The authors of this library find referring to these as `AbbreviatedEntity`
and `Entity` to be more natural, and therefore those names are used. You can
also use `SearchEntity` and `FullEntity` in your Python code, as those names
are effectively type-aliases for `AbbreviatedEntity` and `Entity`.

## Example Usage

### Get a list of abbreviated entities

```python
from nzbn import AbbreviatedEntity

entities: List[AbbreviatedEntity] = AbbreviatedEntity.retrieve_many(
    api_key="your nzbn API access token",
    search_text="some entity name",
    page=0,    # defaults to 0
    limit=20   # per page count, defaults to 20
)
```

### Get detailed data about an entity

```python
from nzbn import Entity

entity: Optional[Entity] = Entity.retrieve(
    api_key="your nzbn API access token",
    nzbn="9429049541410",
    sandbox=False  # defaults to False
)
```
