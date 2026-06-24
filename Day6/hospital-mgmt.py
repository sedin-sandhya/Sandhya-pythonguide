# Person (private name/age/contact) as base. 
# Doctor adds __fee and specialisation. 
# Patient adds __appointments. 
# Hospital holds lists of both and provides find_doctor(), book_appointment(), and daily_summary(). 
# Every attribute is accessed only through public methods -- 
# the same architecture used by hospital ERP systems like SAP Healthcare.

class Person:

    def __init__(self, name, age, contact):

        self.__name = name
        self.__age = age
        self.__contact = contact


    @property
    def name(self):
        return self.__name


    @property
    def age(self):
        return self.__age


    @property
    def contact(self):
        return self.__contact


class Doctor(Person):

    def __init__(self, name, age, contact, specialization, fee):

        super().__init__(
            name,
            age,
            contact
        )

        self.__specialization = specialization
        self.__fee = fee



    @property
    def specialization(self):
        return self.__specialization



    @property
    def fee(self):
        return self.__fee


class Patient(Person):

    def __init__(self, name, age, contact):

        super().__init__(
            name,
            age,
            contact
        )


        self.__appointments = []



    def add_appointment(self, doctor):

        self.__appointments.append(doctor)



    @property
    def appointments(self):

        return self.__appointments


class Hospital:


    def __init__(self):

        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):

        self.doctors.append(doctor)

    def add_patient(self, patient):

        self.patients.append(patient)

    def find_doctor(self, specialization):

        result = []
        for doctor in self.doctors:

            if doctor.specialization == specialization:
                result.append(doctor)

        return result


    def book_appointment(self, patient, doctor):

        patient.add_appointment(doctor)
        print(f"Appointment booked with {doctor.name}")


    def daily_summary(self):

        print("\nDoctors:")
        for d in self.doctors:

            print(d.name, "-", d.specialization)


        print("\nPatients:")

        for p in self.patients:
            print(p.name)



    def billing_report(self, patient):

        total = 0

        print("\nInvoice")
        print("-"*16)

        for doctor in patient.appointments:
            print(doctor.name, doctor.fee)
            total += doctor.fee

        print("-"*16)

        print(
            "Total:",
            total
        )

hospital = Hospital()

d1 = Doctor(
    "Dr Ravi",
    45,
    "9876543210",
    "Cardio",
    1500
)

d2 = Doctor(
    "Dr Kumar",
    38,
    "9999999999",
    "Dental",
    800
)

hospital.add_doctor(d1)
hospital.add_doctor(d2)

p1 = Patient(
    "Aruna",
    30,
    "8888888888"
)

hospital.add_patient(p1)

doctors = hospital.find_doctor("Cardio")

hospital.book_appointment(p1, d1)

hospital.daily_summary()
hospital.billing_report(p1)
print(doctors)