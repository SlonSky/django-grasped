"""
Boundary part of current component.

In UML words, here you describe classes for
providing and consuming interfaces, composing
so-called "joints" - bound consuming-providing
interfaces between subsystems.

In this way, consuming boundary from one django
application can use providing boundary from other.

This is only place, where django applications
can interact.

With growth of modules, feel free to split them
to semantic sub modules, placing in corresponding
consuming and providing packages.

Providing module can use internal django application
classes with respect to N-tier architecture and
abstraction principle. Do not mix levels of abstraction
in single class, optionally, you could create separated
service definitely for uses in providing interface
"""
