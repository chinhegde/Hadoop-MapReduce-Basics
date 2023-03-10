# Hadoop MapReduce Exploration

## 1. What is result of pi using Hadoop MapReduce?
### a. 5 nodes with 5 samples

Answer = 3.680
Command:
```
hadoop jar /*/hadoop-mapreduce-examples-3.2.3.jar pi 5 5 
```

Number of maps = 5
Number of samples per map = 5

### b. 10 nodes with 10 samples
Answer = 3.200

Command is the same as above. Replace 5 with 10.

## 2. Word Count using Hadoop MapReduce & the top 10 most frequent words in the corpus.

Input file given: bibles_shakes.nopunc.gz
* The gunzip command was used to expand the file.
* The input file was copied to HDFS destination.
* “sort_wordcount.py” was used to find the Top 10 words.
* Final output file is “wordcount.txt” (contains all words and their frequencies in
lexicographical order)

Command:
```
hadoop jar "/usr/lib/hadoop-3.3.4-mapreduce/hadoop-examples.jar" wordcount
/hegde/wordcount/input
/hegde/wordcount/output
```

## Kmer Counting with Hadoop MapReduce

* Mapper: “mappero.py” - It slices the streaming string input into lengths of N (in this case,
3 and 9)
* Reducer: “reducero.py” - It counts the frequency of each 3-mer/9-mer and outputs the
Top 10 only.
Command:
```
hadoop jar
/home/hadoop//hadoop-3.2.3/share/hadoop/tools/lib/hadoop-streaming-3.2.3.jar
-mapper /home/hadoop/kmer/cmapper.py
-reducer /home/hadoop/kmer/creducer.py
-input /hegde/cards/cards_input.txt
-output /hegde/cards/cards_out
```
Mapper:
1. The mapper takes the streaming data as input and outputs a (key, value) pair. Here, the
key is the string (a 9-mer from Ecoli and HG19 data) and the value is 1.
2. The mapper does not count the number of times each 9-mer appears.
3. The part “line[i:i+n]” ensures that the overlapping K-mers are being read.

Reducer:
1. The reducer counts the number of times each K-mer appears. It does this by splitting the
input line into -> (K-mer, value). To answer the question asked in the HW, the reducer
only returns the Top 10 9-mers of both datasets.

Output files with Top 10 9-mers of Ecoli and HG19:
a. Ecoli_out.txt
b. HG19_output.txt

## Hadoop Playing Cards Counting

* Code to generate 100 decks and select random number (>40) from each deck:
“generate_input.py”
* Mapper: “cmapper.py” - only outputs numeric cards from the deck
* Reducer: “creducer.py” - calculates the sum of all numeric cards for each suit
* Input file: cards_input.txt (Copied into HDFS using hdfs dfs -put)
* Output file: “output_100.txt”
Command:
```
hadoop jar
/home/hadoop//hadoop-3.2.3/share/hadoop/tools/lib/hadoop-streaming-3.2.3.jar
-mapper /home/hadoop/kmer/cmapper.py
-reducer /home/hadoop/kmer/creducer.py
-input /hegde/cards/cards_input.txt
-output /hegde/cards/cards_out
```
Steps followed:
1. Generate 100/1000 shuffled decks of cards
2. Pick random number of cards from the decks.
a. The random number is different for each deck
b. Random number, r > 40
3. Remove the non-numeric cards
4. Calculate the sums of numeric values for each suit (Diamond, Clubs, Spades, Hearts)
5. Show the total number of cards and the sums.
