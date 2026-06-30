import csv
import glob

from pathlib import Path

class StudentCSVReader:

    def read_students(self, filepath):
        students = []

        with open(filepath, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)
        
        return students

class GradeCalculator:

    def calculate_grade(self, percentage):

        if percentage >= 90:
            return "A+"

        elif percentage >= 80:
            return "A"

        elif percentage >= 70:
            return "B"

        elif percentage >= 50:
            return "C"

        elif percentage >= 40:
            return "D"
        
        else:
            return "F"

class StudentResult:

    def __init__(self, grade_calculator):
        self.grade_calculator = grade_calculator

    def process(self, student):

        marks = [
                int(student["maths"]),
                int(student["science"]),
                int(student["english"]),
                int(student["history"]),
                int(student["pe"])
            ]

        total = sum(marks)

        percentage = (total / 500) * 100

        return {

            "name": student["name"],

            "roll_no": student["roll_no"],

            "total": total,

            "percentage": round(
                percentage, 
                2
            ),

            "grade":
                self.grade_calculator.calculate_grade(percentage)
        }
    
class ResultCSVWriter:

    def write_results(self, results, output):


        Path("results").mkdir(exist_ok=True)

        with open(output, "w", newline="") as file:

            fieldnames = [
                "name",
                "roll_no",
                "total",
                "percentage",
                "grade"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            writer.writerows(results)

class StudentReportApp:
        
        def __init__(self, reader, processor, writer):
            self.reader = reader
            self.processor = processor
            self.writer = writer

        def run(self):

            files = glob.glob("data/*.csv")

            for filepath in files:

                students = self.reader.read_students(filepath)
                results = []

                for student in students:

                    result = self.processor.process(student)

                    results.append(result)


                output_file = ("results/" + Path(filepath).stem
                    + "_results.csv")


                self.writer.write_results(results, output_file)

                print(f"Generated {output_file}")

def main():


    reader = StudentCSVReader()

    grade_calculator = GradeCalculator()

    processor = StudentResult(grade_calculator)

    writer = ResultCSVWriter()


    app = StudentReportApp(reader, processor, writer)

    app.run()



if __name__ == "__main__":
    main()