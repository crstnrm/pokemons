from rest_framework import serializers


def get_generic_serializer(entity):
    """ Create a new serializer class avoiding overwriting the previous one

    Parameters
    ----------
    model: class

    Returns
    -------
    A new GenericSerializer class
    """
    class GenericSerializer(serializers.Serializer):
        class Meta:
            model = entity
            fields = '__all__'

    return GenericSerializer
