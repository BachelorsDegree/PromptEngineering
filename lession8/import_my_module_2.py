import courses
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("test", "D:\PythonProjects\PromptEngineering\lession8\courses\test.py")
test = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = test
spec.loader.exec_module(test)

courses.python.hello("Вася")
print(courses.test)  # This should show you the module, not a string
courses.test.divide(8, 4)
print(dir(courses))


