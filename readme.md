# New Zealand Business Number

A Python library for interacting with New Zealand Business Number services.

## Installation

```
$ pip install nzbn
```

## Example Usage

### Get a list of abbreviated entities

```python
from nzbn import AbbreviatedEntity

entities: List[AbbreciatedEntity] = AbbreviatedEntity.retrieve_many(
    access_token="your nzbn API access token",
    search_text="some entity name",
    page=0,    # defaults to 0
    limit=20   # per page count, defaults to 20
)
```

### Get detailed data about an entity

```python
from nzbn import Entity

entity: Entity = Entity.retrieve(
    access_token="your nzbn API access token",
    nzbn="9429049541410",
    sandbox=False  # defaults to False
)
```
