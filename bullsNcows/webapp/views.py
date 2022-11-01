from django.shortcuts import render
from random import sample

# Create your views here.

def generate_numbers(n):
    return sample(range(1,10), n)
secret = generate_numbers(4)

move = []
message=[]

def index_view(request):
    if request.method == "GET":
        return render(request, 'index.html')

    elif request.method == 'POST':
        if request.POST.get('numbers'):
            try:
                a = request.POST.get('numbers').replace(' ','')
                numbers_int = [int(s) for s in a]
            except ValueError:
                answer = f'Enter only numbers'
                return render(request, 'index.html', {'answer': answer})
        else:
            answer = f'Enter four numbers'
            return render(request, 'index.html', {'answer':  answer})


        if len(numbers_int) != 4:
            answer ='there should be four integers'
            return render(request, 'index.html',{'answer':answer})
        if len(set(numbers_int)) != len(numbers_int):
            answer = 'the integers must be unique'
            return render(request, 'index.html',{'answer':answer})
        for i in numbers_int:
            if i > 9 or i < 0:
                answer = 'the integers must be from 1 to 9'
                return render(request, 'index.html',{'answer':answer})
        b = 0
        c = 0
        for i in range(4):
            if numbers_int[i] == secret[i]:
                b += 1
                move.append(1)
            elif numbers_int[i] in secret:
                c += 1
                move.append(1)
            
        if b == 4:
            secret[:] = generate_numbers(4)
            answer = "You got it right!"
            message.append('victory')
            return render(request, 'index.html',{'answer':answer})
        else:
            answer = f'You got {b} Bulls and {c} Cows'
            message.append(answer)
            move.append(1)
            return render(request, 'index.html',{'answer':answer})
            
        
        

def steps(request):
    step = len(move)
    return render(request, 'steps.html', {'message': message , 'step': step}) 






