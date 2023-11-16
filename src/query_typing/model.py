from dataclasses import dataclass
from query_typing.model_base import ModelBase, QueryBase

@dataclass
class EmployeeModel(ModelBase):
    name: str
    department_id: int | None
    
        

class EmployeeQuery(QueryBase[EmployeeModel]):
    pass


@dataclass
class DepartmentModel(ModelBase):
    name: str
    parent_id: int | None


class DepartmentQuery(QueryBase[DepartmentModel]):
    pass