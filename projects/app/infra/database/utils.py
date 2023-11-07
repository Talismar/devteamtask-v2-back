from sqlalchemy.orm import ColumnProperty, class_mapper


def attribute_names(sqlalchemy_class, with_relationship=False):
    return [
        prop.key
        for prop in class_mapper(sqlalchemy_class).iterate_properties
        if not with_relationship and isinstance(prop, ColumnProperty)
    ]
