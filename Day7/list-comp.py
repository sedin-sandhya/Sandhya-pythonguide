import sys


# 1. Squares of even numbers 1-100
class ListComp:

    def squares(self):
        squares = [
            x ** 2
            for x in range(1, 101)
            if x % 2 == 0
        ]

        print("1. Even Squares:")
        print(squares)



    # 2. Flatten 2D list

    def matrix2D(self):
        matrix = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]


        flat = [
            n
            for row in matrix
            for n in row
        ]


        print("\n2. Flattened list:")
        print(flat)

    # 3. Filter valid emails

    def filter_emails(self):
        data = [
            "sandhya@gmail.com",
            "hello",
            "test@yahoo.com",
            "invalid@",
            "abc.com",
            "user@mail.com"
        ]


        emails = [
            s
            for s in data
            if "@" in s and "." in s
        ]


        print("\n3. Valid emails:")
        print(emails)


    # 4. Generator expression + memory comparison

    # List creates all values immediately
    def listvsgen(self):
        list_data = [
            x ** 2
            for x in range(1, 100)
        ]

        gen_data = (
            x ** 2
            for x in range(1, 100)
        )


        print("\n4. Memory comparison:")

        print(
            "List memory:",
            sys.getsizeof(list_data),
            "bytes"
        )


        print(
            "Generator memory:",
            sys.getsizeof(gen_data),
            "bytes"
        )


        # using generator
        total = sum(gen_data)


        print(
            "Generator sum:",
            total
        )


    # 5. Dictionary comprehension with discount

    def dictComp(self):
        prices = {
            "Laptop": 1080.4567,
            "Phone": 30000,
            "Headphones": 5000,
            "Keyboard": 2000
        }


        discounted = {
            key: round(value * 0.9, 2)
            for key, value in prices.items()
        }


        print("\n5. Discounted prices:")
        print(discounted)

def main():
    listcomp = ListComp()

    listcomp.squares()

    listcomp.matrix2D()

    listcomp.filter_emails()

    listcomp.listvsgen()

    listcomp.dictComp()

if __name__ == "__main__":
    main()

