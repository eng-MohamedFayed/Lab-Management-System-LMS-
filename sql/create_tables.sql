--------------DROPPING--------------
/*

DROP USER FAYED404;
DROP USER SALAH404;
DROP USER EID404;
DROP USER SOBHI404;
DROP USER ADLY404;

DROP ROLE ADMIN;
DROP ROLE STAFF;
DROP ROLE DOCTOR;
DROP ROLE STUDENT;


DECLARE
    CURSOR all_tables IS SELECT table_name FROM user_tables;
BEGIN
    FOR table_rec IN all_tables LOOP
        EXECUTE IMMEDIATE 'DROP TABLE ' || table_rec.table_name || ' CASCADE CONSTRAINTS';
    END LOOP;
END;

DECLARE
  sequence_name VARCHAR2(100);
BEGIN
  FOR sequence_rec IN (SELECT sequence_name FROM user_sequences) LOOP
    sequence_name := sequence_rec.sequence_name;
    EXECUTE IMMEDIATE 'DROP SEQUENCE ' || sequence_name;
  END LOOP;
END;
/

*/

CREATE SEQUENCE sequence_name
  MINVALUE 1
  NOMAXVALUE
  START WITH 1
  INCREMENT BY 1;

CREATE SEQUENCE onepiece_user_id_seq
  MINVALUE 1
  NOMAXVALUE
  START WITH 1
  INCREMENT BY 1;

CREATE SEQUENCE rsrv_id_seq
  MINVALUE 1
  NOMAXVALUE
  START WITH 1
  INCREMENT BY 1;

CREATE SEQUENCE lab_report_id_seq
  MINVALUE 1
  NOMAXVALUE
  START WITH 1
  INCREMENT BY 1;

CREATE SEQUENCE std_report_id_seq
  MINVALUE 1
  NOMAXVALUE
  START WITH 1
  INCREMENT BY 1;

CREATE SEQUENCE Maint_Seq
  MINVALUE 1
  NOMAXVALUE
  START WITH 1
  INCREMENT BY 1;

CREATE SEQUENCE course_id_seq
  MINVALUE 101
  NOMAXVALUE
  START WITH 101
  INCREMENT BY 1;

CREATE SEQUENCE category_id_seq
  MINVALUE 1
  NOMAXVALUE
  START WITH 1
  INCREMENT BY 1;

CREATE SEQUENCE room_id_seq
  MINVALUE 1
  NOMAXVALUE
  START WITH 1
  INCREMENT BY 1;

CREATE SEQUENCE labtype_id_seq
  MINVALUE 1
  NOMAXVALUE
  START WITH 1
  INCREMENT BY 1;

CREATE SEQUENCE lab_id_seq
  MINVALUE 1
  NOMAXVALUE
  START WITH 1
  INCREMENT BY 1;

CREATE SEQUENCE equip_id_seq
  MINVALUE 1
  NOMAXVALUE
  START WITH 1
  INCREMENT BY 1;

CREATE SEQUENCE dept_id_seq
  MINVALUE 1
  NOMAXVALUE
  START WITH 1
  INCREMENT BY 1;



CREATE TABLE PG_STD (
    PG_Std_id NUMBER PRIMARY KEY,
    PG_Fname VARCHAR2(50) NOT NULL,
    PG_Lname VARCHAR2(50) NOT NULL,
    Dept_id NUMBER NOT NULL,
    Advisor_id NUMBER NOT NULL,
    user_id number
);

CREATE TABLE UG_STD (
    UG_Std_id NUMBER PRIMARY KEY,
    UG_Fname VARCHAR2(50) NOT NULL,
    UG_Lname VARCHAR2(50) NOT NULL,
    Dept_id NUMBER NOT NULL,
    user_id number
);

CREATE TABLE DOCTORS (
    Dr_id NUMBER PRIMARY KEY,
    Dr_Fname VARCHAR2(50),
    Dr_Lname VARCHAR2(50) NOT NULL,
    Dept_id NUMBER,
    Hire_date DATE,
    user_id number
);

CREATE TABLE LAB_STAFF (
    Staff_id NUMBER PRIMARY KEY,
    Staff_Fname VARCHAR2(50),
    Staff_Lname VARCHAR2(50) NOT NULL,
    Hire_date DATE,
    user_id number
);

