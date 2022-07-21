import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, session
import ast
from datetime import datetime

app = Flask(__name__)
app.secret_key = "im_proj_sf10"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="im_proj"
)
cursor = db.cursor()


@app.route('/', methods=['GET', 'POST'])
def home_page():
    errors = []
    msg = ''
    alert_color = ''

    if request.method == 'POST':
        if len(str(request.form['lrn'])) != 12:
            if len(str(request.form['lrn'])) != 0:
                errors.append("LRN must be 12 characters length.")

        if request.form['lrn']:
            sql = f"""
            SELECT `lrn`
            FROM `student`
            WHERE `lrn` = {request.form['lrn']} AND `lrn` IS NOT NULL
            """
            cursor.execute(sql)
            duplicateLRN = cursor.fetchone()

            if duplicateLRN:
                errors.append('LRN is present in another student record.')

        # get age (in years) of student based on birth_date
        birth_date = datetime.strptime(request.form['birth_date'], "%Y-%m-%d")
        now = datetime.now()
        age_years = (now - birth_date).days // 365

        if age_years < 3 or age_years > 99:
            errors.append("Please check birthdate value.")

        if errors:
            student_info = {
                'student_id': request.form['student_id'],
                'lrn': request.form['lrn'],
                'surname': request.form['surname'],
                'first_name': request.form['first_name'],
                'middle_name': request.form['middle_name'],
                'birth_date': request.form['birth_date'],
                'birth_place': request.form['birth_place'],
                'gender': request.form['gender'],
                'nationality': request.form['nationality'],
                'religion': request.form['religion'],
                'father_name': request.form['father_name'],
                'mother_name': request.form['mother_name'],
                'address': request.form['address']
            }
            return render_template('sf10.html', option='CREATE', student_info=student_info, errors=errors, css_js="sf10")

        # insert record 
        null = 'NULL'
        sql = f"""INSERT INTO `student`
        VALUES ({request.form['student_id']}, {null if not request.form['lrn'] else request.form['lrn']},
        '{request.form['surname']}', '{request.form['first_name']}',
        '{request.form['middle_name']}', '{request.form['birth_date']}',
        '{request.form['birth_place']}', '{request.form['gender']}',
        '{request.form['nationality']}',  {'NULL' if not request.form['religion'] else "'" + request.form['religion'] + "'"},
         {'NULL' if not request.form['father_name'] else "'" + request.form['father_name'] + "'"} , '{request.form['mother_name']}',
        '{request.form['address']}')
        """
        cursor.execute(sql)
        db.commit()

        msg = f"Student ID: {request.form['student_id']} record successfully added."
        alert_color = 'success'

    return render_template('index.html', css_js="index", msg=msg, alert_color=alert_color)

@app.route('/del/<student_id>')
def delete_student_record(student_id):
    try:
        sql = f"""
        DELETE FROM `student`
        WHERE `student_id` = {student_id}
        """

        cursor.execute(sql)
        sql = f"""
        DELETE FROM `enrollment`
        WHERE `student_id` = {student_id}
        """
        
        cursor.execute(sql)
        db.commit()
        return render_template('index.html', css_js="index", msg=f"Student ID: {student_id} record deleted.", alert_color='warning')
    except:
        return render_template('index.html', css_js="index")


@app.route('/search', methods=['GET', 'POST'])
def search_page():
    if request.method == 'GET':
        try:
            column = (' ' + request.args.get('search_column')).strip()
            value = (' ' + request.args.get('search_value')).strip()
            order_by = (request.args.get('order_by'))
            where = ''
            

            if column == 'lrn' and value == '':
                where = f"""WHERE {column} is NULL
                ORDER BY {column} {order_by}"""
            elif column == 'student_name':
                where = f"""WHERE CONCAT(TRIM(`surname`),TRIM(`first_name`),TRIM(`middle_name`)) LIKE '%{value}%'
                            ORDER BY CONCAT(TRIM(`surname`),TRIM(`first_name`),TRIM(`middle_name`)) {order_by}"""
            else:
                where = f"""WHERE {column} LIKE '%{value}%'
                            ORDER BY {column} {order_by}"""

            sql = f"""
            SELECT `student_id` as "Student ID", 
            `lrn` as "LRN",
            CONCAT(TRIM(`surname`), ", ", TRIM(`first_name`), ", ", TRIM(`middle_name`)) as "Full Name",
            `address` as "Address"
            FROM `student`
            {where}
            """
            cursor.execute(sql)
            result = cursor.fetchall()
        except:
            result = ''
        return render_template('search.html', result=result)

