import os

poem_url = "C:/Users/fawaz/Documents/free_online_poems/topics/"
mega_string = ""

all_folders = os.listdir(poem_url)

for folder in all_folders:
    all_files = os.listdir(poem_url + folder)

    for file in all_files:
        try:
            file_name = file.split(folder.capitalize() + "Poems")[1]
            new_file_name = file_name[0]

            for i in range(1, len(file_name)):
                #print("file_name[" + str(i) + "]: " + file_name[i])
                
                if(file_name[i].isupper()):
                    new_file_name += " " + file_name[i]
                else:
                    new_file_name += file_name[i]



            poem_info = (new_file_name).split("Poemby")
            
            title = poem_info[0]
            author = ((poem_info[1]).split(".")[0])[1:]
            mini_string = "Poem Start\n"
            try:
                mini_string += title + "\n\n"


                with open(poem_url + folder + "/" + file, 'r') as f:
                    lines = f.readlines()
                    if(len(lines) > 20):
                        mini_string = ""
                        continue
                    for line in lines:
                        initial_length = int(len(line) / 60)
                        for i in range(1, initial_length):
                            line = line[:i*60] + "\n" + line[i*60:]
                            
                        mini_string += line

                mini_string += "\nEND\n" + author + "\n\n\n"

                mega_string += mini_string
            except:
                mini_string = ""
                continue
        except:
            print("yikes")
            continue
print(mega_string)
file_to_write_to = "more_mega_poems_2.txt"
the_file = open("more_mega_poem_2.txt", "w")
the_file.write(mega_string)
the_file.close()