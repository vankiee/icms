import tkinter as tk
import tkinter.messagebox
from _tkinter import TclError
import webbrowser
import os
from tkinter import *
from datetime import *
from functools import partial
import calendar
import numpy as np
import mysql.connector
import smtplib, ssl
from socket import gaierror
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

TIME_TO_WAIT = 2000 # in milliseconds 

SIDEBAR_WIDTH = 200
MAINAREA_WIDTH = 750
WINDOW_HEIGHT = 750
BORDER_WIDTH = 1

SIDEBAR_COLOR = '#EBEBEB'
COURSE_FRAME_COLOR = '#FAFAFA'
COURSE_WINDOW_COLOR = '#FFFFFF'


##########################
#SQL codes - connects to SQL server, change details according to yours
con1 = mysql.connector.connect(
host="localhost",
user="root",
passwd="rhmEzhFJ",
database="project"
)

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('noreplyicmshku@gmail.com', 'COMP3278#^&')

# login time
#loginTime = sys.argv[2]
loginTime = '23:04:00'
#loginDate = sys.argv[3]
loginDate = "2021-04-22"

##########################
# Default Information (Will be changed into SQL extraction codes later)
# The group decided to remove timetable ID
class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email


#Removed the Teacher class


# Time_slot Class (Will be changed into Time class later)
class Time_slot:
    def __init__(self, start_day, start_time, end_time):
        self.start_day = start_day
        self.start_time = start_time
        self.end_time = end_time

daydict = {'MON':0, 'TUE':1, 'WED':2, 'THU':3, 'FRI':4, 'SAT':5, 'SUN':6}
def find_day(value):
    return next((k for k, v in daydict.items() if v == value), None)

# wrote the code here a bit to accomodate our new timeslot format
def Split(time_slot):
    daylist = time_slot.split(',')
    for day in daylist:
        # Will be in THU 0930 - 1130 format
        timelist = day.split(' ')
        day = timelist[0]
        time1hour = timelist[1]
        time2hour = timelist[3]
        t1 = Time_slot(daydict[day], time(int(time1hour[:2]), int(time1hour[2:]), 0), time(int(time2hour[:2]), int(time2hour[2:]),0))
    return t1


class Course:
    def __init__(self, course_code, course_name, course_description, time_slot, classroom_address, teacher_id, teacher_message, zoom_link, course_material_link):
        self.course_code = course_code
        self.course_name = course_name
        self.course_description = course_description
        self.time_slot = time_slot
        self.classroom_address = classroom_address
        self.teacher_id = teacher_id
        self.teacher_message = teacher_message
        self.zoom_link = zoom_link
        self.course_material_link = course_material_link


##########################

# I assume that the face recog will output out a student_id
#UID = sys.argv[1]
UID = "3035568324" # 3035568324 - dominique 3035569720 - joyce

cur1 = con1.cursor()
cur1.execute("SELECT * FROM Student WHERE Student_ID like \""+UID+"\"")
row = cur1.fetchall()[0][:]
student = Student(row[0], row[1], row[2])



# Collects timeslots
cur3 = con1.cursor()
cur3.execute("SELECT t.Course_code, ct.Time_slot \
FROM (((course c \
INNER JOIN teaches t \
ON t.Course_code = c.Course_code) \
INNER JOIN takes ta \
ON ta.Course_code = c.Course_code) \
INNER JOIN Course_timeslots ct \
ON ct.Course_code=c.Course_code) \
WHERE ta.Student_ID LIKE \""+UID+"\" \
ORDER BY c.Course_code")
temp = cur3.fetchall()
timeslots = []
for row in temp:
    timeslots.append((row[0], Split(row[1])))

# Collects all the other course data
cur2 = con1.cursor()
#no timeslot table yet, so i hardcoded them
# I also switched teacher_ID for teacher name
# also removed course page link for now
cur2.execute("SELECT c.Course_code, Course_name, Description, cl.Address, ts.name, Message, Zoom_link, cm.Course_material \
FROM (((((course c \
INNER JOIN classroom cl \
ON c.classroom_id = cl.classroom_id) \
INNER JOIN teaches t \
ON t.Course_code = c.Course_code) \
INNER JOIN Teacher ts \
ON t.Teacher_id = ts.Teacher_ID) \
INNER JOIN Course_materials cm \
ON cm.Course_code = c.Course_code) \
INNER JOIN takes ta \
ON ta.Course_code = c.Course_code) \
WHERE ta.Student_ID LIKE \""+UID+"\" \
ORDER BY c.Course_code")

