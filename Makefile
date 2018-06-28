# If code is run with no parameters
prepare:
	echo The current directory is $PWD
	rm -f -r -d ROS-Code
	rm -f ros.py
	rm -f run-file.py
	git clone https://github.com/Richienb/ROS-Code.git
	cd ROS-Code
	pip install -r requirements.txt
	cd ..
	#mv $PWD/ROS-Code/src/syntax.py $PWD/ROS-Code/src/ros.py
	cp ROS-Code/src/syntax.py .
	cp ROS-Code/src/run-file.py .
	rm -f -r -d ROS-Code
# Uninstall ROS Code
uninstall:
	rm syntax.py
	rm run-file.py
# Install main Pip packages
pipmain: mainmodules.txt
	pip install -r mainmodules.txt
# Install main mkdocs packages
pipmkdocs:
	pip install mkdocs mkdocs-material pymdown-extensions Pygments
# Install all required Pip packages
pipall: requirements.txt
	pip install -r requirements.txt