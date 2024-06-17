# MOST IMPORTANT FUNCTIONS:
#   1- admin { 4 display users / 5 insert user / 6 remove user } # SELECT INSERT DELETE
#   2- doctors/pg/ug { 2 submit lab reservation request / 3 manage reservations} # INSERT SELECT
#   3- staff {3 display_reservation_requests / 4 approve_deny_reservation_request} # SELECT UPDATE

import cx_Oracle

def connect_to_database(username, password):
    try:
        connection = cx_Oracle.connect(f"{username}/{password}@localhost:1521/xe")
        return connection
    except cx_Oracle.DatabaseError as e:
        print(f"Error connecting to the database: {e}")
        login_menu()
        return None

def login_menu():
    while True:
        print("Welcome to the LMS Login Menu")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Use LMS credentials for initial connection to check user credentials
        lms_connection = connect_to_database("LMS", "123")
        user_type, user_id = check_credentials(lms_connection, username, password)

        if user_type:
            print(f"User Exist! User Type: {types[user_type]}, User ID: {user_id}\n")
            lms_connection.close()  # Close the LMS connection

            # Establish a new connection using the entered user's credentials
            connection = connect_to_database(username, password)
            if user_type:
                return user_type, user_id, connection
            else:
                print("Invalid user credentials. Please try again.")
        else:
            print("Invalid LMS credentials. Please try again.")

def check_credentials(connection, username, password):
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT User_type, User_id FROM ONEPIECE WHERE Username = '{username}' AND Password = '{password}'")
        result = cursor.fetchone()
        cursor.close()

        if result:
            return result
        else:
            return None
    except cx_Oracle.DatabaseError as e:
        print(f"Error checking credentials: {e}")
        return None

