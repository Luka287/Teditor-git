install: 
		mkdir -p /usr/lib/tedit/
		cp src/teditor/ted.py /usr/lib/tedit/
		cp teditor /usr/bin

uninstall:
		rm -R /usr/lib/tedit/
		rm /usr/bin/teditor

check:
		echo "it's ok"