CREATE TABLE Admins (
    Admin_id NUMBER PRIMARY KEY,
    Admin_Fname VARCHAR2(50),
    Admin_Lname VARCHAR2(50) NOT NULL,
    Hire_date DATE,
    user_id number
);

CREATE TABLE ONEPIECE (
    User_id NUMBER PRIMARY KEY,
    User_type VARCHAR2(50) NOT NULL,
    Username VARCHAR2(50) NOT NULL,
    Password VARCHAR2(50) NOT NULL
);

CREATE TABLE EQUIPMENT (
    Equip_id NUMBER PRIMARY KEY,
    Equip_name VARCHAR2(100) NOT NULL,
    Model VARCHAR2(100),
    Lab_id NUMBER NOT NULL,
    Category_id NUMBER NOT NULL
);

CREATE TABLE EquipCategories (
    Category_id NUMBER PRIMARY KEY,
    Category_name VARCHAR2(100) NOT NULL
);

  CREATE TABLE Departments (
      Dept_id NUMBER PRIMARY KEY,
      Dept_name VARCHAR2(100) NOT NULL,
      Manager_id NUMBER NOT NULL
  );

CREATE TABLE Courses (
    Course_id NUMBER PRIMARY KEY,
    Name VARCHAR2(100) NOT NULL,
    Credits NUMBER NOT NULL,
    Dept_id NUMBER NOT NULL,
    Manager_id NUMBER NOT NULL
);

CREATE TABLE SLOTS (
    Slot_id NUMBER PRIMARY KEY,
    Start_TIME NUMBER NOT NULL,
    End_TIME NUMBER NOT NULL
);

CREATE TABLE Reservations (
    Rsrv_id NUMBER PRIMARY KEY,
    Rsrv_date DATE NOT NULL,
    Status NUMBER(2) NOT NULL,
    Slot_id NUMBER NOT NULL,
    User_id NUMBER NOT NULL,
    Equip_id NUMBER NOT NULL,
    Course_id NUMBER
);

CREATE TABLE ROOMS (
    Room_id NUMBER PRIMARY KEY,
    Capacity NUMBER NOT NULL,
    Room_name VARCHAR2(100),
    Building_no NUMBER NOT NULL
);

CREATE TABLE LABS (
    Lab_id NUMBER PRIMARY KEY,
    LabType_id NUMBER NOT NULL,
    Room_id NUMBER NOT NULL
);

CREATE TABLE LABTYPES (
    LabType_id NUMBER PRIMARY KEY,
    Type VARCHAR2(100) NOT NULL,
    Staff_id NUMBER
);

CREATE TABLE Maintenances (
    Maint_id NUMBER PRIMARY KEY,
    Note VARCHAR2(200),
    Submission_date DATE NOT NULL,
    Staff_id NUMBER NOT NULL,
    Equip_id NUMBER NOT NULL
);

CREATE TABLE Maintenance_History (
    Maint_id NUMBER,
    Maint_date DATE NOT NULL,
    Notes VARCHAR2(500),
    CONSTRAINT PK_Maintenance_History PRIMARY KEY (Maint_id, Maint_date)
);


CREATE TABLE Experiments (
    Rsrv_id NUMBER,
    Lab_id NUMBER NOT NULL,
    Title VARCHAR2(200) NOT NULL,
    Notes VARCHAR2(500)
);

CREATE TABLE STD_REPORTS (
    STD_Report_id NUMBER PRIMARY KEY,
    Course_id NUMBER,
    User_id NUMBER NOT NULL,
    Report_date DATE NOT NULL,
    Author_ID NUMBER NOT NULL,
    Grade VARCHAR2(10) NOT NULL,
    Std_report_desc VARCHAR2(500)
);

CREATE TABLE LAB_REPORTS (
    LAB_Report_id NUMBER PRIMARY KEY,
    LAB_id NUMBER NOT NULL,
    Lab_report_date DATE NOT NULL,
    Author_ID NUMBER NOT NULL,
    Lab_report_desc VARCHAR2(500) NOT NULL
);

CREATE ROLE ADMIN;
GRANT DBA TO ADMIN;
GRANT SELECT ANY TABLE TO ADMIN;
GRANT INSERT ANY TABLE TO ADMIN;
GRANT UPDATE ANY TABLE TO ADMIN;
GRANT DELETE ANY TABLE TO ADMIN;


