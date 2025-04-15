import sqlite3
from datetime import datetime

conn=sqlite3.connect("direct_english.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

def connect_db():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS Trainers (
            trainerid INTEGER PRIMARY KEY AUTOINCREMENT ,
            trainername VARCHAR(255),
            mobileno VARCHAR(20) UNIQUE,
            email VARCHAR(255) UNIQUE,
            address VARCHAR(255),
            experience FLOAT,
            courses VARCHAR(255),
            dob DATE,
            gender VARCHAR(10)
        );

        CREATE TABLE IF NOT EXISTS Students (
            studentid INTEGER PRIMARY KEY AUTOINCREMENT,
            studentname VARCHAR(255),
            mobileno VARCHAR(20) UNIQUE,
            email VARCHAR(255) UNIQUE,
            address VARCHAR(255),
            dob DATE,
            gender VARCHAR(10),
            parentname VARCHAR(255)
        );


        CREATE TABLE IF NOT EXISTS Courses (
            courseid INTEGER PRIMARY KEY AUTOINCREMENT,
            coursename VARCHAR(255),
            courseprice FLOAT,
            duration INTEGER 
        );

        CREATE TABLE IF NOT EXISTS Batches (
            batchid INTEGER PRIMARY KEY,
            batchname VARCHAR(255),
            courseid INTEGER,
            trainerid INTEGER,
            studentid INTEGER,
            startdate DATE,
            enddate DATE,
            batchtiming VARCHAR(255),
            classroom VARCHAR(255),
            coursefees FLOAT,
            paidfees FLOAT,
            balancefees FLOAT,
            FOREIGN KEY (courseid) REFERENCES Courses(courseid),
            FOREIGN KEY (trainerid) REFERENCES Trainers(trainerid),
            FOREIGN KEY (studentid) REFERENCES Students(studentid)
        );

        CREATE TABLE IF NOT EXISTS Trainerpayments (
            batchid INTEGER,
            trainerid INTEGER,
            trainerfees FLOAT,
            trainerpaidfees FLOAT,
            trainerbalancefees FLOAT,
            PRIMARY KEY(batchid , trainerid)
            FOREIGN KEY (batchid) REFERENCES Batches(batchid),
            FOREIGN KEY (trainerid) REFERENCES Trainers(trainerid)
        );

        CREATE TABLE IF NOT EXISTS Expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expensename VARCHAR(255),
            expense FLOAT,
            date DATE,
            paymentmethod VARCHAR(255)
        );

        CREATE TABLE IF NOT EXISTS Transactionhistory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description VARCHAR(255),
            cost FLOAT,
            date DATE,
            paymentstatus VARCHAR(255),
            paymentmethod VARCHAR(255),
            type VARCHAR(255)
                            
        );
""")
    conn.commit()

def insertvalues():
    
    conn = sqlite3.connect('direct_english.db')
    cursor = conn.cursor()

    cursor.executescript("""
    -- Insert into Trainers
    INSERT INTO Trainers (trainername, mobileno, email, address, experience, courses, dob, gender) VALUES 
    ('Alice Johnson', '9000000001', 'alice@example.com', 'New York', 5.0, 'Python, Java', '1985-06-15', 'Female'),
    ('Bob Smith', '9000000002', 'bob@example.com', 'Los Angeles', 8.0, 'Machine Learning, AI', '1980-09-22', 'Male'),
    ('Charlie Brown', '9000000003', 'charlie@example.com', 'Chicago', 6.0, 'C++, Cybersecurity', '1990-04-10', 'Male'),
    ('Diana White', '9000000004', 'diana@example.com', 'Houston', 4.0, 'Web Development', '1995-02-14', 'Female'),
    ('Ethan Davis', '9000000005', 'ethan@example.com', 'San Francisco', 10.0, 'NLP, AI Ethics', '1982-11-05', 'Male');

    -- Insert into Students
    INSERT INTO Students (studentname, mobileno, email, address, dob, gender, parentname) VALUES 
    ('Frank Green', '9000001001', 'frank@example.com', 'Boston', '2002-01-10', 'Male', 'Laura Green'),
    ('Grace Hall', '9000001002', 'grace@example.com', 'Seattle', '2003-05-22', 'Female', 'Robert Hall'),
    ('Harry Lee', '9000001003', 'harry@example.com', 'Denver', '2001-08-15', 'Male', 'Susan Lee'),
    ('Ivy King', '9000001004', 'ivy@example.com', 'Austin', '2000-12-01', 'Female', 'Michael King'),
    ('Jack White', '9000001005', 'jack@example.com', 'Miami', '1999-07-09', 'Male', 'Nancy White');

    -- Insert into Courses
    INSERT INTO Courses (coursename, courseprice, duration) VALUES 
    ('Python Basics', 300.0, 60),
    ('AI and ML', 700.0, 120),
    ('Cybersecurity', 450.0, 90),
    ('Web Development', 400.0, 80),
    ('Data Science', 600.0, 100);

    -- Insert into Batches
    INSERT INTO Batches (batchname, courseid, trainerid, studentid, startdate, enddate, batchtiming, classroom, coursefees, paidfees, balancefees) VALUES 
    ('Python Morning', 1, 1, 1, '2025-03-01', '2025-05-30', '10:00 AM - 12:00 PM', '101', 300.0, 150.0, 150.0),
    ('AI Advanced', 2, 2, 2, '2025-03-19', '2025-06-10', '2:00 PM - 4:00 PM', '102', 700.0, 350.0, 350.0),
    ('Cybersecurity 101', 3, 3, 3, '2025-02-01', '2025-07-01', '6:00 PM - 8:00 PM', '103', 450.0, 450.0, 0),
    ('Web Dev Bootcamp', 4, 4, 4, '2025-02-10', '2025-07-20', '9:00 AM - 11:00 AM', '104', 400.0, 200.0, 200.0),
    ('Data Science Masterclass', 5, 5, 5, '2025-05-01', '2025-08-10', '3:00 PM - 5:00 PM', '105', 600.0, 300.0, 300.0);

    -- Insert into Trainerpayments
    INSERT INTO Trainerpayments (batchid, trainerid, trainerfees, trainerpaidfees, trainerbalancefees) VALUES 
    (1, 1, 500.0, 250.0, 250.0),
    (2, 2, 700.0, 600.0, 100),
    (3, 3, 450.0, 225.0, 225.0),
    (4, 4, 400.0, 200.0, 200.0),
    (5, 5, 600.0, 300.0, 300.0);

    -- Insert into Expenses
    INSERT INTO Expenses (expensename, expense, date, paymentmethod) VALUES 
    ('Electricity Bill', 150.0, '2025-03-01', 'Credit Card'),
    ('Stationery', 50.0, '2025-03-02', 'Cash'),
    ('Internet Bill', 80.0, '2025-03-03', 'UPI'),
    ('Furniture Repair', 120.0, '2025-02-04', 'Cheque'),
    ('Marketing Ads', 200.0, '2025-02-05', 'Online Transfer');

    -- Insert into Transaction History
    INSERT INTO Transactionhistory (description, cost, date, paymentstatus, paymentmethod, type) VALUES 
    ('Course Fee Payment', 150.0, '2025-03-10', 'Paid', 'Credit Card', 'Income'),
    ('Trainer Salary', 500.0, '2025-03-15', 'Paid', 'Bank Transfer', 'Expense'),
    ('Library Purchase', 80.0, '2025-03-20', 'Pending', 'UPI', 'Expense'),
    ('New Course Development', 600.0, '2025-03-25', 'Paid', 'Cheque', 'Investment'),
    ('Maintenance Work', 200.0, '2025-03-30', 'Pending', 'Cash', 'Expense');
    """)

    conn.commit()
    conn.close()
    print("Sample data inserted successfully!")

# INSERTING ####################################################################

def addTrainers(trainername, mobileno, email, address, experience, courses, dob, gender):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    query = """INSERT INTO Trainers (trainername, mobileno, email, address, experience, courses, dob, gender) 
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

    cursor.execute(query, (trainername, mobileno, email, address, experience, courses, dob, gender))
    conn.commit()
    print("Trainer added successfully!")