temp = cur2.fetchall()
courses = []
for row in temp:
    course_timeslot = []
    for item in timeslots:
        if item[0] == row[0]:
            course_timeslot.append(item[1])
    course_timeslot = (sorted(course_timeslot, key = lambda x: x.start_day))
    c1 = Course(row[0], row[1],row[2], course_timeslot, row[3], row[4],row[5],row[6],row[7])
    courses.append(c1)

cur4 = con1.cursor(dictionary=True)
cur4.execute("SELECT Student.Student_ID, takes.Course_code, Course_timeslots.time_slot, Course.Course_name, Teacher.Name, Classroom.Address \
    FROM Student, takes, Course_timeslots, Course, Teacher, teaches, Classroom \
    WHERE Student.Student_ID LIKE \""+UID+"\" AND \
            Student.Student_ID = takes.Student_ID AND \
            takes.Course_code = Course_timeslots.Course_code AND \
            Course_timeslots.Course_code = Course.Course_code AND \
            teaches.Course_code = Course.Course_code AND \
            Course.Classroom_ID = Classroom.Classroom_ID AND \
            Teacher.Teacher_ID = teaches.Teacher_ID \
    ORDER BY Course_timeslots.time_slot")
tt1 = cur4.fetchall()
tt = list(tt1)
for item in tt:
    timeslot = item['time_slot'].split(' ')
    item.update({'time_slot' : [item['time_slot']]})
    FMT = '%H:%M'
    st = timeslot[1]
    st = st[:2]+":"+st[2:]
    et = timeslot[3]
    et = et[:2]+":"+et[2:]
    tdelta = datetime.strptime(et, FMT) - datetime.strptime(st, FMT)
    if (tdelta > timedelta(hours=1)):
        updateTS = []
        for i in range(int(tdelta.seconds/3600)):
            n = 2
            if i == 0:
                n = 3
            st = st[:2]+ st[n:]
            newst =str((int(st[:2])+1))+(st[2:])
            updateTS.append(timeslot[0] + " " + st + " - " + newst)
            st = newst
            if i == int(tdelta.seconds/3600) - 1:
                if(int(et[3:]) - int(st[2:])) != 0:
                    newet = et[:2]+ et[3:]
                    updateTS.append(timeslot[0] + " " + st + " - " + newet)
        additem = item.update({'time_slot' : updateTS})

##########################
# Initialize the next course (!= None if there is lesson within an hour)
next_course = None
next_time_slot = None

