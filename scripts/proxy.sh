#!/bin/bash
echo DOLLAR ONE BEGIN
echo $PROXY
echo DOLLAR ONE END
if [[ -n $PROXY ]]
then
    echo "proxy=$PROXY" >>/etc/yum.conf
    echo "export http_proxy=$PROXY" >/etc/profile.d/set-proxy.sh
    echo "setenv http_proxy=$PROXY" >/etc/profile.d/set-proxy.csh
fi
