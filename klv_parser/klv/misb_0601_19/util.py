from .metadata import Metadata
from .uas_datalink_local_set import UasDatalinkLocalSet
import inspect


def build_class_map():
    # Find all classes in the current module that are subclasses of Metadata
    metadata_classes = [
        cls
        for _, cls in inspect.getmembers(__import__(__name__), inspect.isclass)
        if issubclass(cls, Metadata) and cls is not Metadata
    ]

    # Create a mapping of Enum members to corresponding classes
    return {
        enum_member: cls
        for enum_member, cls in zip(UasDatalinkLocalSet, metadata_classes)
    }


def parse_class(key, data, length):
    class_map = build_class_map()  # Dynamically build the class map

    # Find the enum corresponding to the key
    enum_member = next(
        (enum for enum in UasDatalinkLocalSet if enum.value == key), None
    )

    if enum_member is not None and enum_member in class_map:
        # Instantiate the appropriate Metadata subclass
        metadata_class = class_map[enum_member]
        return metadata_class(data, length, key)

    raise ValueError(f"No class found for key: {key}")
