from django.shortcuts import render, redirect
from .forms import SudokuImageForm
from .solver.new import solve

def upload_sudoku(request):
    # if request.method == 'POST':
    #     form = SudokuImageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         sudoku_image = form.save()
    #         solved_sudoku = main(sudoku_image.image.path)
    #         return render(request, 'solved.html', {'solved_sudoku': solved_sudoku})
    # else:
    #     form = SudokuImageForm()
    # return render(request, 'upload.html', {'form': form})
    if request.method == 'POST':
        sudoku = []
        for i in range(9):
            row = []
            for j in range(9):
                value = request.POST.get(f'cell-{i}-{j}')
                row.append(int(value) if value.isdigit() else 0)
            sudoku.append(row)

        if solve(sudoku):  # Solve the Sudoku
            solved_sudoku = sudoku
        else:
            solved_sudoku = None  # In case the puzzle is not solvable
        
        return render(request, 'solved.html', {'solved_sudoku': solved_sudoku})
    return render(request, 'upload.html')

