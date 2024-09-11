import os
import re

meb = ((10 ** 5) * 10 ) * 48

def split(path, data_length=meb):
    with open(path, "rb") as file:
        i = 1
        x = file.read(data_length)
        while(len(x)):
            with open(f"questions_{i}.bin", "wb") as file_to:
                file_to.write(x)

            x = file.read(data_length)
            i += 1

def get_files_names():
    return sorted(os.listdir())

def merge(end_file = "questions.pdf", pattern="(questions[_])+[?]*"):
    
    def check(text):
        return re.match(pattern, text)

    with open(end_file, "wb+") as file:
        i = 1
        # x = file.read(meb)
        files = list(filter(lambda n: check(n), get_files_names()))

        for name in files:
            # print(name)
            # print(check(name))
            with open(name, "rb") as file_from:
                dump = file_from.read()
                print(len(dump))
                file.write(dump)
            i += 1




def main():
    # split("download.pdf")
    merge()


if __name__ == "__main__":
    main()