CREATE ROLE STAFF;
GRANT CONNECT TO STAFF;
GRANT SELECT ON maint_Seq TO STAFF;
GRANT SELECT ON LAB_REPORTS TO STAFF;
GRANT SELECT ON STD_REPORTS TO STAFF;
GRANT SELECT ON EQUIPMENT TO STAFF;
GRANT SELECT ON EXPERIMENTS TO STAFF;
GRANT SELECT ON LABS TO STAFF;
GRANT SELECT ON LABTYPES TO STAFF;
GRANT SELECT ON ROOMS TO STAFF;
GRANT SELECT ON COURSES TO STAFF;
GRANT SELECT ON DOCTORS TO STAFF;
GRANT SELECT ON UG_STD TO STAFF;
GRANT SELECT ON PG_STD TO STAFF;
GRANT SELECT ON LAB_STAFF TO STAFF;
GRANT SELECT ON SLOTS TO STAFF;
GRANT SELECT ON RESERVATIONS TO STAFF;
GRANT SELECT ON MAINTENANCES TO STAFF;
GRANT SELECT ON ONEPIECE TO STAFF;
GRANT SELECT ON LAB_REPORT_ID_SEQ TO STAFF;
GRANT INSERT ON LAB_REPORTS TO STAFF;
GRANT INSERT ON MAINTENANCES TO STAFF;
GRANT UPDATE ON RESERVATIONS TO STAFF;


CREATE ROLE DOCTOR;
GRANT CONNECT TO DOCTOR;
GRANT SELECT ON STD_REPORT_ID_SEQ TO DOCTOR;
GRANT SELECT ON rsrv_id_seq TO DOCTOR;
GRANT SELECT ON RESERVATIONS TO DOCTOR;
GRANT SELECT ON EQUIPMENT TO DOCTOR;
GRANT SELECT ON COURSES TO DOCTOR;
GRANT SELECT ON SLOTS TO DOCTOR;
GRANT SELECT ON STD_REPORTS TO DOCTOR;
GRANT SELECT ON DOCTORS TO DOCTOR;
GRANT SELECT ON UG_STD TO DOCTOR;
GRANT SELECT ON PG_STD TO DOCTOR;
GRANT SELECT ON LABS TO DOCTOR;
GRANT SELECT ON ROOMS TO DOCTOR;
GRANT SELECT ON ONEPIECE TO DOCTOR;
GRANT INSERT ON RESERVATIONS TO DOCTOR;
GRANT INSERT ON STD_REPORTS TO DOCTOR;
GRANT DELETE ON RESERVATIONS TO DOCTOR;
GRANT DELETE ON EXPERIMENTS TO DOCTOR;

CREATE ROLE STUDENT;
GRANT CONNECT TO STUDENT;
GRANT SELECT ON rsrv_id_seq TO STUDENT;
GRANT SELECT ON RESERVATIONS TO STUDENT;
GRANT SELECT ON EQUIPMENT TO STUDENT;
GRANT SELECT ON COURSES TO STUDENT;
GRANT SELECT ON SLOTS TO STUDENT;
GRANT SELECT ON STD_REPORTS TO STUDENT;
GRANT SELECT ON DOCTORS TO STUDENT;
GRANT SELECT ON UG_STD TO STUDENT;
GRANT SELECT ON PG_STD TO STUDENT;
GRANT SELECT ON LABS TO STUDENT;
GRANT SELECT ON ROOMS TO STUDENT;
GRANT SELECT ON ONEPIECE TO STUDENT;
GRANT INSERT ON RESERVATIONS TO STUDENT;
GRANT DELETE ON RESERVATIONS TO STUDENT;
GRANT DELETE ON EXPERIMENTS TO STUDENT;

insert into Departments (Dept_id, Dept_name, Manager_id) values (dept_id_seq.nextval, 'FOE', 406);
insert into Departments (Dept_id, Dept_name, Manager_id) values (dept_id_seq.nextval, 'FIBH', 404);
insert into Departments (Dept_id, Dept_name, Manager_id) values (dept_id_seq.nextval, 'CSIT', 401);
insert into Departments (Dept_id, Dept_name, Manager_id) values (dept_id_seq.nextval, 'PharmaD', 405);

