git clone https://github.com/ngircd/ngircd.git
cd ngircd
git checkout e17d4bdec7857e7af9deb02681585fad15eb1ebd

apt-get -y install autoconf automake 
./autogen.sh 
./configure 
make