def admin_menu(connection):
    while True:
        print("Admin Menu:")
        print("1: Display Labs Reports")
        print("2: Display Students Reports")
        print("3: Manage Maintenance Requests")
        print("4: Display Users")
        print("5: Insert New User")
        print("6: Remove User")
        print("-1: Logout\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_labs_reports(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '2':
            display_students_reports(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '3':
            manage_maintenance_requests(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '4':
            display_users(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '5':
            insert_new_user(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '6':
            remove_user(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '-1':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def staff_menu(connection):
    while True:
        print("Staff Menu:")
        print("1: Display Labs Reports")
        print("2: Make Lab Reports")
        print("3: Display Reservation Requests")
        print("4: Approve/Deny Reservation Request")
        print("5: Display Student Reports")
        print("6: Display Maintenance Requests")
        print("7: Submit Equipment Maintenance Request")
        print("-1: Logout\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_labs_reports(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '2':
            make_lab_reports(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '3':
            display_reservation_requests(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '4':
            approve_deny_reservation_request(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '5':
            display_students_reports(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '6':
            display_maintenance_requests(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '7':
            submit_equipment_maintenance_request(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '-1':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def doctor_menu(connection):
    while True:
        print("Doctor Menu:")
        print("1: Display All Labs")
        print("2: Request Reservation")
        print("3: Manage Reservation Requests")
        print("4: Display Students Reports")
        print("5: Make Student Reports")
        print("-1: Logout\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_all_labs(connection)
        elif choice == '2':
            submit_lab_reservation_request(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '3':
            user_manage_reservation_requests(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '4':
            display_students_reports(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '5':
            make_student_reports(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '-1':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def ug_menu(connection):
    while True:
        print("Undergraduate Student Menu:")
        print("1: Display All Labs")
        print("2: Request Reservation")
        print("3: Manage Reservation Requests")
        print("4: Display Student Reports")
        print("-1: Logout\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_all_labs(connection)
        elif choice == '2':
            submit_lab_reservation_request(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '3':
            user_manage_reservation_requests(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '4':
            std_display_student_reports(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '-1':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def pg_menu(connection):
    while True:
        print("Postgraduate Student Menu:")
        print("1: Display All Labs")
        print("2: Request Reservation")
        print("3: Manage Reservation Requests")
        print("4: Display Student Reports")
        print("-1: Logout\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_all_labs(connection)
        elif choice == '2':
            submit_lab_reservation_request(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '3':
            user_manage_reservation_requests(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '4':
            std_display_student_reports(connection)
            if input("To go back press 0\n") == 0:
                pass        
        elif choice == '-1':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def display_labs_reports(connection):
    inp = int(input("1: Choose Lab\n2: All Labs\n")) 
    if inp == 1:
        
        lab_id = input("Enter Lab ID\n")
        # select  from the lab reports table of that lab (lab_id)
        # equipment (lab_id)
        # Experiments (lab_id)
        # Labtypes (labtype_id) 
        # Rooms (room_id) 
        # GROUP BY
        try:
            cursor = connection.cursor()
            query = f"""
                    SELECT lr.LAB_ID, lr.LAB_REPORT_ID, lr.LAB_REPORT_DATE, st.STAFF_FNAME||' '||st.STAFF_LNAME, lr.LAB_REPORT_DESC, t.TYPE, r.ROOM_NAME
                    FROM
                    LMS.LAB_REPORTS lr,LMS.LABTYPES t, LMS.ROOMS r, LMS.LABS l, LMS.LAB_STAFF st
                    WHERE 
                    lr.LAB_ID = l.LAB_ID AND l.LABTYPE_ID = t.LABTYPE_ID AND l.ROOM_ID = r.ROOM_ID
                    AND lr.LAB_ID = {lab_id} AND lr.AUTHOR_ID = st.STAFF_ID
                    ORDER BY lr.LAB_ID, lr.LAB_REPORT_ID
            """
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                print("Lab Reports:")
                for result in results:
                    print(f"\n Lab ID: {result[0]}\nReport ID: {result[1]}\n  Report Date: {result[2]}\n Author: {result[3]}\n Describtion: {result[4]}\n Lab Type: {result[5]}\n Name: {result[6]}\n")
            else:
                print("No Lab Reports found.")
            cursor.close()
        except cx_Oracle.DatabaseError as e:
            print(f"Error Displaying Lab Reports: {e}")

    elif inp == 2:
        # select  from the lab reports table of all labs (lab_id)
        # equipment (lab_id)
        # Experiments (lab_id)
        # Labtypes (labtype_id) 
        # Rooms (room_id) 
        # GROUP BY
        try:
            cursor = connection.cursor()
            query = f"""
                    SELECT lr.LAB_ID, lr.LAB_REPORT_ID, lr.LAB_REPORT_DATE, st.STAFF_FNAME||' '||st.STAFF_LNAME, lr.LAB_REPORT_DESC, t.TYPE, r.ROOM_NAME
                    FROM
                    LMS.LAB_REPORTS lr,LMS.LABTYPES t, LMS.ROOMS r, LMS.LABS l, LMS.LAB_STAFF st
                    WHERE 
                    lr.LAB_ID = l.LAB_ID AND l.LABTYPE_ID = t.LABTYPE_ID AND l.ROOM_ID = r.ROOM_ID AND lr.AUTHOR_ID = st.STAFF_ID
                    ORDER BY lr.LAB_ID, lr.LAB_REPORT_ID ASC
            """
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                print("Lab Reports:")
                for result in results:
                    print(f"\n Lab ID: {result[0]}\nReport ID: {result[1]}\n  Report Date: {result[2]}\n Author: {result[3]}\n Describtion: {result[4]}\n Lab Type: {result[5]}\n Name: {result[6]}\n")
            else:
                print("No Lab Reports found.")
            cursor.close()
        except cx_Oracle.DatabaseError as e:
            print(f"Error Displaying Lab Reports: {e}")

    else:
        print("Invalid choice. Going back to main menu.")

def display_students_reports(connection):
    inp = int(input("1: Choose Student\n2: All Students\n"))
    if inp == 1:
        std_id = input("Enter Student ID\n") # USER_ID
        usr_type = input("Enter User Type \n(UG for Undergraduate student - PG for Postgraduate student- DR for Doctor - ST for Staff)\n")
        # select from the student reports table of that student
        # courses(course_id)
        # doctor(author_id)
        # ug/pg (user_id)
        try:
            cursor = connection.cursor()
            query = f"""
                    SELECT s.STD_REPORT_ID, s.REPORT_DATE, s.AUTHOR_ID, s.GRADE, s.STD_REPORT_DESC,
                    c.NAME, r.DR_FNAME ||' '|| r.DR_LNAME, g.{typefn[usr_type]} ||' '||g.{typeln[usr_type]}, g.USER_ID
                    FROM LMS.STD_REPORTS s, LMS.COURSES C, LMS.DOCTORS r, LMS.{types[usr_type]} g
                    WHERE s.USER_ID={std_id} AND s.COURSE_ID = c.COURSE_ID AND s.AUTHOR_ID = r.DR_ID AND s.USER_ID = g.USER_ID
                    ORDER BY g.USER_ID, s.STD_REPORT_ID ASC
            """
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                print("Students Reports:")
                for result in results:
                    print(f"\n Report ID: {result[0]}\n Report Date: {result[1]}\n Author: {result[2]}\n GRADE: {result[3]}\n Describtion: {result[4]}\n COURSE: {result[5]}\n DR. Name: {result[6]}\n STUDENT NAME: {result[7]}\n STUDENT_ID: {result[8]}\n")
            else:
                print("No Student Reports found.")
            cursor.close()
        except cx_Oracle.DatabaseError as e:
            print(f"Error Displaying Student Reports: {e}")

    elif inp == 2:
        # select  from the student reports table of all students
        # courses(course_id)
        # doctor(author_id)
        # ug/pg (user_id)
        usr_type = input("Enter User Type \n(UG for Undergraduate student - PG for Postgraduate student- DR for Doctor - ST for Staff)\n")
        try:
            cursor = connection.cursor()
            query = f"""
                    SELECT s.STD_REPORT_ID, s.REPORT_DATE, s.AUTHOR_ID, s.GRADE, s.STD_REPORT_DESC,
                    c.NAME, r.DR_FNAME ||' '|| r.DR_LNAME, g.{typefn[usr_type]} ||' '||g.{typeln[usr_type]}, g.USER_ID
                    FROM LMS.STD_REPORTS s, LMS.COURSES c, LMS.DOCTORS r, LMS.{types[usr_type]} g
                    WHERE s.COURSE_ID = c.COURSE_ID AND s.AUTHOR_ID = r.DR_ID AND s.USER_ID = g.USER_ID
                    ORDER BY g.USER_ID, s.STD_REPORT_ID ASC
            """
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                print("Students Reports:")
                for result in results:
                    print(f"\n Report ID: {result[0]}\n Report Date: {result[1]}\n Author: {result[2]}\n GRADE: {result[3]}\n Describtion: {result[4]}\n COURSE: {result[5]}\n DR. Name: {result[6]}\n STUDENT NAME: {result[7]}\n STUDENT_ID: {result[8]}\n")
            else:
                print("No Student Reports found.")
            cursor.close()

        except cx_Oracle.DatabaseError as e:
            print(f"Error Displaying Student Reports: {e}")
    else:
        print("Invalid choice. Going back to main menu.")

def display_maintenance_requests(connection):
    # select statement from the maintenances table
    # Equipment(Equip_id)
    # Staff(Staff_id)
    try:
        cursor = connection.cursor()
        query = f"""
                SELECT m.MAINT_ID, m.NOTE, m.SUBMISSION_DATE d,
                s.STAFF_FNAME||' '||s.STAFF_LNAME , e.EQUIP_ID, e.EQUIP_NAME,
                t.TYPE, r.ROOM_NAME, r.BUILDING_NO
                FROM LMS.MAINTENANCES m, LMS.LAB_STAFF s, LMS.EQUIPMENT e, LMS.LABS l, LMS.LABTYPES t, LMS.ROOMS r
                WHERE m.STAFF_ID = S.STAFF_ID AND m.EQUIP_ID = e.EQUIP_ID  AND l.LABTYPE_ID = t.LABTYPE_ID AND L.ROOM_ID = r.ROOM_ID AND e.LAB_ID = l.LAB_ID
                ORDER BY m.MAINT_ID ASC
        """
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            print("Maintenance Requests:")
            for result in results:
                print(f"\n MAINTENANCE ID: {result[0]}\n NOTE: {result[1]}\n DATE: {result[2]}\n REQUESTER: {result[3]}\n EQUIPMENT: {result[4]}\n LAB TYPE: {result[5]}\n ROOM: {result[6]}\n BUILDING: {result[7]}\n ")
        else:
            print("No maintenance requests found.")

        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print(f"Error displaying maintenance requests: {e}")

def manage_maintenance_requests(connection):
    inp = int(input("1: Display Maintenance requests\n2: Manage Maintenance Requests\n"))
    if inp == 1:
        display_maintenance_requests(connection)
    elif inp == 2:
        inpp=int(input("1: COMPLETE\n2: DELETE\n"))
        maint_id = int(input("Enter Maintenance ID \n"))
        if inpp == 1:
            notes = input("NOTES: \n")
            try:
                cursor = connection.cursor()

                # Insert into Maintenance History table
                query = """
                        INSERT INTO LMS.MAINTENANCE_HISTORY (MAINT_ID, MAINT_DATE, NOTES)
                        VALUES (:maint_id, SYSDATE, :notes)
                """
                cursor.execute(query, maint_id=maint_id, notes=notes)

                # Delete from maintenances table
                query2 = """
                        DELETE FROM LMS.MAINTENANCES WHERE MAINT_ID = :maint_id
                """
                cursor.execute(query2, maint_id=maint_id)

                connection.commit()
                print("Maintenance Completed.")
                cursor.close()

            except cx_Oracle.DatabaseError as e:
                print(f"Error completing maintenance request: {e}")
        elif inpp == 2:
            # delete from maintenances table
            try:
                cursor = connection.cursor()
                query = f"""
                        DELETE FROM LMS.MAINTENANCES WHERE MAINT_ID = :maint_id
                """
                cursor.execute(query,maint_id=maint_id)
                connection.commit()
                print("Maintenance Deleted.")
                cursor.close()

            except cx_Oracle.DatabaseError as e:
                print(f"Error deleting maintenance request: {e}")
    else:
        print("Invalid choice. Going back to main menu.")

def display_users(connection):
    usr_type = input("Enter User Type \n(UG for Undergraduate student - PG for Postgraduate student- DR for Doctor - ST for Staff)\n")
    # select statement from the types[user_type] table 
    try:
        cursor = connection.cursor()
        query = f"""
                SELECT * FROM LMS.{types[usr_type]} u
                ORDER BY u.USER_ID
        """
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            print("Users: ")
            if usr_type == 'UG':
                for result in results:
                    print(f"GLOBAL ID: {result[0]}, First Name: {result[1]}, Last Name: {result[2]}, Department ID: {result[3]}, User ID: {result[4]}")
            elif usr_type == 'PG':
                for result in results:
                    print(f"GLOBAL ID: {result[0]}, First Name: {result[1]}, Last Name: {result[2]}, Department ID: {result[3]}, Advisor ID: {result[4]}, User ID: {result[5]}")
            elif usr_type == 'DR':
                for result in results:
                    print(f"GLOBAL ID: {result[0]}, First Name: {result[1]}, Last Name: {result[2]}, Department ID: {result[3]}, Hire Date: {result[4]}, User ID: {result[5]}")
            elif usr_type == 'ST':
                for result in results:
                    print(f"GLOBAL ID: {result[0]}, First Name: {result[1]}, Last Name: {result[2]}, Hire Date: {result[3]}, User ID: {result[4]}")
            else:
                print("INVALID USER TYPE")
        else:
            print("No students found.")

        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print(f"Error Displaying users: {e}")

def insert_new_user(connection):
    usr_type = input("Enter User Type \n(UG for Undergraduate student - PG for Postgraduate student- DR for Doctor - ST for Staff)\n")
    global_id = input("Enter User's GLOBAL ID\n")
    usr = input("Enter User's USERNAME\n")
    pwd = input("Enter User's PASSWORD\n")

    try:
        cursor = connection.cursor()

        # Insert into ONEPIECE
        query0 = """
                        SELECT LMS.ONEPIECE_USER_ID_SEQ.nextval FROM DUAL
        """
        cursor.execute(query0)
        results = cursor.fetchall()

        userrid = results[0][0]
        
        query = f"""
                INSERT INTO LMS.ONEPIECE (USER_ID, USER_TYPE, USERNAME, PASSWORD)
                VALUES (:userrid, :usr_type, :usr, :pwd)
        """
        cursor.execute(query, userrid=userrid, usr_type=usr_type, usr=usr, pwd=pwd)

        # Create User
        query2 = f"""
                CREATE USER {usr} IDENTIFIED BY {pwd}
        """
        cursor.execute(query2)

        # Grant Role
        query3 = f"""
                GRANT {role[usr_type]} TO {usr}
        """
        cursor.execute(query3)
        table = types[usr_type]
        # UPDATE USER ID IN (STUDENT/ DOCTOR / STAFF)'S TABLE
        query4 = f"""
                UPDATE {table}
                SET user_id = :userrid
                WHERE {locids[usr_type]} = :global_id
        """
        cursor.execute(query4, userrid=userrid, global_id=global_id)

        # Commit changes
        connection.commit()

        print("User successfully created and granted role.")

    except cx_Oracle.DatabaseError as e:
        print(f"Error creating user: {e}")

    finally:
        cursor.close()

def remove_user(connection):
    usr_type = input("Enter User Type \n(UG for Undergraduate student - PG for Postgraduate student- DR for Doctor - ST for Staff)\n")
    inp = int(input("1: Display Users\n2: Delete User\n"))

    try:
        cursor = connection.cursor()

        if inp == 1:
            # Display Users
            query = f"""
                    SELECT * FROM LMS.ONEPIECE
                    ORDER BY u.USER_ID
            """
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                print("USERS:")
                for result in results:
                    print(f"USER ID: {result[0]}, USER_TYPE: {result[1]}, USERNAME: {result[2]}, PASSWORD: {result[3]}")
            else:
                print("No USERS found.")

        elif inp == 2:
            # Delete User
            user_id = input("Enter User ID \n")
            table = types[usr_type]

            # Update User ID to NULL and Delete User from ONEPIECE
            query0 = f"""
                    DELETE FROM LMS.RESERVATIONS
                    WHERE user_id = :user_id
            """
            cursor.execute(query0, user_id=user_id)

            query = f"""
                    UPDATE {table}
                    SET user_id = NULL
                    WHERE user_id = :user_id
            """
            cursor.execute(query, user_id=user_id)

            # Retrieve the username associated with that user
            query2 = """
                    SELECT USERNAME FROM LMS.ONEPIECE WHERE USER_ID = :user_id
            """
            cursor.execute(query2, user_id=user_id)
            results = cursor.fetchall()
            usr = results[0][0]
            
            query3 = f"""
                DROP USER {usr}
            """
            cursor.execute(query3)

            query4 = f"""
                    DELETE FROM LMS.ONEPIECE WHERE USER_ID = :user_id
            """
            cursor.execute(query4, user_id=user_id)

            print("User successfully removed.")

            # Commit changes
            connection.commit()
        else:
            print("Invalid choice. Going back to main menu.")


    except cx_Oracle.DatabaseError as e:
        print(f"Error removing user: {e}")

    finally:
        cursor.close()

def display_all_labs(connection):
    # select  from the lab reports table of all labs (lab_id)
    # equipment (lab_id)
    # types[user_type] table (labtype_id) 
    # Rooms (room_id) 
    # GROUP BY
    try:
        cursor = connection.cursor()
        query = f"""
                select l.lab_id "Lab No.", r.room_name "Lab Name", lt.type "Lab Type", s.staff_lname "Lab Staff ID"
                from LMS.lab_staff s, LMS.labs l, LMS.labtypes lt, LMS.rooms r
                where L.room_id=r.room_id and l.labtype_id=lt.labtype_id and lt.staff_id= s.staff_id
                ORDER BY l.LAB_ID
        """
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            print("LABS:")
            for result in results:
                print(f"Lab No.: {result[0]},\n Lab Name: {result[1]}, Lab Type: {result[2]}, Lab Staff ID: {result[3]}")
        else:
            print("No LABS found.")

        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print(f"Error displaying maintenance requests: {e}")

def submit_lab_reservation_request(connection):
    inp = int(input("1: Display Equipment\n2:Display Courses\n3:REQUEST RESERVATION\n"))
    # insert  to reservations table and ask for slot_id, Equip_id, Course_id
    if inp == 1:
        try:
            cursor = connection.cursor()
            query = f"""
                    Select e.EQUIP_ID, e.EQUIP_NAME from LMS.EQUIPMENT e
                    ORDER BY e.EQUIP_ID
            """
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                print("EQUIPMENT:")
                for result in results:
                    print(f"EQUIPMENT ID: {result[0]}, EQUIPMENT NAME: {result[1]}")
            else:
                print("No EQUIPMENT found.")
            cursor.close()

        except cx_Oracle.DatabaseError as e:
            print(f"Error displaying EQUIPMENT: {e}")
    elif inp == 2:
        try:
            cursor = connection.cursor()
            query = f"""
                    Select c.COURSE_ID, c.NAME from LMS.COURSES c
                    ORDER BY c.COURSE_ID
            """
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                print("COURSES:")
                for result in results:
                    print(f"COURSE ID: {result[0]}, COURSE NAME: {result[1]}")
            else:
                print("No COURSES found.")
            cursor.close()

        except cx_Oracle.DatabaseError as e:
            print(f"Error displaying COURSES: {e}")
    elif inp == 3:
        slott = input("Enter Slot number:\n")
        equip_idd = input("Enter Equipment ID:\n")
        course_idd = input("Enter COURSE ID:\n")

        try:
            cursor = connection.cursor()

            query = """
                    INSERT INTO LMS.RESERVATIONS (Rsrv_id, RSRV_DATE, status, slot_id, user_id, equip_id, course_id)
                    VALUES (LMS.rsrv_id_seq.nextval, SYSDATE, 0, :slot, :user_id, :equip_id, :course_id)
            """

            cursor.execute(query, slot=slott, user_id=user_id, equip_id=equip_idd, course_id=course_idd)
            connection.commit()

            print("Reservation request successfully submitted.")

            cursor.close()

        except cx_Oracle.DatabaseError as e:
            print(f"Error inserting Reservation request: {e}")
    else:
        print("Invalid choice. Going back to main menu.")

def make_lab_reports(connection):
    # insert to lab reports table and ask for lab_id, lab_report_desc
    lab_id = input("Enter lab id\n")
    desc = input("Enter description\n")

    try:
        cursor = connection.cursor()

        # Retrieve the staff_id associated with the current user_id
        query2 = """
                SELECT STAFF_ID FROM LMS.LAB_STAFF WHERE USER_ID = :user_id
        """
        cursor.execute(query2, user_id=user_id)
        results = cursor.fetchall()
        
        # Assuming only one result is expected
        staff_id = results[0][0]

        # Insert into LAB_REPORTS using bind variables
        query = """
                INSERT INTO LMS.LAB_REPORTS (LAB_REPORT_ID, LAB_ID, LAB_REPORT_DATE, AUTHOR_ID, LAB_REPORT_DESC)
                VALUES (LMS.LAB_REPORT_ID_SEQ.nextval, :lab_id, SYSDATE, :author_id, :lab_desc)
        """
        cursor.execute(query, lab_id=lab_id, author_id=staff_id, lab_desc=desc)
        connection.commit()

        print("Report Inserted successfully:")
        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print(f"Error Inserting lab reports: {e}")

def display_reservation_requests(connection):
        # select  from the lab reservations table of all users where status = 0
        # equipment(equip_id)
        # courses(course_id)
        # Slot(slot_id)
        try:
            cursor = connection.cursor()
            query = f"""
                    SELECT
                        rsrv.rsrv_id,
                        rsrv.rsrv_date,
                        s.start_time,
                        s.end_time,
                        e.equip_name,
                        r.room_name,
                        c.name,
                        CASE o.user_type
                            WHEN 'DR' THEN d.dr_id
                            WHEN 'UG' THEN u.ug_std_id
                            WHEN 'PG' THEN p.pg_std_id
                            ELSE NULL -- Handle other cases if needed
                            END AS user_id
                    FROM
                        LMS.RESERVATIONS rsrv
                    JOIN
                        LMS.slots s ON rsrv.slot_id = s.slot_id
                    JOIN
                        LMS.EQUIPMENT e ON rsrv.equip_id = e.equip_id
                    JOIN
                        LMS.labs l ON e.lab_id = l.lab_id
                    JOIN
                        LMS.rooms r ON l.room_id = r.room_id
                    JOIN
                        LMS.courses c ON rsrv.COURSE_ID = c.COURSE_ID
                    JOIN
                        LMS.ONEPIECE o ON rsrv.user_id = o.user_id
                    LEFT JOIN
                        LMS.DOCTORS d ON o.user_id = d.user_id
                    LEFT JOIN
                        LMS.UG_STD u ON o.user_id = u.user_id
                    LEFT JOIN
                        LMS.PG_STD p ON o.user_id = p.user_id
                    where
                        rsrv.status=0
                    ORDER BY rsrv.rsrv_id
            """
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                print("Reservation Requests:")
                for result in results:
                    print(f"RESERVATION ID: {result[0]}, RESERVATION DATE: {result[1]}, STARTS AT hr: {result[2]}, ENDS AT hr: {result[3]}, EQUIPMENT: {result[4]}, LAB:{result[5]}, COURSE: {result[6]}\n-------------------------------------")
            else:
                print("No Reservations found.")

            cursor.close()

        except cx_Oracle.DatabaseError as e:
            print(f"Error displaying reservation requests: {e}")

def user_manage_reservation_requests(connection):
    inp = int(input("1: Display Reservation requests\n2: Delete Reservation request\n"))
    if inp == 1:
        # select  from the reservations table of that user
        # equipment(equip_id)
        # courses(course_id)
        # Slot(slot_id)
        try:
            cursor = connection.cursor()
            query = f"""
                    SELECT
                        rsrv.rsrv_id,
                        rsrv.rsrv_date,
                        rsrv.status,
                        s.start_time,
                        s.end_time,
                        e.equip_name,
                        r.room_name,
                        c.name,
                        CASE o.user_type
                            WHEN 'DR' THEN d.dr_id
                            WHEN 'UG' THEN u.ug_std_id
                            WHEN 'PG' THEN p.pg_std_id
                            ELSE NULL -- Handle other cases if needed
                            END AS user_id
                    FROM
                        LMS.RESERVATIONS rsrv
                    JOIN
                        LMS.slots s ON rsrv.slot_id = s.slot_id
                    JOIN
                        LMS.EQUIPMENT e ON rsrv.equip_id = e.equip_id
                    JOIN
                        LMS.labs l ON e.lab_id = l.lab_id
                    JOIN
                        LMS.rooms r ON l.room_id = r.room_id
                    JOIN
                        LMS.courses c ON rsrv.COURSE_ID = c.COURSE_ID
                    JOIN
                        LMS.ONEPIECE o ON rsrv.user_id = o.user_id
                    LEFT JOIN
                        LMS.DOCTORS d ON o.user_id = d.user_id
                    LEFT JOIN
                        LMS.UG_STD u ON o.user_id = u.user_id
                    LEFT JOIN
                        LMS.PG_STD p ON o.user_id = p.user_id
                    where
                        rsrv.USER_ID = {user_id}
                    ORDER BY rsrv.rsrv_id
            """
            cursor.execute(query)
            results = cursor.fetchall()


            if results:
                status = {
                    1:"Approved",
                    0:"Pending",
                    -1:"Rejectetd"
                }
                print("Reservation Requests:")
                for result in results:
                    print(f"RESERVATION ID: {result[0]}, RESERVATION DATE: {result[1]},STATUS: {status[result[2]]} , STARTS AT hr: {result[3]}, ENDS AT hr: {result[4]}, EQUIPMENT: {result[5]}, LAB:{result[6]}, COURSE: {result[7]}\n-------------------------------------")
            else:
                print("No reservation requests found.")

            cursor.close()

        except cx_Oracle.DatabaseError as e:
            print(f"Error displaying reservation requests: {e}")

    elif inp == 2:
        reservation_id = input("Enter reservation id:\n")

        try:
            cursor = connection.cursor()

            query = """
                    DELETE FROM LMS.EXPERIMENTS x WHERE x.RSRV_ID = :reservation_id
            """
            query2 = """
                    DELETE FROM LMS.RESERVATIONS WHERE USER_ID = :user_id AND RSRV_ID = :reservation_id
            """

            cursor.execute(query, reservation_id=reservation_id)
            print("Experiment successfully deleted.")
            cursor.execute(query2, user_id=user_id, reservation_id=reservation_id)
            connection.commit()
            print("Reservation AND Experiment successfully deleted.")
            cursor.close()

        except cx_Oracle.DatabaseError as e:
            print(f"Error deleting Experiment/Reservation: {e}")
    else:
        print("Invalid choice. Going back to main menu.")

def approve_deny_reservation_request(connection):
    rsrv_id = input("Enter the Reservation ID: ")
    new_status = input("Enter 1 to Approve or -1 to Reject: ")
    while int(new_status) >=1 or int(new_status) <=-1:
        new_status = input("Please only Enter 1 to Approve or -1 to Reject: ")
    try:
        cursor = connection.cursor()

        # Use bind variables to avoid SQL injection
        query = """
                UPDATE LMS.reservations
                SET Status = :new_status
                WHERE RSRV_ID = :rsrv_id
        """

        cursor.execute(query, new_status=new_status, rsrv_id=rsrv_id)
        
        # Commit the changes
        connection.commit()
        if new_status == 1:
            print("Reservation successfully Approved.")
        elif new_status == -1:
            print("Reservation successfully Rejected.")
    except cx_Oracle.DatabaseError as e:
        print(f"Error updating reservation status: {e}")

    finally:
        cursor.close()

def std_display_student_reports(connection):
    # select statement from the Student reports table of that user
    # courses(course_id)
    # doctor(author_id)
    # types[user_type] table (user_id) //
    try:
        cursor = connection.cursor()
        query = f"""
                SELECT s.STD_REPORT_ID, s.REPORT_DATE, s.AUTHOR_ID, s.GRADE, s.STD_REPORT_DESC,
                c.NAME, r.DR_FNAME ||' '|| r.DR_LNAME, g.{typefn[user_type]} ||' '||g.{typeln[user_type]}, g.USER_ID
                FROM LMS.STD_REPORTS s, LMS.COURSES C, LMS.DOCTORS r, LMS.{types[user_type]} g
                WHERE s.USER_ID={user_id} AND s.COURSE_ID = c.COURSE_ID AND s.AUTHOR_ID = r.DR_ID AND s.USER_ID = g.USER_ID
                ORDER BY s.STD_REPORT_ID
        """
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            print("Students Reports:")
            for result in results:
                print(f"\n Report ID: {result[0]}\n Report Date: {result[1]}\n Author: {result[2]}\n GRADE: {result[3]}\n Describtion: {result[4]}\n COURSE: {result[5]}\n DR. Name: {result[6]}\n STUDENT NAME: {result[7]}\n STUDENT_ID: {result[8]}\n")
        else:
            print("No Student Reports found.")
        cursor.close()
    except cx_Oracle.DatabaseError as e:
        print(f"Error Displaying Student Reports: {e}")

        cursor.close()

    except cx_Oracle.DatabaseError as e:
        print(f"Error displaying student reports: {e}")

def make_student_reports(connection):

    inpp = int(input("1: Display students\n2: Make Student report\n"))
    if inpp == 1:
        usr_type = input("Enter User Type \n(UG for Undergraduate student - PG for Postgraduate student)\n")
        # select statement from the types[user_type] table 
        try:
            cursor = connection.cursor()
            query = f"""
                    SELECT * FROM LMS.{types[usr_type]} u
                    ORDER BY u.USER_ID
            """
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                print("Users: ")
                if usr_type == 'UG':
                    for result in results:
                        print(f"GLOBAL ID: {result[0]}, First Name: {result[1]}, Last Name: {result[2]}, Department ID: {result[3]}, User ID: {result[4]}")
                elif usr_type == 'PG':
                    for result in results:
                        print(f"GLOBAL ID: {result[0]}, First Name: {result[1]}, Last Name: {result[2]}, Department ID: {result[3]}, Advisor ID: {result[4]}, User ID: {result[5]}")
            else:
                print("No students found.")

            cursor.close()

        except cx_Oracle.DatabaseError as e:
            print(f"Error Displaying students: {e}")

    elif inpp == 2:
        student_id = input("Enter student's USER ID (NOT GLOBAL ONE)\n")
        course_id = input("Enter course_id\n")
        grade = input("Enter grade\n")
        std_report_desc = input("Enter DESCRIPTION\n")

        # insert statement to student reports table and ask him for user_id, course_id, grade, std_report_desc
        try:
            cursor = connection.cursor()
            query0 = """
                    SELECT DR_ID FROM LMS.DOCTORS WHERE USER_ID = :user_id
            """
            cursor.execute(query0, user_id=user_id)
            results = cursor.fetchall()
            AUTHOR = results[0][0]
            query = """
                INSERT INTO LMS.STD_REPORTS (STD_REPORT_ID, USER_ID, course_id, grade, std_report_desc, REPORT_DATE, AUTHOR_ID)
                VALUES (LMS.STD_REPORT_ID_SEQ.nextval, :user_id, :course_id, :grade, :std_report_desc, SYSDATE, :AUTHOR)
            """
            cursor.execute(query, user_id=student_id, course_id=course_id, grade=grade, std_report_desc=std_report_desc, AUTHOR=AUTHOR)
            connection.commit()
            print("Student report inserted")
            cursor.close()

        except cx_Oracle.DatabaseError as e:
            print(f"Error inserting student report: {e}")
    else:
        print("Invalid choice. Going back to main menu.")

def submit_equipment_maintenance_request(connection):
    inp = int(input("1: Display Equipment\n2: Submit Equipment Maintenance Report\n"))
    if inp == 1:
        try:
            cursor = connection.cursor()
            query = f"""
                    Select e.EQUIP_ID, e.EQUIP_NAME from LMS.EQUIPMENT e
                    ORDER BY e.EQUIP_ID
            """
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                print("EQUIPMENT:")
                for result in results:
                    print(f"EQUIPMENT ID: {result[0]}, EQUIPMENT NAME: {result[1]}")
            else:
                print("No EQUIPMENT found.")
            cursor.close()

        except cx_Oracle.DatabaseError as e:
            print(f"Error displaying EQUIPMENT: {e}")

    elif inp == 2:
        # insert statement to maintenances table and ask him for Note, Equip_id
        Equip_id = input("Enter Equip_id \n")
        Note = input("Enter Note \n")
        try:
            cursor = connection.cursor()
            query2= f"""
                    SELECT STAFF_ID FROM LMS.LAB_STAFF WHERE USER_ID = :user_id
            """
            cursor.execute(query2, user_id=user_id)
            results = cursor.fetchall()
            for result in results:
                staff_idd = result[0]
            query = f"""
                    INSERT INTO LMS.Maintenances (Maint_id, Note, Submission_date, Staff_id, Equip_id)
                    VALUES (LMS.maint_Seq.nextval, :note, SYSDATE, :staff_id, :equip_id)
            """
            cursor.execute(query, note=Note, staff_id=staff_idd, equip_id=Equip_id)
            connection.commit()
            print("Maintenance request submitted succesfully\n")
            cursor.close()
        except cx_Oracle.DatabaseError as e:
            print(f"Error submitting equipment maintenance requests: {e}")
    else:
        print("Invalid choice. Going back to main menu.")


if __name__ == "__main__":
    user_type = None
    user_id = None
    connection = None
    types = {
        "A" : "ADMINS",
        "ST" : "LAB_STAFF",
        "DR" : "DOCTORS",
        "UG" : "UG_STD",
        "PG" : "PG_STD"
    }
    locids = {
        "A" : "ADMIN_ID",
        "ST" : "STAFF_ID",
        "DR" : "DR_ID",
        "UG" : "UG_STD_ID",
        "PG" : "PG_STD_ID"
    }
    typefn = {
        "A" : "ADMIN_FNAME",
        "ST" : "STAFF_FNAME",
        "DR" : "DR_FNAME",                           
        "UG" : "UG_FNAME",
        "PG" : "PG_FNAME"
    }
    typeln = {
        "A" : "ADMIN_LNAME",
        "ST" : "STAFF_LNAME",
        "DR" : "DR_LNAME",
        "UG" : "UG_LNAME",
        "PG" : "PG_LNAME"
    }
    role = {
        "A" : "ADMIN",
        "ST" : "STAFF",
        "DR" : "DOCTOR",
        "UG" : "STUDENT",
        "PG" : "STUDENT"
    }

    while not user_type:
        user_type, user_id, connection = login_menu()

    if user_type == "A":
        admin_menu(connection)
    elif user_type == "ST":
        staff_menu(connection)
    elif user_type == "DR":
        doctor_menu(connection)
    elif user_type == "UG":
        ug_menu(connection)
    elif user_type == "PG":
        pg_menu(connection)

    connection.close() 
