from osv.modules import api

api.require('ruby')
default = api.run(cmdline="/ruby.so /KSL/main.rb")
