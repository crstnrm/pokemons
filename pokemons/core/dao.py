from abc import ABC


class GenericDAO(ABC):

    def __init__(self):
        self._model = None

    @property
    def model(self):
        if self._model is None:
            raise NotImplementedError("Subclasses should define a model")
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    def bulk_create(self, raw_data):
        objs = [self.model(**data) for data in raw_data]
        return self.model.objects.bulk_create(objs)

    def data(self):
        return self.model.objects.all()

    def find(self, **kwargs):
        return self.model.objects.filter(**kwargs)