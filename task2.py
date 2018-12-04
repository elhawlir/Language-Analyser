# Task 2

import re
import pandas as pd

# Task 2: Building a Class for Data Analysis

class Analyser:
    def __init__(self):
        self.length_of_transcript = 0       # number of statements, end of a statement indicated by '.', '?' and '!'
        self.num_unique = 0         # number of unique words
        self.rep1slash = 0          # repetition of [/]
        self.rep2slash = 0          # repetition of [//]
        self.rep_sq_star = 0        # repetition of [* m:+ed]
        self.num_pauses = 0         # number of (.)
        self.stat_list_sli = []
        self.stat_list_td = []
        


# This is the function that analyses and counts the different statistics for the SLI cleaned files
    def sli_analyse_script(self, cleaned_file=""):
        file = open(cleaned_file, "r")
        file1 = file.read()

        # number of unique words
        if cleaned_file[0] == "s":
            unique_words = file1
            for words in unique_words:
                target = re.findall(r"[^a-zA-Z]", words)
                if words in target:
                    words.replace(words, "")
            unique_words = unique_words.split(" ")
            self.num_unique = len(set(unique_words))
            self.stat_list_sli.append(self.num_unique)

            # length of transcripts count
            self.length_of_transcript = int(file1.count(".")) + int(file1.count("?")) + int(file1.count("!"))
            self.stat_list_sli.append(self.length_of_transcript)

            # count of [/]
            self.rep1slash = file1.count("[/]")
            self.stat_list_sli.append(self.rep1slash)

            # count of [//]
            self.rep2slash = file1.count("[//]")
            self.stat_list_sli.append(self.rep2slash)

            # count of [* m:+ed]
            self.rep_sq_star = file1.count("[* m:+ed]")
            self.stat_list_sli.append(self.rep_sq_star)

            # count of (.)
            self.num_pauses = file1.count("(.)")
            self.stat_list_sli.append(self.num_pauses)
            
        # Combining stats in a single sli list
        return self.stat_list_sli 
            
            
# This is the function that analyses and counts the different statistics for the TD cleaned files
    def td_analyse_script(self, cleaned_file=""):
        file = open(cleaned_file, "r")
        file1 = file.read()
        
        # number of unique words
        if cleaned_file[0] == "t":
            unique_words = file1
            for words in unique_words:
                target = re.findall(r"[^a-zA-Z]", words)
                if words in target:
                    words.replace(words, "")
            unique_words = unique_words.split(" ")
            self.num_unique = len(set(unique_words))
            self.stat_list_td.append(self.num_unique)
        
            # length of transcripts count
            self.length_of_transcript = int(file1.count(".")) + int(file1.count("?")) + int(file1.count("!"))
            self.stat_list_td.append(self.length_of_transcript)

            # count of [/]
            self.rep1slash = file1.count("[/]")
            self.stat_list_td.append(self.rep1slash)

            # count of [//]
            self.rep2slash = file1.count("[//]")
            self.stat_list_td.append(self.rep2slash)

            # count of [* m:+ed]
            self.rep_sq_star = file1.count("[* m:+ed]")
            self.stat_list_td.append(self.rep_sq_star)

            # count of (.)
            self.num_pauses = file1.count("(.)")
            self.stat_list_td.append(self.num_pauses)
            
        # combining stats in a single td list
        return self.stat_list_td  
            
        
    def __str__(self):
        return str(self.length_of_transcript), "statements", "\n", str(self.num_unique), "unique words", "\n", \
        str(self.rep1slash), "repetitions", "\n", str(self.rep2slash), "retraces", "\n", \
        str(self.rep_sq_star), "grammatical errors", "\n", str(self.num_pauses), "pauses"
    

a1 = Analyser()
sli = a1.sli_analyse_script("sli1_cleaned.txt")
sli = a1.sli_analyse_script("sli2_cleaned.txt")
sli = a1.sli_analyse_script("sli3_cleaned.txt")
sli = a1.sli_analyse_script("sli4_cleaned.txt")
sli = a1.sli_analyse_script("sli5_cleaned.txt")
sli = a1.sli_analyse_script("sli6_cleaned.txt")
sli = a1.sli_analyse_script("sli7_cleaned.txt")
sli = a1.sli_analyse_script("sli8_cleaned.txt")
sli = a1.sli_analyse_script("sli9_cleaned.txt")
sli = a1.sli_analyse_script("sli10_cleaned.txt")

sli_stats = []
sli_lot = sli[::6]
sli_stats.append(sli_lot)
print(sli_lot)
sli_uw = sli[1::6]
sli_stats.append(sli_uw)
print(sli_uw)
sli_repw = sli[2::6]
sli_stats.append(sli_repw)
print(sli_repw)
sli_retw = sli[3::6]
sli_stats.append(sli_retw)
print(sli_retw)
sli_ge = sli[4::6]
sli_stats.append(sli_ge)
print(sli_ge)
sli_np = sli[5::6]
sli_stats.append(sli_np)
print(sli_np)
print(sli_stats)

sli_data = pd.DataFrame(sli_stats)
sli_data = sli_data.transpose()
sli_data.columns = ["L_o_T", "U_W", "Rep_W", "Ret_W", "Gra_Err", "N_o_P"]
sli_data.index = ['SLI1', 'SLI2', 'SLI3', 'SLI4', 'SLI5', 'SLI6', 'SLI7', 'SLI8', 'SLI9', 'SLI10']
print(sli_data)

td = a1.td_analyse_script("td1_cleaned.txt")
td = a1.td_analyse_script("td2_cleaned.txt")
td = a1.td_analyse_script("td3_cleaned.txt")
td = a1.td_analyse_script("td4_cleaned.txt")
td = a1.td_analyse_script("td5_cleaned.txt")
td = a1.td_analyse_script("td6_cleaned.txt")
td = a1.td_analyse_script("td7_cleaned.txt")
td = a1.td_analyse_script("td8_cleaned.txt")
td = a1.td_analyse_script("td9_cleaned.txt")
td = a1.td_analyse_script("td10_cleaned.txt")

td_stats = []
td_lot = td[::6]
td_stats.append(td_lot)
print(td_lot)
td_uw = td[1::6]
td_stats.append(td_uw)
print(td_uw)
td_repw = td[2::6]
td_stats.append(td_repw)
print(td_repw)
td_retw = td[3::6]
td_stats.append(td_retw)
print(td_retw)
td_ge = td[4::6]
td_stats.append(td_ge)
print(td_ge)
td_np = td[5::6]
td_stats.append(td_np)
print(td_np)
print(td_stats)

td_data = pd.DataFrame(td_stats)
td_data = td_data.transpose()
td_data.columns = ["L_o_T", "U_W", "Rep_W", "Ret_W", "Gra_Err", "N_o_P"]
td_data.index = ['TD1', 'TD2', 'TD3', 'TD4', 'TD5', 'TD6', 'TD7', 'TD8', 'TD9', 'TD10']
print(td_data)  
    
    
    
        
