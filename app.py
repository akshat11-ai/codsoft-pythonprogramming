# Class to represent a course
class Course:
    def __init__(self, course_code, title, description, capacity, schedule):
        self.course_code = course_code
        self.title = title
        self.description = description
        self.capacity = capacity
        self.schedule = schedule
        self.registered_students = []

    def is_full(self):
        return len(self.registered_students) >= self.capacity

    def register_student(self, student):
        if not self.is_full():
            self.registered_students.append(student)
            print(f"{student.name} has been successfully registered for {self.title}.")
        else:
            print(f"Registration failed. Course {self.title} is full.")

    def remove_student(self, student):
        if student in self.registered_students:
            self.registered_students.remove(student)
            print(f"{student.name} has been removed from {self.title}.")
        else:
            print(f"{student.name} is not enrolled in {self.title}.")

    def display_course_info(self):
        available_slots = self.capacity - len(self.registered_students)
        print(f"\nCourse Code: {self.course_code}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Schedule: {self.schedule}")
        print(f"Capacity: {self.capacity} | Available Slots: {available_slots}")

# Class to represent a student
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.registered_courses = []

    def register_for_course(self, course):
        if course not in self.registered_courses:
            course.register_student(self)
            self.registered_courses.append(course)
        else:
            print(f"{self.name} is already registered for {course.title}.")

    def drop_course(self, course):
        if course in self.registered_courses:
            course.remove_student(self)
            self.registered_courses.remove(course)
        else:
            print(f"{self.name} is not registered for {course.title}.")

    def display_registered_courses(self):
        print(f"\n{self.name}'s Registered Courses:")
        if self.registered_courses:
            for course in self.registered_courses:
                course.display_course_info()
        else:
            print("No courses registered.")

# Class to manage the course registration system
class CourseRegistrationSystem:
    def __init__(self):
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def list_courses(self):
        print("\n--- Available Courses ---")
        for course in self.courses:
            course.display_course_info()

    def find_course(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                return course
        print(f"Course with code {course_code} not found.")
        return None

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        print(f"Student with ID {student_id} not found.")
        return None

# Main program
if __name__ == "__main__":
    system = CourseRegistrationSystem()

    # Adding sample courses to the system
    course1 = Course("CSE101", "Introduction to Computer Science", "Basic programming concepts", 3, "Mon-Wed 10AM-12PM")
    course2 = Course("MAT201", "Calculus II", "Advanced calculus and integration", 2, "Tue-Thu 2PM-4PM")
    course3 = Course("PHY301", "Physics III", "Electromagnetism and waves", 2, "Mon-Wed 1PM-3PM")
    
    system.add_course(course1)
    system.add_course(course2)
    system.add_course(course3)

    # Adding sample students to the system
    student1 = Student("S1001", "Alice")
    student2 = Student("S1002", "Bob")
    
    system.add_student(student1)
    system.add_student(student2)

    # Simulating the registration process
    while True:
        print("\n--- Student Course Registration System ---")
        print("1. List Available Courses")
        print("2. Register for a Course")
        print("3. Drop a Course")
        print("4. View Registered Courses")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            system.list_courses()

        elif choice == '2':
            student_id = input("Enter student ID: ")
            student = system.find_student(student_id)
            if student:
                course_code = input("Enter course code to register: ")
                course = system.find_course(course_code)
                if course:
                    student.register_for_course(course)

        elif choice == '3':
            student_id = input("Enter student ID: ")
            student = system.find_student(student_id)
            if student:
                course_code = input("Enter course code to drop: ")
                course = system.find_course(course_code)
                if course:
                    student.drop_course(course)

        elif choice == '4':
            student_id = input("Enter student ID: ")
            student = system.find_student(student_id)
            if student:
                student.display_registered_courses()

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
