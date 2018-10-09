from py2neo import Graph, Node, Relationship, authenticate

authenticate("localhost:7474", "neo4j", "iiit123")
graph = Graph()
graph.delete_all()
# graph.schema.create_uniqueness_constraint('Problem', 'name')
# graph.schema.create_uniqueness_constraint('Concept', 'name')
# *********************************************** Topics *********************************************
Array = Node("Topic", name="Array")
LL = Node("Topic", name="Linked List")

graph.create(Array | LL)
# *********************************************** End Topics *****************************************

# *********************************************** Questions ******************************************

PA1 = Node("Problem", name="Min Steps in Infinite Grid", URL="https://www.interviewbit.com/problems/min-steps-in-infinite-grid/", Resource="", Flag=0, Notes="")
PA2 = Node("Problem", name="Add One To Number", URL="https://www.interviewbit.com/problems/add-one-to-number/", Resource="", Flag=0, Notes="")
PA3 = Node("Problem", name="Max Sum Contiguous Subarray", URL="https://www.interviewbit.com/problems/max-sum-contiguous-subarray/", Resource="", Flag=0, Notes="")
PA4 = Node("Problem", name="Maximum Absolute Difference", URL="https://www.interviewbit.com/problems/maximum-absolute-difference/", Resource="", Flag=0, Notes="")
PA5 = Node("Problem", name="Repeat and Missing Number Array", URL="https://www.interviewbit.com/problems/repeat-and-missing-number-array/", Resource="", Flag=0, Notes="")
PA6 = Node("Problem", name="Flip", URL="https://www.interviewbit.com/problems/flip/", Resource="", Flag=0, Notes="")
PA7 = Node("Problem", name="Spiral Order Matrix II", URL="https://www.interviewbit.com/problems/max-non-negative-subarray/", Resource="", Flag=0, Notes="")

PA8 = Node("Problem", name="Max Non Negative SubArray", URL="https://www.interviewbit.com/problems/max-non-negative-subarray/", Resource="", Flag=0, Notes="")
PA9 = Node("Problem", name="Pascals Triangle", URL="https://www.interviewbit.com/problems/pascal-triangle/", Resource="", Flag=0, Notes="")
PA10 = Node("Problem", name="Kth Row of Pascal's Triangle", URL="https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/", Resource="", Flag=0, Notes="")
PA11 = Node("Problem", name="Anti Diagonals", URL="https://www.interviewbit.com/problems/anti-diagonals/", Resource="", Flag=0, Notes="")
PA12 = Node("Problem", name="Largest Number", URL="https://www.interviewbit.com/problems/largest-number/", Resource="", Flag=0, Notes="")
PA13 = Node("Problem", name="Wave Array", URL="https://www.interviewbit.com/problems/wave-array/", Resource="", Flag=0, Notes="")
PA14 = Node("Problem", name="Hotel Bookings Possible", URL="https://www.interviewbit.com/problems/hotel-bookings-possible/", Resource="", Flag=0, Notes="")

PA15 = Node("Problem", name="Max Distance", URL="https://www.interviewbit.com/problems/max-distance/", Resource="", Flag=0, Notes="")
PA16 = Node("Problem", name="Maximum Unsorted Subarray", URL="https://www.interviewbit.com/problems/maximum-unsorted-subarray/", Resource="", Flag=0, Notes="")
PA17 = Node("Problem", name="Find Duplicate in Array", URL="https://www.interviewbit.com/problems/find-duplicate-in-array/", Resource="", Flag=0, Notes="")
PA18 = Node("Problem", name="Maximum Consecutive Gap", URL="https://www.interviewbit.com/problems/maximum-consecutive-gap/", Resource="", Flag=0, Notes="")
PA19 = Node("Problem", name="First Missing Integer", URL="https://www.interviewbit.com/problems/first-missing-integer/", Resource="", Flag=0, Notes="")

graph.create(PA1 | PA2 | PA3 | PA4 | PA5 | PA6 | PA7 | PA8 | PA9 | PA10 | PA11 | PA12 | PA13 | PA14 | PA15 | PA16 | PA17 | PA18 | PA19)

LA1 = Node("Problem", name="Find if a cycle exists in a LL", URL="", Resource="", Flag=0, Notes="")
# ********************************************End Questions ******************************************

# ************************************************ Concepts ******************************************
C1 = Node("Concept", name="2D Number System")
C2 = Node("Concept", name="Overflow")
C3 = Node("Concept", name="Kadane")
C4 = Node("Concept", name="Absolute Value")
C5 = Node("Concept", name="XOR")
C5_1 = Node("Concept", name="Flloyd Cycle Detection")
C5_2 = Node("Concept", name="Sum & Product")
C5_3_1 = Node("Concept", name="Partition Array")
C5_4 = Node("Concept", name="In-place hashing (using Abs)")
C6 = Node("Concept", name="Spiral")

# *********************************************End Concepts ******************************************

# *********************************************Topic -> Problem ******************************************
graph.create(Relationship(Array, "PROBLEM", PA1))
graph.create(Relationship(Array, "PROBLEM", PA2))
graph.create(Relationship(Array, "PROBLEM", PA3))
graph.create(Relationship(Array, "PROBLEM", PA4))
graph.create(Relationship(Array, "PROBLEM", PA5))
graph.create(Relationship(Array, "PROBLEM", PA6))
graph.create(Relationship(Array, "PROBLEM", PA7))
graph.create(Relationship(Array, "PROBLEM", PA8))

graph.create(Relationship(LL, "PROBLEM", LA1))
# ****************************************** End Topic -> Problem ******************************************

# ********************************************* Problem ->Concept ******************************************
graph.create(Relationship(PA1, "CONCEPT", C1))
graph.create(Relationship(PA2, "CONCEPT", C2))
graph.create(Relationship(PA3, "CONCEPT", C3))
graph.create(Relationship(PA4, "CONCEPT", C4))
graph.create(Relationship(PA5, "CONCEPT", C5))
graph.create(Relationship(PA5, "CONCEPT", C5_1))
graph.create(Relationship(PA5, "CONCEPT", C5_2))
graph.create(Relationship(C5, "USES", C5_3_1))
graph.create(Relationship(PA5, "CONCEPT", C5_4))
graph.create(Relationship(PA6, "CONCEPT", C3))
graph.create(Relationship(PA7, "CONCEPT", C6))
graph.create(Relationship(PA8, "CONCEPT", C3))

graph.create(Relationship(LA1, "CONCEPT", C5_1))
# ***************************************** End Problem ->Concept ******************************************