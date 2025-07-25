List Operations in Python
A hands-on demonstration of fundamental list manipulations in Python.

Project Overview
This Python script showcases essential list operations through a structured workflow:

Initializing an empty list

Appending multiple elements

Inserting elements at specific positions

Extending with another list

Removing elements

Sorting and searching

Key Operations Demonstrated
Operation	Method Used	Example	Result
Create empty list	[]	my_list = []	[]
Add elements	append()	my_list.append(10)	[10, 20, 30, 40]
Insert element	insert()	my_list.insert(1, 15)	[10, 15, 20, ...]
Merge lists	extend()	my_list.extend([50, 60, 70])	[..., 50, 60, 70]
Remove element	pop()	my_list.pop()	Removes 70
Sort elements	sort()	my_list.sort()	Ascending order
Locate element	index()	my_list.index(30)	Returns 3
Sample Output
python
[10, 20, 30, 40] → After appending  
[10, 15, 20, 30, 40] → After inserting 15  
[10, 15, 20, 30, 40, 50, 60, 70] → After extending  
[10, 15, 20, 30, 40, 50, 60] → After pop()  
[10, 15, 20, 30, 40, 50, 60] → After sorting  
Index of 30: 3 → Final search result
Educational Value
Illustrates mutability of Python lists

Teaches method chaining potential (e.g., sorted(my_list).index(30))

Highlights zero-based indexing in search operations

Extensions & Challenges
Reverse the list without using reverse()

Remove all occurrences of a value (e.g., duplicates of 20)

Implement a custom sorting key (e.g., by string length if elements were words)