def addStudents(studentname,mobileno,email,address,dob,gender,parentname):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    query = """ INSERT INTO Students (studentname, mobileno, email, address, dob, gender, parentname)
                VALUES (?, ?, ?, ?, ?, ?, ?)"""

    cursor.execute(query,(studentname,mobileno,email,address,dob,gender,parentname))
    conn.commit()
    print("Student added Successfully! ")

def addCourses(coursename,courseprice,duration):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    query = """ INSERT INTO Courses (coursename, courseprice, duration)
                VALUES (?, ?, ?)"""

    cursor.execute(query,(coursename,courseprice,duration))
    conn.commit()
    print("Course added Successfully! ")

def addBatches(batchid,batchname,startdate,courseid,trainerid,studentid,enddate,batchtiming,classroom,coursefees,paidfees,balancefees):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()


    query = """ INSERT INTO BATCHES (batchid, batchname,courseid, trainerid, studentid, startdate, enddate, batchtiming, classroom, coursefees, paidfees, balancefees )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    cursor.execute(query,(batchid, batchname, courseid, trainerid, studentid, startdate, enddate, batchtiming, classroom, coursefees, paidfees, balancefees ))
    conn.commit()
    print("Batches added Successfully! ")

def addTrainerpayments(batchid,trainerid,trainerfees,trainerpaidfees,trainerbalancefees):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    query = """ INSERT INTO Trainerpayments (batchid, trainerid, trainerfees, trainerpaidfees, trainerbalancefees )
                VALUES (?, ?, ?)"""

    cursor.execute(query,(batchid, trainerid, trainerfees, trainerpaidfees, trainerbalancefees ))
    conn.commit()
    print("Trainer Payments added Successfully! ")

def addExpenses(expensename,expense,paymentmethod):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    query = """INSERT INTO Expenses (expensename, expense,date,paymentmethod)
                VALUES (?, ?,DATE('now'), ?)"""
    
    cursor.execute(query,(expensename,expense,paymentmethod))
    conn.commit()
    print("Expenses added Successfully! ")

    query = """INSERT INTO Transactionhistory(description,cost,date,paymentstatus,paymentmethod,type)
                VALUES(?,?,DATE('now'),?,?,?)"""
    
    cursor.execute(query,(expensename,expense,'COMPLETE',paymentmethod,'Expense'))
    conn.commit()
    print("Expense Added to Transaction History !")

def addTransactionhistory(description,cost,paymentstatus,paymentmethod,type):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()
    

    query = """ INSERT INTO Transactionhistory (description, cost,date, paymentstatus, paymentmethod, type)
                VALUES (?, ?, DATE('now'), ?, ?, ?)"""
    
    cursor.execute(query,(description,cost,paymentstatus,paymentmethod,type))
    conn.commit()
    print("Transactionhistory added Successfully! ")

###################################################################################################


# UPDATING ##########################################################################################


def updateTrainers(id,newtrainername,newmobileno,newemail,newaddress,newexperience,newcourses,newdob,newgender):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"""
        UPDATE Trainers 
        SET trainername = '{newtrainername}', 
            mobileno = '{newmobileno}', 
            email = '{newemail}', 
            address = '{newaddress}', 
            experience = {newexperience}, 
            courses = '{newcourses}', 
            dob = '{newdob}', 
            gender = '{newgender}' 
        WHERE trainerid = {id}
    """)
    conn.commit()
    print("Trainer Updated Successfully")


def updateStudents(id,newstudentname,newmobileno,newemail,newaddress,newdob,newgender,newparentname):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"""
        UPDATE Students 
        SET studentname = '{newstudentname}', 
            mobileno = '{newmobileno}', 
            email = '{newemail}', 
            address = '{newaddress}', 
            dob = '{newdob}', 
            gender = '{newgender}', 
            parentname = '{newparentname}' 
        WHERE studentid = {id}
    """)

    conn.commit()
    print("Student Updated Successfully")


def updateCourses(id,newcoursename,newcourseprice,newduration):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"""
        UPDATE Courses 
        SET coursename = '{newcoursename}', 
            courseprice = {newcourseprice}, 
            duration = {newduration} 
        WHERE courseid = {id}
    """)

    conn.commit()
    print("Course Updated Successfully")


def updateBatches(id,newbatchname,newcourseid,newtrainerid,newstudentid,newstartdate,newenddate,newbatchtiming,newclassroom,newcoursefees,newpaidfees,newbalancefees):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"""
        UPDATE Batches 
        SET batchname = '{newbatchname}', 
            courseid = {newcourseid}, 
            trainerid = {newtrainerid}, 
            studentid = {newstudentid}, 
            startdate = '{newstartdate}', 
            enddate = '{newenddate}', 
            batchtiming = '{newbatchtiming}', 
            classroom = '{newclassroom}', 
            coursefees = {newcoursefees}, 
            paidfees = {newpaidfees}, 
            balancefees = {newbalancefees} 
        WHERE batchid = {id}
    """)

    conn.commit()
    print("Batch Updated Successfully")


def updateTrainerPayments(batchid,trainerid,newtrainerfees,newtrainerpaidfees,newtrainerbalancefees):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"""
        UPDATE Trainerpayments 
        SET trainerfees = {newtrainerfees}, 
            trainerpaidfees = {newtrainerpaidfees}, 
            trainerbalancefees = {newtrainerbalancefees} 
        WHERE batchid = {batchid} AND trainerid = {trainerid}
    """)

    conn.commit()
    print("Trainer Payment Updated Successfully")


def updateExpenses(id,newexpensename,newexpense,newpaymentmethod):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"""
        UPDATE Expenses 
        SET expensename = '{newexpensename}', 
            expense = {newexpense}, 
            paymentmethod = '{newpaymentmethod}' 
        WHERE id = {id}
    """)

    conn.commit()
    print("Expense Updated Successfully")


def updateTransactionHistory(id,newdescription,newcost,newpaymentstatus,newpaymentmethod,newtype):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"""
        UPDATE Transactionhistory 
        SET description = '{newdescription}', 
            cost = {newcost}, 
            paymentstatus = '{newpaymentstatus}', 
            paymentmethod = '{newpaymentmethod}', 
            type = '{newtype}' 
        WHERE id = {id}
    """)

    conn.commit()
    print("Transaction History Updated Successfully")

#######################################################################################################

# REMOVING ############################################################################################

def removeTrainer(id):

    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM Trainers WHERE trainerid = {id}")
    conn.commit()
    print(f"Trainer with ID {id} removed successfully.")

def removeStudent(id):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM Students WHERE studentid = {id}")
    conn.commit()
    print(f"Student with ID {id} removed successfully.")

def removeCourse(id):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()
    
    cursor.execute(f"DELETE FROM Courses WHERE courseid = {id}")
    conn.commit()
    print(f"Course with ID {id} removed successfully.")

def removeBatch(id):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM Batches WHERE batchid = {id}")
    conn.commit(id)
    print(f"Batch with ID {id} removed successfully.")

def removeTrainerpayment(batchid,trainerid):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM Trainerpayments WHERE batchid = {batchid} AND trainerid = {trainerid}")
    conn.commit()
    print(f"Trainer Payment for Batch ID {batchid} and Trainer ID {trainerid} removed successfully.")

def removeExpense(id):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()
    
    cursor.execute(f"DELETE FROM Expenses WHERE id = {id}")
    conn.commit()
    print(f"Expense with ID {id} removed successfully.")

def removeTransactionhistory(id):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()
    
    cursor.execute(f"DELETE FROM Transactionhistory WHERE id = {id}")
    conn.commit()
    print(f"Transaction with ID {id} removed successfully.")


################################################################################################################################


# VIEW VALUES ###################################################################################################################

def getTrainer(input):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"""
                    SELECT * FROM Trainers WHERE trainerid = {input} OR mobileno = {input}
                    """)

    result=cursor.fetchone()
    return result

def getStudent(input):
    
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"""
                    SELECT * FROM Students WHERE studentid = {input} OR mobileno = {input}
                    """)

    result=cursor.fetchone()
    return result

def getBatches(input):
    
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
                    SELECT * FROM Batches WHERE batchid = ? OR batchname = ?
                   """,(input,input))

    result=cursor.fetchall()
    return result