insert INTO EquipCategories (Category_id, Category_name) VALUES (category_id_seq.nextval, 'Optical Instruments');
insert INTO EquipCategories (Category_id, Category_name) VALUES (category_id_seq.nextval, 'Lab Tools');
insert INTO EquipCategories (Category_id, Category_name) VALUES (category_id_seq.nextval, 'Analytical Instruments');
insert INTO EquipCategories (Category_id, Category_name) VALUES (category_id_seq.nextval, 'Laboratory Centrifuges');

insert INTO Courses (Course_id, Name, Credits, Dept_id, Manager_id) VALUES (course_id_seq.nextval, 'Chemistry 101', 3, 1, 401);
insert INTO Courses (Course_id, Name, Credits, Dept_id, Manager_id) VALUES (course_id_seq.nextval, 'Physics 201', 4, 2, 402);
insert INTO Courses (Course_id, Name, Credits, Dept_id, Manager_id) VALUES (course_id_seq.nextval, 'Biology Lab Techniques', 3, 3, 403);
insert INTO Courses (Course_id, Name, Credits, Dept_id, Manager_id) VALUES (course_id_seq.nextval, 'Microbiology 301', 4, 4, 404);

insert INTO EQUIPMENT (Equip_id, Equip_name, Model, Lab_id, Category_id) VALUES (equip_id_seq.nextval, 'Microscope', 'Model XYZ', 1, 1);
insert INTO EQUIPMENT (Equip_id, Equip_name, Model, Lab_id, Category_id) VALUES (equip_id_seq.nextval, 'Bunsen Burner', 'Model ABC', 2, 2);
insert INTO EQUIPMENT (Equip_id, Equip_name, Model, Lab_id, Category_id) VALUES (equip_id_seq.nextval, 'Spectrophotometer', 'Model DEF', 3, 3);
insert INTO EQUIPMENT (Equip_id, Equip_name, Model, Lab_id, Category_id) VALUES (equip_id_seq.nextval, 'Centrifuge', 'Model GHI', 1, 4);


insert INTO LABS (Lab_id, LabType_id, Room_id) VALUES (lab_id_seq.nextval, 1, 1);
insert INTO LABS (Lab_id, LabType_id, Room_id) VALUES (lab_id_seq.nextval, 2, 2);
insert INTO LABS (Lab_id, LabType_id, Room_id) VALUES (lab_id_seq.nextval, 3, 3);
insert INTO LABS (Lab_id, LabType_id, Room_id) VALUES (lab_id_seq.nextval, 1, 4);


insert INTO Maintenances (Maint_id, Note, Submission_date, Staff_id, Equip_id) VALUES (maint_Seq.nextval, 'Routine maintenance', SYSDATE, 1001, 1);
insert INTO Maintenances (Maint_id, Note, Submission_date, Staff_id, Equip_id) VALUES (maint_Seq.nextval, 'Calibration check', SYSDATE, 1002, 2);
insert INTO Maintenances (Maint_id, Note, Submission_date, Staff_id, Equip_id) VALUES (maint_Seq.nextval, 'Repair work', SYSDATE, 1003, 3);
insert INTO Maintenances (Maint_id, Note, Submission_date, Staff_id, Equip_id) VALUES (maint_Seq.nextval, 'Service checkup', SYSDATE, 1004, 4);


insert INTO Reservations (Rsrv_id, Rsrv_date, Status, Slot_id, User_id, Equip_id, Course_id) VALUES (rsrv_id_seq.nextval, SYSDATE, 0, 1, 1, 1, 101);
insert INTO Reservations (Rsrv_id, Rsrv_date, Status, Slot_id, User_id, Equip_id, Course_id) VALUES (rsrv_id_seq.nextval, SYSDATE, 0, 2, 2, 2, 102);
insert INTO Reservations (Rsrv_id, Rsrv_date, Status, Slot_id, User_id, Equip_id, Course_id) VALUES (rsrv_id_seq.nextval, SYSDATE, 0, 3, 3, 3, 103);
insert INTO Reservations (Rsrv_id, Rsrv_date, Status, Slot_id, User_id, Equip_id, Course_id) VALUES (rsrv_id_seq.nextval, SYSDATE, 0, 4, 3, 4, 104);




