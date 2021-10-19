from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from price.models import Item, Organization, Project 

# Create your views here.


def item_table(request):
    try:
        all_item = Item.objects.all().order_by('id')
        if not all_item:
            return HttpResponse('工程信息列表为空，请录入！')
    except Exception as e:
        print(e)
    return render(request, 'item_table.html', locals())



def add_item(request):
    
    if request.method == 'GET':
        return render(request, 'add_item.html')

    elif request.method == 'POST':

        iname = request.POST.get('iname')
        if not iname:
            return HttpResponse('输入错误！请输入正确的名称。')

        inum = request.POST.get('inum')
        
        iprice = request.POST.get('iprice')
        if not iprice:
            return HttpResponse('请输入正确的单价！')
        
        itotal = float(iprice) * float(inum)

        pid = request.POST.get('pid')

        oid = request.POST.get('oid')

        try:
            Item.objects.create(iname=iname,inum=inum,iprice=iprice,itotal=itotal,pid=pid,oid=oid)
        except Exception as e:
            print('数据添加错误！---> %s' %(e))
        return HttpResponseRedirect('/price/item_table.html')
    return HttpResponse('请使用正确的 Http 请求方法！')


def del_item(request, item_id):
    item_id = int(item_id)
    try:
        item = Item.objects.get(id=item_id)
    except Exception as e:
        print('查询异常：没找到数据！', e)
        return HttpResponse('没有项目可删除！')

    if request.method == 'GET':
        return render(request, 'del_item.html', locals())
    elif request.method == 'POST':
        item.delete()
        return HttpResponseRedirect('/price/item_table.html')
    return HttpResponse('项目删除功能')


def update_item(request, item_id):
    item_id = int(item_id)
    try:
        item = Item.objects.get(id=item_id)
    except Exception as e:
        return HttpResponse('---没有找到任何项目---')
    
    if request.method == 'GET':
        return render(request, 'update_item.html', locals())
    elif request.method == 'POST':
        iname = request.POST.get('iname')
        inum = request.POST.get('inum')
        iprice = request.POST.get('iprice')
        itotal = float(iprice) * float(inum)
        if not iprice or not itotal:
            return HttpResponse('请输入修改后的价格！')
        pid = request.POST.get('pid')
        oid = request.POST.get('oid')

        item.iname = iname
        item.inum = inum
        item.iprice = iprice
        item.itotal = itotal
        item.pid = pid
        item.oid = oid
        item.save()
        return HttpResponseRedirect('/price/item_table.html')
    return HttpResponse('项目信息更新功能')

