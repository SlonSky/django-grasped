"""
This is Data access layer.

Describe here your Django models and
Django custom model managers.

Split your models module as it will grow up.

Classes from this package describe how to
access, store and manipulate on data.

DO NOT implement here business logic, only
operations with data storages.

As recommendation, you have to create wrapper
classes for Django model managers with methods
for various operations on data, to encapsulate
working with Django model managers and its methods.
This practice helps you to separate features of
how Django model managers work from Service layer.

Short example:
myservice.py
def do_use_case_stuff(var1, var2):
    ...
    specific_manager = MyManagerWrapper()
    data = specific_manager.find_entities_with_common(var1, var2)
    ...
    specific_manager.examine_entity_not_corrupted(data)
    ...

You call encapsulated methods not worrying, which
filtrating on Django model manager you have execute,
which related models you have to use, etc.
"""
