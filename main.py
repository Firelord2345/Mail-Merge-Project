#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    


with open("Mail Merge Project Start/Input/Names/invited_names.txt") as named_file:

    x=named_file.readlines()
    
  
with open("Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    y= file.read()
    for name in x:
        z=name.strip()
        text=y.replace("[name]",z)
        with open(f"Mail Merge Project Start/Output/letter_for_{z}",mode="w") as file1:
            completed=file1.write(text)
          
        
    
# import os
# print(os.getcwd())
