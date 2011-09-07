from fabric.api import local, env, put, settings

def github():
    env.url = "http://toke.github.com"

def live():
    env.hosts = ["toke.de:10022"]
    env.target = "/var/www/sites/toke.de"
    env.url = "http://toke.de"

def serve():
    local('jekyll --url http://127.0.0.1:4000 --server --auto')

def build():
    params = ""
    if env.url:
        params += "--url %s" % env.url
    local('jekyll %s' % params)

def gitpush():
    local('git push')

def publish():
    if env.target:
        build()
        put('_site/*', env.target) 
    else:
        gitpush()
    
