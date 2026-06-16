# Build a hospital emergency ward where patients are treated by severity, not arrival order. 
# Severity: 1 = most critical, 10 = minor. 
# Always treat the most critical patient first using Python's heapq module. 
# Add bump_priority(name) - increases a waiting patient's severity 
# by 1 level (e.g. 5 → 4) if their condition worsens. 
 
import heapq
class Ward:

    def __init__(self):
        self.patients = []
        self.arrival_order = 0

    def admit(self, name, age, severity):
        patient = (
            severity,
            self.arrival_order,
            name,
            age
        )

        heapq.heappush(self.patients, patient)

        self.arrival_order += 1

        print(
            f"Admitted: {name} "
            f"(Severity {severity})"
        )

    def treat_next(self):
        if not self.patients:
            print("No patients waiting")
            return
        
        severity, order, name, age = heapq.heappop(self.patients)

        print(
            f"Treating: {name}, "
            f"Age {age} "
            f"(severity {severity})"
        )

    def show_waiting(self):

        if not self.patients:
            print("No patients waiting")
            return

        print()
        print("Waiting Patients:")

        waiting = sorted(self.patients)


        for i, patient in enumerate(waiting, start=1):

            severity, order, name, age = patient
            print(
                f"{i}. {name} "
                f"Age {age} "
                f"Severity: {severity}"
            )

    def bump_priority(self, name):
        found = False
        new_heap = []

        for patient in self.patients:
            severity, order, pname, age = patient
            if pname == name:
                found = True
                # severity 1 is highest
                if severity > 1:
                    severity -= 1

            new_heap.append(
                (severity, order, pname, age)
            )

        if found:
            heapq.heapify(new_heap)
            self.patients = new_heap
            print()
            print(f"{name}'s priority increased")

        else:
            print("Patient not found")

def main():
    ward = Ward()
    ward.admit("Rahul", 45, 3)
    ward.admit("Priya", 28, 1)
    ward.admit("Arjun", 60, 7)
    ward.admit("Meena", 35, 1)

    print()
    ward.treat_next()
    ward.treat_next()
    ward.show_waiting()


    # Bonus test
    ward.bump_priority("Arjun")
    ward.show_waiting()

if __name__ == "__main__":
    main()