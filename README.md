# 5letters
Python script that constantly generates 5 letter combinations, stores them in a text file, then compares them against a dictionary of 5 letter English words. If a real word is generated, it is printed and stored seperately.
# Dictionary
The dictionary was generated using the built in Linux dictionary, filtered to only 5-letter words: ``grep -x '.\{5\}' /usr/share/dict/words > dict.txt``
# Run
Run with any Python 3. Press ctrl+c to cancel. Results will be stored in the text files ``output.txt`` and ``output_english.txt``. Leave running for long periods of time for best results.
# Results
From running multiple extensive tests, my machine can generate upwards of around 35,000 combinations per second, and about 0.006% of those are real English words, or about 2.2 English words/second. Mileage may vary based on hardware and RNG.
The script automatically gives you generation statistics after pressing ctrl+c, which looks like this:
>Total of 85415690 combinations generated. 5400 were real English words, or 0.006322%.

>Elapsed time:

>Seconds: 2437.17 which is 35047.09 total words per second, and 2.22 real English words per second.

>Minutes: 40.62 which is 2102825.22 total words per minute, and 132.94 real English words per minute.

>Hours: 0.68 which is 126169512.92 total words per hour, and 7976.47 real English words per hour.
