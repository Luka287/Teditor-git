# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: Your Name <youremail@domain.com>
pkgname=teditor-git
pkgver=0.0.1
pkgrel=1
epoch=
pkgdesc="This is my personal text editor made in python"
arch=('any')
url="https://github.com/Luka287/TED.git"
license=('GPL')
groups=()
depends=(tk)
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("https://github.com/Luka287/TED/archive/refs/tags/$pkgver.tar.gz")
noextract=()
md5sums=()
validpgpkeys=()

build() {
	cd "TED-${pkgver}"
	sudo make install
}

package() {
	echo "nothin"
}

check() {
	#cd "$pkgname-$pkgver"
	make -k check
	#cd ..
}

sha256sums=('7f99da3efff71b0170140e060da9b5615162cffb58115b14c52760cffb36e3b2')
