install: 
		mkdir /usr/lib/tedit/
		cp src/teditor/ted.py /usr/lib/tedit
		cp tedit /usr/bin

uninstall:
		rm -R /usr/lib/tedit/
		rm /usr/bin/tedit