#import modules

from tkinter import *
import pyodbc
from tkinter import messagebox


# tk modul for creating gui

root = Tk()
root.title("STUDENT MARK SHEET")
root.geometry("570x230+500+250")
root.resizable(width=False, height=False)
root.config(bg="#2c3e50")


# database connetion

server = 'ANANDHAKUMAR'
db = 'database'
US = 'sa'
PA = 'Admin@123'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server +
                      ';DATABASE=' + db +
                      ';UID=' + US +
                      ';PWD=' + PA +
                      ';Trusted_Connection=yes')

cur = conn.cursor()


# VARIABLE DECLARATION

REG = StringVar()
SEM = StringVar()


#FRAME DESIGN for loging windows

entries_frame = Frame(root, bg="#535c68")
entries_frame.pack()
title = Label(entries_frame, text="MARK AUTOMATION SYSTEM", font=("Calibri", 20, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")


#LABLE AND TEXT TAGS for get register number and semester

lblREGNO1 = Label(entries_frame, text="REGISTER NUMBER", font=("Calibri", 18), bg="#535c68", fg="white")
lblREGNO1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
txtREGNO1 = Entry(entries_frame, textvariable=REG, font=("Calibri", 18), width=8)
txtREGNO1.grid(row=1, column=1, padx=10, pady=5, sticky="w")

lblSEM = Label(entries_frame, text="SEMESTER", font=("Calibri", 18), bg="#535c68", fg="white")
lblSEM.grid(row=2, column=0, padx=10, pady=5, sticky="w")
txtSEM = Entry(entries_frame, textvariable=SEM, font=("Calibri", 18), width=8)
txtSEM.grid(row=2, column=1, padx=10, pady=5, sticky="w")


#CONDITION FUNCTION TO USE DATA FETING AND VALIDATION
""" when it is used to valided the mark and grade in given databases 
use regno # regno is main use for all table connection and show in new windows """

def show():

    # get input from user


    roll = len(REG.get())

    # IF CONDITION FOR CHECKING ROLL

    if 8>= roll >6:
        roll_no = REG.get()

        #if condition for check geting semester is digit

        sem =SEM.get()
        global semester
        global sr

        if sem.isdigit():

            #in the condition is used to fetching to output
            sem=int(sem)
            if sem==1:
                semester='FIRST'
                sr='I'
            elif sem==2:
                semester='SECOND'
                sr='II'
            elif sem==3:
                semester='THIRD'
                sr='III'
            elif sem==4:
                semester='FOURTH'
                sr='IV'
            elif sem==5:
                semester='FIFTH'
                sr='V'
            elif sem==6:
                semester='SIXTH'
                sr='VI'





            #change roll_no in uppercase 
            roll_no=roll_no.upper()


            
            #postion_1 is use to search a data in subject table from major_code 
            #position_2 is used to search a data in subject table from major_code  
            #when difference between is postion_2 is use to take full position eg:20cs0,20ct0,2004L and postion_1 is use to
            #take position from like eg:like 20cs,20ct 
            position_1 = roll_no[0:4]+'%'
            position_2 = roll_no[0:5]

            #position_3 is used to search a data in major table from major_title  
            position_3 = roll_no[2:4]+'%'

            #position_4 is used to check ug and pg  
            position_4=roll_no[2:5]


            #take student name in student table 
            cur.execute("select NAME from student where REGNO='" + roll_no+ "'")
            nam = cur.fetchval()
            n1 = (''.join(str(nam)))

            #take name only
            name=n1[0:-10]

            #take dbo saperete in name
            db=n1[-9:-1]

            global REGNO
            REGNO=[]

            cur.execute("select REGNO from student")
            re = cur.fetchall()
            for r in re:
                r = ''.join(r[0])
            

                cur.execute("select REGNO from student where REGNO='" + str(r) + "'")
                n = cur.fetchval()
                REGNO.append(n)
            

            if (roll_no in REGNO):
                if sem == 1 or sem == 2 or sem == 3 or sem == 4 or sem == 5 or sem == 6:





                    # validate subject per sem

                    val = []

                    cur.execute("select SUBJECT_PER_SEM from subject where ((MAJOR_CODE LIKE '" + str(
                                position_1) + "')or (MAJOR_CODE='" + str(position_2) + "'))")
                    mm = cur.fetchval()
                    ttt = mm.strip()
                    subject = ttt.split()
                    



                    if sem == 1:
                        try:
                            first = subject[0]
                            last = subject[1]
                            for store in range(int(first), int(last)):
                                data = "SUB" + str(store)
                                val.append(data)
                        except IndexError:
                            messagebox.showerror("Error",
                                                 "sorry in the semester is unavailable.")

                    elif sem == 2:
                        try:
                            first = subject[1]
                            last = subject[2]
                            for store in range(int(first), int(last)):
                                data = "SUB" + str(store)
                                val.append(data)
                        except IndexError:
                            messagebox.showerror("Error",
                                                 "sorry in the semester is unavailable.")

                    elif sem == 3:
                        try:
                            first = subject[2]
                            last = subject[3]
                            for store in range(int(first), int(last)):
                                data = "SUB" + str(store)
                                val.append(data)
                        except IndexError:
                            messagebox.showerror("Error",
                                                 "sorry in the semester is unavailable.")

                    elif sem == 4:
                        try:
                            first = subject[3]
                            last = subject[4]
                            for store in range(int(first), int(last)):
                                data = "SUB" + str(store)
                                val.append(data)
                        except IndexError:
                            messagebox.showerror("Error",
                                                 "sorry in this semester is not uploaded.")

                    elif sem==5:
                        try:
                            first = subject[4]
                            last = subject[5]
                            for store in range(int(first), int(last)):
                                data = "SUB" + str(store)
                                val.append(data)
                        except IndexError:
                            if position_4=='010' or position_4=='020' or position_4=='030' or  position_4=='040' or  position_4=='04L' or  position_4=='050' or  position_4=='060' or  position_4=='070' or  position_4=='080' or  position_4=='090' or  position_4=='100' or  position_4=='110' or  position_4=='120' or  position_4=='130' :
                                messagebox.showerror("Error", "Please Enter the semester in-between 1 to 4, including Both.")
                            else:
                                messagebox.showerror("Error", "sorry in the semester is unavailable.")

                    elif sem==6:
                        try:
                            first = subject[5]
                            last = subject[6]
                            for store in range(int(first), int(last) + 1):
                                data = "SUB" + str(store)
                                val.append(data)

                        except IndexError:
                            if position_4 == '010' or position_4 == '020' or position_4 == '030' or position_4 == '040' or position_4 == '04L' or position_4 == '050' or position_4 == '060' or position_4 == '070' or position_4 == '080' or position_4 == '090' or position_4 == '100' or position_4 == '110' or position_4 == '120' or position_4 == '130':
                                messagebox.showerror("Error",
                                                     "Please Enter the semester in-between 1 to 4, including Both.")
                            else:
                                messagebox.showerror("Error", "sorry in the semester is unavailable.")

                    else:
                        messagebox.showerror("Error", "Please Enter valid semester only.")
                    
                    if not val:
                        pass
                    else:



                        # subject code validation

                        colm = []

                        for sub in val:
                            cur.execute("select " + sub + " from subject where MAJOR_CODE LIKE'" + position_1 + "'")
                            col = cur.fetchval()
                            colm.append(col)
                        


                        # sno  number
                        a = []
                        for h in range(1, len(colm) + 1):
                            a.append(sr)


                        #for output to ens of sem
                        global endx
                        global endy

                        if len(a) == 1:
                            endx = 75
                            endy = 260
                        elif len(a) == 2:
                            endx = 75
                            endy = 280
                        elif len(a) == 3:
                            endx = 75
                            endy = 300
                        elif len(a) == 4:
                            endx = 75
                            endy = 320
                        elif len(a) == 5:
                            endx = 75
                            endy = 340
                        elif len(a) == 6:
                            endx = 75
                            endy = 360
                        elif len(a) == 7:
                            endx = 75
                            endy = 380
                        elif len(a) == 8:
                            endx = 75
                            endy = 400
                        elif len(a) == 9:
                            endx = 75
                            endy = 420
                        elif len(a) == 10:
                            endx = 75
                            endy = 440


                        # subject tital and credit

                        cr = []
                        s_t = []
                        for sub in val:
                            cur.execute("select " + sub + " from subject where MAJOR_CODE LIKE'" + position_1 + "'")
                            st = cur.fetchval()
                            # tital
                        
                            cur.execute("select SUBJECT_TITLES from scheme where SUBJECT_CODE='" + str(st) + "'")
                            sst = cur.fetchval()
                            s_t.append(sst)
                            # credits
                            cur.execute("select CREDITS from scheme where SUBJECT_CODE='" + str(st) + "'")
                            noc = cur.fetchval()
                            cr.append(noc)


                        # take mark from eos and cia in database

                        eos = []
                        cia = []
                        Eos = []
                        Cia = []

                        for sub in val:

                            cur.execute(
                                "select NEOS" + sub[3:5] + " from student, subject where ((MAJOR_CODE LIKE '" + str(
                                    position_2) + "') or (MAJOR_CODE='" + str(position_1) + "')) and REGNO='" + str(
                                    roll_no) + "'")
                            eos_mark = cur.fetchval()

                            if eos_mark ==None :
                                cur.execute("select FEOS" + sub[3:5] + " from student, subject where MAJOR_CODE LIKE'" +
                                    position_1 + "' and REGNO='" + str(roll_no) + "'")
                                t = cur.fetchval()
                                Eos = (''.join(t))
                            else:
                                Eos = (''.join(eos_mark))

                            eos.append(''.join(Eos))
                            cur.execute("select NCIA" + sub[3:5] + " from student, subject where MAJOR_CODE LIKE'" +
                                position_1 + "' and REGNO='" + str(roll_no) + "'")
                            cia_mark = cur.fetchval()

                            if cia_mark ==None:
                                cur.execute("select FCIA" + sub[3:5] + " from student, subject where MAJOR_CODE LIKE'" +
                                    position_1 + "' and REGNO='" + str(roll_no) + "'")
                                t = cur.fetchval()
                                Cia = (''.join(str(t)))
                            else:
                                Cia = (''.join(str(cia_mark)))
                            cia.append(''.join(Cia))

                        
                        cur.execute("select MAJOR from major where MAJOR_CODE LIKE'" + position_3 + "'")
                        major = cur.fetchval()

                        dep = major
                        

                        eos_minimum = []

                        for i in colm:
                            cur.execute("select EOS_MIN_MARKS from scheme where SUBJECT_CODE='" + i + "'")
                            mini = cur.fetchval()
                            eos_minimum.append(mini)

                        eos_maximum = []

                        for i in colm:
                            cur.execute("select EOS_MAX_MARKS from scheme where SUBJECT_CODE='" + i + "'")
                            maxi = cur.fetchval()
                            eos_maximum.append(','.join(maxi))

                        cia_minimum = []

                        for i in colm:
                            cur.execute("select CIA_MIN_MARKS from scheme where SUBJECT_CODE='" + i + "'")
                            mini = cur.fetchval()
                            cia_minimum.append(mini)

                        cia_maximum = []

                        for i in colm:
                            cur.execute("select CIA_MAX_MARKS from scheme where SUBJECT_CODE='" + i + "'")
                            maxi = cur.fetchval()
                            cia_maximum.append(maxi)


                        max_mark = []

                        for i in colm:
                            cur.execute("select MAX_MARKS from scheme where SUBJECT_CODE='" + i + "'")
                            maxi = cur.fetchval()
                            max_mark.append(maxi)

                        min_mark = []
                        for i in colm:
                            cur.execute("select MIN_MARKS from scheme where SUBJECT_CODE='" + i + "'")
                            min = cur.fetchval()
                            min_mark.append(min)

                       
                        to = []
                        g_p = []
                        re = []
                        global gr0, gr1, gr2, gr3, gr4, gr5, gr6, gr7, gr8, gr9
                        for j in range(0, len(eos)):
                            global x
                            global y

                            for x in eos[j:j + 1]:
                                pass

                            for y in cia[j:j + 1]:
                                pass
                            if x.isdigit() and y.isdigit():
                                z = (int(x) + int(y))
                                to.append(''.join(str(z)))
                            else:
                                to.append('*****')
                            global n007
                            global nn
                            global mn
                            for n007 in eos_minimum[j:j+1]:
                                pass
                            for nn in cia_minimum[j:j+1]:
                                pass
                            for mn in min_mark[j:j + 1]:
                                pass

                            if x.isdigit() and y.isdigit():
                                if int(x) >= int(n007) and int(y) >= int(nn):
                                    if (int(x) + int(y)) >= int(mn):
                                        g_p.append(str((int(x) + int(y)) / 10))
                                        re.append('pass')
                                    else:
                                        g_p.append('****')
                                        re.append('fail')
                                else:
                                    g_p.append('****')
                                    re.append('fail')
                            else:
                                g_p.append('****')
                                re.append('fail')

                            global gr
                            gr = []
                            for e in range(0, len(g_p)):
                                for u in to[e:e + 1]:
                                    if u.isdigit():

                                        if int(u) > 89:
                                            gr.append('O')
                                        elif 90 > int(u) > 79:
                                            gr.append('D+')
                                        elif 80 > int(u) > 74:
                                            gr.append('D')
                                        elif 75 > int(u) > 69:
                                            gr.append('A+')
                                        elif 70 > int(u) > 59:
                                            gr.append('A')
                                        elif 60 > int(u) > 49:
                                            gr.append('B')
                                        elif 50 > int(u) >= int(mn):
                                            gr.append('C')
                                        else:
                                            gr.append('RA')
                                    else:
                                        gr.append('ABST')

                            #grade values for output

                            gr01 = str(gr[0:1]);gr0 = gr01[2:-2]
                            gr11 = str(gr[1:2]);gr1 = gr11[2:-2]
                            gr21 = str(gr[2:3]);gr2 = gr21[2:-2]
                            gr31 = str(gr[3:4]);gr3 = gr31[2:-2]
                            gr41 = str(gr[4:5]);gr4 = gr41[2:-2]
                            gr51 = str(gr[5:6]);gr5 = gr51[2:-2]
                            gr61 = str(gr[6:7]);gr6 = gr61[2:-2]
                            gr71 = str(gr[7:8]);gr7 = gr71[2:-2]
                            gr81 = str(gr[8:9]);gr8 = gr81[2:-2]
                            gr91 = str(gr[9:10]);gr9 = gr91[2:-2]

                        #semester type 'I' value for output
                        a01 = str(a[0:1]);a0 = a01[2:-2]
                        a11 = str(a[1:2]);a1 = a11[2:-2]
                        a21 = str(a[2:3]);a2 = a21[2:-2]
                        a31 = str(a[3:4]);a3 = a31[2:-2]
                        a41 = str(a[4:5]);a4 = a41[2:-2]
                        a51 = str(a[5:6]);a5 = a51[2:-2]
                        a61 = str(a[6:7]);a6 = a61[2:-2]
                        a71 = str(a[7:8]);a7 = a71[2:-2]
                        a81 = str(a[8:9]);a8 = a81[2:-2]
                        a91 = str(a[9:10]);a9 = a91[2:-2]

                        #subject \ paper name to value for the output
                        s_t01 = str(s_t[0:1]);s_t0 = s_t01[2:-2]
                        s_t11 = str(s_t[1:2]);s_t1 = s_t11[2:-2]
                        s_t21 = str(s_t[2:3]);s_t2 = s_t21[2:-2]
                        s_t31 = str(s_t[3:4]);s_t3 = s_t31[2:-2]
                        s_t41 = str(s_t[4:5]);s_t4 = s_t41[2:-2]
                        s_t51 = str(s_t[5:6]);s_t5 = s_t51[2:-2]
                        s_t61 = str(s_t[6:7]);s_t6 = s_t61[2:-2]
                        s_t71 = str(s_t[7:8]);s_t7 = s_t71[2:-2]
                        s_t81 = str(s_t[8:9]);s_t8 = s_t81[2:-2]
                        s_t91 = str(s_t[9:10]);s_t9 = s_t91[2:-2]
                        # subject name broken to show another line
                        s_t0 = str(s_t0);va00 = str(s_t0[0:37]);va01 = str(s_t0[37:80])
                        s_t1 = str(s_t1); va10 = str(s_t1[0:37]); va11 = str(s_t1[37:80])
                        s_t2 = str(s_t2); va20 = str(s_t2[0:37]); va21 = str(s_t2[37:80])
                        s_t3 = str(s_t3); va30 = str(s_t3[0:37]); va31 = str(s_t3[37:80])
                        s_t4 = str(s_t4); va40 = str(s_t4[0:37]); va41 = str(s_t4[37:80])
                        s_t5 = str(s_t5); va50 = str(s_t5[0:37]); va51 = str(s_t5[37:80])
                        s_t6 = str(s_t6); va60 = str(s_t6[0:37]); va61 = str(s_t6[37:80])
                        s_t7 = str(s_t7); va70 = str(s_t7[0:37]); va71 = str(s_t7[37:80])
                        s_t8 = str(s_t8); va80 = str(s_t8[0:37]); va81 = str(s_t8[37:80])
                        s_t9 = str(s_t9); va90 = str(s_t9[0:37]); va91 = str(s_t9[37:80])


                        #eose mark for output
                        e01 = str(eos[0:1]);e0 = e01[2:-2]
                        e11 = str(eos[1:2]);e1 = e11[2:-2]
                        e21 = str(eos[2:3]);e2 = e21[2:-2]
                        e31 = str(eos[3:4]);e3 = e31[2:-2]
                        e41 = str(eos[4:5]);e4 = e41[2:-2]
                        e51 = str(eos[5:6]);e5 = e51[2:-2]
                        e61 = str(eos[6:7]);e6 = e61[2:-2]
                        e71 = str(eos[7:8]);e7 = e71[2:-2]
                        e81 = str(eos[8:9]);e8 = e81[2:-2]
                        e91 = str(eos[9:10]);e9 = e91[2:-2]

                        #cia mark for output

                        c01 = str(cia[0:1]);c0 = c01[2:-2]
                        c11 = str(cia[1:2]);c1 = c11[2:-2]
                        c21 = str(cia[2:3]);c2 = c21[2:-2]
                        c31 = str(cia[3:4]);c3 = c31[2:-2]
                        c41 = str(cia[4:5]);c4 = c41[2:-2]
                        c51 = str(cia[5:6]);c5 = c51[2:-2]
                        c61 = str(cia[6:7]);c6 = c61[2:-2]
                        c71 = str(cia[7:8]);c7 = c71[2:-2]
                        c81 = str(cia[8:9]);c8 = c81[2:-2]
                        c91 = str(cia[9:10]);c9 = c91[2:-2]

                        #total mark for output

                        to01 = str(to[0:1]);to0 = to01[2:-2]
                        to11 = str(to[1:2]);to1 = to11[2:-2]
                        to21 = str(to[2:3]);to2 = to21[2:-2]
                        to31 = str(to[3:4]);to3 = to31[2:-2]
                        to41 = str(to[4:5]);to4 = to41[2:-2]
                        to51 = str(to[5:6]);to5 = to51[2:-2]
                        to61 = str(to[6:7]);to6 = to61[2:-2]
                        to71 = str(to[7:8]);to7 = to71[2:-2]
                        to81 = str(to[8:9]);to8 = to81[2:-2]
                        to91 = str(to[9:10]);to9 = to91[2:-2]

                        #credits for output

                        cr01 = str(cr[0:1]);cr0 = cr01[1:-1]
                        cr11 = str(cr[1:2]);cr1 = cr11[1:-1]
                        cr21 = str(cr[2:3]);cr2 = cr21[1:-1]
                        cr31 = str(cr[3:4]);cr3 = cr31[1:-1]
                        cr41 = str(cr[4:5]);cr4 = cr41[1:-1]
                        cr51 = str(cr[5:6]);cr5 = cr51[1:-1]
                        cr61 = str(cr[6:7]);cr6 = cr61[1:-1]
                        cr71 = str(cr[7:8]);cr7 = cr71[1:-1]
                        cr81 = str(cr[8:9]);cr8 = cr81[1:-1]
                        cr91 = str(cr[9:10]);cr9 = cr91[1:-1]

                        #grade point for output

                        g_p01 = str(g_p[0:1]);g_p0 = g_p01[2:-2]
                        g_p11 = str(g_p[1:2]);g_p1 = g_p11[2:-2]
                        g_p21 = str(g_p[2:3]);g_p2 = g_p21[2:-2]
                        g_p31 = str(g_p[3:4]);g_p3 = g_p31[2:-2]
                        g_p41 = str(g_p[4:5]);g_p4 = g_p41[2:-2]
                        g_p51 = str(g_p[5:6]);g_p5 = g_p51[2:-2]
                        g_p61 = str(g_p[6:7]);g_p6 = g_p61[2:-2]
                        g_p71 = str(g_p[7:8]);g_p7 = g_p71[2:-2]
                        g_p81 = str(g_p[8:9]);g_p8 = g_p81[2:-2]
                        g_p91 = str(g_p[9:10]);g_p9 = g_p91[2:-2]


                        #result for output

                        re01 = str(re[0:1]);re0 = re01[2:-2]
                        re11 = str(re[1:2]);re1 = re11[2:-2]
                        re21 = str(re[2:3]);re2 = re21[2:-2]
                        re31 = str(re[3:4]);re3 = re31[2:-2]
                        re41 = str(re[4:5]);re4 = re41[2:-2]
                        re51 = str(re[5:6]);re5 = re51[2:-2]
                        re61 = str(re[6:7]);re6 = re61[2:-2]
                        re71 = str(re[7:8]);re7 = re71[2:-2]
                        re81 = str(re[8:9]);re8 = re81[2:-2]
                        re91 = str(re[9:10]);re9 = re91[2:-2]

                        #new window for frame result

                        from PIL import ImageTk, Image
                        ws = Toplevel()
                        ws.title('result')
                        ws.geometry('590x810+500+10')
                        ws.resizable(width=False, height=False)


                        #image resize

                        image = Image.open('D:\\my download\\chrom\\page_1 (1).png')
                        resize = image.resize((587, 801), Image.LANCZOS)
                        image_nw = ImageTk.PhotoImage(resize)

                        #for line separation in long subject name

                        x01 = 0
                        x02 = 0
                        x03 = 0
                        x04 = 0
                        x05 = 0
                        x06 = 0
                        x07 = 0
                        x08 = 0
                        x09 = 0
                        x00 = 0

                        if va01 == '':
                            pass
                        else:
                            x01 = x01 + 10
                        if va11 == '':
                            pass
                        else:
                            x02 = x02 + 10
                        if va21 == '':
                            pass
                        else:
                            x03 = x03 + 10
                        if va31 == '':
                            pass
                        else:
                            x04 = x04 + 10
                        if va41 == '':
                            pass
                        else:
                            x05 = x05 + 10
                        if va51 == '':
                            pass
                        else:
                            x06 = x06 + 10
                        if va61 == '':
                            pass
                        else:
                            x07 = x07 + 10
                        if va71 == '':
                            pass
                        else:
                            x08 = x08 + 10
                        if va81 == '':
                            pass
                        else:
                            pass
                            x09 = x09 + 10
                        if va91 == '':
                            pass
                        else:
                            x00 = x00 + 10


                        rt0 = 260
                        rt1 = 280 + x01
                        rt2 = 300 + x01 + x02
                        rt3 = 320 + x01 + x02 + x03
                        rt4 = 340 + x01 + x02 + x03 + x04
                        rt5 = 360 + x01 + x02 + x03 + x04 + x05
                        rt6 = 380 + x01 + x02 + x03 + x04 + x05 + x06
                        rt7 = 400 + x01 + x02 + x03 + x04 + x05 + x06 + x07
                        rt8 = 420 + x01 + x02 + x03 + x04 + x05 + x06 + x07 + x08
                        rt9 = 440 + x01 + x02 + x03 + x04 + x05 + x06 + x07 + x08 + x09

                        canva = Canvas(ws, width=590, height=800)
                        canva.pack(fill="both", anchor=CENTER)
                        canva.create_image(0, 0, image=image_nw, anchor='nw')
                        # name of the student
                        canva.create_text(55, 143, text=name, fill='black', font=("Helvetica", 8), anchor='w')
                        # Data of birth
                        canva.create_text(335, 143, text=db, fill='black', font=("Helvetica", 8), anchor='w')
                        # Regno
                        canva.create_text(480, 143, text=roll_no, fill='black', font=("Helvetica", 8), anchor='w')
                        # course name
                        canva.create_text(70, 172, text=dep, fill='black', font=("Helvetica", 8), anchor='w')
                        # semester
                        canva.create_text(500, 172, text=semester, fill='black', font=("Helvetica", 8), anchor='w')
                        # paper1
                        # sem row
                        canva.create_text(15, rt0, text=a0, fill='black', font=("Helvetica", 8), anchor='w')
                        # part row
                        canva.create_text(45, rt0, text='', fill='black', font=("Helvetica", 8), anchor='w')
                        # subject/paper row
                        canva.create_text(75, rt0, text=va00, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt0+10, text=va01, fill='black', font=("Helvetica", 8), anchor='w')
                        # eose row
                        canva.create_text(320, rt0, text=e0, fill='black', font=("Helvetica", 8), anchor='w')
                        # cia row
                        canva.create_text(345, rt0, text=c0, fill='black', font=("Helvetica", 8), anchor='w')
                        # total row
                        canva.create_text(370, rt0, text=to0, fill='black', font=("Helvetica", 8), anchor='w')
                        # no.of.credits row
                        canva.create_text(410, rt0, text=cr0, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade points row
                        canva.create_text(450, rt0, text=g_p0, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade row
                        canva.create_text(500, rt0, text=gr0, fill='black', font=("Helvetica", 8), anchor='w')
                        # result row
                        canva.create_text(540, rt0, text=re0, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper2
                        # sem row
                        canva.create_text(15, rt1, text=a1, fill='black', font=("Helvetica", 8), anchor='w')
                        # part row
                        canva.create_text(45, rt1, text='', fill='black', font=("Helvetica", 8), anchor='w')
                        # subject/paper row
                        canva.create_text(75, rt1, text=va10, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt1+10, text=va11, fill='black', font=("Helvetica", 8), anchor='w')
                        # eose row
                        canva.create_text(320, rt1, text=e1, fill='black', font=("Helvetica", 8), anchor='w')
                        # cia row
                        canva.create_text(345, rt1, text=c1, fill='black', font=("Helvetica", 8), anchor='w')
                        # total row
                        canva.create_text(370, rt1, text=to1, fill='black', font=("Helvetica", 8), anchor='w')
                        # no.of.credits row
                        canva.create_text(410, rt1, text=cr1, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade points row
                        canva.create_text(450, rt1, text=g_p1, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade row
                        canva.create_text(500, rt1, text=gr1, fill='black', font=("Helvetica", 8), anchor='w')
                        # result row
                        canva.create_text(540, rt1, text=re1, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper3
                        # sem row
                        canva.create_text(15, rt2, text=a2, fill='black', font=("Helvetica", 8), anchor='w')
                        # part row
                        canva.create_text(45, rt2, text='', fill='black', font=("Helvetica", 8), anchor='w')
                        # subject/paper row
                        canva.create_text(75, rt2, text=va20, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt2+10, text=va21, fill='black', font=("Helvetica", 8), anchor='w')
                        # eose row
                        canva.create_text(320, rt2, text=e2, fill='black', font=("Helvetica", 8), anchor='w')
                        # cia row
                        canva.create_text(345, rt2, text=c2, fill='black', font=("Helvetica", 8), anchor='w')
                        # total row
                        canva.create_text(370, rt2, text=to2, fill='black', font=("Helvetica", 8), anchor='w')
                        # no.of.credits row
                        canva.create_text(410, rt2, text=cr2, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade points row
                        canva.create_text(450, rt2, text=g_p2, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade row
                        canva.create_text(500, rt2, text=gr2, fill='black', font=("Helvetica", 8), anchor='w')
                        # result row
                        canva.create_text(540, rt2, text=re2, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper4
                        # sem row
                        canva.create_text(15, rt3, text=a3, fill='black', font=("Helvetica", 8), anchor='w')
                        # part row
                        canva.create_text(45, rt3, text='', fill='black', font=("Helvetica", 8), anchor='w')
                        # subject/paper row
                        canva.create_text(75, rt3, text=va30, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt3+10, text=va31, fill='black', font=("Helvetica", 8), anchor='w')

                        # eose row
                        canva.create_text(320, rt3, text=e3, fill='black', font=("Helvetica", 8), anchor='w')
                        # cia row
                        canva.create_text(345, rt3, text=c3, fill='black', font=("Helvetica", 8), anchor='w')
                        # total row
                        canva.create_text(370, rt3, text=to3, fill='black', font=("Helvetica", 8), anchor='w')
                        # no.of.credits row
                        canva.create_text(410, rt3, text=cr3, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade points row
                        canva.create_text(450, rt3, text=g_p3, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade row
                        canva.create_text(500, rt3, text=gr3, fill='black', font=("Helvetica", 8), anchor='w')
                        # result row
                        canva.create_text(540, rt3, text=re3, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper5
                        # sem row
                        canva.create_text(15, rt4, text=a4, fill='black', font=("Helvetica", 8), anchor='w')
                        # part row
                        canva.create_text(45, rt4, text='', fill='black', font=("Helvetica", 8), anchor='w')
                        # subject/paper row
                        canva.create_text(75, rt4, text=va40, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt4+10, text=va41, fill='black', font=("Helvetica", 8), anchor='w')
                        # eose row
                        canva.create_text(320, rt4, text=e4, fill='black', font=("Helvetica", 8), anchor='w')
                        # cia row
                        canva.create_text(345, rt4, text=c4, fill='black', font=("Helvetica", 8), anchor='w')
                        # total row
                        canva.create_text(370, rt4, text=to4, fill='black', font=("Helvetica", 8), anchor='w')
                        # no.of.credits row
                        canva.create_text(410, rt4, text=cr4, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade points row
                        canva.create_text(450, rt4, text=g_p4, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade row
                        canva.create_text(500, rt4, text=gr4, fill='black', font=("Helvetica", 8), anchor='w')
                        # result row
                        canva.create_text(540, rt4, text=re4, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper6
                        # sem row
                        canva.create_text(15, rt5, text=a5, fill='black', font=("Helvetica", 8), anchor='w')
                        # part row
                        canva.create_text(45, rt5, text='', fill='black', font=("Helvetica", 8), anchor='w')
                        # subject/paper row
                        canva.create_text(75, rt5, text=va50, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt5+10, text=va51, fill='black', font=("Helvetica", 8), anchor='w')
                        # eose row
                        canva.create_text(320, rt5, text=e5, fill='black', font=("Helvetica", 8), anchor='w')
                        # cia row
                        canva.create_text(345, rt5, text=c5, fill='black', font=("Helvetica", 8), anchor='w')
                        # total row
                        canva.create_text(370, rt5, text=to5, fill='black', font=("Helvetica", 8), anchor='w')
                        # no.of.credits row
                        canva.create_text(410, rt5, text=cr5, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade points row
                        canva.create_text(450, rt5, text=g_p5, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade row
                        canva.create_text(500, rt5, text=gr5, fill='black', font=("Helvetica", 8), anchor='w')
                        # result row
                        canva.create_text(540, rt5, text=re5, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper7
                        # sem row
                        canva.create_text(15, rt6, text=a6, fill='black', font=("Helvetica", 8), anchor='w')
                        # part row
                        canva.create_text(45, rt6, text='', fill='black', font=("Helvetica", 8), anchor='w')
                        # subject/paper row
                        canva.create_text(75, rt6, text=va60, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt6+10, text=va61, fill='black', font=("Helvetica", 8), anchor='w')
                        # eose row
                        canva.create_text(320, rt6, text=e6, fill='black', font=("Helvetica", 8), anchor='w')
                        # cia row
                        canva.create_text(345, rt6, text=c6, fill='black', font=("Helvetica", 8), anchor='w')
                        # total row
                        canva.create_text(370, rt6, text=to6, fill='black', font=("Helvetica", 8), anchor='w')
                        # no.of.credits row
                        canva.create_text(410, rt6, text=cr6, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade points row
                        canva.create_text(450, rt6, text=g_p6, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade row
                        canva.create_text(500, rt6, text=gr6, fill='black', font=("Helvetica", 8), anchor='w')
                        # result row
                        canva.create_text(540, rt6, text=re6, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper8
                        # sem row
                        canva.create_text(15, rt7, text=a7, fill='black', font=("Helvetica", 8), anchor='w')
                        # part row
                        canva.create_text(45, rt7, text='', fill='black', font=("Helvetica", 8), anchor='w')
                        # subject/paper row
                        canva.create_text(75, rt7, text=va70, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt7+10, text=va71, fill='black', font=("Helvetica", 8), anchor='w')
                        # eose row
                        canva.create_text(320, rt7, text=e7, fill='black', font=("Helvetica", 8), anchor='w')
                        # cia row
                        canva.create_text(345, rt7, text=c7, fill='black', font=("Helvetica", 8), anchor='w')
                        # total row
                        canva.create_text(370, rt7, text=to7, fill='black', font=("Helvetica", 8), anchor='w')
                        # no.of.credits row
                        canva.create_text(410, rt7, text=cr7, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade points row
                        canva.create_text(450, rt7, text=g_p7, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade row
                        canva.create_text(500, rt7, text=gr7, fill='black', font=("Helvetica", 8), anchor='w')
                        # result row
                        canva.create_text(540, rt7, text=re7, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper9
                        # sem row
                        canva.create_text(15, rt8, text=a8, fill='black', font=("Helvetica", 8), anchor='w')
                        # part row
                        canva.create_text(45, rt8, text='', fill='black', font=("Helvetica", 8), anchor='w')
                        # subject/paper row
                        canva.create_text(75, rt8, text=va80, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt8+10, text=va81, fill='black', font=("Helvetica", 8), anchor='w')
                        # eose row
                        canva.create_text(320, rt8, text=e8, fill='black', font=("Helvetica", 8), anchor='w')
                        # cia row
                        canva.create_text(345, rt8, text=c8, fill='black', font=("Helvetica", 8), anchor='w')
                        # total row
                        canva.create_text(370, rt8, text=to8, fill='black', font=("Helvetica", 8), anchor='w')
                        # no.of.credits row
                        canva.create_text(410, rt8, text=cr8, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade points row
                        canva.create_text(450, rt8, text=g_p8, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade row
                        canva.create_text(500, rt8, text=gr8, fill='black', font=("Helvetica", 8), anchor='w')
                        # result row
                        canva.create_text(540, rt8, text=re8, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper10
                        # sem row
                        canva.create_text(15, rt9, text=a9, fill='black', font=("Helvetica", 8), anchor='w')
                        # part row
                        canva.create_text(45, rt9, text='', fill='black', font=("Helvetica", 8), anchor='w')
                        # subject/paper row
                        canva.create_text(75, rt9, text=va90, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt9, text=va91, fill='black', font=("Helvetica", 8), anchor='w')
                        # eose row
                        canva.create_text(320, rt9, text=e9, fill='black', font=("Helvetica", 8), anchor='w')
                        # cia row
                        canva.create_text(345, rt9, text=c9, fill='black', font=("Helvetica", 8), anchor='w')
                        # total row
                        canva.create_text(370, rt9, text=to9, fill='black', font=("Helvetica", 8), anchor='w')
                        # no.of.credits row
                        canva.create_text(410, rt9, text=cr9, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade points row
                        canva.create_text(450, rt9, text=g_p9, fill='black', font=("Helvetica", 8), anchor='w')
                        # grade row
                        canva.create_text(500, rt9, text=gr9, fill='black', font=("Helvetica", 8), anchor='w')
                        # result row
                        canva.create_text(540, rt9, text=re9, fill='black', font=("Helvetica", 8), anchor='w')

                        # end of semester
                        endy0 = x01 + x02 + x03 + x04 + x05 + x06 + x07 + x08 + x09 + x00
                        canva.create_text(endx, endy +endy0 + 20, text='## END OF THE SEMESTER ##', fill='black',
                                          font=("Helvetica", 8), anchor='w')


                        ws.mainloop()







                else:
                    messagebox.showerror('error', 'please enter the semester between 1 to 6')
            else:
                messagebox.showerror("Error", "Please check register number")
        else:
            messagebox.showerror("Error", "Please enter the semester number in integer")
    else:
        messagebox.showerror('error', 'please enter the register number between 7 to 8 character')
def clearAll():
    REG.set('')
    SEM.set('')

def Quit():
    root.quit()



btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnsearch = Button(btn_frame, command=show, text="Search Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white",
                   bg="#16a085", bd=0).grid(row=0, column=0)
btnclear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"),
                  fg="white", bg="#2980b9",
                  bd=0).grid(row=0, column=1, padx=10)
btnquit = Button(btn_frame, command=Quit, text="QUIT", width=15, font=("Calibri", 16, "bold"),
                  fg="white", bg="red",
                  bd=0).grid(row=0, column=2, padx=10)




root.mainloop()