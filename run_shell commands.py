import subprocess

def print_echo_statement(*text_to_be_printed):
    print(subprocess.run(["echo",*text_to_be_printed],capture_output=True,text=True).stdout.strip())


def create_new_file_and_add_text(file_name,text_to_be_added): 
    try: 
        with open(file_name, "w") as f:
            command = ["echo", text_to_be_added]
            subprocess.run(command, stdout=f, check= True)
            print(f"File '{file_name}' created and text has been added successfully")
            f.close()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    except IOError as e:
        print(f"Error writing to file: {e}")

print("Added a new branch")

print_echo_statement("Hello","Sanjay!","Hope you are having fun learning Python !")
create_new_file_and_add_text("temp.txt","Hello Sanjay!\nHope you are having a good time learning Python.\nEnjoy")
