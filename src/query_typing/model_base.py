from dataclasses import dataclass
from typing import List, TypeVar, Generic, Tuple, Dict, Any

@dataclass
class ModelBase:
    id: int

T = TypeVar('T', bound='ModelBase')

class QueryBaseMeta(type):
    def __init__(self, name: str, bases: Tuple[type, ...], attrs: Dict[str, Any]) -> None:
        super().__init__(name, bases, attrs)
        if name != 'QueryBase':
            self.NotFoundError = type(f'{name}.NotFoundError', (QueryBase.NotFoundError, ), {})

@dataclass
class QueryBase(Generic[T], metaclass=QueryBaseMeta):
    class NotFoundError(Exception):
        pass

    models: List[T]

    def __init__(self, models: List[T]):
        self.models = models

    def get(self, id: int) -> T:
        for model in self.models:
            if model.id == id:
                return model
        raise self.NotFoundError()