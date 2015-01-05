echo "Number of packages installed is: $(rpm -qa | wc -l)"
sed -i "s/^.*requiretty/#Defaults requiretty/" /etc/sudoers
yum -y install gcc make gcc-c++ kernel-uek-devel-$(uname -r)
