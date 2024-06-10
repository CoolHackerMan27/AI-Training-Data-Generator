import llama_cpp
from llama_cpp import Llama
import csv
import random

model = Llama(model_path="path/to/your/llama/model")

def generate_conversational_data():
    prompt = "Please generate one line of training data in the following format: Input , response. The data should be conversational data and follow basic patterns of human interaction. Only generate 1 prompt/response pair."
    output = model.createCompletion(prompt)
    input_text, output_text = output.split(", ")
    return input_text, output_text

def main():
    file_path = "conversational_data.csv"
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Input", "Output"])  # Write the header row

        num_samples = int(input("Enter the number of prompt/response pairs to generate: "))

        for _ in range(num_samples):
            input_text, output_text = generate_conversational_data()
            writer.writerow([input_text, output_text])

if __name__ == "__main__":
    main()