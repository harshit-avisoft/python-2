class Course:
    def __init__(self,course_name,instructor,duration,platform):
        self.course_name=course_name
        self.instructor=instructor
        self.duration=duration
        self.platform=platform
    
    def update_duration(self,new_duration):
        self.duration=new_duration
        print(f"{new_duration} is now duration of the course")

    def update_all_details(self):
        self.course_name=input("Enter course name: ")
        self.instructor=input("Enter instructor name: ")
        self.duration=int(input("enter duration of the course: "))
        platforms=["Physics Wallah","Udemy","Coursera","Vedantu","Unacademy"]
        platform=input("enter name of the platform: ")
        while platform not in platforms:
            platform=input(("Please enter valid platform: "))
        self.platform=platform

    def __str__(self):
        return f" course_name: {self.course_name} \n instructor: {self.instructor} \n duration: {self.duration} \n platform: {self.platform}"
      

class ProgrammingCourse(Course):
    def __init__(self, course_name, instructor, duration, platform,language,difficulty_level):
        super().__init__(course_name, instructor, duration, platform)

        
        self.language=language
        
        self.difficulty_level=difficulty_level
        

    def update_language(self):
        language=input("enter a language: ")
        languages=["Python","Java","Cpp","C Sharp"]
        while language not in languages:
            language=input(("Enter a valid language: "))
        self.language=language

    def details(self):
        print(f"\n course_name: {self.course_name} \n instructor: {self.instructor} \n duration: {self.duration} \n platform: {self.platform} \n language: {self.language} \n difficulty_level: {self.difficulty_level}")

class DsaCourse(Course):

    def __init__(self, course_name, instructor, duration, platform,language,difficulty_level,practice_platform):
        super().__init__(course_name, instructor, duration, platform)

        self.language=language
        self.difficulty_level=difficulty_level
        self.practice_platform=practice_platform
    
    def update_practice_platform(self,practice_platform):
        practice_platforms=["leetcode","gfg","hackerank","hackerearth"]
        practice_platform=input("enter practice_platform :")
        while practice_platform not in practice_platforms:
            practice_platform=input("enter valid platform name: ")
        self.practice_platform=practice_platform

    def update_duration(self, new_duration):
            self.duration=new_duration
            print(f"your updated duration is {self.duration}")

    def details(self):
            print(f" \n course_name: {self.course_name} \n instructor: {self.instructor} \n duration: {self.duration} \n platform: {self.platform} \n practice_platform: {self.practice_platform}" )


print("=====Menu=====")
print("1. Create course")
print("2. Update Course Details")
print("3. Display Details")
print("4. exit")
choice1=int(input("Enter your choice(1/2/3/4): "))
temp="y"
while temp=="y":
 if choice1==1:
    print("1. Create Programming Course")
    print("2. Create DSA Course")
    choice2=int(input("Enter your choice(1/2): "))
    if choice2==1:
        course_name=input("Enter course name: ")
        instructor=input("Enter instructor name: ")
        duration=int(input("Enter duration of course: "))
        platform=input("Enter platform name: ")
        platforms=["Physics Wallah","Udemy","Coursera","Vedantu","Unacademy"]
        while platform not in platforms:
            platform=input(("Please enter valid platform: "))

        language=input("enter a language: ")
        languages=["Python","Java","Cpp","C Sharp"]
        while language not in languages:
            language=input(("Enter again valid languages: "))
        

        difficulty_level=input("Enter difficulty level: ")
        difficulty_levels=["beginner","intermediate","advanced"]
        while difficulty_level not in difficulty_levels:
            difficulty_level=input("Enter valid difficulty level: ")

        p=ProgrammingCourse(course_name,instructor,duration,platform,language,difficulty_level)
        p.details()

    if choice2==2:
        course_name=input("Enter course name: ")
        instructor=input("Enter instructor name: ")
        duration=int(input("Enter duration of course: "))
        platform=input("Enter platform name: ")
        platforms=["Physics Wallah","Udemy","Coursera","Vedantu","Unacademy"]
        while platform not in platforms:
            platform=input(("Please enter valid platform: "))

        language=input("enter a language: ")
        languages=["Python","Java","Cpp","C Sharp"]
        while language not in languages:
            language=input(("Enter again valid languages: "))
        

        difficulty_level=input("Enter difficulty level: ")
        difficulty_levels=["beginner","intermediate","advanced"]
        while difficulty_level not in difficulty_levels:
            difficulty_level=input("Enter valid difficulty level: ")

        practice_platform=input("Enter a practice platform: ")
        practice_platforms=["leetcode","gfg","hackerank","hackerearth"]
        while practice_platform not in practice_platforms:
            practice_platform=input("enter valid platform name:")

        d=DsaCourse(course_name,instructor,duration,platform,language,difficulty_level,practice_platform)
        d.details()

 if choice1==3:
        print("1. Show programming course details")
        print("2. Show DSA course details")
        choice2=int(input("Enter your choice: "))
        if choice2==1:
            p1=ProgrammingCourse()
            p1.details()
        if choice2==2:
            d1=DsaCourse()
            d1.details()
 temp=input("do you want to continue:(y/n): ")