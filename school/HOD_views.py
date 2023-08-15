from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from school.models import Courses, Session_year, CustomerUser, Student
from django.contrib import messages



@login_required(login_url='/')
def Home(request):
    return render(request, 'HOD/home.html')

@login_required(login_url='/')
def Add_student(request):
    course = Courses.objects.all()
    session_year = Session_year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        
        print(profile_pic, first_name, last_name, email, username, password, address, gender, course_id, session_year_id)

        if CustomerUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken!s')
            return redirect('add_student')
        
        if CustomerUser.objects.filter(username=username).exists():
            messages.warning(request, 'UserName Is Already Taken!s')
            return redirect('add_student')
        else:
            user = CustomerUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Courses.objects.get(id = course_id)
            session_year = Session_year.objects.get(id = session_year_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
            )
            
            print(student)
            student.save()
            messages.success(request, 'Student Sucessfully Saved')
            return redirect('add_student')

    context = {
        'course': course,
        'session_year': session_year,
    }
    return render(request, 'HOD/add_student.html', context)