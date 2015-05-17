Vagrant.configure(2) do |config|
  config.vm.box = "ol6u6-minimal-lvmi9-uek"
  config.vm.box_url = "file:///u01/003-Projects/Corralitos/ol6u6-minimal-lvmi9-uek.box"
  config.vm.hostname = "lvmi9.lab.net"
  config.vm.define "lvmi9" do |lvmi9|
  end
  config.vm.provider :virtualbox do |vb|
    vb.name = "lvmi9"
    vb.customize ["modifyvm", :id, "--cpus", "2"]
  end
  config.vm.provision "install_packages", type: "shell", path: "scripts/install_packages.sh"
  config.vm.provision "user_config", type: "shell", path: "scripts/user_config.py"
end
