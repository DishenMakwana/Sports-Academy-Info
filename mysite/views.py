from django.core.mail import send_mail
from mysite import settings
from mysite.forms import RegisterForm
from yoga.models import Guru, Yoga, TrainingLevels
from fitness.models import Trainer, Fitness, TrainingLevel
from sports.models import Coach, Academy, Sports


def about(request):
    gurus = Guru.objects.all()
    trainers = Trainer.objects.all()
    coachs = Coach.objects.all()

    num_trainers = Coach.objects.all().count() + Trainer.objects.all().count() + Guru.objects.all().count()
    num_clubs = Academy.objects.all().count() + Fitness.objects.all().count() + Yoga.objects.all().count()
    num_trainings = TrainingLevel.objects.all().count() + TrainingLevels.objects.all().count() + Sports.objects.all().count()

    contexts = {"gurus": gurus, "trainers": trainers, "coachs": coachs, "num_trainers": num_trainers,
                "num_clubs": num_clubs, "num_trainings": num_trainings}

    return render(request, 'about.html', contexts)


def index(request):
    num_trainers = Coach.objects.all().count() + Trainer.objects.all().count() + Guru.objects.all().count()
    num_clubs = Academy.objects.all().count() + Fitness.objects.all().count() + Yoga.objects.all().count()
    num_trainings = TrainingLevel.objects.all().count() + TrainingLevels.objects.all().count() + Sports.objects.all().count()

    contexts = {"num_trainers": num_trainers, "num_clubs": num_clubs, "num_trainings": num_trainings}

    return render(request, 'index.html', contexts)


def classes(request):
    num_training = TrainingLevel.objects.values('training_name').count() + TrainingLevels.objects.values(
        'training_name').count() + Sports.objects.values('sports_name').count()
    # print(num_training)

    num_training_type = TrainingLevel.objects.values('training_type').count() + TrainingLevels.objects.values(
        'training_type').count() + Sports.objects.values('sports_type').count()
    # print(num_training)

    num_trainers = Coach.objects.all().count() + Trainer.objects.all().count() + Guru.objects.all().count()
    num_clubs = Academy.objects.all().count() + Fitness.objects.all().count() + Yoga.objects.all().count()

    contexts = {"num_trainers": num_trainers, "num_clubs": num_clubs, "num_training": num_training,
                "num_training_type": num_training_type}

    return render(request, 'classes.html', contexts)


from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)

            subject = 'Welcome to VerywellHealth.com World'
            message = 'Hi {}, thank you for registering in VerywellHealth. Your can now explore our website and find your body fitness routine.\n\n http://verywellhealth.herokuapp.com'.format(
                username)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)

            return redirect("index")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request=request, template_name="registration/register.html", context={"form": form})

    form = RegisterForm
    return render(request=request, template_name="registration/register.html", context={"form": form})


# from django.contrib.auth.models import User
# from django.db.models.query_utils import Q
# from django.template.loader import render_to_string
#
#
# def password_reset_request(request):
#     if request.method == "POST":
#         password_reset_form = PasswordResetForm(request.POST)
#         if password_reset_form.is_valid():
#             data = password_reset_form.cleaned_data['email']
#             associated_users = User.objects.filter(Q(email=data))
#             if associated_users.exists():
#                 for user in associated_users:
#                     subject = "Password Reset Requested on verywellhealth.herokuapp.com"
#                     email_template_name = "main/password/password_reset_email.txt"
#                     c = {
#                         "email": user.email,
#                         'domain': 'verywellhealth.herokuapp.com',
#                         'site_name': 'Website',
#                         "user": user,
#                         'protocol': 'http',
#                     }
#                     email = render_to_string(email_template_name, c)
#
#                     send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
#
#                     return redirect("/password_reset/done/")
#
#     password_reset_form = PasswordResetForm()
#
#     return render(request=request, template_name="main/password/password_reset_form.html",
#                   context={"password_reset_form": password_reset_form})