insert into pg_std (PG_Std_id,PG_Lname,PG_Fname, Dept_id, Advisor_id) values (21001, 'Salah', 'Zeyad', 3 , 401);
insert into pg_std (PG_Std_id,PG_Lname,PG_Fname, Dept_id, Advisor_id) values (21002, 'Ramadan', 'Mohamed', 2 , 404);
insert into pg_std (PG_Std_id,PG_Lname,PG_Fname, Dept_id, Advisor_id) values (21003, 'Youssef', 'Abdelrahman', 3 , 403);
insert into pg_std (PG_Std_id,PG_Lname,PG_Fname, Dept_id, Advisor_id) values (21004, 'Elaswad', 'Saif', 4 , 405);
insert into pg_std (PG_Std_id,PG_Lname,PG_Fname, Dept_id, Advisor_id) values (21005, 'Elhaddad', 'Nada', 1 , 406);
insert into pg_std (PG_Std_id,PG_Lname,PG_Fname, Dept_id, Advisor_id) values (21006, 'Gamal', 'Ibrahim', 1 , 402);

insert into ug_std (UG_Std_id,UG_lname,UG_fname, Dept_id) values (320210034, 'Fayed', 'Mohamed', 3);
insert into ug_std (UG_Std_id,UG_lname,UG_fname, Dept_id) values (320210009, 'Elgammal', 'Ibrahim', 3);
insert into ug_std (UG_Std_id,UG_lname,UG_fname, Dept_id) values (320210021, 'Abdelfattah', 'Hassan', 3);
insert into ug_std (UG_Std_id,UG_lname,UG_fname, Dept_id) values (320210035, 'Morad', 'Eman', 3);
insert into ug_std (UG_Std_id,UG_lname,UG_fname, Dept_id) values (120210034, 'elbromba', 'sab3', 1);
insert into ug_std (UG_Std_id,UG_lname,UG_fname, Dept_id) values (420210034, 'Alonso', 'Marcos', 4);
insert into ug_std (UG_Std_id,UG_lname,UG_fname, Dept_id) values (220210034, 'Messi', 'Lionel', 2);

insert into Doctors (Dr_id,Dr_Lname,Dr_Fname) values (401, 'Eid', 'Walid');
insert into Doctors (Dr_id,Dr_Lname,Dr_Fname) values (402, 'Gomaa', 'Amal');
insert into Doctors (Dr_id,Dr_Lname,Dr_Fname) values (403, 'Zaky', 'Ahmed');
insert into Doctors (Dr_id,Dr_Lname,Dr_Fname) values (404, 'Abdraboh', 'Salah');
insert into Doctors (Dr_id,Dr_Lname,Dr_Fname) values (405, 'Hussien', 'Omar');
insert into Doctors (Dr_id,Dr_Lname,Dr_Fname) values (406, 'Waleed', 'Ahmed');




insert into LAB_STAFF (Staff_id, Staff_lname, Staff_fname) values (1001, 'Sobhi', 'Mohamed');
insert into LAB_STAFF (Staff_id, Staff_lname, Staff_fname) values (1002, 'Behery', 'Khaled');
insert into LAB_STAFF (Staff_id, Staff_lname, Staff_fname) values (1003, 'Hazem', 'Abdelrahman');
insert into LAB_STAFF (Staff_id, Staff_lname, Staff_fname) values (1004, 'Khaled', 'Abdo');
insert into LAB_STAFF (Staff_id, Staff_lname, Staff_fname) values (1005, 'Reda', 'Youssef');

insert into Admins (Admin_id, Admin_Lname, Admin_Fname) values (100001, 'Adly', 'Amr');

insert into ONEPIECE (User_id, User_type, Username, Password) values (onepiece_user_id_seq.nextval, 'A', 'LMS','123');

insert into ONEPIECE (User_id, User_type, Username, Password) values (onepiece_user_id_seq.nextval, 'UG', 'FAYED404','123');

CREATE USER FAYED404 IDENTIFIED BY 123;
GRANT STUDENT TO FAYED404;

UPDATE UG_STD
SET User_ID = onepiece_user_id_seq.currval
WHERE UG_STD_ID= 320210034;

insert into ONEPIECE (User_id, User_type, Username, Password) values (onepiece_user_id_seq.nextval, 'PG', 'SALAH404','123');

