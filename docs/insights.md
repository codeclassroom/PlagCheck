# Insights

PlagCheck provides algorithmic analysis of Moss results.

### Terminologies

### 1. Node
Nodes are results returned by Moss i.e every
individual file.

### 2. Tags
Tags are roles which a file serves i.e. a tag is
a potential distributor or potential culprit or
both.

### 3. M-group
m-groups (moss-groups) are groups of solution which have similar code.
For example A student who solves a programming problem may share their
solution with 3 of his/her friends, that is a single m-group with 4 nodes.

For example if you run [demo.py](https://github.com/codeclassroom/PlagCheck/blob/master/demo.py), `insights()` will return the following data:
```java

{'DCtoC Paths': [('testfiles/test_java5.java', 'testfiles/test_java2.java'),
                 ('testfiles/test_java4.java', 'testfiles/test_java2.java')],
 'DtoC Paths': [('testfiles/test_java3.java', 'testfiles/test_java2.java'),
                ('testfiles/test_java3.java', 'testfiles/test_java.java'),
                ('testfiles/test_java7.java', 'testfiles/test_java6.java')],
 'DtoDC Paths': [('testfiles/test_java3.java', 'testfiles/test_java5.java'),
                 ('testfiles/test_java3.java', 'testfiles/test_java4.java')]}

```

This analysis can be visualized into following _Disconnected Directed Graph_

![moss results](https://drive.google.com/uc?export=view&id=1Lc8obgjihfo7EGimn300mTtqfmHK0Zem)

We assign Tags to every individual Node.

1. D - Distributor
Student(s) who distributed their
code in a group.
2. C - Culprit
Student(s) who copied the shared
code.
3. DC - Both a Distributor & Culprit

In the above depicted graph, there are 2 unique _m-groups_.

1. Group 1 : [1, 2, 3, 4, 5]
2. Group 2 : [7, 6]