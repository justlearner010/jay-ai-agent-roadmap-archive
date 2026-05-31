



## 一句话解释

 

用自己的话解释这个概念是什么。

## 为什么重要

说明它和当前项目、AI Agent、RAG、后端工程或科班基础有什么关系。


## 概念及代码

### Tuple
```python
def main():
	student = get_student()
	printf(f"{student[0]} from {student[1]}")
# student[0]-> name student[1] -> house 
def get_student():
	name = input("Name)
	house = input("House")
	
	return （name,house）
	#return [name,house] it it mutable and you can assign new value
```

tuple:把几个值放在一起
加上括号会更加的明显
**immutable:you can not change the value**

### Dictionary
```python

def main():
	student = get_student()
	print(f"{student['name']} from {student['house']}")
	
def get_student():
	student = {}
	student["name"] = input("Name")
	student["house"] = input("House")
	return student
	#return {"name":name,"house":house} may be more readable but longer
```


### class

invent your own datatype ,it's important feature in object-oriented programming
```python
class Student:

def main():
	student = get_student()
	print(f"{student.name} from {student.house}")
	
def get_student():

	name = input("Name)
	house = input("house)
	student = Student(name,house)
	
	return student
	
	

```

### object

class is a blueprint or model to create an entity /object

define you own class(datatype) ->create your own object



### methods

functions allow to behavior special methods

```python
class Student:
	def __init__(self,name,house):
		if not name:
			#how to signal error?
		#instance methods,initialize the Class
		self.name = name #create new attribute link the variable 
		self.house = house
		#let variable into object
```
passing two values in Student object
instance 


### raise
主动报告错误
```python
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["China","America","Japan"]
        

        self.name = name
        self.house = house
```

### `__str__`

`__str__`是一个特殊方法，作用是：规定“这个对象被当成字符串时应该显示成什么样”
```python
class Student:
	def __str__(self):
		return f"{self.name} from {self.house}"
		# return "你想显示的字符串"
	
```

## 常见错误

- 

## 我今天的理解



## 后续问题

- 