CREATE USER SALAH404 IDENTIFIED BY 123;
GRANT STUDENT TO SALAH404;


UPDATE PG_STD
SET User_ID = onepiece_user_id_seq.currval
WHERE PG_STD_ID= 21001;

insert into ONEPIECE (User_id, User_type, Username, Password) values (onepiece_user_id_seq.nextval, 'DR', 'EID404','123');

CREATE USER EID404 IDENTIFIED BY 123;
GRANT DOCTOR TO EID404;


UPDATE Doctors
SET User_ID = onepiece_user_id_seq.currval
WHERE DR_ID= 401;

insert into ONEPIECE (User_id, User_type, Username, Password) values (onepiece_user_id_seq.nextval, 'ST', 'SOBHI404','123');


CREATE USER SOBHI404 IDENTIFIED BY 123;
GRANT STAFF TO SOBHI404;


UPDATE Doctors
SET User_ID = onepiece_user_id_seq.currval
WHERE DR_ID= 401;


UPDATE Lab_Staff
SET User_ID = onepiece_user_id_seq.currval
WHERE STAFF_ID= 1001;

insert into ONEPIECE (User_id, User_type, Username, Password) values (onepiece_user_id_seq.nextval, 'A', 'ADLY404','123');

CREATE USER ADLY404 IDENTIFIED BY 123;
GRANT ADMIN TO ADLY404;


UPDATE Admins
SET User_ID = onepiece_user_id_seq.currval
WHERE ADMIN_ID= 100001;


UPDATE DOCTORS
SET DEPT_ID = 3
WHERE DR_ID = 401 ;

UPDATE DOCTORS
SET DEPT_ID = 1
WHERE DR_ID = 402 ;

UPDATE DOCTORS
SET DEPT_ID = 3
WHERE DR_ID = 403 ;

UPDATE DOCTORS
SET DEPT_ID = 2
WHERE DR_ID = 404 ;

UPDATE DOCTORS
SET DEPT_ID = 4
WHERE DR_ID = 405 ;

UPDATE DOCTORS
SET DEPT_ID = 1
WHERE DR_ID = 406 ;




insert INTO SLOTS (Slot_id, Start_TIME, End_TIME) VALUES (1, 8, 9);
insert INTO SLOTS (Slot_id, Start_TIME, End_TIME) VALUES (2, 9, 10);
insert INTO SLOTS (Slot_id, Start_TIME, End_TIME) VALUES (3, 10, 11);
insert INTO SLOTS (Slot_id, Start_TIME, End_TIME) VALUES (4, 11, 12);
insert INTO SLOTS (Slot_id, Start_TIME, End_TIME) VALUES (5, 12, 13);
insert INTO SLOTS (Slot_id, Start_TIME, End_TIME) VALUES (6, 13, 14);
insert INTO SLOTS (Slot_id, Start_TIME, End_TIME) VALUES (7, 14, 15);
insert INTO SLOTS (Slot_id, Start_TIME, End_TIME) VALUES (8, 15, 16);


insert INTO ROOMS (Room_id, Capacity, Room_name, Building_no) VALUES (room_id_seq.nextval, 30, 'Lab A', 1);
insert INTO ROOMS (Room_id, Capacity, Room_name, Building_no) VALUES (room_id_seq.nextval, 25, 'Lab B', 2);
insert INTO ROOMS (Room_id, Capacity, Room_name, Building_no) VALUES (room_id_seq.nextval, 35, 'Lab C', 3);
insert INTO ROOMS (Room_id, Capacity, Room_name, Building_no) VALUES (room_id_seq.nextval, 40, 'Lab D', 1);


insert INTO LABTYPES (LabType_id, Type, Staff_id) VALUES (labtype_id_seq.nextval, 'Chemistry Lab', 1001);
insert INTO LABTYPES (LabType_id, Type, Staff_id) VALUES (labtype_id_seq.nextval, 'Physics Lab', 1002);
insert INTO LABTYPES (LabType_id, Type, Staff_id) VALUES (labtype_id_seq.nextval, 'Biology Lab', 1003);
insert INTO LABTYPES (LabType_id, Type, Staff_id) VALUES (labtype_id_seq.nextval, 'Chemistry Lab', 1004);


