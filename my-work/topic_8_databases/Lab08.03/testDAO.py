from zstudentDAO import studentDAO

# create
latestid = studentDAO.create(('mark', 45))
print("Created ID:", latestid)

# find by id
result = studentDAO.findByID(latestid)
print("Found:", result)

# update
studentDAO.update(('Fred', 21, latestid))
result = studentDAO.findByID(latestid)
print("Updated:", result)

# get all
allStudents = studentDAO.getAll()
print("All students:")
for student in allStudents:
    print(student)

# delete
studentDAO.delete(latestid)
print("Deleted:", latestid)
