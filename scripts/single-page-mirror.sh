#!/bin/sh

# https://superuser.com/a/136335
# wget --adjust-extension --span-hosts --convert-links --backup-converted --page-requisites
wget -E -H -k -K -p ''$1''
