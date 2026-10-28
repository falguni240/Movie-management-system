from django.shortcuts import render, redirect, get_object_or_404
from .models import MovieModel, UsersModel, Booking
from .forms import MovieModelForm, UserModelForm, BookingModelForm


# Create your views here.
def create_mov(request):
    form = MovieModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("read_mov")
    return render(request, "create_mov.html", {"form": form})


def read_mov(request):
    records = MovieModel.objects.all()
    return render(request, "read_mov.html", {"context": records})


def update_mov(request, mid):
    record = get_object_or_404(MovieModel, id=mid)
    form = MovieModelForm(request.POST or None, instance=record)

    if form.is_valid():
        form.save()
        return redirect("read_mov")
    return render(request, "update_mov.html", {"form": form})


def delete_mov(request, mid):
    record = get_object_or_404(MovieModel, id=mid)

    if request.method == "POST":
        record.delete()
        return redirect("read_mov")

    return render(request, "delete_mov.html", {"context": record})


# for users
def create_user(request):
    form = UserModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("read_u")
    return render(request, "create_user.html", {"form": form})


def read_user(request):
    records = UsersModel.objects.all()
    return render(request, "read_user.html", {"context": records})


def update_user(request, uid):
    record = get_object_or_404(UsersModel, id=uid)
    form = UserModelForm(request.POST or None, instance=record)

    if form.is_valid():
        form.save()
        return redirect("read_u")
    return render(request, "update_user.html", {"form": form})


def delete_user(request, uid):
    record = get_object_or_404(UsersModel, id=uid)

    if request.method == "POST":
        record.delete()
        return redirect("read_u")

    return render(request, "delete_user.html", {"context": record})


# for booking crud


def add_booking(request):
    form = BookingModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("read_book")
    return render(request, "add_booking.html", {"form": form})


def read_booking(request):
    records = Booking.objects.all()
    return render(request, "read_booking.html", {"context": records})


def update_booking(request, bid):
    record = get_object_or_404(Booking, id=bid)
    form = BookingModelForm(request.POST or None, instance=record)

    if form.is_valid():
        form.save()
        return redirect("read_book")
    return render(request, "update_booking.html", {"form": form})


def delete_booking(request, bid):
    record = get_object_or_404(Booking, id=bid)

    if request.method == "POST":
        record.delete()
        return redirect("read_book")

    return render(request, "delete_booking.html")