@app.route('/sf10/<option>/<student_id>') 
@app.route('/sf10/<option>', methods=['GET', 'POST'])
def sf10_page(option, student_id='', student_info={}, errors=[]):
    student_info = student_info
    if option.upper() == 'READ':
        try:
            sql = f"""
            SELECT *
            FROM `student`
            WHERE `student_id` = {student_id}
            """
            cursor.execute(sql)
            student_info = cursor.fetchone()
            
            student_info = {
                "student_id": student_info[0],
                "lrn": student_info[1],
                "surname": student_info[2],
                "first_name": student_info[3],
                "middle_name": student_info[4],
                "birth_date": student_info[5],
                "birth_place": student_info[6],
                "gender": student_info[7],
                "nationality": student_info[8],
                "religion": student_info[9],
                "father_name": student_info[10],
                "mother_name": student_info[11],
                "address": student_info[12],
                "enroll_info": []
            }

            enroll_sql = f"""
            SELECT * FROM 
            `enrollment` e, `location` l
            WHERE e.`student_id` = {student_id} 
            AND e.`division` = l.`division`
            ORDER BY e.`entrance_date` DESC
            """
            cursor.execute(enroll_sql)
            enroll_info = cursor.fetchall()
            print(enroll_info)
            for e in enroll_info:
                dict_e = {
                    "student_id": e[0],
                    "school_year": e[1],
                    "entrance_date": e[2],
                    "school_attended": e[3],
                    "division": e[4],
                    "level_section": e[5],
                    "days_present": e[6],
                    "final_grade": e[7],
                    "action_taken": e[8],
                    "region": e[10],
                    "district": e[11]
                }
                student_info['enroll_info'].append(dict_e)
        except:
            result = ''

    elif option.upper() == 'CREATE':
        try:            
            sql = f"""
            SELECT MAX(`student_id`)
            FROM `student`
            """
            cursor.execute(sql)
            max_id = cursor.fetchone()[0]
            if max_id == None:
                student_info['student_id'] = 1
            else:
                student_info['student_id'] = max_id + 1
            
        except:
            result = ''
    elif option.upper() == 'EDIT': 
        try:
            sql = f"""
            SELECT *
            FROM `student`
            WHERE `student_id` = {request.args.get('student_id')}
            """
            cursor.execute(sql)
            student_info = cursor.fetchone()
            
            student_info = {
                "student_id": student_info[0],
                "lrn": student_info[1],
                "surname": student_info[2],
                "first_name": student_info[3],
                "middle_name": student_info[4],
                "birth_date": student_info[5],
                "birth_place": student_info[6],
                "gender": student_info[7],
                "nationality": student_info[8],
                "religion": student_info[9],
                "father_name": student_info[10],
                "mother_name": student_info[11],
                "address": student_info[12],
            }

            session['saved_lrn'] = student_info['lrn']
        except Exception as e:
            print(e)

    return render_template('sf10.html', option=option.upper(), student_info=student_info, errors=errors)

@app.route('/enrollment/<option>', methods=['GET', 'POST'])
def enrollment_page(option):
    if request.method == 'POST':
        if request.form['reset_session']:
            # clear session data
            session_keys = [key for key in session]
            for key in session_keys:
                session.pop(key, None)

    return render_template('enrollment.html', option=option.upper())


@app.route('/insert_enrollment_record', methods=['GET', 'POST'])
def insert_enrollment_record():
    try:
        # clear session data
        session_keys = [key for key in session]
        for key in session_keys:
            session.pop(key, None)
        
        # store request.form to session
        for key in request.form:
            session[key] = request.form[key]


        # check if student_id does not exist in database 
        sql = f"""
        SELECT * FROM `student`
        WHERE `student_id` = {request.form['student_id']}
        """
        cursor.execute(sql)
        result = cursor.fetchone()
        if not result:
            session['errors'] = []
            session['errors'].append(f"""Student Id: {request.form['student_id']} does not exist.""")

            return redirect(url_for('enrollment_page', option='create'))
        

        # check if student_id and school_year exist in database 
        school_year = request.form['school_year'].split('-')[0]

        sql = f"""
        SELECT * 
        FROM `student` s, `enrollment` e
        WHERE s.`student_id` = {request.form['student_id']}
        AND e.`student_id` = {request.form['student_id']}
        AND e.`school_year` = {school_year} 
        """
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            session['errors'] = []
            session['errors'].append(f"""Student ID: {request.form['student_id']} is already enrolled in School Year {school_year}-{int(school_year)+1}.""")
            return redirect(url_for('enrollment_page', option='create'))
    

        # insert enrollment record 
        sql = f""" INSERT INTO `enrollment`
        VALUES ({request.form['student_id']}, {school_year}, '{request.form['entrance_date']}', '{request.form['school_attended']}',
        '{request.form['division']}', '{request.form['level_section']}', {request.form['days_present']},
        {request.form['final_grade']}, '{request.form['action_taken']}')
        """
        cursor.execute(sql)
        db.commit()

        msg = f"Student ID: {request.form['student_id']} School Year {request.form['school_year']} record successfully added."
        alert_color = 'success'
        return render_template('index.html', css_js="index", msg=msg, alert_color=alert_color)
    except Exception as e:
        print(e)
    return redirect(url_for('enrollment_page', option='create'))


