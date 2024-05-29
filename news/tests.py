from django.test import TestCase

# Create your tests here.
def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

parameters = {'param1': 'value1', 'param2': 'value2'}
example_function(**parameters)
