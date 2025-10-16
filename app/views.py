from django.shortcuts import render
from PIL import Image
import qrcode
import base64
from io import BytesIO
from .forms import TestForm  # 追加
from django.views.generic import TemplateView

class GoogleView(TemplateView):
    template_name = "app/google51925de0612ccd11.html"

def index(request):
  # img = qrcode.make('satou')
  # buffer = BytesIO()
  # img.save(buffer, format="PNG")
  # qr = base64.b64encode(buffer.getvalue()).decode().replace("'", "")
  # param = { 'qr': qr}
  # return render(request, 'app/index.html', param)
  my_dict = {
        'insert_something':"views.pyのinsert_something部分です。",
        'name':'Bashi',
        'test_titles': ['title 1', 'title 2', 'title 3'],
        'form': TestForm(),  # 追加
        'insert_forms': 'ここに表示されます',  # 追加
        'qr': '',
  }
  if (request.method == 'POST'):
        # my_dict['insert_forms'] = '文字列:' + request.POST['text'] + '\n整数型:' + request.POST['num']
        my_dict['insert_forms'] = '文字列:' + request.POST['text']
        my_dict['form'] = TestForm(request.POST)
        img = qrcode.make(request.POST['text'])
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr = base64.b64encode(buffer.getvalue()).decode().replace("'", "")
        my_dict['qr'] = qr
  return render(request, 'app/index.html', my_dict)