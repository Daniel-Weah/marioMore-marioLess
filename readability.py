def calculateGradeLevel(text):
    letters = sum(1 for char in text if char.isalpha())
    words = len(text.split())
    sentences = sum(1 for char in text if char in '.!?')
    
    L = (letters / words) * 100
    S = (sentences / words) * 100
    
    index = 0.0588 * L - 0.296 * S - 15.8
    
    return round(index)


text = input("Please type in your text: ")

grade = calculateGradeLevel(text)
if grade < 1:
    print("Grade Level: Before Grade 1")
elif grade >= 16:
    print("Grade Level: Grade 16+ (college level)")
else:
    print(f"Grade Level: Grade {grade}")