import psycopg2
from datetime import date

class Main:
    @staticmethod
    def connect():
        conn = psycopg2.connect(
            dbname="Assignment3q1",
            user="postgres",
            password="Yaman2003!",
            host="localhost",
            port="5432"
        )
        return conn

    @staticmethod
    def get_all_students():
        print("Printing all students:")
        try:
            with Main.connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM students")
                    students = cur.fetchall()
                    if students:
                        print("{:<10}{:<15}{:<15}{:<30}{:<15}".format("Student ID", "First Name", "Last Name", "Email", "Enrollment Date"))
                        for student in students:
                            print("{:<10}{:<15}{:<15}{:<30}{:<15}".format(*student))
                    else:
                        print("No students found.")
        except Exception as e:
            print("Error:", e)
        print("getAllStudents function completed")

    @staticmethod
    def add_student(first_name, last_name, email, enrollment_date):
        print("Adding a new student:")
        try:
            with Main.connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                                (first_name, last_name, email, enrollment_date))
                    conn.commit()
                    print("Student added successfully.")
                    Main.get_all_students()
        except Exception as e:
            print("Error:", e)
        print("addStudent function completed")

    @staticmethod
    def update_student_email(student_id, email):
        print("Updating student email:")
        try:
            with Main.connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (email, student_id))
                    conn.commit()
                    print("Student email updated successfully.")
                    Main.get_all_students()
        except Exception as e:
            print("Error:", e)
        print("updateStudentEmail function completed")

    @staticmethod
    def delete_student(student_id):
        print("Deleting student:")
        try:
            with Main.connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
                    conn.commit()
                    print("Student deleted successfully.")
                    Main.get_all_students()
        except Exception as e:
            print("Error:", e)
        print("deleteStudent function completed")

if __name__ == "__main__":
    #Main.get_all_students()
    #Main.add_student("Leo", "Messi", "new@example.com", date(2011, 1, 1))
    #Main.delete_student(1)
    Main.update_student_email(2, "xxx@example.com")