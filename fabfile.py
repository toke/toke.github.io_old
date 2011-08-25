from fabric.api import *
import os
import fabric.contrib.project as project

def serve():
    local('jekyll --url http://127.0.0.1:4000 --server')

def gitpush():
    local('git push')

def publish():
    gitpush()
    
