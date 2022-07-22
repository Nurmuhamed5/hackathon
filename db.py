import json
from typing import List, Optional, Type
from models import BaseModel, Car


class DB:
    model: Type[BaseModel]

    def create(self, obj: BaseModel):
        models = self.get_object_list()
        obj.id = self._get_id(models)
        
        with open(self.model.FILE, "w") as file:
            models = [obj.to_json() for obj in models]
            models.append(obj.to_json())
            file.write(json.dumps(models))

    def get_by_id(self, id: int) -> Optional[BaseModel]:
        for obj in self.get_object_list():
            if obj.id == id:
                return obj
        return None

    def get_object_list(self) -> List[BaseModel]:
        with open(self.model.FILE, "r") as file:
            models = json.loads(file.read())
            return [self.model.from_json(obj) for obj in models]

    def _get_id(self, models: list):
        models = sorted(models, key=lambda e: e.id)
        return models[-1].id + 1 if len(models) > 0 else 1

    def delete(self, id: int):
        objs = self.get_object_list()
        objs = [obj for obj in objs if obj.id != id]
        with open(self.model.FILE, "w") as file:
            models = [obj.to_json() for obj in objs]
            file.write(json.dumps(models))

    def update(self, obj: BaseModel):
        objs = self.get_object_list()
        objs = [o for o in objs if o.id != obj.id]
        objs.append(obj)
        with open(self.model.FILE, "w") as file:
            models = [obj.to_json() for obj in objs]
            file.write(json.dumps(models))


class DBCar(DB):
    model = Car
