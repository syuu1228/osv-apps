from osv.modules import api

default = api.run("--maxnic=0 /httpd --network-stack native --dpdk-pmd")
