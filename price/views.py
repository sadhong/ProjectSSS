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

        iplace_tmp = request.POST.get('iplace')
        if iplace_tmp.strip() == '':
            iplace = '---'
        else:
            iplace = iplace_tmp

        idate = request.POST.get('idate')

        inum = request.POST.get('inum')
        
        iprice = request.POST.get('iprice')
        if not iprice:
            return HttpResponse('请输入正确的单价！')

        itaxi = request.POST.get('itaxi')
        print('税率为：', itaxi, '%')
        itaxi_tmp = round(int(itaxi)/100,2) + 1
        print('运算税率为：',itaxi_tmp)

        tcount = float(iprice) * float(inum) * float(itaxi_tmp)

        isUrgency = request.POST.get('isUrgency')

        toWhere = request.POST.get('toWhere')

        shipcount = request.POST.get('shipcount')

        memo_tmp = request.POST.get('imemo')
        if memo_tmp.strip() == '':
            imemo = '---'
        else:
            imemo = memo_tmp.strip()
        
        itotal = (float(iprice) * float(inum) + float(shipcount)) * itaxi_tmp
        print('含税总价为：', itotal)
        imemo = request.POST.get('imemo')
        
        pid = request.POST.get('pid')

        oid = request.POST.get('oid')

        try:
            Item.objects.create(iname=iname, iplace=iplace, idate=idate, inum=inum, iprice=iprice, itaxi=itaxi, isUrgency=isUrgency, toWhere=toWhere, shipcount=shipcount, imemo=imemo, itotal=itotal, tcount=tcount, pid=pid, oid=oid)
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
        iplace_tmp = request.POST.get('iplace')
        if iplace_tmp.strip() == '':
            iplace = '---'
        else:
            iplace = iplace_tmp.strip()

        idate = request.POST.get('idate')
        inum = request.POST.get('inum')
        iprice = request.POST.get('iprice')
        itaxi = request.POST.get('itaxi')
        itaxi_tmp = round(int(itaxi)/100,2) + 1
        tcount = float(iprice) * float(inum) * float(itaxi_tmp)
        isUrgency = request.POST.get('isUrgency')
        toWhere = request.POST.get('toWhere')
        shipcount = request.POST.get('shipcount')
        itotal = (float(iprice) * float(inum) + float(shipcount)) * float(itaxi_tmp)
        memo_tmp = request.POST.get('imemo')
        if memo_tmp.strip() == '':
            imemo = '---'
        else:
            imemo = memo_tmp
        
        if not iprice or not itotal:
            return HttpResponse('请输入修改后的价格！')
        pid = request.POST.get('pid')
        oid = request.POST.get('oid')

        item.iname = iname
        item.iplace = iplace
        item.inum = inum
        item.idate = idate
        item.iprice = iprice
        item.itaxi = itaxi
        item.tcount = tcount
        item.isUrgency = isUrgency
        item.toWhere = toWhere
        item.shipcount = shipcount
        item.itotal = itotal
        item.imemo = imemo
        item.pid = pid
        item.oid = oid
        item.save()
        return HttpResponseRedirect('/price/item_table.html')
    return HttpResponse('项目信息更新功能')

