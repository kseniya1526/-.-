grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5,]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_= list(students)
students_.sort()
print(students_)
dictionary = {}
print(dictionary)
dictionary = ({students_[0]: sum(grades[0])/len(grades[0]), students_[1]: sum(grades[1])/len(grades[1]), students_[2]: sum(grades[2])/len(grades[2]), students_[3]: sum(grades[3])/len(grades[3]), students_[4]: sum(grades[4])/len(grades[4])})
print(dictionary)