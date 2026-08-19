# Queue = FIFO
# First In, First Out

queue = []

queue.append("Person 1")
queue.append("Person 2")
queue.append("Person 3")

print("Queue:", queue)

person = queue.pop(0)

print("Removed:", person)
print("Queue:", queue)

person = queue.pop(0)

print("Removed:", person)
print("Queue:", queue)
