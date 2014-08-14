from osv.modules import api

api.require('ruby')
default = api.run(cmdline="--cwd=/KSL /ruby.so main.rb")
