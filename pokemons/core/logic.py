from abc import ABC
from .serializers import get_generic_serializer


class GenericLogic(ABC):

    def __init__(self):
        self._dao = None
        self._serializer = None

    @property
    def dao(self):
        if self._dao is None:
            raise NotImplementedError("Subclasses must be define dao")
        return self._dao

    @dao.setter
    def dao(self, value):
        self._dao = value

    @property
    def serializer(self):
        if self._serializer is None:
            return get_generic_serializer(self.dao.model)
        return self._serializer

    @serializer.setter
    def serializer(self, value):
        self._serializer = value

    def create(self, instance=None, partial=False, **kwargs):
        """ Create a model in the database

        Parameters
        ----------
        kwargs : dict
        Required attributes of entity

        Returns
        -------
        A instance
        """
        serializer = self.serializer(instance, data=kwargs, partial=partial)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
        return instance

    def bulk_create(self, raw_data):
        """ Create several records in the database

        Parameters
        ----------
        raw_data : list
        Required attributes of entity

        Returns
        -------
        Multiples instances of model
        """
        return self.dao.bulk_create(raw_data)

    def data(self):
        """ Get all records

        Returns
        -------
        A Querysets list
        """
        return self.dao.data()

    def serialize(self, instances, **kwargs):
        """Serialize one or multiple objects"""
        return self.serializer(instances, **kwargs).data
