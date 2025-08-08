import os
import shutil

#change these 4 variable with your folders destination
folder_img = "D:/ImageFolder"
folder_pdf = "D:/PdfFolder"
folder_notes = "D:/NotesFolder"
folder_videos = "D:/VideosFolder"

#C:\Users\rusua\Desktop

def move_files(source, files):
    for file in files:
                file_name = os.path.join(source, file)
                try:
                    if(file.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))):
                        os.makedirs(folder_img, exist_ok=True) 
                        shutil.move(file_name, folder_img)
                    if(file.lower().endswith((".pdf", ".docx", ".pptx", ".ppt"))):
                        os.makedirs(folder_pdf, exist_ok=True) 
                        shutil.move(file_name, folder_pdf)
                    if(file.lower().endswith((".txt", ".docx", ".csv", ".doc"))):
                        os.makedirs(folder_notes, exist_ok=True) 
                        shutil.move(file_name, folder_notes)  
                except Exception as e:
                   print(f"\nError moving {file}: {e}") 

def delete_file(file):
    if os.path.exists(file):
       os.remove(file)
    else:
       print("The file does not exist")
       
def delete_folder(folder):
    if os.path.exists(folder):
       shutil.rmtree(folder)
    else:
       print("The folder does not exist")
    

while True:
      print("\n1 - Move Files in the correct folder\n2 - Delete Files\n3 - Delete Folder\n4 - Quit")
      try:
          mode = int(input("What command do you want to run? "))
      except ValueError:
             print("\nInvalid input! Please type a number 1-4")
             continue  
      if mode == 1:
         source = input("Where are the files that you need to move? ") 
         fixed = source.replace('\\', '/')
         source = fixed
         files = os.listdir(source)
         move_files(source, files)
         print("\nThe files are organized")
      elif mode == 2:
           file = input("\nWhich file do you want to delete? ")
           fixed = file.replace('\\', '/')
           file = fixed
           try:
               consent_button = int(input("\nAre you sure you want to permanently delete this file? 1 - Yes 2 - No"))
               if(consent_button == 1):
                  delete_file(file)
                  print(f"\nI've deleted the file")
               elif consent_button == 2:
                     print("\nThe file was not deleted")
               else:
                     print("\nInvalid number")
           except ValueError:
                  print("\nInvalid input. Please enter a number (1 or 2).")
      elif mode == 3:
            folder = input("\nWhich folder do you want to delete?")
            fixed = folder.replace('\\', '/')
            folder = fixed
            try:
                consent_button = int(input("\nAre you sure you want to permanently delete this folder with all the content inside? 1 - Yes 2 - No"))
                if(consent_button == 1):
                   delete_folder(folder)
                   print(f"\nI've deleted the folder")
                elif consent_button == 2:
                   print("\nYou need to be more decisive next time")
                else:
                     print("\nInvalid number")
            except ValueError:
                   print("\nInvalid input. Please enter a number (1 or 2).")  
      elif mode == 4:
             print("\nI hope you organized your Files and Folders Goodbye!")
             break
      else:
            print("\nInvalid request, choose a number 1-4")