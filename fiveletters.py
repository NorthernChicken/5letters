import random
import time

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num_gen = 0
num_english = 0

with open('dict.txt', 'r') as dict_file:
    dictionary = set(line.strip() for line in dict_file)

start_time = time.time()  # Start the timer before the loop begins

try:
    while True:
        final_string = ''.join(random.choice(letters) for _ in range(5))
        num_gen += 1

        with open('output.txt', 'a') as output_file, open('output_english.txt', 'a') as english_output_file:
            if final_string in dictionary:
                output_file.write(final_string + '\n')
                english_output_file.write(final_string + '\n')
                num_english += 1
                print(final_string)
            else:
                output_file.write(final_string + '\n')

except KeyboardInterrupt:
    end_time = time.time()
    elapsed_time = end_time - start_time

    decimal_english = num_english / num_gen
    percent_english = decimal_english * 100

    print(f"\nTotal of {num_gen} combinations generated. {num_english} were real English words, or {percent_english:.6f}%.")
    print("Elapsed time:")
    print(f"Seconds: {elapsed_time:.2f} which is {num_gen / elapsed_time:.2f} total words per second, and {num_english / elapsed_time:.2f} real English words per second.")
    print(f"Minutes: {elapsed_time / 60:.2f} which is {num_gen / (elapsed_time / 60):.2f} total words per minute, and {num_english / (elapsed_time / 60):.2f} real English words per minute.")
    print(f"Hours: {elapsed_time / 3600:.2f} which is {num_gen / (elapsed_time / 3600):.2f} total words per hour, and {num_english / (elapsed_time / 3600):.2f} real English words per hour.")