def getCourses(input):
    
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"""
                    SELECT * FROM Courses WHERE courseid = ? OR coursename = ? 
                    """,(input,input))

    result=cursor.fetchall()
    return result


def getTrainerpayments(id):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM Trainerpayments WHERE trainerid = {id}")
    result = cursor.fetchone()
    return result

 
def getExpenses(id):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM Expenses WHERE id = {id}")
    result = cursor.fetchone()
    return result
    

def getTransactionhistory(id):
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM Transactionhistory WHERE id = {id}")
    result = cursor.fetchone()
    return result


def updatestudentpayment(studentid, batchid, courseid, amount, paymentmethod):
    conn = sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Batches
        SET balancefees = balancefees - ?, 
            paidfees = paidfees + ?
        WHERE studentid = ? AND courseid = ? AND batchid = ?
    """, (amount, amount, studentid, courseid, batchid))

    conn.commit()

    cursor.execute("""
        SELECT balancefees FROM Batches 
        WHERE studentid = ? AND courseid = ? AND batchid = ?
    """, (studentid, courseid, batchid))

    result = cursor.fetchone()  
    
    balance = result[0] if result else 0  

    paymentstatus = "COMPLETE" if balance <= 0 else "PENDING"

    cursor.execute("""
        INSERT INTO Transactionhistory (description, cost, date, paymentstatus, paymentmethod, type)
        VALUES (?, ?, DATE('now'), ?, ?, 'Income')
    """, ('Student Payment', amount, paymentstatus, paymentmethod))

    conn.commit()
    conn.close()


def updatetrainerpaymnent(batchid,trainerid,amount,paymentmethod):
    
    conn = sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Trainerpayments
        SET trainerbalancefees = trainerbalancefees - ?, 
            trainerpaidfees = trainerpaidfees + ?
        WHERE trainerid = ?  AND batchid = ?
    """, (amount, amount, trainerid, batchid))

    conn.commit()

    cursor.execute("""
        SELECT trainerbalancefees FROM trainerpayments 
        WHERE trainerid = ? AND batchid = ?
    """, (trainerid, batchid))

    result = cursor.fetchone()  
    
    balance = result[0] if result else 0  

    paymentstatus = "COMPLETE" if balance <= 0 else "PENDING"

    cursor.execute("""
        INSERT INTO Transactionhistory (description, cost, date, paymentstatus, paymentmethod, type)
        VALUES (?, ?, DATE('now'), ?, ?, 'Expense')
    """, ('Trainer Payment', amount, paymentstatus, paymentmethod))

    conn.commit()
    conn.close()

