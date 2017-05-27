
# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import MysqlAccounts
from common.crypt import MyCrypto
from common.common import run_cmd
from django.contrib import messages

key = 'djfhj878DFHGFDJ3'


@login_required()
def show_all(request):
    all_accounts = MysqlAccounts.objects.all()
    account_list = list()
    for one_item in all_accounts:
        temp = dict()
        temp['name'] = one_item.name
        temp['host'] = one_item.host
        temp['priv'] = one_item.priv
        temp['remoteHost'] = one_item.remoteHost
        temp['database'] = one_item.database
        temp['tableName'] = one_item.tableName
        temp['password'] = MyCrypto(key).decrypt(one_item.password)
        account_list.append(temp)
    return render(request, 'my_account/show_all_account.html', context={'MysqlAccounts': account_list})


@login_required()
def new_account(request):
    hostlist = set()
    for account in MysqlAccounts.objects.all():
        hostlist.add(account.host)
    if request.method == 'POST':
        if not request.form['name'] or not request.form['password'] or not request.form['host'] or not request.form[
            'priv'] \
                or not request.form['remoteHost'] or not request.form['database'] or not request.form['tableName']:
            messages.error(request, 'Please enter all the fields')
        else:
            dec_passwd = MyCrypto(key).encrypt(request.form['password'])
            messages.debug(request, "encrypt passwd was %s" % dec_passwd)

            account = MysqlAccounts(name=request.form['name'], password=dec_passwd,
                                    host=request.form['host'], priv=request.form['priv'],
                                    remoteHost=request.form['remoteHost'],
                                    database=request.form['database'], tableName=request.form['tableName'])
            if add_account(account):
                account.save()
                messages.success(request, 'Record was successfully added')
                return redirect('http://bigdata-app.whaley.cn/show_all')
                # return redirect(url_for('show_all'))
            else:
                messages.error(request, 'cmd run Faild.PLS check it')

    return render(request, 'new_account.html', Hostlist=hostlist)


def add_account(account):
    cmd = '''mysql -u{login_user} -p{login_passwd} -h{host}  -e "grant {priv} on {database}.{table_name} to {name}@'{remote_host}'  IDENTIFIED BY '{passwd}';"'''.format \
        (login_user=account.loginUser, login_passwd=MyCrypto(key).decrypt(account.loginPassword),
         host=account.host, priv=account.priv, database=account.database, name=account.name,
         remote_host=account.remoteHost, passwd=MyCrypto(key).decrypt(account.password),
         table_name=account.tableName)
    print cmd
    status, out = run_cmd(cmd)
    return status
