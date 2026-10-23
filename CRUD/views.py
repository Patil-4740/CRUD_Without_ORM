from django.shortcuts import render, redirect
from django.db import connection

def insert(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        city = request.POST.get("city")

        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO CRUD_student (name, email, city)
                VALUES (%s, %s, %s)
                """,
                [name, email, city]
            )

        return redirect('show')

    return render(request, 'insert.html')

#print('---------------------------------------------------------------------')

def show(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name, email, city FROM  CRUD_student")
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

    students = [
        dict(zip(columns, row))
        for row in rows
    ]

    return render(request, 'show.html', {'students': students})

#print('--------------------------------------------------------------------')

#update view
def edit(request):
    if request.method == "POST":
        student_id = request.POST.get("id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        city = request.POST.get("city")

        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE CRUD_student
                SET name = %s, email = %s, city = %s
                WHERE id = %s
                """,
                [name, email, city, student_id]
            )

        return redirect('show')

    student_id = request.GET.get("id")

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, name, email, city
            FROM CRUD_student
            WHERE id = %s
            """,
            [student_id]
        )

        row = cursor.fetchone()

    if row is None:
        return redirect('show')

    st = {
        'id': row[0],
        'name': row[1],
        'email': row[2],
        'city': row[3]
    }

    return render(request, 'edit.html', {'st': st})

#print('------------------------------------------------------------')

#Delete view
def delete(request):
    student_id = request.GET.get('id')

    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM CRUD_student WHERE id = %s",
            [student_id]
        )

    return redirect('show')

# Create your views here.
