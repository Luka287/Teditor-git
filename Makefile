install: 
#		mkdir /usr/lib/tedit/
		install src/teditor/ted.py /usr/lib/tedit/
		install teditor /usr/bin

uninstall:
		rm -R /usr/lib/tedit/
		rm /usr/bin/teditor

check:
		echo "it's ok"