sed -i "s/^.*requiretty/#Defaults requiretty/" /etc/sudoers
case $(sed 's/.*\([0-9][0-9]*\)\.[0-9][0-9]*/\1/' /etc/oracle-release) in
    5) rpm -Uvh http://mirror.sfo12.us.leaseweb.net/epel/5/i386/epel-release-5-4.noarch.rpm;;
    6) rpm -Uvh http://mirror.sfo12.us.leaseweb.net/epel/6/i386/epel-release-6-8.noarch.rpm
       # I found that ol6u4 just wouldn't load from the mirror locations although ol6u6 would!
       # So the following line simply corrects this for all ol6 versions
       sed -i -e 's/^#baseurl/baseurl/' -e 's/^mirror/#mirror/' /etc/yum.repos.d/epel.repo;;
    7) rpm -Uvh http://mirror.symnds.com/distributions/fedora-epel/7/x86_64/e/epel-release-7-5.noarch.rpm;;
esac
yum -y install dkms gcc make gcc-c++ kernel-uek-devel-$(uname -r)
