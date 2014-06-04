from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from grid.models import Grid_Square, Command
from grid.forms import IndexForm

def main(request):
    squares = Grid_Square.objects.all()

    return render(request, 'grid/main.html', {'squares':squares})

def index(request):
    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():

            #Match code to Commands and Image keys
            code = form.cleaned_data['code']
            squares = Grid_Square.objects.all().filter(has_image=True)
            commands = [com.command for com in Command.objects.all().filter(is_active=True)]


            for square in squares:
                if square.image_code == code:
                    if not square.is_revealed:
                        square.is_revealed = not square.is_revealed
                        square.save()
                    return HttpResponseRedirect("main")

            if code in commands:
                if code == 'reset':
                    for square in squares:
                        square.is_revealed=False
                        square.save()
                if code == 'reveal':
                    for square in squares:
                        square.is_revealed=True
                        square.save()
                return HttpResponseRedirect("main")

            return render(request, 'grid/index.html', {'form': form, 'error_message':'Please enter a valid code', 'code':code})

    else:
        form = IndexForm()

    return render(request, 'grid/index.html', {'form': form})
            