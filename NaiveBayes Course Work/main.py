import sys
from preprocessing import preprocessing as prep
import NB as nb

#setting up cosntant terms for use in dicts

TRAINING_FILENAME = "training"
TEST_FILENAME = "test"
PARAMETER_FILENAME = "parameter_filename"
OUTPUT_FILENAME = "output_filename"
VOCAB_FILENAME = "vocab_filename"
PREP_TRAIN = "prep_train"
PREP_TEST = "prep_test"

files = {}
with open(sys.argv[1], "r") as file:
    for line in file:
        line = line.split()
        files[line[0]] = line[1]


preprocessing = prep(files[TRAINING_FILENAME])
preprocessing.run(files[PREP_TRAIN])

preprocessing = prep(files[TEST_FILENAME])
preprocessing.run(files[PREP_TEST])


with open(sys.argv[2], "r") as file:
    for line in file:
        line = line.split()
        files[line[0]] = line[1]

nb.parameterize(files[PARAMETER_FILENAME], 
                *nb.train(files[TRAINING_FILENAME]), 
                nb.vocab(files[VOCAB_FILENAME]))
nb.output(files[OUTPUT_FILENAME], nb.test(files[TEST_FILENAME], 
                files[PARAMETER_FILENAME]))