def gettrainerrecord():

    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    cursor.execute("""
                    SELECT trainerid , trainername ,courses , mobileno FROM Trainers
                    """)
    
    result= cursor.fetchall()
    return result

def getstudentrecord():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    cursor.execute("""
                    SELECT S.studentid,S.studentname,C.coursename,S.mobileno 
                   FROM Students S 
                   LEFT JOIN Batches B ON S.studentid = B.studentid
                   LEFT JOIN Courses C ON B.courseid = C.courseid
                    """)
    
    result = cursor.fetchall()
    return result

def geteveryExpenses():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    cursor.execute("""
                    SELECT * From Expenses
                    """)
    
    result = cursor.fetchall()
    return result

###########################################################################################################








############################################################################################################


def showtable():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()
    table = input("Enter the Table you want to Show : ") ###### SAME LIKE DELETE #######
    cursor.execute (f" SELECT * FROM {table}")
    conn.commit()
    print(cursor.fetchall())
    print(f"{table} Retrieved Successfully")

def deleteallvalues():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()
    
    cursor.executescript("""
                    
                    DELETE FROM Trainerpayments;
                    DELETE FROM Batches ;
                    DELETE FROM Expenses;
                    DELETE FROM Transactionhistory;
                    DELETE FROM Trainers ;
                    DELETE FROM Students ;
                    DELETE FROM Courses ;

                    """) 
    conn.commit()
    print(cursor.fetchall())
    print(f" All Tables Records Deleted Successfully")

#CHECKING FUNCTION  
def check():
    cursor.execute("pragma table_info(Trainers)")
    print(cursor.fetchall())


#############################################################################################################


## QUERIES ####################################################################################################



def closeconnect():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()
    conn.close()

def get_ongoing_courses():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT courseid)
        FROM Batches
        WHERE DATE('now') BETWEEN startdate AND enddate 
    """)
    result = cursor.fetchone()[0]
    return result

def trainersavailable():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
                    SELECT COUNT(DISTINCT trainerid) FROM Trainers
                   """)
    result = cursor.fetchone()[0]
    return result

def studentsjoinedtoday():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
                    SELECT COUNT(DISTINCT studentid) FROM BATCHES WHERE startdate=DATE('now')                   
                   """)
    
    result = cursor.fetchone()[0]
    return result

def thismonthrevenue():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute(""" 
                     SELECT SUM(paidfees) FROM Batches
                    WHERE strftime('%m-%Y', startdate) = strftime('%m-%Y', DATE('now'))
                    """)
    
    result = cursor.fetchone()[0]
    return result

def thismonthexpense():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
                    SELECT SUM(cost) FROM Transactionhistory 
                   WHERE strftime('%m-%Y',date) = strftime('%m-%Y',DATE('now')) AND type = 'Expense'
                    """)
    
    result=cursor.fetchone()[0]
    return result

def getstudentpaymentreminder():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
                    SELECT B.batchid , B.studentid , S.studentname , C.coursename, B.coursefees, B.paidfees, B.balancefees ,s.mobileno
                   FROM Batches B
                   INNER JOIN Students S ON B.studentid = S.studentid
                   INNER JOIN Courses C ON B.courseid = C.courseid 
                   WHERE B.balancefees > 0
                    """)
    
    result=cursor.fetchall()
    return result

def gettrainerpaymentreminder():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT T.batchid , T.trainerid , Tr.trainername , C.coursename, T.trainerfees, T.trainerpaidfees, T.trainerbalancefees , Tr.mobileno
                   FROM Trainerpayments T
                   INNER JOIN Trainers Tr ON T.trainerid = Tr.trainerid
                   INNER JOIN Batches B ON T.batchid = B.batchid
                   INNER JOIN Courses C ON B.courseid = C.courseid
                   WHERE T.trainerbalancefees > 0 
                    """)
    result=cursor.fetchall()
    return result
    
