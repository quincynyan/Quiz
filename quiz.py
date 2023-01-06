import csv
from helpers import input_int

def main():
# Ask the user to choose mode: Create new quiz, Load quiz file, Exit
    while True:
        print("Choose an option:")
        print("1: Create new quiz")
        print("2: Load quiz file")
        print("3: Exit")
        opt = input_int("Enter a number between 1 and 3: ")
        while opt < 1 or opt > 3:
            opt = input_int("Please enter a valid number: ")
        if opt == 1:
            # Allow the user to create a new quiz
            questions = []
            length = input_int("How many questions would you like to ask? ")
            while length < 1:
                length = input_int("Please enter a number above 0: ")
            # Ask the user for their questions and answers
            for i in range(length):
                ques = input("Enter a question:\n")
                ans = input("Enter its answer:\n")
                questions.append([ques, ans])
            outfile = input("Please enter the name of the output file\n(note: a .csv extension will be added at the end)\n")
            with open(outfile + ".csv", 'w') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerow(["Question", "Answer"])
                writer.writerows(questions)
            print("CSV file successfully written")

        elif opt == 2:
            # Read the quiz file and let the user answer it
            path = input("Enter the file name/path of the quiz: ")
            totalScore = 0
            userScore = 0
            try: 
                f = open(path, "r")
            except:
                print("File not found")
            reader = csv.DictReader(f)
            for row in reader:
                totalScore += 1
                Question = row["Question"]
                answer = input(f"Question: {Question}\nAnswer: ")
                if answer.lower().strip() == row["Answer"].lower().strip():
                    print("Correct answer!")
                    userScore += 1
                else:
                    print("Wrong answer! The correct answer is", row["Answer"])
            print(f"Your score is {userScore} out of {totalScore}")
        elif opt == 3:
            # Exit the program
            break
            exit

main()
