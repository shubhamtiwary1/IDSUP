#Name : Priyansu Nagchowdhary
#Reg. no. : 2141014004
import matplotlib.pyplot as plt

def count_alphabet_frequencies(text):
    text = text.lower()
    frequencies = {}
    for char in text:
        if char.isalpha():
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1
       
            
    return frequencies

def plot_bar_chart(frequencies):
    alphabets = list(frequencies.keys())
    frequencies_list = list(frequencies.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(alphabets, frequencies_list, color='skyblue')
    plt.xlabel('Alphabet')
    plt.ylabel('Frequency')
    plt.title('Alphabet Frequency Distribution')
    plt.show()

user_input = input("Enter a string: ")
frequencies = count_alphabet_frequencies(user_input)
print(frequencies)
plot_bar_chart(frequencies)