def getallTrainers():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
                    SELECT * FROM Trainers 
                    """)

    result=cursor.fetchall()
    return result

def studentpayment(id):

    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    cursor.execute(f"""
                    SELECT B.batchid , B.courseid , C.coursename, B.coursefees, B.paidfees, B.balancefees
                   FROM Batches B 
                   INNER JOIN Courses C ON B.courseid = C.courseid WHERE B.studentid = {id} AND B.balancefees > 0
                    """)
    
    result = cursor.fetchall()
    return result

def trainerpayment(id):

    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    cursor.execute(f""" 
                    SELECT T.batchid , B.courseid , C.coursename , T.trainerfees, T.trainerpaidfees , T.trainerbalancefees
                   FROM Trainerpayments T
                   INNER JOIN Batches B ON T.batchid = B.batchid
                   INNER JOIN Courses C ON B.courseid = C.courseid
                   WHERE T.trainerid = {id} AND T.trainerbalancefees > 0

                    """)
    
    result=cursor.fetchall()
    return result

def getallpayments():

    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    cursor.execute("""
                    SELECT * FROM Transactionhistory 
                    """)
    
    result=cursor.fetchall()
    return result

def getallincome():

    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    cursor.execute("""
                    SELECT * FROM Transactionhistory WHERE LOWER(type) = 'income'
                    """)
    
    result=cursor.fetchall()
    return result

def getallexpense():

    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    cursor.execute("""
                    SELECT * FROM Transactionhistory WHERE LOWER(type) = 'expense'
                    """)
    
    result=cursor.fetchall()
    return result

def getallpending():

    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    cursor.execute("""
                    SELECT * FROM Transactionhistory WHERE LOWER(paymentstatus) = 'pending'
                    """)
    
    result=cursor.fetchall()
    return result

def checktrainermobile(mobileno):
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    cursor.execute(f"""
                    SELECT * FROM Trainers WHERE mobileno = {mobileno}
                    """)
    
    result = cursor.fetchone()
    return result

def checktraineremail(email):
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    cursor.execute(" SELECT * FROM Trainers WHERE email = ?",(email,))
    
    result =cursor.fetchone()
    return result

def checkstudentmobile(mobile):
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    cursor.execute(f"""
                    SELECT * FROM Students WHERE mobileno = {mobile}
                    """)
    
    result =cursor.fetchone()
    return result

def checkstudentemail(email):
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM Students WHERE email= ? ",(email,))
    
    result =cursor.fetchone()
    return result

def getallStudents():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
                    SELECT * FROM Students 
                    """)

    result=cursor.fetchall()
    return result

def getallCourses():
    conn=sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
                    SELECT * FROM Courses
                    """)

    result=cursor.fetchall()

    return result



###########################################################################################################################




# GENERATE REPORT ###########################################################################################################


def totalstudentsjoinedthismonth():

    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()
    cursor.execute("""
                    SELECT IFNULL(COUNT(DISTINCT studentid),0)
                    FROM Batches
                    WHERE strftime('%Y-%m',startdate) = strftime('%Y-%m', DATE('now'))
                    """)
    result = cursor.fetchone()[0]
    conn.close()
    return result

def totaltrainersaddedthismonth():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()
    cursor.execute("""
        SELECT IFNULL(COUNT(DISTINCT Trainerid), 0)
        FROM Batches
        WHERE strftime('%Y-%m', startdate) = strftime('%Y-%m', DATE('now'))
                    """)
    result = cursor.fetchone()[0]
    conn.close()
    return result

def getnewbatchesstartedthismonth():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()
    cursor.execute("""
        SELECT COUNT(*) 
        FROM Batches 
        WHERE strftime('%Y-%m', startdate) = strftime('%Y-%m', DATE('now'))
    """)
    result = cursor.fetchone()[0]
    conn.close()
    return result

def gettotalrevenuethismonth():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()
    cursor.execute("""
                   SELECT IFNULL(SUM(paidfees), 0) FROM Batches WHERE strftime('%Y-%m', startdate) = strftime('%Y-%m',DATE('now'))
                   """)
    result = cursor.fetchone()[0]
    conn.close()
    return result

def gettotalexpensesthismonth():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()
    cursor.execute("""SELECT IFNULL(SUM(expense), 0) FROM Expenses WHERE strftime('%Y-%m', date) = strftime('%Y-%m',DATE('now'))
                   """)
    result = cursor.fetchone()[0]
    conn.close()
    """trainerfees= gettotaltrainerpaidfeesthismonth()
    final = result+trainerfees"""
    return result
    
def getstudentbalancefees():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()
    cursor.execute("""
                   SELECT IFNULL(SUM(balancefees), 0) FROM Batches
                   """)
    result = cursor.fetchone()[0]
    conn.close()
    return result

def getbalancetrainerfees():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()
    cursor.execute("""SELECT IFNULL(SUM(trainerbalancefees), 0) FROM Trainerpayments
                   """)
    result = cursor.fetchone()[0]
    conn.close()
    return result

def gettotaltransactionsforthismonth():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()
    cursor.execute("""
        SELECT COUNT(id)
        FROM Transactionhistory
        WHERE strftime('%Y-%m', date) = strftime('%Y-%m',DATE('now'))
        ORDER BY date ASC
    """)
    result = cursor.fetchone()[0]
    conn.close()
    return result

def gettotalstudentpaidfeesthismonth():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()
    cursor.execute("""
                    SELECT SUM(paidfees) FROM Batches
                    WHERE strftime('%Y-%m',startdate) = strftime('%Y-%m',DATE('now'))
                   """)
    result = cursor.fetchone()[0]
    return result

def gettotaltrainerpaidfeesthismonth():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()
    cursor.execute("""
                    SELECT SUM(T.trainerpaidfees) FROM Trainerpayments T
                   INNER JOIN Batches B 
                   ON T.batchid = B.batchid WHERE strftime('%Y-%m',B.startdate) = strftime('%Y-%m',DATE('now'))
                   """)
    result = cursor.fetchone()[0]
    return result

def gettotalamountspentthismonth():

    result1= gettotalexpensesthismonth() + gettotaltrainerpaidfeesthismonth()
    return result1

def gettotalnetprofitthismonth():

    revenue = gettotalrevenuethismonth()
    expense= gettotalamountspentthismonth()

    netprofit= (revenue - expense)
    return netprofit

def gettotalnetprofitpercentthismonth():

    revenue = gettotalrevenuethismonth()
    expense= gettotalamountspentthismonth()

    if revenue == 0:
        return 0  

    net_profit_percent = ((revenue - expense) / revenue) * 100  
    return net_profit_percent

def getmostpopularcoursethismonth():
    conn = sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT C.coursename, COUNT(B.batchid) AS batch_count 
        FROM Batches B
        INNER JOIN Courses C ON B.courseid = C.courseid 
        WHERE strftime('%Y-%m', B.startdate) = strftime('%Y-%m', DATE('now'))
        GROUP BY B.courseid 
        ORDER BY batch_count DESC 
        LIMIT 1;
    """)

    result = cursor.fetchone()
    conn.close()

    return result if result else ("No data", 0)

