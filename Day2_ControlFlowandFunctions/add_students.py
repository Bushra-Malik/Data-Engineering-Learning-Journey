import csv

# Step 1: Create the student.csv file and write the header
with open('student.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    # writer.writerow(['Name', 'Score1', 'Score2', 'Score3', 'Average'])
    
# Step 2: Function to add student records
def add_student_records():
    while True:
        name = input("Enter student's name: ")
        scores = []
        # Collect scores
        for i in range(1, 4):
            score = float(input(f"Enter score {i}: "))
            scores.append(score)
        # Calculate average
        average = sum(scores) / len(scores)
        
        print(f" {name} ,average: {average:.2f}")
        # Step 3: Write the record to the CSV file
        with open('student.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name] + scores + [average]) #writerow () function is used to write a row in the csv file, it takes list only 
        
        # Ask if the user wants to continue
        continue_input = input("Do you want to add another student record? (yes/no): ")
        if continue_input.lower() == 'yes':
            continue  # Continue the loop to add more records
        else:
            break  # Exit the loop if the user says no

def read_student_records():
    with open('student.csv', mode='r', newline='') as file1:
        reader = csv.reader(file1)
        for row in reader:
            print(row)
            
UserID = input("Enter your ID: ")
if UserID == "0":
    print("Welcome, admin!")
    read_student_records()
else:
    print("Welcome, user!")
    add_student_records()             
    