#Destroys all the widgets in the window
def RemoveAll(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Home Page Window

class homepageWindow(tk.Frame):

    def __init__(self, master, firstcreate, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        ##### window layout #####
        if firstcreate:
            # sidebar:
            self.sidebar = tk.Frame(self, height=WINDOW_HEIGHT, width=SIDEBAR_WIDTH, bg=SIDEBAR_COLOR, borderwidth=BORDER_WIDTH)
            self.sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

            # main content area:
            self.mainCanvas = Canvas(self, bg='white', height=WINDOW_HEIGHT, width=MAINAREA_WIDTH)
            self.mainCanvas.pack(expand=True, fill='both', side='left', padx=20)

            ##### sidebar content #####

            # Create "HKU System" label (Will be changed into Image later)
            Label(self.sidebar, text="HKU System", bg="green", fg="white", font="none 20 bold", height=2).pack(fill='x')

            # Create a frame and put it in the middle
            self.infoBox = tk.Frame(self.sidebar, bg=SIDEBAR_COLOR)
            self.infoBox.pack(fill="none", expand=True)

            # Create labels for student's information
            Label(self.infoBox, text="Name: "+student.name, font="none 12 bold", bg=SIDEBAR_COLOR).pack(anchor='w')
            Label(self.infoBox, text="UID: "+str(student.student_id), font="none 12 bold", bg=SIDEBAR_COLOR).pack(anchor='w')
            Label(self.infoBox, text="Email: "+student.email, font="none 12 bold", bg=SIDEBAR_COLOR).pack(anchor='w')
            Label(self.infoBox, text="Login Date: "+loginDate, font="none 12 bold", bg=SIDEBAR_COLOR).pack(anchor='w')
            Label(self.infoBox, text="Login Time: "+loginTime, font="none 12 bold", bg=SIDEBAR_COLOR).pack(anchor='w')

            # Create 'Timetable' button
            Button(self.infoBox, text="Timetable", command=partial(self.createTimetable)).pack(fill='x', pady=10)

            # Create 'Logout' button
            Button(self.sidebar, text="Logout", command=partial(self.click_logout_button)).pack(fill='x', side='bottom')

        else:
            self.mainCanvas = master
        self.createHomepage()

        if firstcreate:
            self.mainCanvas.configure(scrollregion = (0,0,1500,1200))#self.mainCanvas.bbox("all"))
            scrollbar = Scrollbar(self)
            scrollbar.pack(side = RIGHT, fill = Y)
            scrollbar.config(command=self.mainCanvas.yview)
            self.mainCanvas.config(yscrollcommand=scrollbar.set)

    def create_course_frame(self, isThisTime, timelabel, timeCourses):
        if isThisTime:
            label = Label(self.mainFrame, text=timelabel, font="none 25 bold", bg='white').pack(anchor='w', pady=10)
            for course in timeCourses:
                # Create a frame and put it in the middle
                courseFrame = tk.Frame(self.mainFrame, bg=COURSE_FRAME_COLOR, borderwidth=BORDER_WIDTH, relief='ridge')
                courseFrame.pack(fill='x', pady=10)

                Label(courseFrame, text=course.course_code, font="none 12 bold", bg=COURSE_FRAME_COLOR).pack(anchor='w')
                Label(courseFrame, text=course.course_name, font="none 12 bold", bg=COURSE_FRAME_COLOR).pack(anchor='w')
                for timeslot in course.time_slot:
                    Label(courseFrame, text="{} {} - {}".format(find_day(timeslot.start_day), timeslot.start_time, timeslot.end_time), font="none 12 bold", bg=COURSE_FRAME_COLOR).pack(anchor='w')
                Label(courseFrame, text=course.teacher_id, font="none 12 bold", bg=COURSE_FRAME_COLOR).pack(anchor='w')
                Button(courseFrame, text="Enter Course", highlightbackground=COURSE_FRAME_COLOR, command=partial(self.createNewWindow, course)).pack(padx=5, pady=5, side='right')

    def click_logout_button(self):
        root.destroy()
        loginDT = loginDate + " " + loginTime
        now = datetime.now()
        logoutDT = now.strftime("%Y-%m-%d %H:%M:%S")
        FMT = '%Y-%m-%d %H:%M:%S'
        duration = datetime.strptime(logoutDT, FMT) - datetime.strptime(loginDT, FMT)
        update =  "UPDATE `student` SET `duration (h:min:s)` = %s WHERE `student`.`Student_ID` = %s"
        val = (duration, UID)
        cur1.execute(update, val)
        con1.commit()
        exit()

    def createNewWindow(self, course):
        RemoveAll(self.mainCanvas)
        courseInfoWindow(self.mainCanvas, course)

    def createTimetable(self):
        RemoveAll(self.mainCanvas)
        TimeTable(self.mainCanvas, 14,8)

    def createHomepage(self):
        self.mainFrame = Frame(self.mainCanvas, bg='white')
        self.mainCanvas.create_window(MAINAREA_WIDTH/2,0, anchor=tk.N, window = self.mainFrame)        ##### main content #####

        today = datetime.today()
        tomororow = today + timedelta(days=1)

        # Categorize courses by time
        isToday = False
        todayCourses = []
        isTomorrow = False
        tomorrowCourses = []
        isThisWeek = False
        thisWeekCourses = []

        for course in courses:
            for time_slot in course.time_slot:
                if time_slot.start_day == int(today.weekday()) and course not in todayCourses:
                    isToday = True
                    todayCourses.append(course)
                elif time_slot.start_day == int(tomororow.weekday()) and course not in tomorrowCourses:
                    isTomorrow = True
                    tomorrowCourses.append(course)
                elif course not in thisWeekCourses:
                    isThisWeek = True
                    thisWeekCourses.append(course)
                    
        for course in todayCourses:
            if course in tomorrowCourses:
                tomorrowCourses.remove(course)
            if course in thisWeekCourses:
                thisWeekCourses.remove(course)

        for course in tomorrowCourses:
            if course in thisWeekCourses:
                thisWeekCourses.remove(course)

        # Show today's courses
        self.create_course_frame(isToday, "TODAY", todayCourses)

        # Show tomorrow's courses
        self.create_course_frame(isTomorrow, "TOMORROW", tomorrowCourses)

        # Show this week's courses
        self.create_course_frame(isThisWeek, "THIS WEEK", thisWeekCourses)


# Course Information Window

class courseInfoWindow(tk.Frame):

    def click_download_material_button(self, link):
            print("Clicked 'Download Course Materials' Button: " + link)

    # Send to Default Email for testing
    def click_email_information_button(self, email):
        from_addr = 'noreplyicmshku@gmail.com'
        to_addr = email
        courseIDName = self.course.course_code + " " + self.course.course_name
        message = MIMEMultipart("alternative")
        message["Subject"] = "(Please Do Not Reply!) Sent Course Information: " + courseIDName
        message["From"] = from_addr
        message["To"] = to_addr
        # use 'f' to  automatically insert variables in the text
        content = f"""\
Dear Student,

Your Requested Course Information as below:

        Course: {courseIDName}

        Classroom Address: {self.course.classroom_address}

        Teahcer's message: {self.course.teacher_message}

        Links of Zoom: {self.course.zoom_link}

        Link of Course Materials: {self.course.course_material_link}

This is the end of the email. Thank you."""

        part1 = MIMEText(content, "plain")
        message.attach(part1)
        try:
            status = smtp.sendmail(from_addr, to_addr, message.as_string())
            notification = "Successfully Sent"
            smtp.quit()
        except (gaierror, ConnectionRefusedError):
            notification = 'Failed to connect to the server. Bad connection settings?'
        except smtplib.SMTPServerDisconnected:
            notification = 'Failed to connect to the server. Wrong user/password?'
        except smtplib.SMTPException as e:
            notification = 'SMTP error occurred: ' + str(e)
        messagebox.showinfo("Email Status", notification)

    def open_link(self, zoom_link):
        new = 1
        webbrowser.open(zoom_link,new=new)

    def click_back_button(self):
        RemoveAll(self.mainCanvas)
        homepageWindow(self.mainCanvas, False)

    def __init__(self, newCanvas, course,*args, **kwargs):
        tk.Frame.__init__(self, newCanvas, *args, **kwargs)
        self.mainCanvas = newCanvas
        self.course = course
        mainFrame = Frame(newCanvas, bg='white')

        banner_label = Label(mainFrame, text=course.course_code + " " + course.course_name, bg="green", fg="white", font="none 16 bold", height=2)
        banner_label.bind('<Configure>', lambda e: banner_label.config(wraplength=root.winfo_width()-SIDEBAR_WIDTH))
        banner_label.pack(fill='x')

        Label(mainFrame, text=course.course_description, font="none 12", wraplength=MAINAREA_WIDTH, bg=COURSE_WINDOW_COLOR).pack(fill='x')

        Label(mainFrame, text="Lecture time: ", font="none 12 bold", bg=COURSE_WINDOW_COLOR).pack(anchor='w')
        for time_slot in course.time_slot:
            Label(mainFrame, text="         {} {} - {}".format(find_day(time_slot.start_day),time_slot.start_time.strftime("%H:%M"), time_slot.end_time.strftime("%H:%M")), font="none 12", bg=COURSE_WINDOW_COLOR).pack(anchor='w')
        Label(mainFrame, text="Teacher: ", font="none 12 bold", bg=COURSE_WINDOW_COLOR).pack(anchor='w')
        Label(mainFrame, text="         "+course.teacher_id, font="none 12", bg=COURSE_WINDOW_COLOR).pack(anchor='w')

        Label(mainFrame, text="Venue: ", font="none 12 bold", bg=COURSE_WINDOW_COLOR).pack(anchor='w')
        Label(mainFrame, text="         "+course.classroom_address, font="none 12", bg=COURSE_WINDOW_COLOR).pack(anchor='w')

        Label(mainFrame, text="Teacher Message: ", font="none 12 bold", bg=COURSE_WINDOW_COLOR).pack(anchor='w')
        Label(mainFrame, text="         "+course.teacher_message, font="none 12", bg=COURSE_WINDOW_COLOR).pack(anchor='w')

        Label(mainFrame, text="ZOOM Link: ", font="none 12 bold", bg=COURSE_WINDOW_COLOR).pack(anchor='w')
        Label(mainFrame, text="         "+course.zoom_link, font="none 12", fg='blue', bg=COURSE_WINDOW_COLOR).pack(anchor='w')

        newCanvas.create_window(MAINAREA_WIDTH/2,0, anchor=tk.N, window = mainFrame)
        Button(mainFrame,
                                  text = "Start the Lecture",
                                  fg = "white",
                                  bg = "blue",
                            command = partial(self.open_link, course.zoom_link)).pack()
        Button(mainFrame,text = "Send To My Email", fg = "white", bg = "green",
               command = partial(self.click_email_information_button, student.email)).pack()
        Button(mainFrame, text ="Back", highlightbackground=COURSE_WINDOW_COLOR, command=partial(self.click_back_button)).pack(anchor='se')

class TimeTable(tk.Frame):
    def __init__(self, parent, rows=14, columns=8):
        tk.Frame.__init__(self, parent, background="white")
        self.mainCanvas = parent
        self.mainCanvas.propagate(0)
        self._widgets = []
        days = ["filler", "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
        time = 830
        table = np.empty((rows, columns), dtype=object)
        table_content = ""
        global table_timeslot

        for column in range(columns):
            current_row = []
            for row in range(rows):
                if row == 0 and column == 0:
                    label = tk.Label(self, text= "", bg = "green",
                                    borderwidth=1, width = 9, font="none 12 bold")
                    table_content = ""
                elif row == 0 and column != 0:
                    label = tk.Label(self, bg = "green", text = days[column], 
                                 borderwidth=1, width = 18, height = 2, font="none 12 bold", fg = "white")
                    table_content = days[column]
                elif column == 0 and row != 0:
                    time_range = str(time).zfill(4) + " - " + str(time + 100).zfill(4) 
                    label = tk.Label(self, text = time_range, 
                                 borderwidth=1, width = 9, font="none 12 bold", bg = "light grey")
                    time += 100
                    table_content = time_range
                else:
                    label = tk.Label(self, text= "", relief = "groove",
                                    borderwidth=1, width = 18, font="none 12 bold")
                    table_content = ""
                        
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
                table[row][column] = table_content

            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

        for column in range(columns):
            for row in range(rows):
                table_timeslot = str(table[0][column]) + " " + str(table[row][0])
                for x in range(len(tt)):
                    if tt[x]['time_slot'][0] == table_timeslot:
                        content = tt[x]['Course_code'] + "\n" + tt[x]['Course_name'] + "\n\n" + tt[x]['Name'] + "\n" + tt[x]['Address']
                        table_content = content
                        label = tk.Label(self, text = content, font="none 12 bold", relief = "groove",
                                    borderwidth=1, width = 18, height = 8, wraplength = 155, justify=tk.CENTER)
                        label.grid(row = row,  column=column, sticky="nsew", padx=1, pady=1, rowspan = len(tt[x]['time_slot']))
                        
        
        self.mainCanvas.create_window(0,0, anchor=tk.NW, window = self)
        backButton = Button(self.mainCanvas, text ="Back", width = 10, command=self.click_back_button).pack(side = "bottom", 
                                                                                    pady = (20, 5))
        #backButton.grid(row=20, columnspan=20)
        xscrollbar = Scrollbar(root,orient=HORIZONTAL)
        xscrollbar.pack(side = BOTTOM, fill = X)
        xscrollbar.config(command=self.mainCanvas.xview)
        self.mainCanvas.config(xscrollcommand=xscrollbar.set)
        
    def click_back_button(self):
        RemoveAll(self.mainCanvas)
        homepageWindow(self.mainCanvas, False)

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)
    
#https://stackoverflow.com/questions/30965033/python-tkinter-application-fit-on-screen
#https://stackoverflow.com/questions/14817210/using-buttons-in-tkinter-to-navigate-to-different-pages-of-the-application
# Main

if __name__ == "__main__":

    # Get Current Time
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M:%S")
    current_timeT = time(int(current_time[:2]), int(current_time[3:5]), int(current_time[6:]))
    one_hour_later = time((int(current_time[:2])+1)%24, int(current_time[3:5]), int(current_time[6:]))
    current_timeNoS = current_datetime.strftime("%H:%M")

    # Find if there is lesson within an hour
    for course in courses:
        for time_slot in course.time_slot:
            if (time_slot.start_day == current_datetime.weekday() and
                time_slot.start_time > current_timeT and
                time_slot.start_time < one_hour_later):
                next_course = course
                next_time_slot = time_slot
     
    
    # Initalize root window
    root = tk.Tk()
    
    root.withdraw()
    try:
        root.after(TIME_TO_WAIT, root.destroy) 
        messagebox.showinfo("Welcome to HKU System", "Hello, "+student.name+"!\nYou successfully logged in at "+loginDate+" "+loginTime)
    except TclError:
        pass
    root = tk.Tk()
    
    root.title("HKU System")
    root.configure(background="white")
    homepage = homepageWindow(root, True)
    homepage.pack(fill=BOTH, expand=1)
    
    
    # If there is lesson within an hour, show notification. Otherwise, show homepage.
    if next_course != None:
        nextStartTime = next_time_slot.start_time.strftime("%H:%M")
        if (current_timeNoS[:2] == nextStartTime[:2]):
            remainingTime = int(nextStartTime[3:5]) - int(current_timeNoS[3:5])
        else:
            remainingTime = (60 - int(current_timeNoS[3:5])) + int(nextStartTime[3:5])
        remainingTime = str(remainingTime)
        messagebox.showinfo("Course: "+next_course.course_code, "You have a class in "+remainingTime+" minutes")
        homepage.createNewWindow(next_course)

    root.mainloop()
