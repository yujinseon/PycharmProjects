from django.shortcuts import render, get_object_or_404

from .models import Bookstore

# Create your views here.
def BookstoreListView(request):

    bookstores = Bookstore.objects.all()

    return render(request, 'bookstore_list.html', {'bookstores': bookstores})

def BookstoreDetailView(request, pk):
    # 인자로 들어온 pk값과 테이블의 pk값이 같은 행만 가져옴
    bookstore2 = Bookstore.objects.get(pk=pk)


    return render(request, 'bookstore_detail.html', {'bookstore': bookstore2})

