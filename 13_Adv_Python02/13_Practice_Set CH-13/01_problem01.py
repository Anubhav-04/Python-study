# create two virtual environments and install some packages in first virtual environment
# and do the same for second virtual environment
print('''
step1:--- Create virtual environment
            virtualenv env1
step2:--- Activate virual environment
            chmod +x env1/bin/activate (For permission)
            source env1/bin/activate (For activation)
step3:--- Install packages
            pip install panda
            pip install pyjkes
step3:--- Create a text file of packages installed in the virtual environment
            pip freeze > packageForenv2.txt
step4:--- Now deactivate from env1
            deactivate
step5:--- Now activate virtual environment env2 following step 2 and then install packages using the above text file
          (packageForenv2.txt)
            pip install -r packageForenv2.txt
ste6:--- Check and verify that packages are installed 
            pip freeze
''')