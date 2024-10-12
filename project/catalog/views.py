from django.shortcuts import render, redirect, get_object_or_404
from .models import Courses, Comments, Profile, User, Enrollment
from .forms import LoginForm, RegisterForm, CourseForm, CommentForm, EditProfileForm, EditUserForm, RequestForm
from django.contrib.auth import login, logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


class IndexView(ListView):
    model = Courses
    template_name = 'catalog/index.html'
    context_object_name = 'courses'
    extra_context = {
        'title': 'Main page'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RequestForm()
        return context


class CoursesList(ListView):
    model = Courses
    template_name = 'catalog/courses.html'
    context_object_name = 'courses'
    extra_context = {
        'title': 'Our courses'
    }


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                try:
                    profile = Profile.objects.get(user=user)
                except:
                    Profile.objects.create(user=user)
                return redirect('index')
            else:
                return redirect('index')
        else:
            return redirect('index')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('index')
        else:
            return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')


class CourseDetail(DetailView):
    model = Courses
    template_name = 'catalog/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        course = Courses.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'Course: {course.title}'
        context['comment_form'] = CommentForm()
        context['comments'] = Comments.objects.filter(course=course, parent=None)
        context['comment_count'] = Comments.objects.filter(course=course, parent=None).count()
        return context


def about(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses,
        'title': 'About'
    }
    return render(request, 'catalog/about.html', context)


class CreateCourse(CreateView):
    model = Courses
    form_class = CourseForm
    template_name = 'catalog/course_form.html'
    extra_context = {
        'title': 'Create course'
    }


class UpdateCourse(UpdateView):
    model = Courses
    form_class = CourseForm
    template_name = 'catalog/course_form.html'
    extra_context = {
        'title': 'Change course'
    }


class DeleteCourse(DeleteView):
    model = Courses
    context_object_name = 'course'
    success_url = reverse_lazy('index')


def save_comment(request, course_id):
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.course = Courses.objects.get(pk=course_id)
        comment.auth = request.user
        parent_id = request.POST.get('comment_id')
        if parent_id:
            comment.parent = Comments.objects.get(pk=parent_id)
        comment.save()
        return redirect('detail', course_id)


def profile_view(request, pk):
    profile = get_object_or_404(Profile, user_id=pk)
    enrollments = Enrollment.objects.filter(user_id=pk)
    courses = [enrollment.course for enrollment in enrollments]
    context = {
        'profile': profile,
        'courses': courses,
    }
    return render(request, 'catalog/profile.html', context)


class UpdateProfile(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'catalog/course_form.html'
    extra_context = {
        'title': 'Change profile'
    }


class UpdateUser(UpdateView):
    model = User
    form_class = EditUserForm
    template_name = 'catalog/course_form.html'
    extra_context = {
        'title': 'Change account'
    }

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})


class SearchView(ListView):
    model = Courses
    template_name = 'catalog/courses.html'
    context_object_name = 'courses'
    extra_context = {
        'title': 'Our courses'
    }

    def get_queryset(self):
        word = self.request.GET.get('searchKeyword')
        articles = Courses.objects.filter(title__icontains=word)
        return articles


def manage_enrollment(request, course_id, action):
    course = get_object_or_404(Courses, id=course_id)
    if action == 'enroll':
        if not Enrollment.objects.filter(user=request.user, course=course).exists():
            Enrollment.objects.create(user=request.user, course=course)
    elif action == 'unenroll':
        Enrollment.objects.filter(user=request.user, course=course).delete()
    return redirect('profile', pk=request.user.id)
