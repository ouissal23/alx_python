def is_kind_of_class(obj, a_class):
    """returns True if object is an instance of the class or of a class that inherited from"""
    if issubclass(type(obj),a_class):
        return True
    else:
        return False
    