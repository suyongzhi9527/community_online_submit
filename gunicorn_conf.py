import multiprocessing

bind = "127.0.0.1:8080"
workers = multiprocessing.cpu_count() * 2 + 1
reload = True
daemon = True
# errorlog = '/root/workplace/servers/cczu_kexie_online_submit/logs/gunicorn_error.log'
errorlog = '/home/lvpeng/workplace/django/kexie_online_submit/logs/gunicorn_error.log'
proc_name = 'gunicorn_cczu_kexie_online_submit_project'
