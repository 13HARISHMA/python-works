#student info
import csv
def write_info(info_list):
    with open('studentadmin.csv','a') as file:
        writer=csv.writer(file)
        if csv_file.tell()==0:
            writer.writerow("name","age","roll_no")
        writer.writerow(info_list)
if __name__=='__main__':
condition=True
student_num=1
while(condition):
    student_info=input("enter students info (name,age,roll_no)")
    student_split=student_info.split(' ')
    print("\nentered info is \nname:{}\nage:{}\nroll_no:{}".format(student_info[0],student_info[1],student_info[2])
    msg=input("enter 'yes' for continue and 'no' end")
          if msg=="yes":
             write_info(student_info)
             msg=input("enter 'yes' for continue and 'no' end")
             if msg=="yes":
                condition=True
                student_num+=1
             elif msg=="no":
                condition==False
              elif msg==0:
                 print("\nenter the values again")
          
