sudo yum update -y

sudo yum install openssh

wget http://sourceforge.net/projects/sshpass/files/latest/download -O sshpass.tar.gz
tar -xvf sshpass.tar.gz
cd sshpass-1.08
sudo yum groupinstall "Development Tools"
./configure
sudo make install

sudo yum install git-all -y
git --version
