# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

* Create parent and child classes
* Use inheritance to extend functionality
* Understand class and instance namespaces
* Demonstrate shallow and deep copying
* Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.



# Implementation Summary



I created a Computer parent class with a class variable, instance variables for brand and processor, a constructor, and a method that displayed object information.

I created a GamingComputer child class that inherited from Computer. The child class added its own class variable, GPU and RAM instance variables, a new gaming\_ready() method, and an overridden display\_info() method.

I demonstrated class and instance namespaces by creating two GamingComputer objects, accessing class variables through both the class and an object, adding an owner attribute to only one object, and displaying the object and class namespaces using \_\_dict\_\_.

I demonstrated shallow and deep copying using a dictionary that contained a nested list of computer components. After modifying the original nested list, the shallow copy reflected the change while the deep copy remained unchanged.

As a student-created extension, I added the gaming\_ready() method to the GamingComputer class.

