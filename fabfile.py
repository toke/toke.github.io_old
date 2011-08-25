from fabric.api import *
import os
import fabric.contrib.project as project


def gitpush():
    local('git push')

def publish():
    gitpush()
    
