questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
]


Prizes = [2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000]

i = 0
for question in questions:
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    a  = int(input("Enter your answer as 1, 2, 3, 4. \n"))
    if (question[5] == a):
        print("Correct Answer")
    else:
        print(f"Incorrect , the correct answer was {question[5]}")
        print("Better luck next time!")
        break
    print(f"You won {Prizes[i]}\n")
    i+=1

    if(i==11):
        print("Congratulation you answered all of my question, take this check and enjoy!!\n")