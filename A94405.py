'''
----------------------PSEUDO CODE----------------
Algorithm searches for the registration number in the serving list and marks meal card if the student hasn't yet eaten
worst case of algorithm == O(n)
1.name,regno,accessno,course,has eaten are the parameters in  the student class(student data)
2. the algorithms checks whether the day of the week i present in the dictionary
3.If present, algorithm loops through student data and searches for the student's registration number(reg no)
and checks if the student has eaten or not. 
4.If the student has eaten, return True else return False
5.If the reg no is not present RETURN false
6.If the input day is not present in the list return False
Big O complexity==O(N)
'''
class Student:
    def __init__(self,name,regno,accessno,course,hasEaten):
        self.name = name
        self.regno = regno
        self.accessno = accessno
        self.course = course
        self.hasEaten = hasEaten
        
    def storage(self):
        studentDict = {}
        studentDict['name'] = self.name
        studentDict['regno'] = self.regno
        studentDict['accessno'] = self.accessno
        studentDict['course'] = self.course
        studentDict['hasEaten'] = self.hasEaten
        return studentDict

class ServingList:
    def __init__(self,dayOfweek,studentList):
        self.dayOfweek = dayOfweek
        self.studentList = studentList
        
    def storage(self):
        servingListDict = {}
        servingListDict[self.dayOfweek] = self.studentList
        return servingListDict
    
def searchToMarkMealCard(servingListDict, registrationNumber, dayOfTheWeek):
    if dayOfTheWeek in servingListDict:#checking if the day is present in the serving list
        for student in servingListDict[dayOfTheWeek]:
            if(registrationNumber == student['regno']):
                if(not student['hasEaten']):
                    print("Student has not YET eaten")
                    return True
    return False

def main():
    student1 = Student("Q","S21B23/019","A94172","B23",False)
    student2 = Student("B","S21B23/010","A94172","B23",True)
    student3=  Student("H","S21B23/012","A94165","B23",False)
    student4=  Student("W","S21B13/047","A94412","B13",True)
    
    studentDict1 = student1.storage()
    studentDict2 = student2.storage()
    studentDict3 = student3.storage()
    studentDict4 = student4.storage()
    
    studentlist = []
    studentlist.append(studentDict1)
    studentlist.append(studentDict2)
    studentlist.append(studentDict3)
    studentlist.append(studentDict4)
    
    servingList = ServingList("THURSDAY",studentlist)
    servingListDict = servingList.storage()
    
    print(searchToMarkMealCard(servingListDict,"S21B23/010","THURSDAY"))
    print(searchToMarkMealCard(servingListDict,"S21B23/012","THURSDAY"))
    print(searchToMarkMealCard(servingListDict,"S21B23/019","THURSDAY"))
    print(searchToMarkMealCard(servingListDict,"S21B23/047","THURSDAY"))
    
main()