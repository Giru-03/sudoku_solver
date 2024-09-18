from django.shortcuts import render, redirect
from .forms import SudokuImageForm
from .models import SudokuImage
from .solver.new import main

def upload_sudoku(request):
    if request.method == 'POST':
        form = SudokuImageForm(request.POST, request.FILES)
        if form.is_valid():
            sudoku_image = form.save()
            solved_sudoku = main(sudoku_image.image.path)
            return render(request, 'solved.html', {'solved_sudoku': solved_sudoku})
    else:
        form = SudokuImageForm()
    return render(request, 'upload.html', {'form': form})

