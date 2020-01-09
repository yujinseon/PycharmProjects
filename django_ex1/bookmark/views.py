from django.shortcuts import render, get_object_or_404

from .models import Bookmark

# Create your views here.
def BookmarkListView(request):
    # Bookmark 테이블의 모든 Row를 가져옴. list 형태로 저장됨
    bookmarks = Bookmark.objects.all()
    for bookmark in bookmarks:
        print("ID : {}, Name : {}, URL : {}".format(bookmark.id, bookmark.name, bookmark.url))

    return render(request, 'bookmark_list.html', {'bookmarks': bookmarks})

def BookmarkDetailView(request, pk):
    """
    Bookmark 테이블의 특정 Row만 가져오는 방법 두 가지
    1. get_object_or_404(): 객체가 존재하지 않을 때 Http 404 예외를 발생
    - 하나의 오브젝트만 받을 수 있으므로 주의
    -  Django 모델을 첫번째 인자로 받고, 키워드 인수들을 모델 관리자의 get() 함수에 넘김

    2. models.py에 정의된 모델 클래스를 직접 사용
    """
    # 인자로 들어온 pk값과 테이블의 pk값이 같은 행만 가져옴
    bookmark1 = get_object_or_404(Bookmark, pk=pk)
    bookmark2 = Bookmark.objects.get(pk=pk)


    return render(request, 'bookmark_detail.html', {'bookmark': bookmark2})
