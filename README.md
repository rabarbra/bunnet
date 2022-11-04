[![shields badge](https://shields.io/badge/-docs-blue)](https://roman-right.github.io/bunnet/)
[![pypi](https://img.shields.io/pypi/v/bunnet.svg)](https://pypi.python.org/pypi/bunnet)

[![Bunnet](docs/assets/1.png)](https://github.com/roman-right/bunnet)

## Overview

[Bunnet](https://github.com/roman-right/bunnet) - is a Python object-document mapper (ODM) for MongoDB. It is synchronous fork of [Beanie ODM](https://github.com/roman-right/beanie).

When using Bunnet each database collection has a corresponding `Document` that
is used to interact with that collection. In addition to retrieving data,
Bunnet allows you to add, update, or delete documents from the collection as
well.

Bunnet saves you time by removing boilerplate code, and it helps you focus on
the parts of your app that actually matter.

## Installation

### PIP

```shell
pip install bunnet
```

### Poetry

```shell
poetry add bunnet
```
## Example

```python
from typing import Optional

from pymongo import MongoClient
from pydantic import BaseModel

from bunnet import Document, Indexed, init_bunnet


class Category(BaseModel):
    name: str
    description: str


class Product(Document):
    name: str                          # You can use normal types just like in pydantic
    description: Optional[str] = None
    price: Indexed(float)              # You can also specify that a field should correspond to an index
    category: Category                 # You can include pydantic models as well



# Beanie uses Pymongo client under the hood 
client = MongoClient("mongodb://user:pass@host:27017")

# Initialize bunnet with the Product document class
init_bunnet(database=client.db_name, document_models=[Product])

chocolate = Category(name="Chocolate", description="A preparation of roasted and ground cacao seeds.")
# Beanie documents work just like pydantic models
tonybar = Product(name="Tony's", price=5.95, category=chocolate)
# And can be inserted into the database
tonybar.insert() 

# You can find documents with pythonic syntax
product = Product.find_one(Product.price < 10).run()

# And update them
product.set({Product.name:"Gold bar"})

```

## Links

### Documentation

- **[Doc](https://roman-right.github.io/bunnet/)** - Tutorial, API documentation, and development guidelines.

### Resources

- **[GitHub](https://github.com/roman-right/bunnet)** - GitHub page of the
  project
- **[Changelog](https://roman-right.github.io/bunnet/changelog)** - list of all
  the valuable changes
- **[Discord](https://discord.gg/ZTTnM7rMaz)** - ask your questions, share
  ideas or just say `Hello!!`

----
Supported by [JetBrains](https://jb.gg/OpenSource)

[![JetBrains](https://raw.githubusercontent.com/roman-right/beanie/main/assets/logo/jetbrains.svg)](https://jb.gg/OpenSource)
