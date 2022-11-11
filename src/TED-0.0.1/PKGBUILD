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
arch=()
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
source=("$pkgname-$pkgver.tar.gz"
        "$pkgname-$pkgver.patch")
noextract=()
md5sums=()
validpgpkeys=()

build() {
	cd "$pkgname-$pkgver"
	make
}