insert INTO Experiments (Rsrv_id, lab_id, Title, Notes) VALUES (1, 1, 'Chemical Reaction Kinetics', 'Observing reaction rates under different conditions');
insert INTO Experiments (Rsrv_id, lab_id, Title, Notes) VALUES (2, 2, 'Optical Spectroscopy', 'Analyzing light absorption in various compounds');
insert INTO Experiments (Rsrv_id, lab_id, Title, Notes) VALUES (3, 3, 'Microbiology Culture Growth', 'Studying bacterial growth patterns');
insert INTO Experiments (Rsrv_id, lab_id, Title, Notes) VALUES (4, 2, 'Centrifugation Efficiency', 'Measuring centrifuge separation performance');


insert INTO Maintenance_History (Maint_id, Maint_date, Notes) VALUES (1, SYSDATE, 'Cleaned lenses, checked electrical connections');
insert INTO Maintenance_History (Maint_id, Maint_date, Notes) VALUES (2, SYSDATE, 'Verified gas supply and burner functionality');
insert INTO Maintenance_History (Maint_id, Maint_date, Notes) VALUES (3, SYSDATE, 'Replaced damaged components');
insert INTO Maintenance_History (Maint_id, Maint_date, Notes) VALUES (4, SYSDATE, 'Checked motor and rotor integrity');

insert INTO STD_REPORTS (STD_Report_id, Course_id, User_id, Report_date, Author_ID, Grade, Std_report_desc) VALUES (std_report_id_seq.nextval, 101, 1, SYSDATE, 401, 'A', 'Excellent understanding of course material');
insert INTO STD_REPORTS (STD_Report_id, Course_id, User_id, Report_date, Author_ID, Grade, Std_report_desc) VALUES (std_report_id_seq.nextval, 102, 2, SYSDATE, 402, 'B+', 'Good grasp but needs improvement');
insert INTO STD_REPORTS (STD_Report_id, Course_id, User_id, Report_date, Author_ID, Grade, Std_report_desc) VALUES (std_report_id_seq.nextval, 103, 1, SYSDATE, 403, 'A-', 'Strong analytical skills demonstrated');
insert INTO STD_REPORTS (STD_Report_id, Course_id, User_id, Report_date, Author_ID, Grade, Std_report_desc) VALUES (std_report_id_seq.nextval, 104, 2, SYSDATE, 404, 'B', 'Satisfactory performance shown');


insert INTO LAB_REPORTS (LAB_Report_id, LAB_id, Lab_report_date, Author_ID, Lab_report_desc) VALUES (lab_report_id_seq.nextval, 1, SYSDATE, 1001, 'Successful experiment, no issues encountered');
insert INTO LAB_REPORTS (LAB_Report_id, LAB_id, Lab_report_date, Author_ID, Lab_report_desc) VALUES (lab_report_id_seq.nextval, 2, SYSDATE, 1002, 'Minor equipment malfunction, resolved swiftly');
insert INTO LAB_REPORTS (LAB_Report_id, LAB_id, Lab_report_date, Author_ID, Lab_report_desc) VALUES (lab_report_id_seq.nextval, 3, SYSDATE, 1003, 'Unexpected results, further investigation needed');
insert INTO LAB_REPORTS (LAB_Report_id, LAB_id, Lab_report_date, Author_ID, Lab_report_desc) VALUES (lab_report_id_seq.nextval, 4, SYSDATE, 1004, 'Experiment executed smoothly, no abnormalities');



ALTER TABLE PG_STD ADD CONSTRAINT fk_onepiece_pg_std FOREIGN KEY (user_id) REFERENCES Onepiece(user_id);

ALTER TABLE UG_STD ADD CONSTRAINT fk_onepiece_ug_std FOREIGN KEY (user_id) REFERENCES Onepiece(user_id);

ALTER TABLE doctors ADD CONSTRAINT fk_onepiece_doctor FOREIGN KEY (user_id) REFERENCES Onepiece(user_id);

ALTER TABLE EQUIPMENT ADD CONSTRAINT fk_category_equipment FOREIGN KEY (Category_id) REFERENCES EquipCategories(Category_id);

ALTER TABLE Courses ADD CONSTRAINT fk_dept_courses FOREIGN KEY (Dept_id) REFERENCES Departments(Dept_id);