def gettrainerwithmostbatchesthismonth():
    conn = sqlite3.connect("direct_english.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT T.trainername, COUNT(B.batchid) AS batch_count
        FROM Batches B
        INNER JOIN Trainers T ON B.trainerid = T.trainerid WHERE strftime('%Y-%m', B.startdate) = strftime('%Y-%m', DATE('now'))
        GROUP BY B.trainerid
        ORDER BY batch_count DESC
        LIMIT 1;
    """)

    result = cursor.fetchone()
    conn.close()

    return result if result else ("No data", 0)


###################################################################################################################################

def gettotalrevenuelastmonth():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()
    cursor.execute("""
                   SELECT IFNULL(SUM(paidfees), 0) FROM Batches WHERE strftime('%Y-%m', startdate) = strftime('%Y-%m',DATE('now', 'start of month', '-1 day', 'start of month'))
                   """)
    result = cursor.fetchone()[0]
    conn.close()
    return result

def gettotalexpenseslastmonth():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()
    cursor.execute("""SELECT IFNULL(SUM(expense), 0) FROM Expenses WHERE strftime('%Y-%m', date) = strftime('%Y-%m',DATE('now', 'start of month', '-1 day', 'start of month'))
                   """)
    result = cursor.fetchone()[0]
    conn.close()
    """trainerfees= gettotaltrainerpaidfeesthismonth()
    final = result+trainerfees"""
    return result

def gettotaltrainerpaidfeeslastmonth():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()
    cursor.execute("""
                    SELECT IFNULL(SUM(T.trainerpaidfees),0) FROM Trainerpayments T
                   INNER JOIN Batches B 
                   ON T.batchid = B.batchid WHERE strftime('%Y-%m',B.startdate) = strftime('%Y-%m',DATE('now', 'start of month', '-1 day', 'start of month'))
                   """)
    
    result = cursor.fetchone()[0]
    return result

def gettotalamountspentlastmonth():

    result1= gettotalexpenseslastmonth() + gettotaltrainerpaidfeeslastmonth()
    return result1

def getpreviousmonthnetprofit():

    revenue = gettotalrevenuelastmonth()
    expense= gettotalamountspentlastmonth()

    netprofit= (revenue - expense)
    return netprofit

def getcompareprofithwithpreviousmonth():
    conn=sqlite3.connect("direct_english.db")
    cursor=conn.cursor()

    thismonth = gettotalnetprofitthismonth()
    lastmonth = getpreviousmonthnetprofit()

    compare =  thismonth - lastmonth

    return compare

"""
    print("Total Revenue Last month :",gettotalrevenuelastmonth())
    print("Total Expense Last Month :",gettotalexpenseslastmonth())
    print("Total Trainer Paid Fees Last Month :",gettotaltrainerpaidfeeslastmonth())
    print("Total Previous Month Profit",getpreviousmonthnetprofit())
    print("Total Amount Spent Last Month ",gettotalamountspentlastmonth()
"""



#MAIN MENU ##################################################################################################################


def main_menu():
    while True:
        print("\n===== DATABASE MANAGEMENT MENU =====")
        print("0. Insert")
        print("1. Trainers")
        print("2. Students")
        print("3. Courses")
        print("4. Batches")
        print("5. Expenses")
        print("6. Trainer Payments")
        print("7. Transaction History")
        print("8. Show Table Data")
        print("9. Delete Table Data")
        print("10.Create")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice =='0':
            insertvalues()
        elif choice == '1':
            trainer_menu()
        elif choice == '2':
            student_menu()
        elif choice == '3':
            course_menu()
        elif choice == '4':
            batch_menu()
        elif choice == '5':
            expense_menu()
        elif choice == '6':
            trainer_payment_menu()
        elif choice == '7':
            transaction_menu()
        elif choice == '8':
            showtable()
        elif choice == '9':
            deleteallvalues()
        elif choice =='10':
            connect_db()
        elif choice == '11':
            print("Exiting... Goodbye!")
            """conn.close()"""
            break
        else:
            print("Invalid choice! Please select a valid option.")



###########################################################################################################################


# SUB MENU ######################################################################################################################


def trainer_menu():
    while True:
        print("\n===== TRAINER MENU =====")
        print("1. Add Trainer")
        print("2. Update Trainer")
        print("3. Remove Trainer")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
                trainername = input("Enter Trainer Name: ")
                mobileno = input("Enter Mobile No: ")
                email = input("Enter Email: ")
                address = input("Enter Address: ")
                experience = float(input("Enter Experience : ")) 
                courses = input("Enter Courses: ")
                dob = input("Enter Date of Birth : ")
                gender = input("Enter Gender : ")
                addTrainers(trainername,mobileno,email,address,experience,courses,dob,gender)
        elif choice == '2':
                id = input("Enter the id : ")
                newtrainername = input("Enter the Updated Trainer name : ")
                newmobileno = input("Enter the Updated mobileno : ")
                newemail = input("Enter the Updated email : ")
                newaddress = input("Enter the Updated address : ")
                newexperience = input("Enter the Updated experience : ")
                newcourses = input("Enter the Updated course name : ")
                newdob = input("Enter the Updated DOB in  : ")
                newgender = input("Enter the Updated Gender : ")

                updateTrainers(id,newtrainername,newmobileno,newemail,newaddress,newexperience,newcourses,newdob,newgender)
        elif choice == '3':
            id = input("Enter the Trainer ID to remove: ")
            removeTrainer(id)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please select a valid option.")

def student_menu():
    while True:
        print("\n===== STUDENT MENU =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Remove Student")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
                studentname = input("Enter Student Name : ")
                mobileno = input("Enter Mobile Number : ")
                email = input("Enter Email address : ")
                address = input("Enter the Address  : ")
                dob = input ("Enter the Date of Birth : ")
                gender = input("Enter ther Gender : ")
                parentname = input ("Enter the Parent Name : " )
                addStudents(studentname,mobileno,email,address,dob,gender,parentname)
        elif choice == '2':

            id = input("Enter the id : ")
            newstudentname = input("Enter the Updated Student name : ")
            newmobileno = input("Enter the Updated mobileno : ")
            newemail = input("Enter the Updated email : ")
            newaddress = input("Enter the Updated address : ")
            newdob = input("Enter the Updated DOB in YYYY-MM-DD : ")
            newgender = input("Enter the Updated Gender : ")
            newparentname = input("Enter the Updated Parent Name : ")
            updateStudents(id,newstudentname,newmobileno,newemail,newaddress,newdob,newgender,newparentname)
            
        elif choice == '3':
            id = input("Enter the Student ID to remove: ")
            removeStudent(id)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please select a valid option.")

def course_menu():
    while True:
        print("\n===== COURSE MENU =====")
        print("1. Add Course")
        print("2. Update Course")
        print("3. Remove Course")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
                coursename = input("Enter Course Name : ")
                courseprice = input("Enter Course Price : ")
                duration = input("Enter Course Duration : ")
                addCourses(coursename,courseprice,duration)
        elif choice == '2':
            
            id = input("Enter the id : ")
            newcoursename = input("Enter the Updated Course Name : ")
            newcourseprice = input("Enter the Updated Course Price : ")
            newduration = input("Enter the Updated Duration : ")
            updateCourses(id,newcoursename,newcourseprice,newduration)
        elif choice == '3':
            id = input("Enter the Course ID to remove: ")
            removeCourse(id)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please select a valid option.")

def batch_menu():
    while True:
        print("\n===== BATCH MENU =====")
        print("1. Add Batch")
        print("2. Update Batch")
        print("3. Remove Batch")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
                batchid = input("Enter Batch Id : ")
                batchname = input("Enter Batch Name : ")
                startdate = input("Enter the Start Date in YYYY-MM-DD : ")
                courseid= input("Enter the Course Id : ")
                trainerid= input("Enter the Trainer Id : ")
                studentid= input("Enter the Student Id :")
                enddate = input("Enter the End Date in DD-MM-YYYY  : ")
                batchtiming = input ("Enter the Timings of the Batch : ")
                classroom = input("Enter ther Classroom Name : ")
                coursefees= input("Enter the Course Fees : ")
                paidfees= input("Enter the Paid Fees : ")
                balancefees=input("Enter the Balance Fees : ")
                addBatches(batchid,batchname,startdate,courseid,trainerid,studentid,enddate,batchtiming,classroom,coursefees,paidfees,balancefees)
        elif choice == '2':
            id = input("Enter the id : ")
            newbatchname = input("Enter the Updated Batch Name : ")
            newcourseid = input("Enter the Updated Course ID : ")
            newtrainerid = input("Enter the Updated Trainer ID : ")
            newstudentid = input("Enter the Updated Student ID : ")
            newstartdate = input("Enter the Updated Start Date (YYYY-MM-DD) : ")
            newenddate = input("Enter the Updated End Date (YYYY-MM-DD) : ")
            newbatchtiming = input("Enter the Updated Batch Timing : ")
            newclassroom = input("Enter the Updated Classroom : ")
            newcoursefees = input("Enter the Updated Course Fees : ")
            newpaidfees = input("Enter the Updated Paid Fees : ")
            newbalancefees = input("Enter the Updated Balance Fees : ")
            updateBatches(id,newbatchname,newcourseid,newtrainerid,newstudentid,newstartdate,newenddate,newbatchtiming,newclassroom,newcoursefees,newpaidfees,newbalancefees)

        elif choice == '3':
            id = input("Enter the Batch ID to remove: ")
            removeBatch(id)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please select a valid option.")

def expense_menu():
    while True:
        print("\n===== EXPENSE MENU =====")
        print("1. Add Expense")
        print("2. Update Expense")
        print("3. Remove Expense")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
                expensename= input("Enter the Expense Name : ")
                expense= float(input("Enter the Expense Amount : "))

                paymentmethod = input("Enter the Mode of Payment : ")
                addExpenses(expensename,expense,paymentmethod)
        elif choice == '2':
                id = input("Enter the id : ")
                newexpensename = input("Enter the Updated Expense Name : ")
                newexpense = input("Enter the Updated Expense Amount : ")
                newpaymentmethod = input("Enter the Updated Payment Method : ")
                updateExpenses(id,newexpensename,newexpense,newpaymentmethod)
        elif choice == '3':
            id = input("Enter the Expense ID to remove: ")
            removeExpense(id)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please select a valid option.")

def trainer_payment_menu():
    while True:
        print("\n===== TRAINER PAYMENT MENU =====")
        print("1. Add Trainer Payment")
        print("2. Update Trainer Payment")
        print("3. Remove Trainer Payment")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
                batchid = input("Enter the Batch Id :")
                trainerid = input("Enter the Trainer Id : ")
                trainerfees = float(input("Enter Trainer Fees : "))
                trainerpaidfees = float(input("Enter Batch Name : "))
                trainerbalancefees = float(input("Enter the Start Date in DD-MM-YYYY : "))
                addTrainerpayments(batchid,trainerid,trainerfees,trainerpaidfees,trainerbalancefees)
        elif choice == '2':
                
                batchid = input("Enter the Batch ID : ")
                trainerid = input("Enter the Trainer ID : ")
                newtrainerfees = input("Enter the Updated Trainer Fees : ")
                newtrainerpaidfees = input("Enter the Updated Trainer Paid Fees : ")
                newtrainerbalancefees = input("Enter the Updated Trainer Balance Fees : ")
                updateTrainerPayments(batchid,trainerid,newtrainerfees,newtrainerpaidfees,newtrainerbalancefees)

        elif choice == '3':
                batchid = input("Enter the Batch ID: ")
                trainerid = input("Enter the Trainer ID: ")
                removeTrainerpayment(batchid,trainerid)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please select a valid option.")

def transaction_menu():
    while True:
        print("\n===== TRANSACTION MENU =====")
        print("1. Add Transaction")
        print("2. Update Transaction")
        print("3. Remove Transaction")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
                description=input("Enter the Description : ")
                cost = float(input("Enter the Cost : "))
                paymentstatus=input("Enter the Payment Status : ")
                paymentmethod=input("Enter the Mode of Payment : ")
                type = input("Enter the Type of Pay (Payors/Payee) : ")
                addTransactionhistory(description,cost,paymentstatus,paymentmethod,type)
        elif choice == '2':
            id = input("Enter the id : ")
            newdescription = input("Enter the Updated Description : ")
            newcost = input("Enter the Updated Cost : ")
            newpaymentstatus = input("Enter the Updated Payment Status : ")
            newpaymentmethod = input("Enter the Updated Payment Method : ")
            newtype = input("Enter the Updated Type : ")
            updateTransactionHistory(id,newdescription,newcost,newpaymentstatus,newpaymentmethod,newtype)
        elif choice == '3':
            id = input("Enter the Transaction ID to remove: ")
            removeTransactionhistory(id)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Run the Menu
if __name__ == "__main__":

    main_menu()

    """
    print(getTrainer(1))
    print(getStudent(1))
    print(getCourses(1))
    print(getTransactionhistory(1))
    print(getExpenses(1))
    print(getTrainerpayments(1))
    print(get_ongoing_courses())
    print(trainersavailable())
    print(studentsjoinedtoday())
    print(thismonthrevenue())
    print(thismonthexpense())
    print(getstudentpaymentreminder())
    print(gettrainerpaymentreminder())
    print(studentpayment(1))
    print(trainerpayment(1))
    print(updatestudentpayment(1,1,1,150,"Gpay"))
    print(updatestudentpayment(2,2,2,150,"Card"))
    print(updatetrainerpaymnent(1,1,250,"Cash"))
    print(gettrainerrecord())
    print(getstudentrecord())
    print(getallpayments())
    print(getallincome())
    print(getallexpense())
    print(getallpending())
    print(checktrainermobile(9000000001))
    print(checktraineremail('bob@example.com'))
    print(checkstudentmobile(9000001001))
    print(checkstudentemail('grace@example.com'))
    print(getTrainer(9000000001))
    print(getStudent(9000001002))
    print(getTrainer(5))
    print(getStudent(4))
    print(getBatches(2))
    print(getCourses(1))
    print(getBatches("AI Advanced"))
    print(getCourses("Data Science"))
    print(geteveryExpenses())"
    """

    print("Total Students :",totalstudentsjoinedthismonth())
    print("Total Trainers :",totaltrainersaddedthismonth())
    print("Total Batches :",getnewbatchesstartedthismonth())
    print("Total Revenue :",gettotalrevenuethismonth())   
    print("Total Expense :",gettotalexpensesthismonth())
    print("Total Student Paid :",gettotalstudentpaidfeesthismonth())
    print("Total Trainer Paid :",gettotaltrainerpaidfeesthismonth())
    print("Total Student Balance :",getstudentbalancefees())
    print("Total Trainer Balance :",getbalancetrainerfees())
    print("Total Transaction :",gettotaltransactionsforthismonth())
    print("Total Amount Spent:",gettotalamountspentthismonth())
    print("Total Profit :",gettotalnetprofitthismonth())
    print("Total Profit Percent:", gettotalnetprofitpercentthismonth())
    print("Compare Profit :",getcompareprofithwithpreviousmonth())
    print("Most Popular Course :",getmostpopularcoursethismonth())
    print("Most Famous Teachers :",gettrainerwithmostbatchesthismonth())

    