@app.route('/check_student_id/<option>', methods=['GET', 'POST'])
def check_student_id(option):
    if request.method == "POST":
        if option == "edit_student_record":
            try: 
                sql = f"""
                SELECT * FROM `student`
                WHERE `student_id` = {request.form['student_id']}
                """
                cursor.execute(sql)
                result = cursor.fetchone()

                # if input student_id doesn't exist 
                if not result:
                    msg = f"Student ID: {request.form['student_id']} doesn't exist."
                    alert_color = 'danger'
                    return render_template('index.html', css_js="index", msg=msg, alert_color=alert_color)
                # redirect to sf10 page 
                elif result:
                    student_id = request.form['student_id']
                    return redirect(url_for('sf10_page', option="edit".upper(), student_id=student_id))
            except Exception as e:
                print(e)
    return "hmmmmm"

@app.route('/validate_student_record/<option>', methods=['GET', 'POST'])
def validate_student_record(option):
    try:
        errors = []
        msg = ''
        alert_color = ''

        if request.method == 'POST':
            if len(str(request.form['lrn'])) != 12:
                if len(str(request.form['lrn'])) != 0:
                    errors.append("LRN must be 12 characters length.")

            
            if request.form['lrn']:
                if session['saved_lrn']:
                    not_same_lrn = f"AND {request.form['lrn']} != {session['saved_lrn']}"
                else:
                    not_same_lrn = ''

                sql = f"""
                SELECT *
                FROM `student`
                WHERE `lrn` = {request.form['lrn']}  AND `lrn` IS NOT NULL
                {not_same_lrn}
                """
                print(sql)
                cursor.execute(sql)
                duplicateLRN = cursor.fetchone()

                if duplicateLRN:
                    errors.append('LRN is present in another student record.')
             

            # get age (in years) of student based on birth_date
            birth_date = datetime.strptime(request.form['birth_date'], "%Y-%m-%d")
            now = datetime.now()
            age_years = (now - birth_date).days // 365

            if age_years < 3 or age_years > 99:
                errors.append("Please check birthdate value.")

            if errors:
                student_info = {
                    'student_id': request.form['student_id'],
                    'lrn': request.form['lrn'],
                    'surname': request.form['surname'],
                    'first_name': request.form['first_name'],
                    'middle_name': request.form['middle_name'],
                    'birth_date': request.form['birth_date'],
                    'birth_place': request.form['birth_place'],
                    'gender': request.form['gender'],
                    'nationality': request.form['nationality'],
                    'religion': request.form['religion'],
                    'father_name': request.form['father_name'],
                    'mother_name': request.form['mother_name'],
                    'address': request.form['address']
                }
                
                return render_template('sf10.html', option='EDIT', student_info=student_info, errors=errors, css_js="sf10")


            # update record 
            null = 'NULL'
            sql = f"""UPDATE `student`
            SET `lrn` = {null if not request.form['lrn'] else request.form['lrn']},
            `surname` = '{request.form['surname']}', 
            `first_name` = '{request.form['first_name']}', 
            `middle_name` = '{request.form['middle_name']}',
            `birth_date` = '{request.form['birth_date']}',
            `birth_place` = '{request.form['birth_place']}',
            `gender` = '{request.form['gender']}',
            `nationality` = '{request.form['nationality']}',
            `religion` = {'NULL' if not request.form['religion'] else "'" + request.form['religion'] + "'"},
            `father_name` = {'NULL' if not request.form['father_name'] else "'" + request.form['father_name'] + "'"},
            `mother_name` = '{request.form['mother_name']}',
            `address` = '{request.form['address']}'
            WHERE `student_id` = {request.form['student_id']}
            """
            cursor.execute(sql)
            db.commit()

            msg = f"Student ID: {request.form['student_id']} record successfully updated."
            alert_color = 'success'
            return render_template('index.html', css_js="index", msg=msg, alert_color=alert_color)
    except Exception as e:
        return f"{e}"