ALTER TABLE Admins ADD CONSTRAINT fk_onepiece_admin FOREIGN KEY (user_id) REFERENCES Onepiece(user_id);

ALTER TABLE lab_staff ADD CONSTRAINT fk_onepiece_lab_staff FOREIGN KEY (user_id) REFERENCES Onepiece(user_id);

ALTER TABLE PG_STD ADD CONSTRAINT fk_dept_pg_std FOREIGN KEY (Dept_id) REFERENCES Departments(Dept_id);

ALTER TABLE PG_STD ADD CONSTRAINT fk_advisor_pg_std FOREIGN KEY (Advisor_id) REFERENCES DOCTORS(Dr_id);

ALTER TABLE UG_STD ADD CONSTRAINT fk_dept_ug_std FOREIGN KEY (Dept_id) REFERENCES Departments(Dept_id);

ALTER TABLE DOCTORS ADD CONSTRAINT fk_dept_doctors FOREIGN KEY (Dept_id) REFERENCES Departments(Dept_id);

ALTER TABLE Departments ADD CONSTRAINT fk_manager_dept FOREIGN KEY (Manager_id) REFERENCES DOCTORS(Dr_id);

ALTER TABLE EQUIPMENT ADD CONSTRAINT fk_lab_equipment FOREIGN KEY (Lab_id) REFERENCES LABS(Lab_id);

ALTER TABLE Courses ADD CONSTRAINT fk_manager_courses FOREIGN KEY (Manager_id) REFERENCES DOCTORS(Dr_id);

ALTER TABLE Reservations ADD CONSTRAINT fk_slot_reservations FOREIGN KEY (Slot_id) REFERENCES SLOTS(Slot_id);

ALTER TABLE Reservations ADD CONSTRAINT fk_user_reservations FOREIGN KEY (User_id) REFERENCES ONEPIECE(User_id);

ALTER TABLE Reservations ADD CONSTRAINT fk_equip_reservations FOREIGN KEY (Equip_id) REFERENCES EQUIPMENT(Equip_id);

ALTER TABLE Reservations ADD CONSTRAINT fk_course_reservations FOREIGN KEY (Course_id) REFERENCES Courses(Course_id);

ALTER TABLE LABS ADD CONSTRAINT fk_room_labs FOREIGN KEY (Room_id) REFERENCES ROOMS(Room_id);

ALTER TABLE LABS ADD CONSTRAINT fk_labtype_labs FOREIGN KEY (LabType_id) REFERENCES LABTYPES(LabType_id);

ALTER TABLE LABTYPES ADD CONSTRAINT fk_staff_labtypes FOREIGN KEY (Staff_id) REFERENCES LAB_STAFF(Staff_id);

ALTER TABLE Maintenances ADD CONSTRAINT fk_staff_maintenances FOREIGN KEY (Staff_id) REFERENCES LAB_STAFF(Staff_id);

ALTER TABLE Maintenances ADD CONSTRAINT fk_equip_maintenances FOREIGN KEY (Equip_id) REFERENCES EQUIPMENT(Equip_id);

ALTER TABLE Experiments ADD CONSTRAINT fk_experiment_reservations FOREIGN KEY (Rsrv_id) REFERENCES Reservations(Rsrv_id);

ALTER TABLE Experiments ADD CONSTRAINT fk_experiment_lab_id FOREIGN KEY (lab_id) REFERENCES LABS(lab_id);

ALTER TABLE STD_REPORTS ADD CONSTRAINT fk_course_std_reports FOREIGN KEY (Course_id) REFERENCES Courses(Course_id);

ALTER TABLE STD_REPORTS ADD CONSTRAINT fk_user_std_reports FOREIGN KEY (User_id) REFERENCES ONEPIECE(User_id);

ALTER TABLE STD_REPORTS ADD CONSTRAINT fk_author_std_reports FOREIGN KEY (Author_ID) REFERENCES Doctors(Dr_id);

ALTER TABLE LAB_REPORTS ADD CONSTRAINT fk_lab_lab_reports FOREIGN KEY (LAB_id) REFERENCES LABS(Lab_id);

ALTER TABLE LAB_REPORTS ADD CONSTRAINT fk_author_lab_reports FOREIGN KEY (Author_ID) REFERENCES Lab_Staff(Staff_id);