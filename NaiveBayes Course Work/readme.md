
### Instructions
1. Open prep_files.txt in an editor
2. The first line should be "training directory\\location\\of\\training\\data"
3. The second line should be "test directory\\location\\of\\test\\data"
4. The third line should be "prep_train training_preprocessing_output_file.txt"
5. The fourth/last line should be "prep_test testing_preprocessing_output_file.txt"
6. Close prep_files.txt
7. open NB_files.txt in an editor
8. The first line should be "training training_preprocessing_output_file.txt"
9. The second line should be "test testing_preprocessing_output_file.txt"
10. The third line should be "parameter_filename movie-review-BOW.NB"
11. The fourth line should be "output_filename output_filename.txt"
12. The fifth and last line should be "vocab_filename file\\location\\of\\the\\vocab.txt"
13. close NB_files.txt
14. from command line run "python main.py prep_files.txt NB_files.txt"
---
Please note the following:

The first token on each line of prep_files.txt and of NB_files.txt should remain unchanged. You
should only edit the 2nd token after the first space. 

The directories in prep_files.txt should lead to the directory housing both the pos and neg
directories, not to files. 

The filepath in NB_files.txt should lead directly to the vocab file for this project. \
The output files are up to the naming conventions of the user, but the third and fourth line file 
names in prep_files.txt must match the first and second line file names of NB_files.txt .

When running the small corpus for 2b and 2c, the file structure must match that of the larger corpus, 
that is there must be a directory containing a pos directory and a neg directory. The small corpus 
must be placed in one of these folders. 

When running the small corpus for 2b and 2c, there must be a corresponding vocab file. I create it 
manually based on the provided information. If needed you could certainly use the larger vocab for 
part 2d.  

Make sure to include "&" and "%" in the vocabulary of part 2d